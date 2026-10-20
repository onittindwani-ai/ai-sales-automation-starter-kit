# Glossary (plain words)

Every technical word in this kit, explained simply. Sorted by topic, then A to Z inside each topic.

## Moving data (the 4 big ideas from step 3)

| Word | Plain meaning | Sales example |
| --- | --- | --- |
| Webhook | A doorbell. When something happens in one app, it rings a bell (sends a message) in another app, right away | A call ends, and the calling tool sends the result to your system |
| HTTP request | The opposite of a webhook. Your system knocks on another app's door to ask for something or send something | Your system asks the calling tool to start a call |
| Filter | A gate that only lets the right things through | Only calls longer than 40 seconds go on to AI analysis |
| Router | A switch that sends each thing down a different path | Interested leads go to sales, call backs go to the calendar |

## Building blocks

| Word | Plain meaning |
| --- | --- |
| API | The menu of things an app lets other programs do with it, like "start a call" or "create a contact" |
| API key | A secret password that lets your system use an app's API. Never share it, never put it in your code or in a chat. Keep it in environment variables |
| Backend | The part of your system that runs on a server, out of sight: receives webhooks, starts calls, runs the AI, updates the CRM |
| CSV | A simple spreadsheet file. Each row is a lead, each column is a detail (name, phone, time zone) |
| Database | Where your system stores its data in an organised way, so nothing gets lost |
| Deployment | Putting your code on a server so it runs all the time, not just on your laptop |
| Endpoint | One specific address in an API, like a single item on the menu |
| Environment variables | A safe place on the server for secrets like API keys, kept outside your code |
| Frontend | The screens you see and click: upload a sheet, start a campaign, see results |
| JSON | A simple, strict text format computers use to pass data, like `{"outcome": "interested"}` |
| Payload | The data inside a webhook or a request |
| Queue | A waiting line for jobs. Leads wait in the queue until it is their turn to be called |
| Repository (repo) | The folder that holds all the code of a project, usually on GitHub |
| Schema | The exact shape data must have, like a form with fixed fields |
| Server | A computer that is always on, in a data centre, running your backend |

## Making it reliable

| Word | Plain meaning |
| --- | --- |
| Concurrency | How many things happen at the same time, like how many calls run at once |
| Idempotency | Doing the same thing twice has the same effect as doing it once. If a webhook arrives twice, the lead is not called twice and the CRM is not updated twice |
| Logs | A diary your system writes: what happened, when, and to which lead |
| Production | The real world: real leads, real calls, real money. The opposite of testing |
| Rate limit | A rule from an app about how many requests you can send per minute or per day |
| Retry | Trying again after a failure, usually after waiting a little longer each time |
| Signature (webhook) | A secret check that proves a webhook really came from the tool, not from someone pretending |
| Staging or test mode | A safe copy of your system for testing, that does not touch real leads |

## Calls

| Word | Plain meaning |
| --- | --- |
| AI voice caller | An AI that talks on the phone like a person, following a prompt you write |
| Batch calling | Calling a whole list in one go |
| Carrier (telephony provider) | The company that gives you phone numbers and connects calls to the phone network |
| Double dial | Calling a second time when the first call hit voicemail or nobody picked up |
| IVR (phone menu) | The automatic "press 1 for sales" menu some businesses have |
| Latency | The delay between when the person stops talking and when the AI answers. Lower is better and sounds more human |
| SIP | A standard way to connect calls between phone systems over the internet |
| System prompt | The instructions you give the AI caller: who it is, what it wants, how to talk |
| Transcript | The call written out as text, line by line |
| Voicemail detection | Working out that a machine, not a person, answered |

## AI

| Word | Plain meaning |
| --- | --- |
| AI agent | An AI that can take actions (look things up, call tools), not just answer |
| Claude Code | An AI coding tool from Anthropic that writes, runs and fixes code in your project from plain English instructions |
| Codex | An AI coding agent from OpenAI |
| Confidence | How sure the AI says it is about its answer, from 0 to 1. Low confidence means a human should check |
| Model | The AI brain itself. Different models are better at different jobs and cost different amounts |
| Placeholder | A slot in a prompt like `{{COMPANY_NAME}}` that you replace with your own details |
| Prompt | The instructions you give an AI |
| RAG | Retrieval augmented generation: the AI looks things up in your own documents before answering |

## Sales and outreach

| Word | Plain meaning |
| --- | --- |
| AI SDR | An AI sales development rep: a system that reaches out to leads, qualifies them and books meetings |
| Cold outreach | Reaching people who do not know you yet |
| CRM | Customer relationship management: the app where every lead, call, note and deal lives |
| Deliverability | Whether your emails land in the inbox instead of spam |
| DKIM, SPF, DMARC | 3 DNS settings that prove your emails really come from your domain. Without them, cold email goes to spam |
| DNS | The internet's address book. It says where your domain points |
| Do not call list (DNC) | A list of people who must never be contacted. Your own list, plus any official national lists where you call |
| Opt out | When a person says stop. You must stop on every channel, right away |
| Qualified | A lead who fits what you sell and has a real need, budget or timing |
| Sequence | A planned series of follow ups across days and channels |
| Warm lead | Someone who already knows you or your business |
