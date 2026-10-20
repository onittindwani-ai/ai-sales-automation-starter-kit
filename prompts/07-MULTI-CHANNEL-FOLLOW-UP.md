# Prompt 07: Multi Channel Follow Up

## When to use it

- Step 6 of the path, to plan which channels you follow up on and in what order.
- Step 8, to add follow up to your system, only after calls already work end to end.

Our channel tools: email through Instantly or Sendkit, SMS through Telnyx, LinkedIn and WhatsApp through Unipile (or your own WhatsApp Business API setup from Meta). Details in [02-OUR-TOOL-STACK.md](../02-OUR-TOOL-STACK.md).

Before you send anything automated, read [05-COMPLIANCE-BASICS.md](../05-COMPLIANCE-BASICS.md). Each channel has its own rules.

## What to paste

- Your offer in one line, and who you are reaching.
- Which channels you actually have set up.
- The call outcomes you want to follow up on (from [prompt 05](05-POST-CALL-ANALYSIS.md)).

## The prompt

Part 1 runs in Claude and writes the sequence and the messages. Part 2 runs in Claude Code and builds it.

Part 1, design the sequence:

```
You are an expert in multi channel B2B sales follow up. Design a short, respectful follow up sequence that runs after an AI phone call.

About the offer
- Business: {{COMPANY_NAME}}, which helps {{WHO_YOU_HELP}} to {{RESULT}}.
- The human who takes meetings: {{HUMAN_NAME_OR_TEAM}}. Booking link or method: {{BOOKING_METHOD}}.
- Channels I have set up: {{CHANNELS, for example email via Instantly or Sendkit, SMS via Telnyx, LinkedIn via Unipile, WhatsApp via Unipile or the official WhatsApp Business API}}.
- Countries I reach: {{COUNTRIES}}.

Design one sequence for each of these call outcomes:
A. interested (showed interest, no meeting booked)
B. call_back (asked to be called later)
C. voicemail or no_answer after the last call attempt
D. meeting_booked (confirmation and one reminder only)

For each sequence give a table: day, channel, goal, the exact message, and the stop check before it is sent.

SEQUENCE RULES
- Maximum {{MAX_TOUCHES}} touches per sequence, over at most {{MAX_DAYS}} days.
- Never more than 1 touch per day per lead, across all channels combined.
- Only use a channel if we have a legal basis to use it for this lead in that country, and the details for it (email, mobile number, LinkedIn profile). If unsure, leave it out and say why.
- Every message must refer to the actual call ("thanks for chatting earlier", "sorry I missed you") using the call summary, not generic text.
- Messages are short: SMS and WhatsApp under 300 characters, LinkedIn under 300 characters, email under 120 words with a plain subject line.
- One clear ask per message (book a time, reply with a time, or say no thanks).
- Every email has a working unsubscribe line. Every SMS mentions how to opt out (for example "Reply STOP to opt out") where that is required.
- For WhatsApp on the official Business API, mark which messages need an approved template (messages outside the customer service window, as described in Meta's docs).
- No fake urgency, no fake personal touches, no claims we cannot prove.

STOP CONDITIONS (the sequence stops for this lead immediately, on every channel)
- They reply on any channel (a human then takes over, or the reply goes to AI classification first).
- They book a meeting.
- They opt out on any channel, or are added to the do not call list.
- The email bounces or the number is invalid (stop that channel, keep the others).
- The CRM shows the lead was moved to a stage like customer, lost or do not contact.

Also give me
1. Template variables used in each message, as {{LIKE_THIS}}.
2. A reply classification list (interested, question, not now, not interested, opt out, wrong person, out of office) and what the system does for each.
3. The 3 things most likely to hurt deliverability or get an account restricted on each channel, and how to avoid them.
```

Part 2, build it (in Claude Code, in your campaign project):

```
Add the follow up sequences from {{PATH_TO_SEQUENCE_FILE}} to the campaign system.

Rules
- Read the OFFICIAL API docs of each channel tool before writing code ({{CHANNEL_TOOLS, for example Instantly or Sendkit, Telnyx, Unipile, Meta WhatsApp Business Platform}}). Never guess endpoints or webhook formats. List the docs pages you used.
- One module per channel tool behind one shared interface (send message, receive reply, receive delivery status, opt out).
- Before EVERY send: check the do not call list, the stop conditions, the 1 touch per day rule, and the lead's local time ({{SEND_HOURS}} in their time zone).
- Inbound replies and opt outs from every channel arrive by webhook, are verified, stored, and stop the sequence on all channels right away.
- Idempotent sends: the same step for the same lead can never be sent twice, even after a restart or a retried job.
- Update the CRM with every touch and every reply. Send Slack alerts for replies that show interest.
- Tests: stop on reply, stop on opt out from another channel, no send outside hours, no second touch on the same day, bounce stops only email, duplicate webhook does nothing.
- Development and tests never message real people. Use fake leads and my own test contacts only.
Work in small phases and wait for my OK between them.
```

## What a good output looks like

- 4 short sequence tables, each with no more than your maximum touches, and a stop check on every row.
- Messages that mention the real call, with one ask each.
- A clear reply classification list with an action for each type.
- In Claude Code: tests that prove every stop condition works across channels.

## Common fixes

- **Too many touches:** reply "Cut every sequence to 4 touches over 10 days or less."
- **Messages sound like AI:** reply "Rewrite every message the way a busy person types to a contact: short, plain, no buzzwords, no exclamation marks."
- **Generic messages:** reply "Every first message must use one fact from the call summary."
- **Channels used without consent or details:** reply "Remove any channel where we do not have the right details or a legal basis, and explain each removal."
- **Opt out only stops one channel:** reply "Opt out on any channel must stop every channel. Add a test for it."
