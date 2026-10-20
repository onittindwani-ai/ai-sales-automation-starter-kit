# The 8 Step Path

This is the path I would follow if I started AI automation for sales from zero today. Do the steps in order. Each step has:

- **Goal:** what the step is for.
- **This week:** what to actually do.
- **Done when:** a test you can check. Do not move on until it passes.
- **The mistake to avoid:** a real mistake from our own journey.
- **Prompt:** which prompt in [prompts/](prompts/README.md) to use.

A rough pace: 1 step per week for a beginner, so about 8 weeks to a first real system. Some steps take longer. That is fine. The order matters more than the speed.

| Step | Name | Prompt |
| --- | --- | --- |
| 1 | Find one problem that costs money | [01](prompts/01-FIND-YOUR-MONEY-PROBLEM.md) |
| 2 | Do it by hand first | [02](prompts/02-DOCUMENT-YOUR-MANUAL-PROCESS.md), [04](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md) |
| 3 | Learn how data moves | [00](prompts/00-LEARN-THE-BASICS.md) |
| 4 | Add AI as one step | [05](prompts/05-POST-CALL-ANALYSIS.md) |
| 5 | Go deep on one tool | [03](prompts/03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md), [08](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md) |
| 6 | Pick your channel tools by cost and speed | [04](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md), [07](prompts/07-MULTI-CHANNEL-FOLLOW-UP.md) |
| 7 | Stay flexible with your tools | none, it is a habit |
| 8 | Turn it all into one system | [06](prompts/06-CLAUDE-CODE-BUILD-SPEC.md), [07](prompts/07-MULTI-CHANNEL-FOLLOW-UP.md), [08](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md) |

---

## Step 1. Find one problem that costs money

**Goal:** start from a problem a business owner can see in money, not from a tool. If the owner can see the loss, they will pay you to fix it.

**This week:**

1. Write down 10 businesses you can actually talk to. Start with people who already know you: friends, past clients, past colleagues, local businesses you buy from.
2. Talk to at least 3 of them. Ask where they lose leads, sales or time. Use [prompt 01](prompts/01-FIND-YOUR-MONEY-PROBLEM.md) to prepare the questions and to score what you hear.
3. Pick 1 problem. Write it in one sentence with a number in it, for example: "They get 200 new leads a month and only call back about half of them."
4. Tell the owner your idea for fixing it, and listen to how they change it.

**Done when:**

- [ ] You have 1 problem written in one sentence, with a number the owner gave you.
- [ ] At least 1 real owner said "yes, that costs me money" in their own words.
- [ ] You know what "fixed" would look like for them (more meetings booked, fewer leads lost, less time spent).

**The mistake to avoid (ours):** our first idea was AI calls to people who left items in an online store cart. To find clients, we searched for store owners on Instagram by hand and sent DMs one by one. It took a lot of time, and our first client did not come from Instagram at all. He came from a warm lead, someone who already knew us. And he changed our idea: "if your AI can call people, why not call new people?" That turned a cart recovery idea into a cold calling business. So: start with warm leads, talk to a real buyer early, and let them reshape your idea.

**Prompt:** [01 Find your money problem](prompts/01-FIND-YOUR-MONEY-PROBLEM.md).

---

## Step 2. Do it by hand first

**Goal:** run the whole process manually, a few times, and write down every single step. That list becomes your automation plan.

**This week:**

1. Do the work by hand for real, for at least 5 working days. For an AI calling offer, that means: get a small lead list, load it into a voice calling tool, write the caller prompt ([prompt 04](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md)), run a small batch, then review the results yourself.
2. Every time you do the review, write each action down in the [manual process log](templates/MANUAL-PROCESS-LOG.md): what you opened, what you filtered, what you looked for, what you wrote where, and how long it took.
3. At the end of the week, paste your notes into [prompt 02](prompts/02-DOCUMENT-YOUR-MANUAL-PROCESS.md) and turn them into a clean step list.

**Done when:**

- [ ] You ran the process by hand on at least 5 different days.
- [ ] You have a numbered step list where every step has an input, an action and an output.
- [ ] For every step you have marked: rule (a simple yes or no check), AI (needs reading or judging), or human (needs a person).
- [ ] Someone else could follow your list and get the same result.

**The mistake to avoid (ours):** this one is not a mistake we made, it is the thing that saved us. When we started, we knew nothing about automation, so we did everything by hand. The client sent a lead sheet, we uploaded it to a voice calling tool, wrote the prompt and ran the calls overnight (I live in India and the people we called were in another time zone). Every morning I opened the call history, filtered to calls longer than 30 or 40 seconds (shorter ones were usually voicemail), listened to every call, read every transcript, and typed the interested people into a Google Sheet. Boring, yes. But that list (filter, listen, read, write it down) became our first automation, because we knew every step by heart. The mistake to avoid is skipping this and automating a process you have never run.

