# Thinking-Enhanced Workflow Command Template

<task>
Execute [SPECIFY: workflow name] process for: $ARGUMENTS with intelligent orchestration and adaptive decision-making
</task>

<context>
This command guides through a complete [SPECIFY: workflow type] workflow with thinking-driven execution, validation checkpoints, and intelligent rollback capabilities.

Thinking-enhanced workflow:
- Pre-execution planning and risk assessment
- Checkpoint decision reasoning
- Adaptive path selection
- Continuous validation thinking
- Intelligent error recovery
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate workflow request "$ARGUMENTS":
- Number of steps in workflow: _____
- External dependencies: _____
- Irreversible operations: _____
- Risk level: _____
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Workflow orchestration strategy below
If complexity <= 3:
  USE: Structured thinking blocks below
</complexity_detection>

## Pre-Workflow Thinking
<pre_workflow_thinking>
Before starting the workflow:

1. What's the end goal of this workflow?
   - Explicit goal: "$ARGUMENTS"
   - Implicit expectations: [infer]
   - Success criteria: [define]

2. What could go wrong?
   - Known risks: [identify]
   - Potential blockers: [predict]
   - Rollback triggers: [define]

3. What's the optimal path?
   - Standard path: [default flow]
   - Alternative paths: [contingencies]
   - Skip opportunities: [optimizations]

4. What state needs tracking?
   - Critical checkpoints: [identify]
   - Rollback points: [mark]
   - Validation gates: [define]
</pre_workflow_thinking>

## Workflow Strategy Thinking
<strategy_thinking>
Workflow execution strategies:
- Sequential (safe, predictable)
- Parallel where possible (faster)
- Adaptive (intelligent branching)
- Fail-fast (early termination)

For "$ARGUMENTS", optimal strategy:
<thinking>
Considering the workflow:
- Risk tolerance: [high/medium/low]
- Time constraints: [urgent/normal/flexible]
- Rollback complexity: [simple/moderate/complex]
Selected strategy: [choice] because [reasoning]
</thinking>
</strategy_thinking>

## Dependency Analysis
<dependency_thinking>
Analyzing workflow dependencies:
- Prerequisites that must be met: [list]
- Resources that must be available: [list]
- States that must be verified: [list]
- Tools that must be accessible: [list]

Dependency validation approach:
- Critical deps: [must have before starting]
- Optional deps: [can work around]
- Runtime deps: [can acquire during workflow]
</dependency_thinking>
</thinking_orchestration>

<prerequisites>
## Intelligent Prerequisite Verification
<prerequisite_thinking>
Before starting, thinking about requirements:
- Which are absolutely critical?
- Which can be worked around?
- Which can be fixed automatically?
</prerequisite_thinking>

Verify with reasoning:
- [ ] [REQUIREMENT: e.g., All tests passing]
  <thinking>Why critical: [reasoning]</thinking>
- [ ] [REQUIREMENT: e.g., Clean git status]
  <thinking>Why needed: [reasoning]</thinking>
- [ ] [REQUIREMENT: e.g., Required tools installed]
  <thinking>Alternatives if missing: [fallback]</thinking>
- [ ] [REQUIREMENT: e.g., Proper permissions]
  <thinking>How to verify: [check method]</thinking>
</prerequisites>

<workflow_steps>
## Step 1: [CUSTOMIZE: Initial Setup] (Thinking-Driven)
<step1_thinking>
**Pre-Step Analysis**:
- What must be true before this step?
- What will change after this step?
- What could fail and how to detect it?
- Should we proceed or wait?
</step1_thinking>

**Objective**: [What this step accomplishes]

Actions with reasoning:
1. [Specific action]
   <action_thinking>Why this first: [reasoning]</action_thinking>
2. [Specific action]
   <action_thinking>Depends on #1 because: [reasoning]</action_thinking>
3. [Specific action]
   <action_thinking>Validates #1 and #2: [reasoning]</action_thinking>

Validation thinking:
<validation_thinking>
- Check [condition] → Expected: [value] → Actual: [value]
- Verify [condition] → Success means: [criteria]
- Decision: [proceed/retry/abort] because [reasoning]
</validation_thinking>

## Step 2: [CUSTOMIZE: Processing] (Adaptive Execution)
<step2_thinking>
**Mid-Workflow Analysis**:
- How did Step 1 actually go?
- Should we adjust our approach?
- Any new risks detected?
- Optimal path forward?
</step2_thinking>

**Objective**: [What this step accomplishes]

Adaptive actions:
<branch_thinking>
If [condition from Step 1]:
  Path A: [actions] because [reasoning]
Else if [alternative condition]:
  Path B: [actions] because [reasoning]
