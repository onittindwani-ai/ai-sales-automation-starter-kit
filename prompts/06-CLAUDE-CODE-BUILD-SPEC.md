# Prompt 06: Claude Code Build Spec for the Campaign System

## When to use it

Step 8 of the path, when you are ready to build the full system from [03-SYSTEM-MAP.md](../03-SYSTEM-MAP.md). Run it inside a project you set up with [prompt 03](03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md).

Do not use it on day 1. You should already have: a working step list from step 2, a voice caller prompt you tested ([prompt 04](04-AI-VOICE-CALLER-SYSTEM-PROMPT.md)), and an analysis prompt that agrees with your own judgement ([prompt 05](05-POST-CALL-ANALYSIS.md)).

## What to paste

- Your filled in placeholders (limits, schedule, CRM, channels).
- Your caller prompt and analysis prompt, saved as files in the project (for example `prompts/caller.md` and `prompts/analysis.md`).
- Accounts and API keys for each tool, already stored in your `.env` file by you. Never paste keys into the chat.

## The prompt

```
Build a production quality outbound AI calling campaign system in this project. I am a beginner, so work in small phases, explain each phase in plain words, and wait for my OK between phases.

GOLDEN RULES (follow these in every phase)
1. Before writing code for ANY outside tool (Ultravox, the CRM, Slack, the AI model, any messaging tool), read that tool's OFFICIAL API documentation first. Never guess endpoints, field names, authentication, webhook event names or payload formats. In your plan, list the exact docs pages you read for each tool. If the docs are unclear, stop and ask me.
2. Never put secrets in code, logs, tests or chat. Read them from environment variables, and list every variable in .env.example with no real values.
3. One module per outside tool, behind a small interface, so I can switch tools later without touching the rest.
4. Every webhook handler: verify the signature if the tool supports it (read the tool's security docs), respond fast with a 2xx, then process the work in the background. Make it idempotent: the same event arriving twice must never cause a second call, a second message or a duplicate CRM record.
5. Write tests for every phase, including failure cases, and run them before saying a phase is done. Show me the test results.
6. Never call real phone numbers or message real people during development or tests. Use a test mode with fake leads and my own phone number only: {{MY_TEST_PHONE_NUMBER_STORED_IN_ENV}}.

WHAT THE SYSTEM DOES
1. Lead upload: a simple frontend page where I upload a CSV and create a campaign.
   CSV columns: {{CSV_COLUMNS, for example first_name, last_name, company, phone, email, time_zone, country, source, consent_note}}.
   Validate every row: phone numbers converted to one international format, duplicates removed (inside the file and against existing leads), rows with missing phone or time zone set aside with a reason I can see and download.
2. Do not call list: one shared list for every channel. Check it before every call and every message. Leads on it are skipped and the reason is logged. I can add numbers to it by hand.
3. Daily limit and pacing: at most {{DAILY_CALL_LIMIT}} new leads called per campaign per day, at most {{MAX_CONCURRENT_CALLS}} calls at the same time (also respect the voice tool's own concurrency limit from its docs), and at most {{MAX_ATTEMPTS_PER_LEAD}} attempts per lead in total.
4. Schedule and time zones: calls only go out {{ALLOWED_DAYS, for example Monday to Friday}}, between {{START_HOUR}} and {{END_HOUR}} in the LEAD'S OWN time zone. Skip public holidays if I provide a list. If a lead has no valid time zone, do not call them. A call is never started less than {{BUFFER_MINUTES}} minutes before the end of the window.
5. Calls through Ultravox: start each call through the Ultravox API using my caller prompt from {{PATH_TO_CALLER_PROMPT}}, passing lead details as variables. Phone line: {{MY_TELEPHONY_SETUP, for example Twilio, Telnyx, Plivo or SIP, whichever I have set up}}. Store the call id from Ultravox against the lead and the attempt.
6. Ultravox webhooks back to the backend: register a webhook for the call ended event (use the exact event names from the Ultravox docs). When it arrives, verify it, store the raw event, fetch the transcript and call details through the API if they are not in the webhook, and queue the analysis.
7. Double dial: if the result is voicemail, no answer or a phone menu (based on the voice tool's end reason and duration first, AI second), call again once, {{REDIAL_DELAY, for example 2 minutes later or the next allowed day}}, inside the schedule and limits. Never more than {{MAX_ATTEMPTS_PER_LEAD}} attempts.
8. AI analysis: calls where a real person talked go to the AI model with my analysis prompt from {{PATH_TO_ANALYSIS_PROMPT}}. Validate the JSON against the schema. Retry once if invalid, then send to human review. Use structured output mode if the model's API supports it.
9. Branches: route on the outcome exactly as in the routing table in my analysis prompt file. Safety override: if the transcript contains stop words but the outcome is not do_not_call, send to human review and pause all contact for that lead.
10. CRM sync with {{MY_CRM, for example Twenty CRM, HubSpot or GoHighLevel}}: create or update the person (match on phone, then email, never create duplicates), log every call with outcome, summary and recording or transcript link, and set the next step and its date. Read the CRM's API docs for rate limits and respect them.
11. Slack alerts to {{SLACK_CHANNEL_NAME}} through an incoming webhook or the Slack API: meeting booked, interested lead (alert a human now), needs human review, run failures, and a daily summary at {{DAILY_SUMMARY_TIME}} (calls made, human answers, outcomes by category, meetings booked, errors).
12. Opt out: a do_not_call outcome, an opt out reply on any channel, or a manual opt out adds the lead to the do not call list immediately and cancels every scheduled call and message on every channel.
13. Logging: every step for every lead is logged with time, campaign, lead id, attempt, what happened and why. No secrets or full phone numbers in plain logs (mask them). I can see a timeline per lead in the frontend.
14. Retries: outside API calls retry with backoff on temporary errors (timeouts, rate limits, server errors), up to {{MAX_RETRIES}} times, then alert Slack. Never retry in a way that could start a second call for the same attempt.
15. Controls: in the frontend I can pause and resume a campaign, and there is one global stop switch that stops all calls and messages right away.

TECH CHOICES
- Stack: {{STACK_OR_YOU_CHOOSE_THE_SIMPLEST_RELIABLE_OPTION}}. Frontend for Vercel, backend for {{RAILWAY_OR_MY_OWN_SERVER}}.
- A real database (not a spreadsheet) with tables for campaigns, leads, attempts, calls, analyses, do_not_call, events (raw webhooks), and logs.
- A background job queue or scheduler that survives restarts.

PHASES (wait for my OK after each one)
1. Plan: list the docs you read for each tool (with links), the data model, the folder structure and the test plan. No code yet.
2. Data model, CSV upload, validation, do not call list. Tests.
3. Scheduler, limits, time zones, queue. Tests that prove no call is ever started outside the schedule or over the limit.
4. Ultravox call start and webhook handler, with signature check and idempotency. Tests with recorded sample webhook payloads from the docs.
5. Double dial, AI analysis, validation, routing, safety override. Tests for every outcome.
6. CRM sync and Slack alerts. Tests with mocked APIs.
7. Frontend: upload, campaign controls, lead timeline, daily stats.
8. Dry run: a full campaign with 5 fake leads where every number is my own test number, end to end. Show me the logs.

After each phase tell me: what you built, how you tested it, the test results, and anything you were unsure about.
```

## What a good output looks like

- Phase 1 lists the exact official docs pages it read for each tool before any code exists.
- Each phase ends with passing tests and a short plain words summary.
- Tests prove the scary things: no calls outside hours, no calls over the limit, no duplicate calls from duplicate webhooks, opt outs stop everything.
- The dry run in phase 8 only ever calls your own number.

## Common fixes

- **It guessed an API endpoint:** reply "Stop. Open the official docs for this tool, quote the exact endpoint and fields, then fix the code."
- **It built everything at once:** reply "Undo the last change. Do only phase X, then wait for my OK."
- **Tests only check the happy path:** reply "Add tests for: duplicate webhook, missing transcript, CRM down, invalid JSON from the AI, opt out mid sequence, lead with no time zone."
- **You do not understand the plan:** reply "Explain the plan as a numbered list a beginner can follow, with one line per part."
- **Something breaks in production later:** paste the log lines for that lead and say "Find the root cause, write a test that fails because of it, fix it, and show me the test passing."