**Prompt:** [02 Document your manual process](prompts/02-DOCUMENT-YOUR-MANUAL-PROCESS.md), and [04 AI voice caller system prompt](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md) if your offer is calls.

---

## Step 3. Learn how data moves

**Goal:** understand the 4 ideas that show up in almost every automation: webhooks, HTTP requests, filters and routers.

**This week:**

1. Run [prompt 00](prompts/00-LEARN-THE-BASICS.md) in Claude. Ask follow up questions until you can explain each idea to a friend.
2. Do the small exercises the prompt gives you. Use a free webhook testing site or a tiny test project so you can see a real webhook arrive.
3. Optional: watch a couple of good YouTube videos on the basics of building and development, the basics of running a business, and how to build and understand an AI operating system.
4. Go back to your step list from step 2 and label each step with the idea it uses (for example "call ends" is a webhook, "only calls longer than 40 seconds" is a filter).

**Done when:**

- [ ] You can explain webhook, HTTP request, filter and router in one sentence each, without notes.
- [ ] You have seen a real webhook arrive (on a test site or your own test project).
- [ ] Every step in your step 2 list has a label: webhook, HTTP request, filter, router, AI, or human.

**The mistake to avoid (ours):** we learned these ideas on Make.com, then spent about 19 or 20 months on n8n. You do not need to go through both today. If I started today, I would go straight to Claude Code, but I would learn the basics first. A few hours of basics saves weeks of confusion later.

**Prompt:** [00 Learn the basics](prompts/00-LEARN-THE-BASICS.md).

---

## Step 4. Add AI as one step

**Goal:** use AI only for the part that needs thinking (reading a call, writing a reply, making a decision), and simple rules for everything else.

**This week:**

1. From your step list, pick the one step that needs judgement. For calls, that is "read the call and decide what the person wants".
2. Use [prompt 05](prompts/05-POST-CALL-ANALYSIS.md) to turn that step into an AI step that returns strict JSON.
3. Test it on at least 20 real transcripts from step 2. Compare what the AI decided with what you decided by hand.
4. Write the rules around it: what gets filtered out before the AI, what happens after each AI answer.

**Done when:**

- [ ] The AI step returns valid JSON in the exact same shape every time (test 20 transcripts).
- [ ] The AI agrees with your own manual decision on at least 17 of 20 (or you know why it does not, and you fixed the prompt).
- [ ] Everything before and after the AI step is a simple rule you can write in one line.

**The mistake to avoid (ours):** in our first automation, AI was one box in the middle. A call ended, the webhook rang, a filter took out voicemails, no answers and automatic phone menus (and those got called a second time automatically), and only calls where a real person picked up went to AI (we used ChatGPT as one step). The AI decided: interested, wants a call back, booked a meeting, or something else. Then a router sent each person down the right path. That worked because the AI did one job. The mistake to avoid is making AI the whole system, so you cannot tell what it did or why.

**Prompt:** [05 Post call analysis](prompts/05-POST-CALL-ANALYSIS.md).

---

## Step 5. Go deep on one tool

**Goal:** pick one building tool and stay with it until real things work in production. Today, make that tool Claude Code.

**This week:**

1. Set up Claude Code and your first project with [prompt 03](prompts/03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md).
2. Build one small piece of your system: for example, a tiny backend that receives a webhook, runs your filter, calls the AI analysis from step 4, and writes the result to a sheet or a database.
3. Run it on real, messy data from step 2, not on clean examples you made up.
4. Before it touches real leads, run [prompt 08](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md) and follow its test plan.

**Done when:**

- [ ] Your project runs, and you can explain what every file does in one line (ask Claude Code to explain it to you).
- [ ] It handled at least 20 real, messy inputs, including at least 3 broken ones (missing phone, empty transcript, duplicate), without crashing.
- [ ] Every run is logged, so you can see what happened to each lead.

**The mistake to avoid (ours):** we built more than 500 automations that worked on n8n, and n8n taught us the most important lesson of all: things that work in testing break in real life. I would test a flow again and again, it worked every time, then real people, real data and real calls arrived and something broke. No matter how many times you test, there is always a chance it breaks in the real world. So: test with real, messy data; start small with a few real leads before thousands; and check the real runs every day at the start, then fix what breaks. Also: do not jump between 10 tools. Pick 1 and go deep.

**Prompt:** [03 Set up a project in Claude Code](prompts/03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md), [08 Production checklist](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md).

---

## Step 6. Pick your channel tools by cost and speed

**Goal:** choose one tool per channel (calls, email, LinkedIn, WhatsApp, SMS) based on cost, speed (latency on calls), limits and how good the results are.

**This week:**

1. List the channels your buyer actually answers on. Start with 1 or 2, not all of them.
2. For each channel, compare 2 or 3 tools on: price per minute or per message, call delay (latency), daily or concurrency limits, API and webhook quality, and the quality of the voice or delivery. Our current picks are in [02-OUR-TOOL-STACK.md](02-OUR-TOOL-STACK.md).
3. Do the math for your volume. Example: if one tool costs 14 cents a minute and another 9 cents, then 1,000 minutes is 140 dollars versus 90 dollars. At real volume, that gap decides profit or loss.
4. Read [05-COMPLIANCE-BASICS.md](05-COMPLIANCE-BASICS.md) and check the calling and messaging rules in every country you will reach.

