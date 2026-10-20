# AI Sales Automation Starter Kit

The exact path I would follow if I had to learn AI automation for sales from zero today. 8 steps in order, the prompts that do the heavy lifting, the full tool stack we use right now for every channel, and a map of the system we build today.

By Onit Tindwani, co founder and CTO of Sendora AI. Over the last 2 and a half years we went from knowing nothing about automation to building complete AI sales systems with Claude Code, and along the way we booked over 1,600 qualified appointments and more than 10 million dollars in client pipeline for our clients.

**The video board (FigJam):** https://www.figma.com/board/mj8Hn6dpYOkjC5vBCXXPpL/AI-Sales-Automation-Starter-Kit--8-Step-Path-Board--Public--view-only-

## Who this is for

- You want to build AI sales systems (AI calls, follow ups, CRM updates) for your own business or for clients.
- You are a beginner, or you know a little no code automation and want to move to building with Claude Code.
- You do not need to know how to code. You do need to be willing to do the work by hand first.

## Start here (in this order)

1. **Open the board** at the link above and look at all 8 steps on one page. It takes 2 minutes.
2. **Read [01-THE-8-STEP-PATH.md](01-THE-8-STEP-PATH.md).** Every step has a goal, what to do this week, a "done when" test you can check, the real mistake to avoid, and the prompt to use.
3. **Run [prompt 00](prompts/00-LEARN-THE-BASICS.md)** in Claude today. It teaches you webhooks, HTTP requests, filters and routers with sales examples. This is the foundation for everything else.
4. **Work through the steps one at a time.** Do not skip step 2 (doing it by hand). It is the reason everything after it works.
5. **Use [02-OUR-TOOL-STACK.md](02-OUR-TOOL-STACK.md)** when you reach step 6 and need to pick tools.
6. **Use [03-SYSTEM-MAP.md](03-SYSTEM-MAP.md)** when you reach step 8 and are ready to build the full system.
7. **Read [05-COMPLIANCE-BASICS.md](05-COMPLIANCE-BASICS.md) before you make a single AI call** or send a single automated message.

Stuck on a word? Look it up in [04-GLOSSARY.md](04-GLOSSARY.md).

## What is inside

| File | What it gives you |
| --- | --- |
| [01-THE-8-STEP-PATH.md](01-THE-8-STEP-PATH.md) | The 8 steps, week by week, with checkable tests and the mistakes we made |
| [02-OUR-TOOL-STACK.md](02-OUR-TOOL-STACK.md) | Every tool we use today: calls, LinkedIn, WhatsApp, email, SMS, backend, frontend, CRM, AI models, DNS, team chat, UI |
| [03-SYSTEM-MAP.md](03-SYSTEM-MAP.md) | The step 8 system as a diagram and a table, with the real tool at every box |
| [04-GLOSSARY.md](04-GLOSSARY.md) | Every technical word in this kit, in plain words |
| [05-COMPLIANCE-BASICS.md](05-COMPLIANCE-BASICS.md) | Consent, opt out, AI disclosure and calling hours: what to check before you start |
| [prompts/](prompts/README.md) | 9 detailed prompts, from learning the basics to a full Claude Code build spec and a production test plan |
| [templates/](templates/README.md) | A lead sheet template, a manual process log and a daily run check sheet |

## The prompts at a glance

| # | Prompt | Use it in step |
| --- | --- | --- |
| 00 | [Learn the basics with Claude](prompts/00-LEARN-THE-BASICS.md) | 3 |
| 01 | [Find your money problem](prompts/01-FIND-YOUR-MONEY-PROBLEM.md) | 1 |
| 02 | [Turn your manual process into a step list](prompts/02-DOCUMENT-YOUR-MANUAL-PROCESS.md) | 2 |
| 03 | [Set up a new project in Claude Code](prompts/03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md) | 5 |
| 04 | [AI voice caller system prompt](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md) | 2, 6 |
| 05 | [Post call analysis (strict JSON)](prompts/05-POST-CALL-ANALYSIS.md) | 4 |
| 06 | [Claude Code build spec for the campaign system](prompts/06-CLAUDE-CODE-BUILD-SPEC.md) | 8 |
| 07 | [Multi channel follow up](prompts/07-MULTI-CHANNEL-FOLLOW-UP.md) | 6, 8 |
| 08 | [Production checklist and test plan](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md) | 5, 8 |

## The one rule

Only automate what you have already done by hand and seen work.

## Honest notes

- Everything about our journey here is our own experience. Your results depend on your offer, your market, your data and your work.
- Tools and prices change all the time. Every price in this kit is either clearly marked as what we paid back then, or not given at all. Check each tool's own pricing page before you buy.
- Calling and messaging rules differ by country. This kit is general information, not legal advice. Check the rules where you call.
- Tool names are the ones we use. We have no paid deal with any of them.

## Check the kit yourself

The kit has a small checker that makes sure every link works and nothing private slipped in:

```
python3 tests/check_kit.py
```

It runs on every change through GitHub Actions ([.github/workflows/check.yml](.github/workflows/check.yml)).

## License

MIT. Use it, copy it, change it, share it. See [LICENSE](LICENSE). Version history is in [CHANGELOG.md](CHANGELOG.md).
