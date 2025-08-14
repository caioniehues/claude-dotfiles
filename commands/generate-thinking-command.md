# Generate Thinking Command - Create Commands with Built-in Reasoning

<task>
Generates new Claude commands with built-in thinking architecture and pattern learning: $ARGUMENTS
</task>

<context>
This meta-command generates well-structured Claude commands with mandatory thinking patterns, complexity detection, and MCP integration by learning from existing command patterns.

Process:
1. Analyze existing commands to learn patterns
2. Determine appropriate command type and location
3. Generate commands with thinking-first structure
4. Enforce complexity detection and MCP integration
5. Create supporting documentation
6. Validate command syntax and thinking blocks
</context>

<thinking_orchestration>
## Command Creation Complexity Assessment
<complexity_detection>
Evaluating command creation request: "$ARGUMENTS"

Creation complexity factors:
- Command type complexity: _____
- Integration requirements: _____
- Pattern variations needed: _____
- Thinking depth required: _____
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  WITH: Command architecture planning
If complexity <= 3:
  USE: Structured thinking blocks below
</complexity_detection>

## Pre-Creation Thinking
<pre_creation_thinking>
Before creating the command, I need to understand:

1. What problem does this command solve?
   - User's request: "$ARGUMENTS"
   - Actual problem: [infer]
   - Success criteria: [define]

2. What type of command is this?
   - Category: [analysis/generation/workflow/utility/integration]
   - Complexity level: [simple/moderate/complex]
   - Thinking requirements: [minimal/standard/extensive]

3. What patterns should it follow?
   - Existing similar commands: [identify]
   - Patterns to apply: [select]
   - Unique requirements: [determine]

4. Where should it be placed?
   - User-level: ~/.claude/commands/
   - Project-level: .claude/commands/
   - Decision: [based on scope]
</pre_creation_thinking>
</thinking_orchestration>

<command_structure>
## Generated Command Structure

Every generated command includes:

```markdown
# [Command Name] - [Descriptive Title]

<task>
[Concise description of what the command does with: $ARGUMENTS]
</task>

<context>
[Detailed explanation of capabilities and approach]
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
[Complexity evaluation logic]
</complexity_detection>

## Pre-Execution Thinking
<pre_execution_thinking>
[Understanding and planning]
</pre_execution_thinking>
</thinking_orchestration>

[Command implementation with thinking blocks]
```
</command_structure>

<usage_examples>
## Command Generation Examples

### Generate Simple Utility Command
```bash
/user:generate-thinking-command "validate JSON schemas"
# Creates: json-schema-validator with thinking blocks
```

### Generate Complex Analysis Command
```bash
/user:generate-thinking-command "analyze database performance"
# Creates: database-performance-analyzer with MCP integration
```

### Generate Integration Command
```bash
/user:generate-thinking-command "sync with external API"
# Creates: api-sync-manager with error recovery thinking
```

### Generate Workflow Command
```bash
/user:generate-thinking-command "automated deployment pipeline"
# Creates: deployment-pipeline-manager with checkpoint thinking
```
</usage_examples>

<integration_notes>
## Integration with Commands

Works with:
- `/user:reasoning-wrapper` - Enhance generated commands
- `/user:adaptive-complexity-router` - Add routing logic
- `/user:context-enhanced-executor` - Add documentation awareness

Command validation:
- Ensures all thinking blocks present
- Validates complexity detection
- Checks MCP integration points
- Verifies pattern compliance
</integration_notes>