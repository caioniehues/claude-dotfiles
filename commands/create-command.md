# Command Creator - Thinking-Enhanced

<task>
Create well-structured Claude Code commands with thinking-first architecture by learning from patterns and ensuring all new commands include proper thinking orchestration based on: $ARGUMENTS
</task>

<context>
This meta-command creates custom Claude commands with mandatory thinking patterns through:
1. Analyzing existing commands to learn patterns
2. Determining appropriate command type and location
3. Generating commands with thinking-first structure
4. Enforcing complexity detection and MCP integration
5. Creating supporting documentation
6. Validating command syntax and thinking blocks
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
   - Template to use: [select]
   - Thinking blocks needed: [list]

4. How will thinking be integrated?
   - Complexity triggers: [define thresholds]
   - MCP integration points: [identify]
   - Decision points: [map]
</pre_creation_thinking>
</thinking_orchestration>

<auto_detection>
## Intelligent Pattern Detection with Thinking
<pattern_detection_thinking>
When creating a new command, my thinking process:

1. Pattern Discovery Phase
   <thinking>
   Scanning directories for patterns:
   - ~/.claude/commands/: [user patterns]
   - .claude/commands/: [project patterns]
   - Common structures: [identified]
   - Thinking blocks present: [assessed]
   </thinking>

2. Convention Analysis
   <thinking>
   Detecting conventions:
   - Naming patterns: [discovered]
   - XML tag usage: [analyzed]
   - Thinking integration: [evaluated]
   - MCP tool usage: [identified]
   </thinking>

3. Template Selection
   <thinking>
   Best template for "$ARGUMENTS":
   - Similar commands: [listed]
   - Template match: [selected]
   - Thinking depth needed: [determined]
   </thinking>

4. Learning Application
   <thinking>
   Applying learned patterns:
   - Successful patterns: [to replicate]
   - Avoided patterns: [to skip]
   - Thinking requirements: [to enforce]
   </thinking>
</pattern_detection_thinking>
</auto_detection>

<command_types>
## Command Categories

### 1. **Analysis Commands**
- Purpose: Review, audit, analyze, validate
- Pattern: Read-heavy operations with reporting
- Examples: code review, security audit, performance analysis
- Key features: Comprehensive scanning, detailed reports

### 2. **Generation Commands**
- Purpose: Create, scaffold, generate content
- Pattern: Create new files or modify existing ones
- Examples: component generator, test creator, documentation builder
- Key features: Template usage, consistent output

### 3. **Workflow Commands**
- Purpose: Multi-step processes, orchestration
- Pattern: Sequential operations with state management
- Examples: release process, deployment pipeline, feature workflow
- Key features: Step tracking, validation checkpoints

### 4. **Utility Commands**
- Purpose: Simple tools, helpers, formatters
- Pattern: Single-purpose operations
- Examples: formatter, cleaner, optimizer
- Key features: Quick execution, focused scope

### 5. **Integration Commands**
- Purpose: Connect with external tools and services
- Pattern: MCP tool usage, API interactions
- Examples: database queries, API calls, service integrations
- Key features: Tool coordination, error handling
</command_types>

<creation_process>
## Interactive Command Creation Process with Thinking

### Phase 1: Requirements Gathering with Understanding
<requirements_thinking>
Understanding the real need:
- Surface request: "$ARGUMENTS"
- Actual problem: [deep analysis]
- User's workflow: [context understanding]
- Success metrics: [defining criteria]
</requirements_thinking>

Questions I'll explore:
- What problem does this command solve? (with reasoning)
- Who will use it and when? (usage patterns)
- What inputs does it need? (validation thinking)
- What outputs should it produce? (format decisions)
- What complexity level? (thinking depth needed)

### Phase 2: Pattern Analysis with Learning
<pattern_analysis_thinking>
Examining existing commands:
- Similar patterns found: [list with reasoning]
- Reusable structures: [identified with purpose]
- Project conventions: [detected and understood]
- Template selection: [reasoned choice]
- Thinking patterns to apply: [mandatory blocks]
</pattern_analysis_thinking>

### Phase 3: Location Decision with Reasoning
<location_thinking>
Determining optimal location:

**Project Command** (`.claude/commands/`)
- Reasoning: [why project-specific]
- Dependencies: [project resources needed]
- Integration: [project patterns followed]

**User Command** (`~/.claude/commands/`)
- Reasoning: [why general-purpose]
- Reusability: [cross-project value]
- Independence: [no project dependencies]

Decision: [location] because [detailed reasoning]
</location_thinking>

