---
title: "Get started with Claude Code hooks"
source: "https://docs.anthropic.com/en/docs/claude-code/hooks-guide"
author:
  - "[[Anthropic]]"
published:
created: 2025-08-14
description: "Learn how to customize and extend Claude Code's behavior by registering shell commands"
tags:
  - "clippings"
---
Claude Code hooks are user-defined shell commands that execute at various points in Claude Code’s lifecycle. Hooks provide deterministic control over Claude Code’s behavior, ensuring certain actions always happen rather than relying on the LLM to choose to run them.

For reference documentation on hooks, see [Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks).

Example use cases for hooks include:

- **Notifications**: Customize how you get notified when Claude Code is awaiting your input or permission to run something.
- **Automatic formatting**: Run `prettier` on.ts files, `gofmt` on.go files, etc. after every file edit.
- **Logging**: Track and count all executed commands for compliance or debugging.
- **Feedback**: Provide automated feedback when Claude Code produces code that does not follow your codebase conventions.
- **Custom permissions**: Block modifications to production files or sensitive directories.

By encoding these rules as hooks rather than prompting instructions, you turn suggestions into app-level code that executes every time it is expected to run.

You must consider the security implication of hooks as you add them, because hooks run automatically during the agent loop with your current environment’s credentials. For example, malicious hooks code can exfiltrate your data. Always review your hooks implementation before registering them.

For full security best practices, see [Security Considerations](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations) in the hooks reference documentation.

## Hook Events Overview

Claude Code provides several hook events that run at different points in the workflow:

- **PreToolUse**: Runs before tool calls (can block them)
- **PostToolUse**: Runs after tool calls complete
- **UserPromptSubmit**: Runs when the user submits a prompt, before Claude processes it
- **Notification**: Runs when Claude Code sends notifications
- **Stop**: Runs when Claude Code finishes responding
- **Subagent Stop**: Runs when subagent tasks complete
- **PreCompact**: Runs before Claude Code is about to run a compact operation
- **SessionStart**: Runs when Claude Code starts a new session or resumes an existing session

Each event receives different data and can control Claude’s behavior in different ways.

## Quickstart

In this quickstart, you’ll add a hook that logs the shell commands that Claude Code runs.

### Prerequisites

Install `jq` for JSON processing in the command line.

### Step 1: Open hooks configuration

Run the `/hooks` [slash command](https://docs.anthropic.com/en/docs/claude-code/slash-commands) and select the `PreToolUse` hook event.

`PreToolUse` hooks run before tool calls and can block them while providing Claude feedback on what to do differently.

### Step 2: Add a matcher

Select `+ Add new matcher…` to run your hook only on Bash tool calls.

Type `Bash` for the matcher.

You can use `*` to match all tools.

### Step 3: Add the hook

Select `+ Add new hook…` and enter this command:

### Step 4: Save your configuration

For storage location, select `User settings` since you’re logging to your home directory. This hook will then apply to all projects, not just your current project.

Then press Esc until you return to the REPL. Your hook is now registered!

### Step 5: Verify your hook

Run `/hooks` again or check `~/.claude/settings.json` to see your configuration:

### Step 6: Test your hook

Ask Claude to run a simple command like `ls` and check your log file:

You should see entries like:

For a complete example implementation, see the [bash command validator example](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py) in our public codebase.

### Code Formatting Hook

Automatically format TypeScript files after editing:

### Custom Notification Hook

Get desktop notifications when Claude needs input:

### File Protection Hook

Block edits to sensitive files:

## Learn more

- For reference documentation on hooks, see [Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks).
- For comprehensive security best practices and safety guidelines, see [Security Considerations](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations) in the hooks reference documentation.
- For troubleshooting steps and debugging techniques, see [Debugging](https://docs.anthropic.com/en/docs/claude-code/hooks#debugging) in the hooks reference documentation.