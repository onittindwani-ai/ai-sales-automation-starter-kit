# Prompt 03: Set Up a New Project in Claude Code

## When to use it

Step 5 of the path, the first time you open Claude Code for your sales system, and any time you want to add a new tool or library to a project.

**The rule we follow:** we never install tools by hand. We give Claude Code the GitHub link (or a screenshot) of the tool and tell it to set it up for the current project. Claude Code reads the instructions, installs what is needed, and checks that it works.

## What to paste

- An empty folder for your project, opened in Claude Code. (To install Claude Code itself, follow the official docs at [code.claude.com/docs](https://code.claude.com/docs).)
- Your step list from [prompt 02](02-DOCUMENT-YOUR-MANUAL-PROCESS.md).
- Optional: the GitHub link or a screenshot of any tool or library you want to use.

## The prompt

Part 1, the first message in a new project:

```
I am a beginner building an AI sales automation system. Set up this folder as a new project for me.

What the system will do (from my manual process): {{ONE_PARAGRAPH_DESCRIPTION}}
My step list:
{{MY_STEP_LIST}}
Language and framework preference: {{YOUR_PREFERENCE_OR_WRITE_YOU_CHOOSE}}
Where I plan to run it: {{FOR_EXAMPLE_RAILWAY_OR_MY_OWN_SERVER_OR_NOT_SURE_YET}}

Please:
1. Before you write any code, explain in plain words the plan for the folder structure and why. Wait for my OK.
2. Set up the project with:
   - a clear folder structure, with one module (file or folder) per outside tool, so I can switch tools later,
   - a .env.example file listing every environment variable with a short comment, and a .gitignore that keeps the real .env and any secrets out of git,
   - a README.md that explains in plain words what the project does, how to run it, and how to test it,
   - a CLAUDE.md file with the project rules (listed below) so you follow them in every future session,
   - a simple test setup with one example test that passes,
   - basic logging, so every run writes what happened.
3. Install everything yourself and run the test to prove the setup works. Show me the result.
4. At the end, tell me in plain words: what you created, how to run it, how to run the tests, and what I need to fill in .env myself.

Project rules to put in CLAUDE.md:
- Never put API keys, passwords or tokens in code, logs, chat or git. Only in environment variables.
- Before using any outside tool's API, read its official API docs first and never guess endpoints, field names or webhook formats.
- Keep each outside tool behind its own small module.
- Every webhook handler must verify the webhook signature if the tool supports it, and must be idempotent (safe if the same webhook arrives twice).
- Write a test for every new feature, and run all tests before saying something is done.
- Explain changes to me in plain words. I am a beginner.
- Ask me before deleting files, changing the database structure, or doing anything that touches real leads, real calls or real money.
```

Part 2, adding a tool or library (use this every time):

```
Here is the GitHub link (or a screenshot) of a tool I want to use: {{GITHUB_LINK_OR_ATTACH_SCREENSHOT}}

Set it up for my current project.
1. Read its official README and docs first. Tell me in 3 lines what it does and whether it fits this project.
2. If it fits, install and configure it yourself, following its official instructions exactly.
3. Add any new environment variables to .env.example (never real values) and tell me which ones I must fill in.
4. Add a small test or example that proves it works, run it, and show me the result.
5. Update the README and CLAUDE.md if anything about running the project changed.
If it does not fit or looks unmaintained or unsafe, tell me why and suggest an alternative instead of installing it.
```

## What a good output looks like

- Claude Code shows you the plan first and waits for your OK.
- After setup, the test runs and passes, and you see the output.
- You get a short list of environment variables to fill in yourself, with no real secrets anywhere in the files.
- A CLAUDE.md exists with the project rules, so new sessions follow them too.

## Common fixes

- **It started writing code before showing a plan:** reply "Stop. Show me the plan in plain words first."
- **It asked you to run install commands yourself:** reply "Please run the setup yourself and show me the result. I do not want to install anything by hand."
- **Too much code at once:** reply "Build only the folder structure and one test today. We add features one at a time."
- **You do not understand a file:** reply "Explain what each file does in one line each, in plain words."
- **Something failed:** paste the full error and say "Find the root cause, fix it, and run the tests again."
