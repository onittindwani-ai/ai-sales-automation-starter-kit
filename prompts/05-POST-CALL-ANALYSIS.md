# Prompt 05: Post Call Analysis (strict JSON)

## When to use it

Step 4 of the path. This is the "AI as one step" box: after a call ends and the webhook arrives, your backend sends the transcript to an AI model with this prompt, gets back strict JSON, and routes the lead based on it.

It replaces what I used to do by hand every morning: listen to each call, read each transcript, decide if the person was interested, and write them down.

## What to paste

Your backend fills these in for every call (from the voice tool's webhook and your own database):

- The transcript.
- Call metadata: call id, lead id, duration, how the call ended, lead time zone, attempt number, the date and time in the lead's time zone.
- Your offer in one line, and your fit rules (from [prompt 04](04-AI-VOICE-CALLER-SYSTEM-PROMPT.md)).

## The prompt

Use this as the system prompt (or the full prompt) for the analysis call. If the AI model's API supports a structured output or JSON schema mode, turn it on and give it the same schema. Check the model provider's docs for how.

```
You are a careful sales call analyst. You read one outbound sales call and return ONLY a JSON object in the exact schema below. No text before or after the JSON. No markdown.

CONTEXT
- Business: {{COMPANY_NAME}}, which helps {{WHO_YOU_HELP}} to {{RESULT}}.
- Goal of the call: find out if there is a fit and book a meeting with {{HUMAN_NAME_OR_TEAM}}.
- Fit rules: {{FIT_RULES_IN_PLAIN_WORDS}}

CALL METADATA
- call_id: {{CALL_ID}}
- lead_id: {{LEAD_ID}}
- attempt_number: {{ATTEMPT_NUMBER}}
- duration_seconds: {{DURATION_SECONDS}}
- end_reason_from_voice_tool: {{END_REASON}}
- call_started_at_lead_local_time: {{CALL_STARTED_AT_LOCAL}} ({{LEAD_TIME_ZONE}})

TRANSCRIPT
{{TRANSCRIPT}}

OUTCOME CATEGORIES (pick exactly one, use the first that applies in this priority order)
1. do_not_call: the person asked not to be contacted again, to be removed, or said anything like "stop calling", in any words, even if they said other things too.
2. meeting_booked: a specific day and time for a meeting was clearly agreed by the person.
3. call_back: the person asked to be called again, ideally at a specific time.
4. interested: the person showed real interest or asked for information, but no meeting or call back time was agreed.
5. wrong_person: the person is not the lead, or not the right person for this topic.
6. not_interested: the person clearly declined, without asking to stop contact.
7. voicemail: a voicemail greeting or answering machine, no live conversation.
8. ivr: an automatic phone menu or recorded system, no live person.
9. no_answer: no one answered, the line was silent, or the call dropped before any real conversation.

RULES
- Use ONLY what is in the transcript and metadata. Never guess. If something is not said, use null.
- If the transcript is empty or only machine speech, the outcome must be voicemail, ivr or no_answer.
- callback_time: only if a time was said. Convert it to ISO 8601 with the lead's time zone offset, using call_started_at_lead_local_time to resolve words like "tomorrow" or "Friday". Keep the person's exact words in callback_time_text. If no time was said, both are null.
- meeting_time follows the same rules as callback_time.
- summary: 2 sentences maximum, plain words, facts only.
- objections: short phrases, in the person's own words where possible.
- key_quotes: up to 3 short exact quotes that justify the outcome.
- next_action: one of the allowed values below, matching the outcome.
- confidence: a number from 0 to 1. Use below 0.7 if the transcript is unclear, cut off, or the outcome could reasonably be another category.
- needs_human_review: true if confidence is below 0.7, if the person was upset, if they asked a question the AI could not answer, or if anything legal, medical or financial was raised.
- ai_disclosed: true if the caller said it was an AI assistant, false if not, null if the call never reached a live person.

SCHEMA (return exactly these keys, in this order)
{
  "call_id": "string",
  "lead_id": "string",
  "outcome": "interested | call_back | meeting_booked | not_interested | wrong_person | voicemail | no_answer | ivr | do_not_call",
  "human_answered": true,
  "callback_time": "ISO 8601 string or null",
  "callback_time_text": "string or null",
  "meeting_time": "ISO 8601 string or null",
  "meeting_time_text": "string or null",
  "email_given": "string or null",
  "fit": "yes | no | unclear",
  "summary": "string",
  "objections": ["string"],
  "key_quotes": ["string"],
  "next_action": "confirm_meeting | schedule_callback | alert_human_now | start_follow_up | find_right_person | close_lead | redial | add_to_do_not_call",
  "confidence": 0.0,
  "needs_human_review": false,
  "ai_disclosed": true
}
```

## What a good output looks like

```json
{
  "call_id": "call_123",
  "lead_id": "lead_456",
  "outcome": "call_back",
  "human_answered": true,
  "callback_time": "2026-11-03T15:00:00-05:00",
  "callback_time_text": "Tuesday around 3",
  "meeting_time": null,
  "meeting_time_text": null,
  "email_given": null,
  "fit": "unclear",
  "summary": "The owner was driving and asked to talk on Tuesday afternoon. He said they get more leads than they can call back.",
  "objections": ["driving right now"],
  "key_quotes": ["call me Tuesday around 3", "we can't call everyone back"],
  "next_action": "schedule_callback",
  "confidence": 0.86,
  "needs_human_review": false,
  "ai_disclosed": true
}
```

## How to route on it (your backend, not the AI)

The AI only decides the outcome. Simple rules in your code do the rest:

| outcome | What your system does | Channels after |
| --- | --- | --- |
| do_not_call | Add to the do not call list right away. Cancel every scheduled call and message. Log it | None, ever |
| meeting_booked | Create or confirm the meeting, update the CRM, send a Slack alert, send a confirmation | Reminder only |
| call_back | Schedule a call at callback_time (if inside allowed hours, otherwise the next allowed slot). If no time was given, use your default rule | Optional short text or email confirming the time |
| interested | Slack alert to a human right away. Update the CRM. Start the follow up sequence | Email, then LinkedIn or WhatsApp ([prompt 07](07-MULTI-CHANNEL-FOLLOW-UP.md)) |
| wrong_person | Log the right person if one was named. Close this lead | Optional, only to the right person |
| not_interested | Update the CRM and close the lead. No more calls in this campaign | None |
| voicemail, no_answer, ivr | If this was attempt 1, redial once (double dial), inside allowed hours. After the last attempt, move to follow up or close | Optional follow up per your rules |

Always, before routing:

- **Validate the JSON** against the schema. If it is invalid, retry the AI call once. If it is still invalid, mark the call for human review. Never guess.
- **Safety override:** if the transcript contains stop words ("stop", "remove me", "don't call") but the AI did not return do_not_call, send it to human review. Treat opt outs as the most important rule in the system.
- **needs_human_review true:** route it to a person before any automatic action, except do_not_call, which always applies right away.
- **Idempotency:** store the call_id. If the same call is analysed twice, do not act twice.

## Common fixes

- **Text around the JSON:** turn on the model's structured output or JSON mode, and keep "No text before or after the JSON" at the top.
- **Wrong categories on short calls:** add a rule in your code before the AI: calls under {{MIN_SECONDS}} seconds with no human speech skip the AI and go straight to redial.
- **Too many interested leads:** make the interested definition stricter with an example from your own calls.
- **Wrong call back times:** always pass the call start time in the lead's own time zone. Check 20 real examples against the transcript.
- **Test it properly:** run it on 20 real transcripts you already judged by hand in step 2 and compare. Fix the prompt until it agrees on at least 17 of 20, and look closely at every disagreement.
