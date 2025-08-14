# Thinking-Enhanced Mode-Based Command Template

<task>
Execute [SPECIFY: operation type] based on mode specified in: $ARGUMENTS with intelligent mode selection and adaptive behavior
</task>

<context>
This command adapts its behavior through thoughtful mode analysis and intelligent path selection.

Thinking-driven mode execution:
- Mode detection reasoning
- Path optimization per mode
- Adaptive behavior based on context
- Cross-mode learning
- Intelligent fallback strategies
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate mode-based request "$ARGUMENTS":
- Number of possible modes: _____
- Ambiguity in mode selection: _____
- Target complexity: _____
- Option parsing complexity: _____
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Mode selection strategy below
If complexity <= 3:
  USE: Structured thinking blocks below
</complexity_detection>

## Pre-Mode Selection Thinking
<pre_mode_thinking>
Before selecting mode, I need to understand:

1. What's the user trying to achieve?
   - Explicit mode request: [parse from $ARGUMENTS]
   - Implicit goal: [infer from context]
   - Likely intent: [predict from patterns]

2. Is the mode explicitly specified?
   - First argument analysis: [mode or target?]
   - Alias detection: [check shortcuts]
   - Default trigger: [no mode specified?]

3. What context suggests the best mode?
   - Target type: [file/directory/pattern]
   - Previous usage: [learned preferences]
   - Current state: [environmental factors]

4. What if the mode is ambiguous?
   - Best guess: [based on what?]
   - Fallback options: [alternatives]
   - User clarification: [when to ask?]
</pre_mode_thinking>

## Mode Strategy Thinking
<strategy_thinking>
Mode execution strategies:
- Direct mode (explicit selection)
- Inferred mode (context-based)
- Adaptive mode (learns from use)
- Hybrid mode (combines approaches)

For "$ARGUMENTS", optimal approach:
<thinking>
Parsing arguments:
- Explicit mode: [detected/not detected]
- Target clarity: [clear/ambiguous]
- Options present: [yes/no]
Selected strategy: [choice] because [reasoning]
</thinking>
</strategy_thinking>

## Mode Compatibility Analysis
<compatibility_thinking>
Checking mode-target compatibility:
- Mode requirements: [what each mode needs]
- Target characteristics: [what we have]
- Compatibility matrix: [mode x target]
- Optimal mode: [best match]

Fallback planning:
- If incompatible: [alternative mode]
- If partially compatible: [adaptation]
- If unclear: [discovery approach]
</compatibility_thinking>
</thinking_orchestration>

<mode_detection>
## Intelligent Argument Parsing
<parsing_thinking>
Input: "$ARGUMENTS"

Parsing strategy:
<thinking>
Step 1: Tokenize arguments
- Tokens: [split result]
- Count: [number of tokens]

Step 2: Analyze first token
- Is it a known mode? [check]
- Is it a mode alias? [check]
- Is it a valid target? [check]
- Ambiguous? [assess]

Step 3: Determine structure
- Pattern detected: [mode target options] OR [target options] OR [mode only]
- Confidence level: [high/medium/low]
- Decision: [interpretation]
</thinking>
</parsing_thinking>

Mode resolution:
```
If arguments empty:
  <thinking>No args means: [default behavior reasoning]</thinking>
  → Use default mode
  → Target = current directory
Else:
  <thinking>
  First word analysis:
  - Known mode? [yes/no]
  - Valid target? [yes/no]
  - Ambiguous? [yes/no]
  </thinking>
  → Mode = [resolved]
  → Target = [identified]
  → Options = [extracted]
```

Mode aliases with reasoning:
[CUSTOMIZE: Add if you want shortcuts]
- `m1` → `mode1` 
  <thinking>Short form for frequent use</thinking>
- `quick` → `mode2`
  <thinking>Semantic alias for speed</thinking>
- `full` → `mode3`
  <thinking>Semantic alias for completeness</thinking>
</mode_detection>