Else:
  Default: [actions] because [safest]
</branch_thinking>

Checkpoint thinking:
<checkpoint_thinking>
- User confirmation needed? [yes/no] because [reasoning]
- State snapshot needed? [yes/no] because [reasoning]
- Rollback point? [yes/no] because [reasoning]
</checkpoint_thinking>

## Step 3: [CUSTOMIZE: Validation] (Intelligence Verification)
<step3_thinking>
**Validation Strategy**:
- What proves success?
- What indicates partial success?
- What confirms failure?
- How deep should validation go?
</step3_thinking>

**Objective**: [What this step accomplishes]

Intelligent validation:
<test_thinking>
Priority order reasoning:
1. [Critical test] - Must pass or workflow fails
2. [Important test] - Should pass for quality
3. [Nice-to-have test] - Bonus validation

Depth decision:
- Quick validation if: [conditions]
- Deep validation if: [conditions]
- Skip validation if: [never/conditions]
</test_thinking>

## Step 4: [CUSTOMIZE: Finalization] (Decision Point)
<step4_thinking>
**Final Assessment**:
- Did we achieve the goal?
- Any compromises made?
- Any cleanup needed?
- Should we actually finalize?
</step4_thinking>

**Objective**: [What this step accomplishes]

Decision tree:
<decision_thinking>
Based on validation results:
- If all passed: [finalize normally]
- If partial pass: [finalize with warnings]
- If critical failure: [rollback decision]

User interaction:
- Show: [what to display]
- Ask: [what confirmation needed]
- Explain: [reasoning for decision]
</decision_thinking>

## Step 5: [CUSTOMIZE: Post-Process] (Learning & Cleanup)
<step5_thinking>
**Post-Workflow Reflection**:
- What went well?
- What could improve?
- What to remember for next time?
- Any follow-up needed?
</step5_thinking>

**Objective**: [What this step accomplishes]

Intelligent cleanup:
<cleanup_thinking>
- Essential cleanup: [must do]
- Optional cleanup: [nice to do]
- Deferred cleanup: [can do later]
Priority based on: [reasoning]
</cleanup_thinking>
</workflow_steps>

<adaptive_checkpoints>
## Intelligent Checkpoint Management
<checkpoint_strategy>
Dynamic checkpoint creation based on:
- Risk level of next operation
- Complexity of current state
- Cost of potential rollback
- User preferences detected

Checkpoint depth:
- Light (fast): Just mark position
- Medium (balanced): Save key state
- Heavy (safe): Full state snapshot
</checkpoint_strategy>

## User Interaction Thinking
<interaction_thinking>
When to ask for confirmation:
- Before irreversible operations: ALWAYS
- After complex steps: IF uncertainty detected
- Before external changes: IF first time
- After failures: IF recovery unclear

How to present information:
- Show only what matters now
- Explain reasoning if complex
- Offer smart defaults
</interaction_thinking>
</adaptive_checkpoints>

<state_management>
## Intelligent State Tracking
<state_thinking>
What state to track and why:
- Critical state: [what] because [recovery needs]
- Performance metrics: [what] because [optimization]
- Decision history: [what] because [learning]
- Error patterns: [what] because [prevention]
</state_thinking>

Enhanced state structure:
```json
{
  "current_step": 1,
  "completed_steps": [],
  "step_decisions": {
    "step1": {"path_taken": "A", "reason": "..."}
  },
  "rollback_points": [],
  "artifacts": {},
  "metrics": {
    "time_per_step": [],
    "retry_counts": {},
    "validation_scores": {}
  },
  "thinking_trace": [],
  "status": "in_progress"
}
```

## Rollback Intelligence
<rollback_thinking>
Smart rollback decisions:
- Full rollback if: [critical failure]
- Partial rollback if: [recoverable error]
- No rollback if: [safe to continue]

Rollback optimization:
- Can we rollback just the failed part?
- Can we preserve any successful work?
- Can we retry before rollback?
</rollback_thinking>
</state_management>

<intelligent_error_handling>
## Error Analysis and Recovery
<error_thinking>
When an error occurs, analyze:
1. Is this expected or unexpected?
2. Is this recoverable or fatal?
3. Is this a symptom or root cause?
4. Have we seen this before?
</error_thinking>

## Adaptive Recovery Strategies
<recovery_thinking>
For each error type:

### Transient Errors (network, timing)
<thinking>
- Retry with backoff? [yes if under 3 attempts]
- Alternate approach? [if available]
- Wait and retry? [if resource contention]
</thinking>

### Logic Errors (validation, state)
<thinking>
- Can we fix automatically? [check conditions]
- Need user input? [if ambiguous]
- Must rollback? [if inconsistent state]
</thinking>