### Phase 4: Command Generation with Thinking-First
<generation_thinking>
Creating the command structure:
- XML tags needed: [with purpose for each]
- Thinking blocks: [mandatory sections]
- Complexity triggers: [thresholds defined]
- MCP integration: [connection points]
- Error recovery: [with reasoning]
</generation_thinking>

Based on analysis, I'll create:
- **Thinking orchestration wrapper** (mandatory)
- **Complexity detection block** (required)
- **Pre-execution thinking** (essential)
- **Decision point thinking** (at all branches)
- **Learning mechanisms** (pattern capture)
- **Error recovery thinking** (intelligent handling)
</creation_process>

<validation_framework>
## Command Validation with Thinking Verification

<validation_thinking>
Before finalizing, my validation thinking:
- Structure completeness: [checking]
- Thinking integration: [verifying]
- Pattern compliance: [assessing]
- Quality standards: [measuring]
</validation_thinking>

### Mandatory Checks (All Must Pass)
- ✓ Required XML tags present (`<task>`, `<context>`)
- ✓ **`<thinking_orchestration>` block present** (MANDATORY)
- ✓ **Complexity detection included** (REQUIRED)
- ✓ **MCP integration point defined** (ESSENTIAL)
- ✓ `$ARGUMENTS` properly used
- ✓ No hardcoded paths (use relative/home paths)
- ✓ MCP tools referenced correctly
- ✓ Examples provided
- ✓ Error handling with thinking included
- ✓ Documentation complete

### Thinking-Specific Validation
- ✓ Pre-execution thinking block exists
- ✓ Decision points have thinking blocks
- ✓ Error recovery includes reasoning
- ✓ Learning mechanisms present
- ✓ Complexity thresholds defined (> 3 triggers MCP)
</validation_framework>

<smart_features>
## Intelligent Features

### Pattern Learning
- Analyze naming conventions in your commands
- Detect common XML tag patterns
- Learn argument handling styles
- Identify frequently used tools

### Template Selection
Based on command type, suggest:
- Appropriate XML structure
- Common sections to include
- Tool integration patterns
- Error handling approaches

### Convention Detection
- Project-specific naming patterns
- Preferred documentation style
- Common MCP tool usage
- Typical argument formats
</smart_features>

<implementation>
## Creating Your Command

### Step 1: Analyze Existing Commands
```bash
# I'll scan for patterns
ls -la ~/.claude/commands/
ls -la .claude/commands/
```

### Step 2: Understand Requirements
Tell me about your command needs, and I'll:
- Identify the command category
- Find similar existing commands
- Suggest the best approach

### Step 3: Generate Command
I'll create a command with:
- Proper structure for your use case
- Learned patterns from your existing commands
- Appropriate error handling
- Clear documentation

### Step 4: Test and Validate
- Verify command loads correctly
- Test with and without arguments
- Check tool integrations work
- Validate output format
</implementation>

<templates>
## Thinking-Enhanced Templates (ALL MANDATORY PATTERNS)

### Analysis Command with Thinking
```markdown
<task>
Analyze $ARGUMENTS for [specific purpose] with intelligent reasoning
</task>

<context>
This command performs [type of analysis] with thinking-first approach.
</context>

<thinking_orchestration>
<complexity_detection>
Analysis complexity for "$ARGUMENTS":
- Scope: _____
- Depth required: _____
- Integration points: _____
- Complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
Else:
  USE: Structured thinking below
</complexity_detection>

<pre_analysis_thinking>
Understanding the analysis needs:
- Target: "$ARGUMENTS"
- Real goal: [infer]
- Success criteria: [define]
</pre_analysis_thinking>
</thinking_orchestration>

<process>
1. Load target with thinking: [reasoning]
2. Perform analysis with decisions: [logic]
3. Generate report with insights: [synthesis]
</process>

<output>
Findings with reasoning traces
</output>
```

### Generation Command with Thinking-First
```markdown
<task>
Generate [what] based on: $ARGUMENTS with pattern-aware thinking
</task>

<context>
Intelligent generation with thinking orchestration.
</context>

<thinking_orchestration>
<complexity_detection>
Generation complexity: _____
If > 3: Use MCP sequential thinking
</complexity_detection>

<pre_generation_thinking>
What to generate and why:
- Request: "$ARGUMENTS"
- Patterns to follow: [detected]
- Quality standards: [defined]
</pre_generation_thinking>
</thinking_orchestration>

<generation>
<generation_thinking>
Creating with reasoning:
- Structure decisions: [why]
- Pattern applications: [which]
- Quality validations: [how]
</generation_thinking>
</generation>
```

