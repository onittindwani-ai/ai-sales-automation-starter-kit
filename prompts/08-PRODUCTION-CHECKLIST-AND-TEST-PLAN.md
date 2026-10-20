# Prompt 08: Production Checklist and Test Plan

## When to use it

- Step 5 of the path, before your first small build touches real data.
- Step 8, before any campaign goes live, and again after every big change.

The lesson behind it, from building more than 500 automations: things that work in testing break in real life. No matter how many times you test, there is always a chance it breaks in the real world. So we follow 3 rules:

1. Test with real, messy data, not perfect examples.
2. Start small. Run it on a few real leads before you run it on thousands.
3. When it goes live, check the real runs every day at the start, and fix what breaks.

## What to paste

- Run this inside your project in Claude Code, so it can read your code.
- A sample of real, messy input you collected in step 2 (with personal details replaced by fake ones).

## The prompt

```
Act as a senior engineer doing a go live review of this AI sales automation project. I am a beginner. Be strict and explain everything in plain words.

About the system
- What it does: {{ONE_PARAGRAPH_DESCRIPTION}}
- Channels: {{CHANNELS}}
- Outside tools: {{TOOLS, for example Ultravox, Twenty CRM, Slack, an AI model}}
- First live run planned: {{NUMBER_OF_LEADS}} real leads in {{COUNTRIES}}
- Sample of real messy input (personal details replaced): {{PATH_TO_SAMPLE_FILE}}

PART 1: REVIEW
Read the code and check each item. For each one answer PASS, FAIL or NOT FOUND, with the file and line, and how to fix any FAIL.
1. Secrets: none in code, logs, tests or git history. All in environment variables.
2. Webhooks: signature verified, fast 2xx response, idempotent on duplicates, raw events stored.
3. Limits: daily limit, concurrency limit and max attempts enforced in code, not only in the frontend.
4. Schedule: no call or message outside allowed days and hours in the lead's own time zone. Leads with no time zone are never contacted.
5. Opt out: one do not call list checked before every call and message on every channel. An opt out on any channel stops all channels right away.
6. AI step: output validated against a schema, retried once, then human review. Safety override for stop words.
7. Retries: backoff on temporary errors, no duplicate calls or messages from retries, alert after the last retry.
8. Logging: every step per lead, with masked personal data. A timeline per lead is visible.
9. Alerts: failures, hot leads and daily summary go to the team channel.
10. Kill switch: one global stop that halts all calls and messages right away.
11. Outside API usage matches the official docs (endpoints, fields, rate limits). Flag anything that looks guessed.
12. Data: personal data stored only where needed, with access limited.

PART 2: TEST PLAN
Write and run automated tests for these cases, using the sample file and fake data. Show me the results.
- Messy input: phone numbers in mixed formats, missing country codes, duplicate rows, empty cells, wrong time zones, extra columns, non English names, a very large file.
- Webhooks: the same event twice, events out of order, a missing transcript, an empty transcript, an unknown event type, a bad signature.
- Outside tools down: the voice tool, the AI model, the CRM and Slack each failing or timing out.
- AI output: invalid JSON, a missing field, an unknown outcome, low confidence.
- Schedule edges: a call due 1 minute before the window closes, a daylight saving change, a weekend, a holiday.
- Opt out: on a call, by SMS reply, by email reply, mid sequence, and added by hand.
- Restart: the server restarts in the middle of a campaign. Nothing is lost and nothing is sent twice.

PART 3: GO LIVE PLAN
Write a short plan I can follow:
1. Dry run: the full system with 5 fake leads that all point to my own test contacts.
2. First live run: no more than {{FIRST_LIVE_BATCH_SIZE}} real leads, on 1 channel, while I watch.
3. Ramp up: how to increase volume step by step, and what must be true before each increase.
4. What to check every day for the first 2 weeks (see below), and what numbers mean something is wrong.
5. How to roll back or stop quickly if something goes wrong.

DAILY CHECK (write this as a checklist I fill in every morning)
- Calls made versus the daily limit. Any call outside allowed hours (must be 0).
- Outcome counts by category, and anything unusual (for example a jump in no_answer or voicemail).
- Listen to or read at least {{NUMBER_TO_SPOT_CHECK}} real calls and compare with the AI's analysis.
- Every needs_human_review item handled.
- Every opt out applied on every channel.
- CRM records match what happened (spot check 5).
- Errors and retries in the logs, and their causes.
- Cost so far versus budget.
- One thing to fix today.
```

## What a good output looks like

- A 12 row review table with PASS, FAIL or NOT FOUND, file and line references, and a fix for every FAIL.
- Tests that actually run, with results shown, covering the messy cases.
- A go live plan that starts with fake leads, then a small real batch.
- A one page daily checklist you can print. A copy is also in [templates/DAILY-RUN-CHECK.md](../templates/DAILY-RUN-CHECK.md).

## Common fixes

- **It marked everything PASS without proof:** reply "For every PASS, show me the exact code that proves it."
- **Tests were written but not run:** reply "Run all the tests now and paste the results."
- **The plan goes live too fast:** reply "Start with fake leads, then at most 20 real leads on 1 channel, and do not increase until 5 days with no critical issues."
- **Something broke live:** pause the campaign first, then paste the lead's log lines and say "Find the root cause, add a test that fails because of it, fix it, and show me the test passing."
