---
title: "Slash commands"
source: "https://docs.anthropic.com/en/docs/claude-code/slash-commands"
author:
  - "[[Anthropic]]"
published:
created: 2025-08-14
description: "Control Claude's behavior during an interactive session with slash commands."
tags:
  - "clippings"
---
## Built-in slash commands

| Command | Purpose |
| --- | --- |
| `/add-dir` | Add additional working directories |
| `/agents` | Manage custom AI subagents for specialized tasks |
| `/bug` | Report bugs (sends conversation to Anthropic) |
| `/clear` | Clear conversation history |
| `/compact [instructions]` | Compact conversation with optional focus instructions |
| `/config` | View/modify configuration |
| `/cost` | Show token usage statistics |
| `/doctor` | Checks the health of your Claude Code installation |
| `/help` | Get usage help |
| `/init` | Initialize project with CLAUDE.md guide |
| `/login` | Switch Anthropic accounts |
| `/logout` | Sign out from your Anthropic account |
| `/mcp` | Manage MCP server connections and OAuth authentication |
| `/memory` | Edit CLAUDE.md memory files |
| `/model` | Select or change the AI model |
| `/permissions` | View or update [permissions](https://docs.anthropic.com/en/docs/claude-code/iam#configuring-permissions) |
| `/pr_comments` | View pull request comments |
| `/review` | Request code review |
| `/status` | View account and system statuses |
| `/terminal-setup` | Install Shift+Enter key binding for newlines (iTerm2 and VSCode only) |
| `/vim` | Enter vim mode for alternating insert and command modes |

## Custom slash commands

Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands are organized by scope (project-specific or personal) and support namespacing through directory structures.

### Syntax

#### Parameters

| Parameter | Description |
| --- | --- |
| `<command-name>` | Name derived from the Markdown filename (without `.md` extension) |
| `[arguments]` | Optional arguments passed to the command |

### Command types

#### Project commands

Commands stored in your repository and shared with your team. When listed in `/help`, these commands show “(project)” after their description.

**Location**: `.claude/commands/`

In the following example, we create the `/optimize` command:

#### Personal commands

Commands available across all your projects. When listed in `/help`, these commands show “(user)” after their description.

**Location**: `~/.claude/commands/`

In the following example, we create the `/security-review` command:

### Features

#### Namespacing

Organize commands in subdirectories. The subdirectories determine the command’s full name. The description will show whether the command comes from the project directory (`.claude/commands`) or the user-level directory (`~/.claude/commands`).

Conflicts between user and project level commands are not supported. Otherwise, multiple commands with the same base file name can coexist.

For example, a file at `.claude/commands/frontend/component.md` creates the command `/frontend:component` with description showing “(project)”. Meanwhile, a file at `~/.claude/commands/component.md` creates the command `/component` with description showing “(user)”.

#### Arguments

Pass dynamic values to commands using the `$ARGUMENTS` placeholder.

For example:

#### Bash command execution

Execute bash commands before the slash command runs using the `!` prefix. The output is included in the command context. You *must* include `allowed-tools` with the `Bash` tool, but you can choose the specific bash commands to allow.

For example:

#### File references

Include file contents in commands using the `@` prefix to [reference files](https://docs.anthropic.com/en/docs/claude-code/common-workflows#reference-files-and-directories).

For example:

#### Thinking mode

Slash commands can trigger extended thinking by including [extended thinking keywords](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking).

Command files support frontmatter, useful for specifying metadata about the command:

| Frontmatter | Purpose | Default |
| --- | --- | --- |
| `allowed-tools` | List of tools the command can use | Inherits from the conversation |
| `argument-hint` | The arguments expected for the slash command. Example: `argument-hint: add [tagId] \| remove [tagId] \| list`. This hint is shown to the user when auto-completing the slash command. | None |
| `description` | Brief description of the command | Uses the first line from the prompt |
| `model` | Specific model string (see [Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)) | Inherits from the conversation |

For example:

## MCP slash commands

MCP servers can expose prompts as slash commands that become available in Claude Code. These commands are dynamically discovered from connected MCP servers.

### Command format

MCP commands follow the pattern:

### Features

#### Dynamic discovery

MCP commands are automatically available when:

- An MCP server is connected and active
- The server exposes prompts through the MCP protocol
- The prompts are successfully retrieved during connection

#### Arguments

MCP prompts can accept arguments defined by the server:

#### Naming conventions

- Server and prompt names are normalized
- Spaces and special characters become underscores
- Names are lowercased for consistency

### Managing MCP connections

Use the `/mcp` command to:

- View all configured MCP servers
- Check connection status
- Authenticate with OAuth-enabled servers
- Clear authentication tokens
- View available tools and prompts from each server

## See also

- [Interactive mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
- [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference) - Command-line flags and options
- [Settings](https://docs.anthropic.com/en/docs/claude-code/settings) - Configuration options
- [Memory management](https://docs.anthropic.com/en/docs/claude-code/memory) - Managing Claude’s memory across sessions