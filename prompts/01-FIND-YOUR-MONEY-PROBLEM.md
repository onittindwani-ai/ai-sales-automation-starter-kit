# Prompt 01: Find Your Money Problem

## When to use it

Step 1 of the path. Use it twice:

1. **Before** you talk to a business owner, to prepare your questions.
2. **After** the conversation, to score the problems you heard and pick one.

Remember the lesson from our start: talk to people who already know you first, and let the buyer change your idea.

## What to paste

- Who you will talk to (type of business, size, their role). No private details are needed.
- After the talk: your notes, as rough as they are.

## The prompt

```
You are an experienced sales operations consultant. You help beginners find one business problem that clearly costs money and can be fixed with AI automation for sales (AI calls, follow up messages, CRM updates, lead handling).

PART A: PREPARE THE CONVERSATION
The person I will talk to:
- Type of business: {{TYPE_OF_BUSINESS}}
- Size (team, rough number of leads or customers per month if known): {{SIZE}}
- Their role: {{ROLE}}
- How I know them: {{HOW_I_KNOW_THEM}}

Give me:
1. A 20 minute conversation plan with 10 to 12 open questions, in a natural order. Focus on: where leads come from, how fast they are followed up, how many are never contacted, missed calls, no shows, how much a customer is worth, how much time the team spends on repetitive sales tasks, and which tools they already use (CRM, phone, email).
2. For each question, one follow up that turns a vague answer into a number (for example "roughly how many per week?").
3. 3 questions that help me understand how they would judge success.
4. Things I must NOT do in the conversation (for example pitching too early, promising results).

PART B: SCORE WHAT I HEARD (I will paste my notes below after the conversation)
My notes:
{{MY_CONVERSATION_NOTES}}

From my notes:
1. List every problem you can find, in one sentence each, using the owner's own words where possible.
2. Score each problem from 1 to 5 on:
   - Money: can the owner see the money being lost?
   - Measurable: is there a number we can track before and after?
   - Frequency: does it happen every day or week?
   - Fixable: can AI automation for sales realistically fix a big part of it?
   - Urgency: does the owner want it fixed now?
   - Access: can I get the data and access needed (lead lists, CRM, phone line)?
   Show a table with the scores and a total out of 30.
3. Estimate the money at stake for the top 2 problems, showing your math step by step, using ONLY numbers from my notes. If a number is missing, write "missing: ask about X" instead of guessing.
4. Pick the best problem and write it as one sentence with a number in it.
5. Describe what "fixed" would look like in 30 days, as something we could measure.
6. Suggest the smallest manual test I could run by hand next week to prove the idea (step 2 of the path: do it by hand first).
7. List the questions I still need to ask the owner.

Rules:
- Never invent numbers. Mark every assumption clearly.
- Plain words. Numbers as digits.
- If my notes are thin, say so and tell me what to ask next time.
```

## What a good output looks like

- Part A: a short, friendly question list, not a sales script.
- Part B: a scoring table, money math that only uses numbers from your notes, and "missing" markers where you did not ask.
- One clear problem sentence, for example: "About 40 percent of new web leads are never called back, and each customer is worth about 2,000 dollars a year."
- A small manual test you can do next week.

## Common fixes

- **It made up numbers:** reply "Remove every number that is not in my notes. Mark them as missing instead."
- **All problems scored the same:** reply "Be stricter. Only one problem can score above 24."
- **The test is too big:** reply "Make the manual test smaller: 1 week, 1 channel, under 50 leads, no code."
- **No problem is good enough:** that is a real answer. Talk to 2 more businesses before you build anything.
