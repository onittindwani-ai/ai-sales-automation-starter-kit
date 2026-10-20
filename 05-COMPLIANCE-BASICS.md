# Compliance Basics (read before you call or message anyone)

**This is general information, not legal advice.** Rules for calls, texts, email and messaging apps are different in every country, sometimes in every state or region, and they change. Before you make a single AI call or send a single automated message, check the rules in every place you will reach, and talk to a local lawyer if you are not sure. You are responsible for following the law where you call.

## Why this matters

AI makes it easy to reach thousands of people in a day. That also makes it easy to break rules at scale. Fines can be large, phone numbers and sending domains can be blocked, and your reputation suffers. Building the rules into your system from day 1 is much easier than adding them later.

## The 7 things to check for every country you reach

1. **Consent.** Do you need the person's permission before you call or message them? Does it matter if it is a business or a private person? Is the rule different for automated or AI calls, for texts, and for messaging apps?
2. **Do not call lists.** Is there an official national do not call list you must check? How often must you check it?
3. **Calling hours.** What hours and days are allowed, in the person's own local time?
4. **AI and recorded voice rules.** Do you have to say at the start that the caller is an AI? Are AI or artificial voices treated like recorded messages, with extra rules?
5. **Call recording.** Do you need to tell people the call is recorded? Do you need everyone's consent?
6. **Opt out.** How must people be able to say stop, and how fast must you act on it?
7. **Data protection.** What are the rules for storing names, numbers, recordings and transcripts, and for how long?

Write the answers down per country, with the date you checked and where you found them. Recheck every few months.

## What to build into your system no matter where you call

These are good practice everywhere and make most rules easier to follow:

- **One do not call list for every channel.** Every call, email, SMS, LinkedIn and WhatsApp message checks it first, every time.
- **Opt out works instantly, everywhere.** If someone says "stop", "remove me", "don't call me" or similar on any channel, the system adds them to the do not call list and stops all channels. The AI analysis prompt in this kit has a `do_not_call` outcome for this ([prompt 05](prompts/05-POST-CALL-ANALYSIS.md)).
- **Say it is an AI.** Our voice caller template ([prompt 04](prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md)) tells the AI to be honest that it is an AI assistant, and never to claim to be a human. That is the safe default.
- **Say who is calling and why.** The business name, and the reason for the call, in the first few seconds.
- **Call in the person's own time zone and allowed hours only.** Store a time zone for every lead. If you do not know it, do not call.
- **Limits.** A daily cap and a cap on attempts per person (for example no more than 2 call attempts on the same day), so nobody is flooded.
- **Keep records.** Where each lead came from, any consent you have, every attempt, and every opt out, with dates.
- **Protect data.** Keep secrets in environment variables, limit who can see transcripts and recordings, and delete data you no longer need.

## Channel notes

- **Calls:** AI calls are a fast moving area of law in many countries. Check specifically for rules about automated, artificial or AI voices.
- **SMS:** many countries and carriers require sender registration and support for opt out words such as STOP. Your SMS provider's docs usually explain the local requirements.
- **Email:** most countries require a real sender identity, an honest subject line, and an easy way to unsubscribe. Some require consent first.
- **WhatsApp:** the official WhatsApp Business Platform has its own rules on opt in and approved message templates. Read Meta's policies before you start.
- **LinkedIn:** LinkedIn's own terms limit automated activity. Keep volumes low and human.

## A simple pre launch check

- [ ] I listed every country, state or region my leads are in.
- [ ] For each one I wrote down the 7 answers above, with the date and source.
- [ ] My system checks the do not call list before every call and message.
- [ ] An opt out on any channel stops all channels, and I tested it.
- [ ] My AI caller says it is an AI and who it is calling for.
- [ ] Calls only go out in allowed hours in the lead's own time zone, and I tested it.
- [ ] If I am not sure about any rule, I asked a local lawyer.