<modes>
[CUSTOMIZE: Define each mode's behavior with thinking]

## Mode 1: [NAME] (Thinking-Enhanced)
<mode1_thinking>
**Pre-Mode Analysis**:
- Why would user choose this mode?
- What problem does it solve?
- What are the trade-offs?
- When is this optimal?
</mode1_thinking>

**Purpose**: [What this mode does]
**When to use**: [Use case]

### Intelligent Implementation
<implementation_thinking>
For this mode, the approach should be:
1. [Step 1] because [reasoning]
2. [Step 2] following [logic]
3. [Step 3] to ensure [goal]

Optimization opportunities:
- Can skip [step] if [condition]
- Can parallelize [operations] if [safe]
- Can cache [results] for [reuse]
</implementation_thinking>

### Mode-Specific Validation
<validation_thinking>
What validates success in this mode:
- Primary indicator: [what to check]
- Secondary confirmation: [backup check]
- Quality metric: [measurement]
</validation_thinking>

### Adaptive Output
<output_thinking>
Output formatting based on:
- Target size: [adjust verbosity]
- User preference: [learned style]
- Success level: [detail accordingly]
</output_thinking>

---

## Mode 2: [NAME] (Speed-Optimized)
<mode2_thinking>
**Speed vs Completeness Trade-off**:
- What can we safely skip?
- Where can we make assumptions?
- How to maintain accuracy?
- When to fall back to thorough mode?
</mode2_thinking>

**Purpose**: [What this mode does]
**When to use**: [Use case]

### Performance-Driven Implementation
<performance_thinking>
Optimization strategy:
- Priority order: [what matters most]
- Skip conditions: [when safe to skip]
- Batch operations: [what to combine]
- Early termination: [when good enough]
</performance_thinking>

---

## Mode 3: [NAME] (Comprehensive)
<mode3_thinking>
**Depth vs Time Trade-off**:
- How deep should analysis go?
- What's the point of diminishing returns?
- How to present comprehensive results?
- When is thoroughness warranted?
</mode3_thinking>

**Purpose**: [What this mode does]
**When to use**: [Use case]

### Thorough Implementation
<thoroughness_thinking>
Comprehensive approach:
- Leave no stone unturned: [what to check]
- Cross-validation: [redundant checks]
- Edge case handling: [corner cases]
- Complete documentation: [what to record]
</thoroughness_thinking>

---

## Default Mode (Intelligent Fallback)
<default_thinking>
**When no mode specified**:
- What's the most likely intent?
- What would be most helpful?
- Should we suggest a specific mode?
- How to be useful without explicit direction?
</default_thinking>

**When triggered**: No mode specified or unrecognized mode
**Behavior**: [Intelligent default based on context]

### Adaptive Default Implementation
<adaptive_default>
Context-based behavior:
- If target is file: [likely mode]
- If target is directory: [likely mode]
- If no target: [discovery mode]
- If pattern: [search mode]
</adaptive_default>
</modes>

<mode_selection>
## Intelligent Mode Selection Logic
<selection_thinking>
Mode selection decision tree:
1. Explicit mode? → Use it (with validation)
2. Alias detected? → Resolve to mode
3. Context suggests? → Infer mode
4. Ambiguous? → Use smart default
5. Unknown? → Explain options
</selection_thinking>

```javascript
// Thinking-driven mode selection
function selectMode(args) {
  // <thinking>
  // Analyzing: args = "$ARGUMENTS"
  // First token: [extracted]
  // Looks like: [mode/target/ambiguous]
  // Context suggests: [inference]
  // </thinking>
  
  switch(intelligentParse(args)) {
    case detectExplicitMode(args):
      // <thinking>Clear mode specified</thinking>
      return executeMode(mode, validateCompatibility(mode, target));
    
    case detectAlias(args):
      // <thinking>Alias detected, resolving</thinking>
      return executeMode(resolveAlias(alias), target);
    
    case inferFromContext(args):
      // <thinking>No explicit mode, inferring from context</thinking>
      return executeInferredMode(context, target);
    
    default:
      // <thinking>Ambiguous input, need intelligent handling</thinking>
      return handleAmbiguous(args);
  }
}
```
</mode_selection>

<cross_mode_learning>
## Mode Usage Learning
<learning_thinking>
Track and learn from mode usage:
- Which modes used most?
- What patterns emerge?
- Which mode for which targets?
- User preference signals?

Apply learning:
- Suggest preferred mode
- Optimize common paths
- Pre-load likely mode
- Adapt defaults
</learning_thinking>

## Mode Performance Tracking
<performance_tracking>
For each mode execution:
- Time taken: [measure]
- Success rate: [track]
- User satisfaction: [infer from retries]
- Resource usage: [monitor]

Optimization opportunities:
- Mode 1 could be faster if: [observation]
- Mode 2 often fails when: [pattern]
- Mode 3 rarely needed for: [targets]
</performance_tracking>
</cross_mode_learning>

<intelligent_help>
## Context-Aware Help System
<help_thinking>
When user needs guidance, consider:
- What are they trying to do?
- Which mode would help most?
- What examples are relevant?
- How to explain simply?
</help_thinking>

Dynamic help based on context:
```
Based on your input "$ARGUMENTS", here's what might help:

🎯 Recommended: [mode] mode
   Why: [reasoning based on context]
   Usage: /user:command [mode] [your-target]
   Example: /user:command [mode] [contextualized example]

📋 All available modes:
[List with contextual relevance scoring]

💡 Smart tip: [Contextual suggestion based on patterns]
```
</intelligent_help>

<error_handling>
## Intelligent Error Recovery
<error_thinking>
When mode execution fails:
1. Was it the wrong mode?
2. Was the target incompatible?
3. Were options incorrect?
4. Should we try different mode?
</error_thinking>

### Mode Selection Errors
<selection_error_thinking>
User selected [mode] but:
- Target suggests [better mode]
- Previous usage suggests [preferred mode]
- Error pattern suggests [alternative]

Recovery strategy:
- Suggest: "Did you mean [mode]?"
- Offer: "Try [mode] for this target"
- Explain: "This failed because..."
</selection_error_thinking>

### Adaptive Error Messages
```
❌ Mode [mode] failed with [target]

<thinking>
Why it failed: [analysis]
What might work: [suggestion]
Learning: [pattern to remember]
</thinking>

💡 Suggestion: [Specific recovery action]
🔄 Alternative: Try [other mode] instead
📚 Context: This usually happens when [explanation]
```
</error_handling>

<examples>
## Intelligent Usage Examples
<example_thinking>
Examples should show:
- Common use cases
- Edge cases
- Mode selection reasoning
- Learning from context
</example_thinking>

### Smart Mode Selection
```bash
# Explicit mode with reasoning
/user:command mode1 target.file
# Thinking: Clear mode1 request for file target

# Inferred mode from context
/user:command large-dataset.csv
# Thinking: Large file suggests mode2 (quick) for performance

# Alias with learning
/user:command quick src/
# Thinking: User prefers quick mode for src/ directory

# Adaptive default
/user:command
# Thinking: No args, checking last usage... suggesting mode1
```
</examples>

<continuous_improvement>
## Mode Evolution System
<evolution_thinking>
This template improves by:
- Learning mode preferences
- Optimizing mode performance
- Adapting mode behavior
- Refining mode selection

Next iteration ideas:
- Combine modes dynamically
- Create custom modes from patterns
- Predict mode before asking
- Auto-optimize based on usage
</evolution_thinking>
</continuous_improvement>

<customization_notes>
TO CUSTOMIZE THIS THINKING-ENHANCED TEMPLATE:
1. Replace [SPECIFY] and [CUSTOMIZE] with your context
2. Define modes with clear thinking patterns
3. Add mode-specific complexity triggers
4. Create intelligent fallback strategies
5. Build learning mechanisms for mode preferences
6. Set up smart error recovery paths

REMEMBER: Mode selection should be intelligent, not mechanical!
</customization_notes>