**Done when:**

- [ ] You have one chosen tool per channel you will use, with today's price written down from its own pricing page and the date you checked.
- [ ] You know your cost for 1,000 minutes or 1,000 messages on each.
- [ ] You know the rules for consent, calling hours, opt out and AI disclosure where you call.

**The mistake to avoid (ours):** we moved voice tools 3 times. Back then, Vapi cost us about 14 cents a minute, so we went with Bland at about 9 cents. Later we tried Retell, which moved between about 7 and 11 cents a minute for us and still got too expensive. Since around December 2025 we use Ultravox: pay as you go, great voices, very low delay on the call. These are the prices we paid back then, not today's prices. The lesson: compare on cost per minute, latency and limits, and move when a better or cheaper option appears.

**Prompt:** [04 AI voice caller system prompt](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md), [07 Multi channel follow up](prompts/07-MULTI-CHANNEL-FOLLOW-UP.md).

---

## Step 7. Stay flexible with your tools

**Goal:** do not marry a tool. When a tool gets worse, move.

**This week:**

1. Write down every tool your system depends on, and what you would switch to if it got worse or more expensive.
2. Ask Claude Code to keep each outside tool behind its own small module (one file or folder per tool), so switching later means changing one place, not the whole system. [Prompt 06](prompts/06-CLAUDE-CODE-BUILD-SPEC.md) already asks for this.
3. Set a reminder to recheck prices and quality every 3 months.

**Done when:**

- [ ] You have a list: tool, what it does, backup option.
- [ ] In your code, each outside tool lives in its own module.

**The mistake to avoid (ours):** at the start of 2026 we moved from no code to custom code written with AI. We did not get it right the first time. First Cursor: really good, we built real projects, then its model started making mistakes. So we moved to Google Antigravity, because Google's models were better at that time, and that worked well too. Then Claude Code came, then Codex. Claude Code is what we built our biggest client systems with, and they are running today. Our honest ranking for building automations today: 1, Claude Code or Codex. 2, n8n (it still works, and people still want to learn it). 3, tools like Make and Zapier, which are getting old.

**Prompt:** none. This is a habit, not a task.

---

## Step 8. Turn it all into one system

**Goal:** build the full campaign system: lead sheet upload, daily limit, schedule, AI calls, webhooks, filter, AI analysis, branches, CRM update and multi channel follow up. The full map is in [03-SYSTEM-MAP.md](03-SYSTEM-MAP.md).

**This week (and probably the next few):**

1. Open [03-SYSTEM-MAP.md](03-SYSTEM-MAP.md) and mark which boxes you already have from steps 4 and 5.
2. Fill in [prompt 06](prompts/06-CLAUDE-CODE-BUILD-SPEC.md) and give it to Claude Code. Build in small pieces, one box at a time, and test each one.
3. Add follow up with [prompt 07](prompts/07-MULTI-CHANNEL-FOLLOW-UP.md) only after calls work end to end.
4. Before going live, run [prompt 08](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md) and go through every item.
5. Go live small: 1 campaign, 1 channel, a few real leads, then grow.

**Done when:**

- [ ] You can upload a lead sheet and start a campaign without touching code.
- [ ] The system never goes over the daily limit, and only calls inside the schedule and time zone you set (test it).
- [ ] Every finished call is analysed, routed to the right branch and shows up in the CRM.
- [ ] Opt outs stop all channels for that person, every time (test it).
- [ ] You checked the real runs every day for the first 2 weeks and fixed what broke.

**The mistake to avoid (ours):** look closely at the system we build now. It is the same list from my mornings: filter, listen, read, write it down. The only difference is that Claude Code wrote it as real code, with limits, schedules and the CRM built in. Our journey was by hand, then no code, then code. If you start today you can skip the middle: learn the basics, do it by hand, then build it with Claude Code. The mistake to avoid is starting at step 8.

**Prompt:** [06 Claude Code build spec](prompts/06-CLAUDE-CODE-BUILD-SPEC.md), [07 Multi channel follow up](prompts/07-MULTI-CHANNEL-FOLLOW-UP.md), [08 Production checklist](prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md).

---

## Recap

1. Find one problem that costs money, and let a real buyer shape it.
2. Do it by hand first, and write down every step.
3. Learn how data moves: webhooks, requests, filters, routers. Ask Claude to teach you.
4. Use AI as one step, not the whole system.
5. Go deep on one tool (today, Claude Code), and expect real life to break your tests.
6. Pick channel tools by cost and speed.
7. Stay flexible. When a tool gets worse, move.
8. Turn it into a system with limits, schedules and a CRM.

The one rule: only automate what you have already done by hand and seen work.
