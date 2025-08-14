# Context-Enhanced Executor - Execute Commands with Relevant Documentation

<task>
Loads relevant documentation and context before executing commands for informed decisions: $ARGUMENTS
</task>

<context>
This command automatically discovers and loads relevant documentation, best practices, and contextual information before executing any command, ensuring all decisions are informed by available knowledge.

Core capabilities:
- Automatic documentation discovery
- Context injection into commands
- Knowledge-enhanced execution
- Best practices enforcement
- Learning from documentation patterns
</context>

<thinking_orchestration>
## Documentation-Aware Complexity Assessment
<complexity_detection>
Evaluating execution request: "$ARGUMENTS"

Documentation factors:
- Command complexity: _____
- Documentation availability: _____
- Context requirements: _____
- Knowledge depth needed: _____
- Integration complexity: _____
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  WITH: Documentation analysis and execution strategy
Else:
  USE: Direct documentation-enhanced execution
</complexity_detection>

## Pre-Execution Documentation Analysis
<pre_execution_thinking>
Before executing "$ARGUMENTS":

1. Documentation Discovery
   - Command type: [identify]
   - Related docs: [search locations]
   - Best practices: [identify sources]
   - Examples: [locate relevant]

2. Context Requirements
   - Required knowledge: [assess]
   - Dependencies: [identify]
   - Constraints: [discover]
   - Guidelines: [extract]

3. Loading Strategy
   - Priority docs: [most relevant first]
   - Context depth: [determine needed]
   - Integration approach: [plan injection]
</pre_execution_thinking>
</thinking_orchestration>

<documentation_sources>
## Documentation Discovery Sources

### Priority 1: Project Documentation
- `.claude/docs/` - Project-specific Claude docs
- `docs/` - General project documentation
- `README.md` - Project overview
- `CONTRIBUTING.md` - Development guidelines
- `ARCHITECTURE.md` - System design

### Priority 2: Command Documentation
- Command file inline documentation
- Command usage examples
- Command pattern library
- Previous execution patterns

### Priority 3: System Documentation
- `~/.claude/docs/` - User-level Claude docs
- Framework documentation
- Library documentation
- API specifications

### Priority 4: External Sources
- Official documentation sites
- Best practice guides
- Community standards
- Stack-specific patterns
</documentation_sources>

<usage_examples>
## Context Loading Examples

### Load Context for Java Implementation
```bash
/user:context-enhanced-executor /user:java-rapid-implementation "implement caching"
# Loads: Spring Cache docs, caching patterns, best practices
```

### Load Context for Refactoring
```bash
/user:context-enhanced-executor /user:intelligent-refactor-session "UserService"
# Loads: Architecture docs, refactoring patterns, service conventions
```

### Force Specific Documentation
```bash
/user:context-enhanced-executor --docs="security-guide.md" /user:java-test-driven-development
# Loads: Specified doc plus relevant testing context
```

### Load All Available Context
```bash
/user:context-enhanced-executor --deep /user:analyze-project-architecture
# Loads: All available documentation for comprehensive context
```
</usage_examples>

<integration_notes>
## Integration with Commands

Works with all commands:
- `/user:intelligent-refactor-session` - Context for refactoring
- `/user:java-clean-code-generator` - Best practices for implementation
- `/user:analyze-project-architecture` - System documentation
- All other commands benefit from context

Can be chained:
```bash
/user:reasoning-wrapper /user:context-enhanced-executor /user:command
# Adds both reasoning and documentation context
```
</integration_notes>