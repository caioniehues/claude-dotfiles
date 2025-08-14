# Thinking-Enhanced Utility Command Template

<task>
[SPECIFY: Perform specific utility operation] on: $ARGUMENTS with intelligent execution and adaptive behavior
</task>

<context>
This command provides a simple yet intelligent utility for [SPECIFY: what it does].

Thinking-driven utility execution:
- Smart input interpretation
- Optimal tool selection
- Performance adaptation
- Error prevention
- Learning from usage patterns
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate utility request "$ARGUMENTS":
- Input complexity (single/multiple/pattern): _____
- Operation complexity: _____
- Risk level: _____
- Performance considerations: _____
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Optimization strategy below
If complexity <= 3:
  USE: Simple execution with thinking checkpoints
</complexity_detection>

## Pre-Execution Thinking
<pre_execution_thinking>
Before executing utility:

1. What's the real intent?
   - Explicit request: "$ARGUMENTS"
   - Likely goal: [infer from context]
   - Expected outcome: [predict]

2. Is this the right tool for the job?
   - Problem to solve: [identify]
   - This utility's strength: [assess fit]
   - Alternative approaches: [consider]

3. What could go wrong?
   - Common pitfalls: [identify]
   - Edge cases: [consider]
   - Prevention strategies: [plan]

4. How to optimize execution?
   - Batch processing opportunity: [check]
   - Caching possibility: [assess]
   - Parallel execution: [evaluate]
</pre_execution_thinking>

## Tool Selection Thinking
<tool_thinking>
Available tools for this operation:
- Primary tool: [main CLI tool]
- Alternative tools: [fallback options]
- Helper tools: [supporting utilities]

Selection reasoning:
<thinking>
For "$ARGUMENTS":
- Best tool: [selected] because [reasoning]
- Fallback: [alternative] if [condition]
- Optimization: [enhancement] when [scenario]
</thinking>
</tool_thinking>
</thinking_orchestration>

<input_handling>
## Intelligent Input Parsing
<input_thinking>
Arguments: "$ARGUMENTS"

Input analysis:
<thinking>
- Format detected: [single/multiple/pattern/empty]
- Intent inference: [what user wants]
- Validation needed: [what to check]
- Optimization opportunity: [bulk processing?]
</thinking>
</input_thinking>

Expected format with reasoning:
- Single file: `filename.ext`
  <thinking>Simple case, direct processing</thinking>
- Multiple files: `file1 file2 file3`
  <thinking>Batch opportunity, optimize order</thinking>
- Pattern: `*.ext` or `path/to/files`
  <thinking>Glob expansion, check match count</thinking>
- Empty: Use current directory/default
  <thinking>Infer intent from context</thinking>

Intelligent validation:
<validation_thinking>
- Existence check: [strategy based on input type]
- Format verification: [pattern matching approach]
- Permission check: [early fail if no access]
- Size check: [warn if large operation]
</validation_thinking>
</input_handling>

<execution>
## Thinking-Driven Operation Steps
[CUSTOMIZE: Add your specific steps with thinking]

