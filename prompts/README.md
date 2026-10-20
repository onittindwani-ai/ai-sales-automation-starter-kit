# Prompts

9 prompts, one per job in the path. Each file has the same parts:

- **When to use it:** the step and the moment.
- **What to paste:** what you need ready before you start.
- **The prompt:** in a code block. Copy the whole block.
- **What a good output looks like:** so you can tell if it worked.
- **Common fixes:** what to say when the output is not right.

## How to use them

1. Copy the whole prompt from the code block.
2. Replace every `{{PLACEHOLDER}}` with your own details. Placeholders are in capital letters inside double curly brackets. If you do not know a value yet, write "not sure yet" and the prompt will handle it.
3. Paste it into Claude (prompts 00, 01, 02, 04, 05, 07) or into Claude Code inside your project folder (prompts 03, 06, 08).
4. Never paste real API keys, passwords or tokens into any prompt. Keep them in environment variables. The prompts tell the AI to do the same.

## The list

| # | Prompt | Step | Where to run it |
| --- | --- | --- | --- |
| 00 | [Learn the basics](00-LEARN-THE-BASICS.md) | 3 | Claude |
| 01 | [Find your money problem](01-FIND-YOUR-MONEY-PROBLEM.md) | 1 | Claude |
| 02 | [Document your manual process](02-DOCUMENT-YOUR-MANUAL-PROCESS.md) | 2 | Claude |
| 03 | [Set up a project in Claude Code](03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md) | 5 | Claude Code |
| 04 | [AI voice caller system prompt](04-AI-VOICE-CALLER-SYSTEM-PROMPT.md) | 2, 6 | Your voice tool (for example Ultravox) |
| 05 | [Post call analysis](05-POST-CALL-ANALYSIS.md) | 4 | Your backend, through an AI model's API |
| 06 | [Claude Code build spec](06-CLAUDE-CODE-BUILD-SPEC.md) | 8 | Claude Code |
| 07 | [Multi channel follow up](07-MULTI-CHANNEL-FOLLOW-UP.md) | 6, 8 | Claude, then Claude Code |
| 08 | [Production checklist and test plan](08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md) | 5, 8 | Claude Code |

Back to the [main README](../README.md).