### Workflow Command with Decision Thinking
```markdown
<task>
Execute [workflow] for: $ARGUMENTS with step-wise thinking
</task>

<context>
Multi-step workflow with decision reasoning.
</context>

<thinking_orchestration>
<complexity_detection>
Workflow complexity: _____
Steps requiring thinking: _____
If > 3: Sequential MCP needed
</complexity_detection>
</thinking_orchestration>

<steps>
<step_1_thinking>
Why this step first: [reasoning]
Expected outcome: [prediction]
</step_1_thinking>
1. Execute with validation

<decision_point>
If success: [next step reasoning]
If failure: [recovery thinking]
</decision_point>

2. Continue with reasoning
</steps>

<error_recovery_thinking>
Intelligent rollback strategy
</error_recovery_thinking>
```
</templates>

<best_practices>
## Best Practices

### DO:
- Use XML tags for clear structure
- Include examples in commands
- Handle empty $ARGUMENTS gracefully
- Provide clear error messages
- Document expected inputs/outputs
- Test with various inputs

### DON'T:
- Use hardcoded absolute paths
- Forget error handling
- Skip validation steps
- Omit documentation
- Use MCP tools when CLI alternatives exist
- Assume context without checking
</best_practices>

<example_usage>
## Example Creation Session with Thinking-First

User: "I need a command to validate JSON schemas"

<creation_thinking>
Understanding the request:
- Type: Analysis command
- Complexity: Moderate (score: 2)
- Thinking needed: Validation logic decisions
- MCP needed: No (complexity < 3)
</creation_thinking>

### Pattern Analysis Results:
<pattern_thinking>
- **Category**: Analysis Command (reasoning: validation = analysis)
- **Similar to**: refactor, understand (pattern: deep inspection)
- **Location**: User command (reasoning: general-purpose tool)
- **Thinking depth**: Standard (reasoning: clear decision points)
</pattern_thinking>

### Generated Command with Mandatory Thinking:

```markdown
<task>
Validate JSON schemas and data files in: $ARGUMENTS with reasoning
</task>

<context>
This command validates JSON with thinking-first approach for intelligent error detection.
</context>

<thinking_orchestration>
<complexity_detection>
Validation complexity for "$ARGUMENTS":
- File count: _____
- Schema complexity: _____
- Validation depth: _____
- Complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  WITH: Complex validation strategy
Else:
  USE: Structured validation thinking
</complexity_detection>

<pre_validation_thinking>
Understanding validation needs:
- Input: "$ARGUMENTS"
- Schema provided: [check]
- Validation level: [strict/lenient]
- Output format: [detailed/summary]
</pre_validation_thinking>
</thinking_orchestration>

<validation_steps>
<step_thinking>
1. Parse input with reasoning:
   - File vs schema detection: [logic]
   - Multiple file handling: [strategy]
</step_thinking>

2. Load and validate:
   <validation_thinking>
   - Schema interpretation: [approach]
   - Error prioritization: [ranking]
   - Fix suggestions: [generated]
   </validation_thinking>

3. Generate intelligent report
</validation_steps>

<error_recovery_thinking>
When validation fails:
- Root cause analysis: [reasoning]
- Fix recommendations: [intelligent suggestions]
- Alternative approaches: [fallback strategies]
</error_recovery_thinking>

<output>
Results with reasoning traces:
✅ Valid: [filename] (why: [reasoning])
❌ Invalid: [filename]
   - Issue: [description]
   - Reasoning: [why this matters]
   - Suggested fix: [how to resolve]
</output>
```

### Key Differences in Thinking-First:
1. **Mandatory complexity detection** - determines thinking depth
2. **Pre-execution thinking** - understands before acting
3. **Decision point thinking** - reasons through choices
4. **Error recovery thinking** - intelligent failure handling
5. **MCP integration ready** - triggers for complex scenarios

### Testing the Enhanced Command:
```bash
# Simple validation (uses structured thinking)
/user:validate-json simple.json

# Complex validation (triggers MCP if score > 3)
/user:validate-json "schema.json data1.json data2.json --deep --recursive"
```
</example_usage>

<final_notes>
## Quick Reference

### Command Invocation
- Project: `/project:command-name arguments`
- User: `/user:command-name arguments`

### Testing Your Command
```bash
# Test without arguments
/user:your-command

# Test with arguments
/user:your-command test-input

# Test with complex arguments
/user:your-command "multiple words" file.txt
```

### Getting Help
When stuck, I can:
- Analyze your existing commands
- Suggest improvements
- Debug issues
- Create variations
</final_notes>
