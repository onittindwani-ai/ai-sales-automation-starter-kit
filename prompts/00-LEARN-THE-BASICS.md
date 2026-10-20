# Prompt 00: Learn the Basics (webhooks, HTTP requests, filters, routers)

## When to use it

Step 3 of the path. Use it before you build anything. It turns Claude into a patient teacher for the 4 ideas that show up in almost every automation.

The short version from the video, if you just want a quick start:

```
Explain webhooks, HTTP requests, filters and routers to me like a beginner, with one simple sales example for each.
```

The full version below goes further: it checks your understanding, gives you small exercises and maps the ideas onto your own process.

## What to paste

- Your step list from step 2 (or a few lines about your process if you do not have it yet).
- How much you already know (for example "never coded" or "used Zapier a little").

## The prompt

```
You are a patient teacher who explains technical ideas to complete beginners using everyday words.
I want to learn AI automation for sales. Teach me the 4 basic ideas of moving data between apps:
1. webhooks
2. HTTP requests
3. filters
4. routers

About me:
- What I already know: {{WHAT_I_ALREADY_KNOW}}
- The business process I want to automate: {{MY_PROCESS_IN_ONE_OR_TWO_SENTENCES}}
- My step list from doing it by hand (may be empty): {{MY_STEP_LIST}}

How to teach me:
- One idea at a time, in the order above. Do not move to the next idea until I say "next".
- For each idea give me:
  a) a one sentence definition in plain words (no jargon, or explain any jargon you use),
  b) an everyday comparison (for example a doorbell for a webhook),
  c) one simple sales example (AI calls, follow up emails, CRM updates),
  d) what it looks like in real life: a short, clearly labelled example of the data (a small JSON example is fine), with every field explained,
  e) one common beginner mistake with it,
  f) a 2 question quiz. Wait for my answers and correct me kindly.
- After all 4 ideas, show me how they work together in one flow:
  a call ends, a webhook arrives, a filter removes voicemails, AI reads the call, a router sends the lead down the right path, an HTTP request updates the CRM.
  Draw it as a simple numbered list, and label each step with the idea it uses.
- Then give me 3 small hands on exercises I can do today without paying for anything
  (for example: receive a real webhook on a free webhook testing website, send an HTTP request from my browser or a free API tool, write a filter rule in plain words).
  Give exact click by click steps, and tell me what I should see if it worked.
- Finally, take my step list and label every step: webhook, HTTP request, filter, router, AI, or human.
  If my step list is empty, ask me 5 short questions about my process first.

Rules:
- Short paragraphs. Numbers as digits.
- Never ask me for passwords, API keys or tokens.
- If I say "I don't get it", explain it again in a completely different way, simpler.
```

## What a good output looks like

- Claude teaches only the first idea and waits for you.
- The examples are about sales (calls, leads, CRM), not random topics.
- The data examples are tiny and every field is explained.
- At the end, your own step list comes back with a label on every step.

## Common fixes

- **Too technical:** reply "Explain that again like I am 12, with no technical words."
- **Too long:** reply "Half as long, please. Only the definition, the comparison and the sales example."
- **It skipped ahead:** reply "Stop. Only idea 1 until I say next."
- **You want to see it, not read it:** reply "Give me an exercise where I can see a real webhook arrive in the next 10 minutes, step by step."