### Resource Errors (permissions, availability)
<thinking>
- Can we acquire resource? [try alternatives]
- Can we proceed without? [check if optional]
- Must abort? [if critical dependency]
</thinking>
</recovery_thinking>

## Learning from Errors
<error_learning>
After error recovery:
- Pattern detected: [what went wrong]
- Prevention strategy: [how to avoid]
- Recovery improvement: [better approach]
- Documentation update: [what to note]
</error_learning>
</intelligent_error_handling>

<progress_tracking>
## Intelligent Progress Display
<progress_thinking>
Show progress adaptively:
- Verbose if: Complex step or slow operation
- Concise if: Simple step or fast operation
- Detailed if: Error or unexpected result
</progress_thinking>

Dynamic status:
```
[WORKFLOW NAME] Progress:
[✓] Step 1: Initial Setup (2.3s, optimal path)
[⚡] Step 2: Processing... (5.1s, retry 1 of 3)
    └─ Substep: Validating... [thinking: checking consistency]
[ ] Step 3: Validation (estimated: 3s)
[ ] Step 4: Finalization (estimated: 1s)
[ ] Step 5: Post-Process (optional)

Status: Processing step 2 of 5 (40% complete)
Confidence: High (all validations passing)
Time remaining: ~7s (based on current pace)
```
</progress_tracking>

<workflow_learning>
## Workflow Optimization Learning
<optimization_thinking>
After workflow completion, analyze:
- Which steps took longest? Why?
- Which steps failed/retried? Pattern?
- Which validations were redundant?
- Which paths were never taken?

Improvements for next run:
- Skip [step] if [condition detected]
- Parallelize [steps] if [safe to do so]
- Add checkpoint before [risky operation]
- Remove validation of [always passes]
</optimization_thinking>

## Pattern Recognition
<pattern_thinking>
Detected patterns:
- User preference: [always chooses X]
- Common failure: [Y fails when Z]
- Optimal path: [A→B→D skipping C]
- Resource usage: [peak at step N]

Apply next time:
- Default to user preference
- Pre-check for failure condition
- Suggest optimal path
- Pre-allocate resources
</pattern_thinking>
</workflow_learning>

<output_summary>
## Intelligent Completion Summary
<summary_thinking>
What to emphasize in summary:
- Critical achievements: [what matters most]
- Important metrics: [what indicates success]
- Action items: [what needs attention]
- Lessons learned: [what to remember]
</summary_thinking>

```
✅ [WORKFLOW NAME] Completed Successfully!

## Execution Analysis
- Strategy used: [selected approach]
- Path taken: [actual flow vs planned]
- Optimizations applied: [shortcuts taken]
- Challenges overcome: [issues resolved]

## Performance Metrics
- Total duration: [time] ([vs estimate])
- Steps completed: [count] ([skipped])
- Retry count: [number] ([which steps])
- Validation score: [percentage]

## Key Outcomes
📊 What changed:
  • [Change 1] - Impact: [assessment]
  • [Change 2] - Impact: [assessment]
  • [Change 3] - Impact: [assessment]

## Intelligent Recommendations
Based on this run:
1. [Suggestion] because [reasoning]
2. [Optimization] could save [estimate]
3. [Warning] to watch for [pattern]

## Next Steps (Prioritized)
1. 🔴 [Critical action] - [why urgent]
2. 🟡 [Important action] - [why needed]
3. 🟢 [Optional action] - [why beneficial]
```
</output_summary>

<examples>
## Usage Examples with Expected Thinking
```bash
# Basic workflow execution
/user:workflow
# Triggers: Full planning, standard path thinking

# With specific target
/user:workflow target-name
# Triggers: Target analysis, customized path selection

# With options
/user:workflow target-name --skip-tests --verbose
# Triggers: Risk assessment for skipping, adjusted validation
```
</examples>

<continuous_improvement>
## Workflow Evolution
<evolution_thinking>
This workflow template improves by:
- Learning user preferences
- Optimizing common paths
- Preventing repeated failures
- Streamlining validations

Next iteration considerations:
- Add parallel execution where safe
- Implement predictive checkpoints
- Create smart defaults
- Build failure prevention
</evolution_thinking>
</continuous_improvement>

<customization_notes>
TO CUSTOMIZE THIS THINKING-ENHANCED TEMPLATE:
1. Replace [SPECIFY] and [CUSTOMIZE] with context
2. Define thinking triggers for decision points
3. Set complexity thresholds for MCP invocation
4. Create adaptive checkpoint strategies
5. Build learning mechanisms for optimization
6. Configure intelligent error recovery paths

REMEMBER: Let thinking guide the workflow, not the other way around!
</customization_notes>