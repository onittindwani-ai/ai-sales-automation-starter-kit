# Our Tool Stack (as of October 2026)

These are the exact tools we use today to build and run AI sales systems, grouped by job, with what each one does for us and why we picked it.

Read this first:

- **This is our stack, not the only right stack.** Use it as a starting point. Step 7 of the path says it plainly: when a tool gets worse, move.
- **No current prices here on purpose.** Prices change all the time. Always check each tool's own pricing page on the day you buy, and write down the date.
- **Every link below is the tool's official website.** We checked that each one loads on 20 October 2026.
- **No paid deals.** We are not paid to mention any of these tools.
- You do not need all of this on day 1. For a first system you need: one calling tool, Claude Code, somewhere to run your backend, and a CRM. Add channels one at a time.

## The stack at a glance

| Area | Tool(s) we use |
| --- | --- |
| Calls (AI voice) | Ultravox |
| LinkedIn | Unipile |
| WhatsApp | Unipile, or your own WhatsApp Business API setup from Meta |
| Email | Instantly and Sendkit |
| SMS | Telnyx |
| Backend deployment | Hetzner, Netcup, Railway |
| Frontend deployment | Vercel |
| AI coding | Claude Code (mainly, with the Opus 5.5 and Fable 5.1 models) and Codex |
| CRM (our own) | Twenty CRM |
| DNS and domains | Cloudflare |
| Team communication | Slack |
| UI components and design ideas | shadcn/ui, Magic UI, MUI, Dribbble |

---

## 1. Outreach channels

### Calls: Ultravox

