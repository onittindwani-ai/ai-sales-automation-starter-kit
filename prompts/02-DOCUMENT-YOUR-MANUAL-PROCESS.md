# Prompt 02: Turn Your Manual Process into a Step List

## When to use it

Step 2 of the path, at the end of each week of doing the work by hand. The lesson from our own start: when you do something by hand, write down every step you take. That list is your automation plan.

Our own morning list looked like this, and it became our first automation:

1. Open the call history.
2. Filter to calls longer than 30 or 40 seconds (shorter ones were usually voicemail).
3. Listen to every call.
4. Read every transcript.
5. If the person sounded interested, type their name, email and phone number into a Google Sheet.

## What to paste

- Your notes from the [manual process log](../templates/MANUAL-PROCESS-LOG.md), exactly as you wrote them. Messy is fine.
- What the process is for, in one sentence.

## The prompt

```
You are an automation architect. Your job is to turn my messy notes about a manual sales process into a clean, numbered step list that could later be automated. Do not design any software yet. Only document what I actually did.

What the process is for: {{WHAT_THE_PROCESS_IS_FOR}}
Tools I used by hand: {{TOOLS_I_USED}}
How many days I did it: {{NUMBER_OF_DAYS}}
My raw notes:
{{MY_RAW_NOTES}}

Do this:
1. Write the process as a numbered list. For every step give:
   - Trigger: what starts this step
   - Input: what information I needed
   - Action: exactly what I did (click, read, decide, type)
   - Output: what came out of it and where it went
   - Time: how long it took me (from my notes, or "unknown")
   - Type: RULE (a simple yes or no check anyone could do), AI (needs reading, judging or writing), or HUMAN (needs a person, for example a sales call or a final decision)
2. For every decision I made, write the rule I was really using, as an if/then sentence.
   Example: "If the call was shorter than 40 seconds, skip it, because it was usually voicemail."
   If my notes do not show the rule, write "rule unclear" and ask me.
3. List the edge cases I hit (missing phone number, wrong person, duplicate lead, someone asking to be removed, and so on) and what I did with each. Add any common edge cases I have not mentioned yet, clearly marked "not seen yet".
4. List every piece of data that moved between tools, as a table: data, from, to.
5. Mark the 3 steps that took the most time. These are the best first things to automate.
6. Mark any step where a mistake would hurt a real person or the business (for example calling someone who asked not to be called). These need extra checks later.
7. End with a list of questions I need to answer before this can be automated.

Rules:
- Use only what is in my notes. Do not invent steps. If something seems missing, ask.
- Plain words. Numbers as digits.
- Do not suggest tools or code yet.
```

## What a good output looks like

- A numbered list where every step has a trigger, input, action, output, time and type.
- Your gut feelings turned into clear if/then rules (or flagged as "rule unclear").
- A short table of data moving between tools.
- The 3 slowest steps marked as your first automation targets.

## Common fixes

- **It added steps you never did:** reply "Remove every step that is not in my notes."
- **Too many AI steps:** reply "Be strict. Only mark a step AI if a simple rule cannot do it."
- **Rules are vague:** reply "Rewrite every rule with a number or an exact word in it."
- **You want to share it:** reply "Turn this into a one page checklist someone else could follow tomorrow."