### 1. Intelligent Preparation
<prep_thinking>
Before starting:
- Resource availability: [check what's needed]
- Optimal approach: [based on input size]
- Risk mitigation: [backup if needed]
</prep_thinking>

Actions:
- Validate inputs with reasoning
- Check prerequisites intelligently
- Set up environment optimally

### 2. Adaptive Main Operation
<operation_thinking>
Execution strategy:
- If small dataset: [direct approach]
- If large dataset: [chunked processing]
- If risky operation: [safe mode with confirmations]
</operation_thinking>

Smart execution:
- [Primary action via Bash tool]
  <thinking>Why this approach: [reasoning]</thinking>
- [Process results intelligently]
  <thinking>Optimization applied: [what]</thinking>
- [Apply transformations adaptively]
  <thinking>Based on: [context/patterns]</thinking>

### 3. Intelligent Finalization
<finalization_thinking>
Cleanup decisions:
- What to preserve: [for potential reuse]
- What to clean: [temporary artifacts]
- What to report: [meaningful summary]
</finalization_thinking>

Smart cleanup:
- Clean temporary files selectively
- Report results with insights
- Save output if valuable
</execution>

<tool_usage>
## Intelligent Tool Management
<tool_selection>
[SPECIFY: List CLI tools with selection reasoning]

Primary tool selection:
<thinking>
Best tool for this: [tool] because [reasoning]
Version matters: [yes/no] because [compatibility]
</thinking>

```bash
# Smart tool usage via Bash
# <thinking>Using this command because [reason]</thinking>
Bash tool: [command] [options] [target]
```
</tool_selection>

Tool availability check with fallback:
<availability_thinking>
Check strategy:
1. Is preferred tool available?
2. Is alternative acceptable?
3. Can we install on-the-fly?
4. Should we fail or adapt?
</availability_thinking>

```bash
# Intelligent tool detection
# <thinking>Checking availability with fallback plan</thinking>
Bash tool: which [tool-name] || which [alternative] || echo "Need to install"
```

Smart installation:
<installation_thinking>
If tool missing:
- Auto-install safe? [assess]
- User permission needed? [check]
- Alternative available? [evaluate]
</installation_thinking>
</tool_usage>

<options>
## Intelligent Configuration Options
<options_thinking>
Parse options from "$ARGUMENTS":
- Explicit flags: [detect]
- Implicit preferences: [infer from usage]
- Optimal defaults: [based on context]
</options_thinking>

Smart defaults:
- [Default based on input size]
- [Default based on risk level]

Adaptive flags (intelligently parsed):
- `--verbose`: Detailed output
  <thinking>Enable if: [complex operation or error]</thinking>
- `--dry-run`: Preview without changes
  <thinking>Suggest if: [risky or first time]</thinking>
- `--force`: Skip confirmations
  <thinking>Allow if: [safe context confirmed]</thinking>
- Auto-detected: [Infer from context]
  <thinking>User patterns suggest: [preferences]</thinking>
</options>

<performance>
## Intelligent Performance Optimization
<performance_thinking>
For this operation:
- Expected duration: [estimate based on input]
- Bottleneck likely: [identify weak point]
- Optimization available: [technique]
- Trade-off: [speed vs accuracy/safety]
</performance_thinking>

Adaptive optimization:
<optimization_strategy>
Small operations (< 10 items):
- Direct processing
- No progress needed
- Immediate feedback

Medium operations (10-100 items):
- Batch processing
- Simple progress indicator
- Periodic updates

Large operations (> 100 items):
- Chunked processing
- Detailed progress bar
- Interruptible (Ctrl+C)
- Result caching
- Parallel execution if safe
</optimization_strategy>
</performance>

<output>
## Intelligent Result Formatting
<output_thinking>
Result presentation based on:
- Operation complexity: [simple/detailed]
- Success level: [full/partial/failed]
- User preference: [learned style]
- Context: [terminal width, etc.]
</output_thinking>

### Adaptive Success Output
```
✅ Operation completed successfully

<thinking>
What to highlight:
- Most important metric: [what]
- Unexpected finding: [if any]
- Performance note: [if relevant]
</thinking>

📊 Intelligent Summary:
- Processed: [count] files [faster than usual]
- Modified: [count] files [as expected]
- Time: [duration] [vs estimate]
- Insight: [pattern detected or optimization applied]
```

### Smart Verbose Output
<verbose_strategy>
Show details when:
- Error occurred (automatic verbosity)
- User requested (--verbose)
- Unusual pattern detected
- First time operation
</verbose_strategy>
</output>

<error_handling>
## Intelligent Error Recovery
<error_thinking>
When error occurs:
1. Is this recoverable?
2. Can we work around it?
3. Should we retry?
4. What's the helpful suggestion?
</error_thinking>

Smart error messages:

- **No input provided**:
  <thinking>User might want: [infer intent]</thinking>
  ```
  ❌ No target specified
  💡 Based on context, did you mean: [suggestion]
  📝 Usage: /user:utility [target]
  ```

- **Target not found**:
  <thinking>Typo or wrong location?</thinking>
  ```
  ❌ Cannot find: [target]
  💡 Similar files found: [smart matches]
  🔍 Did you mean: [closest match]?
  ```

- **Tool not available**:
  <thinking>Can we work around this?</thinking>
  ```
  ❌ Preferred tool not found: [tool]
  💡 Alternative available: [fallback tool]
  📦 Or install with: [installation command]
  ```

- **Operation failed**:
  <thinking>Root cause analysis</thinking>
  ```
  ❌ Operation failed: [immediate cause]
  🔍 Root cause: [deeper analysis]
  💡 Solution: [specific fix]
  🔄 Retry with: [modified command]
  ```
</error_handling>

<learning_system>
## Usage Pattern Learning
<pattern_learning>
Track and learn:
- Common input patterns
- Preferred options
- Error patterns
- Performance preferences

Apply learning:
- Suggest common operations
- Pre-select likely options
- Prevent repeated errors
- Optimize for user's patterns
</pattern_learning>

## Performance Learning
<performance_learning>
Monitor and adapt:
- Average input sizes
- Typical execution times
- Resource usage patterns
- Success rates

Optimize based on history:
- Pre-allocate resources
- Choose optimal strategy
- Adjust timeouts
- Cache frequent operations
</performance_learning>
</learning_system>

<examples>
## Intelligent Usage Examples
<example_thinking>
Examples should demonstrate:
- Smart input handling
- Adaptive behavior
- Error prevention
- Performance optimization
</example_thinking>

```bash
# Basic usage with smart detection
/user:utility target.file
# Thinking: Single file, using direct processing

# Pattern with optimization
/user:utility "*.js"
# Thinking: Multiple files detected, batching for performance

# Empty with context inference
/user:utility
# Thinking: No args, checking current directory context

# Large operation with auto-optimization
/user:utility large-dataset/
# Thinking: 1000+ files detected, enabling parallel processing

# Learned preference application
/user:utility data.json
# Thinking: User typically wants --verbose for JSON, auto-enabling
```

## Adaptive Scenarios
[CUSTOMIZE: Add specific examples with thinking]

1. **Smart Batch Processing**
   <thinking>Detected multiple related files</thinking>
   ```bash
   /user:utility file1.txt file2.txt file3.txt
   # Automatically groups related operations
   ```

2. **Intelligent Error Prevention**
   <thinking>Risk detected, suggesting dry-run</thinking>
   ```bash
   /user:utility important-file.conf
   # Suggests: "This looks important. Run with --dry-run first?"
   ```
</examples>

<limitations>
## Intelligent Limitation Handling
<limitation_thinking>
Known limitations and smart workarounds:
- [Limitation 1] → [Intelligent workaround]
- [Limitation 2] → [Adaptive alternative]
- [Edge case] → [Graceful degradation]
</limitation_thinking>

When limits reached:
- Explain clearly why
- Suggest alternatives
- Offer partial completion
- Remember for next time
</limitations>

<quick_reference>
## Intelligent Quick Reference
**What**: [One-line description]
**Smart Input**: [Accepts various formats, auto-detects]
**Adaptive Output**: [Adjusts based on context]
**Performance**: [Scales from instant to optimized batch]
**Safety**: [Intelligent risk assessment]
**Learning**: [Improves with usage]
</quick_reference>

<continuous_improvement>
## Utility Evolution
<evolution_thinking>
This utility improves by:
- Learning usage patterns
- Optimizing common operations
- Preventing repeated errors
- Adapting to user preferences

Next iteration possibilities:
- Predictive optimization
- Smarter error prevention
- Custom shortcut creation
- Performance auto-tuning
</evolution_thinking>
</continuous_improvement>

<customization_notes>
TO CUSTOMIZE THIS THINKING-ENHANCED TEMPLATE:
1. Replace [SPECIFY] and [CUSTOMIZE] with context
2. Define thinking triggers for decisions
3. Add complexity thresholds
4. Create adaptive strategies
5. Build learning mechanisms
6. Set up intelligent fallbacks

REMEMBER: Even simple utilities benefit from thinking!
</customization_notes>