- **Website:** [ultravox.ai](https://www.ultravox.ai) (developer docs: [docs.ultravox.ai](https://docs.ultravox.ai))
- **What it does for us:** runs our AI voice calls. Our backend starts each call through the Ultravox API, and when a call ends, Ultravox sends a webhook back to our backend with the result, so our system can analyse it.
- **Why we picked it:** the best voice tool we have used. Great voice models, proper calling limits, pay as you go pricing, very low delay on the call (latency), and consistently great results. We have used it since around December 2025.
- **Good to know:** Ultravox does not give you phone numbers by itself. Its docs list native support for Twilio, Telnyx, Plivo and Exotel, plus SIP (checked 20 October 2026). The Ultravox website also says Ultravox has been acquired by Inworld (seen 20 October 2026).

### LinkedIn: Unipile

- **Website:** [unipile.com](https://www.unipile.com) (developer docs: [developer.unipile.com](https://developer.unipile.com))
- **What it does for us:** connects LinkedIn accounts to our own backend through one API, so our system can send connection requests and messages and read replies as part of a sequence.
- **Why we picked it:** one API for several messaging channels (we also use it for WhatsApp), so our code talks to one tool instead of many.
- **Good to know:** LinkedIn has its own rules and limits on automated activity. Keep daily volumes low and human, and read LinkedIn's terms before you automate anything.

### WhatsApp: Unipile, or your own WhatsApp Business API setup from Meta

- **Option A, Unipile:** [unipile.com](https://www.unipile.com). The same API we use for LinkedIn. The fastest way to start.
- **Option B, your own WhatsApp Business API setup from Meta:** [WhatsApp Business Platform docs](https://developers.facebook.com/docs/whatsapp) and [business.whatsapp.com](https://business.whatsapp.com). This is the official route. It needs business verification and documents, takes longer to set up, and comes with Meta's rules on approved message templates and opt in.
- **How to choose:** if you are testing an idea, start with the faster route. If WhatsApp will be a main channel at volume, plan for the official Meta setup early, because verification can take time.

### Email: Instantly and Sendkit

- **Websites:** [instantly.ai](https://instantly.ai) (API docs: [developer.instantly.ai](https://developer.instantly.ai)) and [sendkit.ai](https://www.sendkit.ai)
- **What they do for us:** send cold email sequences from warmed up sending accounts, track replies, and handle sending limits and deliverability (getting into the inbox, not spam).
- **Why we use both:** having two lets us split volume, compare results, and keep a backup ready.
- **Good to know:** send cold email from separate domains, not your main company domain, so your main domain's reputation stays safe. Set up SPF, DKIM and DMARC on every sending domain (see the [glossary](04-GLOSSARY.md)).

### SMS: Telnyx

- **Website:** [telnyx.com](https://telnyx.com) (developer docs: [developers.telnyx.com](https://developers.telnyx.com))
- **What it does for us:** sends and receives text messages from our backend through its API, with webhooks for replies and delivery status.
- **Why we picked it:** a direct API for messaging and phone numbers, with webhooks that fit the same pattern as the rest of our system.
- **Good to know:** SMS has strict rules in many countries (for example sender registration and opt out words like STOP). Check [05-COMPLIANCE-BASICS.md](05-COMPLIANCE-BASICS.md) before you send.

---

## 2. Backend and frontend deployment

The backend is the part of your system that runs on a server: it receives webhooks, starts calls, runs the AI analysis and talks to the CRM. The frontend is the screen you use: upload a lead sheet, start a campaign, see results.

### Backend: Hetzner, Netcup, Railway

| Tool | Website | What it does for us | Why |
| --- | --- | --- | --- |
| Hetzner | [hetzner.com](https://www.hetzner.com) | Virtual servers where our backends run all the time | Strong servers for the money, good for always on workers |
| Netcup | [netcup.com](https://www.netcup.com) | More virtual servers | Another good value server provider, useful to spread systems out |
| Railway | [railway.com](https://railway.com) | Runs a backend straight from a code repository, without managing a server | Fastest way to get a backend online. Great for beginners and small projects |

**For a beginner:** start with Railway. You connect your code and it runs. Move to your own server (Hetzner or Netcup) later, when you need more control or lower cost at scale.

### Frontend: Vercel

- **Website:** [vercel.com](https://vercel.com)
- **What it does for us:** hosts our frontends (dashboards, upload screens). Every change you push goes online in a few minutes.
- **Why:** very easy to use, especially for apps built with Next.js and React.

---

## 3. AI coding and AI models

### Claude Code (our main tool)

- **Website:** [claude.com/product/claude-code](https://claude.com/product/claude-code) (docs: [code.claude.com/docs](https://code.claude.com/docs))
- **What it does for us:** writes, runs and fixes the code for our systems. We describe what we want in plain English, and Claude Code builds it in our project. Our biggest client systems were built with it and are running today.
- **Models we mainly use:** Opus 5.5 and Fable 5.1.
- **How we set up new tools:** we give Claude Code the GitHub link (or a screenshot) of a tool and tell it to set it up for the current project. We do not install things by hand. See [prompt 03](prompts/03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md).

### Codex

- **Website:** [developers.openai.com/codex](https://developers.openai.com/codex)
- **What it does for us:** OpenAI's coding agent. Part of our current stack next to Claude Code.
- **Why both:** models get better and worse over time. Having two strong coding tools means we can switch when one struggles (step 7: stay flexible).

### Our honest ranking for building automations today

1. Claude Code or Codex.
2. [n8n](https://n8n.io). It still works, and people still want to learn it. We built more than 500 automations on it.
3. Tools like [Make](https://www.make.com) and Zapier. They are getting old.

---

## 4. CRM: Twenty CRM

- **Website:** [twenty.com](https://twenty.com) (docs: [docs.twenty.com](https://docs.twenty.com))
- **What it does for us:** our own CRM, where every lead, call result, follow up and meeting lives.
- **Why:** it is open source with an API, so our custom code can create and update records, and we stay in control of our data.
- **For client systems:** clients often already have a CRM. We connect our custom code to [HubSpot](https://www.hubspot.com) and [GoHighLevel](https://www.gohighlevel.com) too, using their APIs, webhooks and workflows. Your system should update whatever CRM the business already uses.

---

## 5. DNS and domains: Cloudflare

- **Website:** [cloudflare.com](https://www.cloudflare.com)
- **What it does for us:** manages our domains and DNS (where each domain points), and protects our sites and backends.
- **Why:** fast, reliable, and one place for all domains. Also where we set up the DNS records for email sending domains (SPF, DKIM, DMARC).

---

## 6. Team communication: Slack

- **Website:** [slack.com](https://slack.com)
- **What it does for us:** our team chat, and the place our systems send alerts: a meeting was booked, a hot lead wants a call back, a run failed, a daily summary.
- **Why:** alerts in a chat channel get seen fast. A system that fails quietly is the worst kind.

---

## 7. UI components and design references

| Tool | Website | What it does for us |
| --- | --- | --- |
| shadcn/ui | [ui.shadcn.com](https://ui.shadcn.com) | Clean, copy in React components (buttons, tables, forms) for our frontends |
| Magic UI | [magicui.design](https://magicui.design) | Animated components for nicer looking pages |
| MUI | [mui.com](https://mui.com) | A large React component library, good for data heavy dashboards |
| Dribbble | [dribbble.com](https://dribbble.com) | Design ideas: we find a layout we like and show a screenshot to Claude Code as a reference |

**Tip:** tell Claude Code which component library to use at the start of a project (for example "use shadcn/ui"), so every screen looks consistent.

---

## 8. Our voice tool journey, with what we paid back then

These are **past prices, what we paid at the time**, from our own memory. They are **not today's prices**. Today's prices are different (some higher, some lower), so check each tool's pricing page yourself.

| Order | Tool | What we paid back then, per minute | What happened |
| --- | --- | --- | --- |
| 1 | [Vapi](https://vapi.ai) | About 14 cents | The most famous voice tool when we started, but expensive for us |
| 2 | [Bland](https://www.bland.ai) | About 9 cents | Cheaper for us back then. We ran our first cold calling campaigns on it |
| 3 | [Retell](https://www.retellai.com) | Between about 7 and 11 cents | Widely used, but it still got too expensive for us |
| 4 | [Ultravox](https://www.ultravox.ai) | Pay as you go | Since around December 2025. The best voice tool we have used |

**How to compare voice tools yourself:** price per minute all in (platform, model, voice, phone line), delay on the call, how many calls can run at the same time, API and webhook quality, and how natural the voice sounds to your buyers. Run the same 10 test calls on each before you decide.
