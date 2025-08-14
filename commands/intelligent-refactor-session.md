# Intelligent Refactor Session - Persistent Code Refactoring

<task>
Session-based code refactoring with persistence, validation, and automatic rollback capabilities for: $ARGUMENTS
</task>

<context>
This command provides session-based refactoring with state persistence, incremental execution, continuous validation, and automatic rollback capabilities, ensuring safe and complete code transformations.

Arguments: `$ARGUMENTS` - files, directories, or refactoring scope
</context>

<thinking_orchestration>
## Refactoring Complexity Assessment
<complexity_detection>
Evaluating refactoring scope: "$ARGUMENTS"

Refactoring dimensions:
- Files/modules affected: _____
- Architectural changes: _____
- Pattern transformations: _____
- Risk level: _____
- Estimated complexity score: _____

Decision routing:
If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  WITH: Refactoring strategy planning, risk mitigation
Else:
  USE: Structured thinking blocks throughout
</complexity_detection>

## Pre-Refactoring Analysis
<pre_refactoring_thinking>
Before starting any refactoring:

1. Understanding the codebase:
   - Current architecture: [analyze]
   - Pain points: [identify]
   - Technical debt: [assess]
   - Test coverage: [evaluate]

2. Refactoring goals:
   - Explicit request: "$ARGUMENTS"
   - Implied improvements: [infer]
   - Success criteria: [define]
   - Constraints: [identify]

3. Risk assessment:
   - Breaking changes: [evaluate]
   - Performance impact: [predict]
   - Rollback strategy: [plan]
   - Testing approach: [design]

4. Optimal refactoring path:
   - Quick wins first: [list]
   - Structural improvements: [prioritize]
   - Architectural changes: [sequence]
</pre_refactoring_thinking>
</thinking_orchestration>

**KEY FEATURE: Built-in validation and refinement after EVERY change ensures nothing breaks and no code is left behind. The AI will automatically fix its own mistakes during the refactoring process.**

**SESSION FILES LOCATION: Always use refactor/ folder in current directory**

## Session Intelligence

I'll maintain refactoring continuity across sessions:

**Session Files (in current project):**
- `refactor/plan.md` - Refactoring plan with progress tracking  
- `refactor/state.json` - Current state and completed actions

**IMPORTANT:** The `refactor` folder is created in your CURRENT PROJECT directory. Use `refactor/` to access it.

**Auto-Detection:**
- If session exists: Resume from last checkpoint
- If no session: Create new refactoring plan
- Commands: `resume`, `continue`, `status`, `new`

**EXAMPLE OF CORRECT PATH USAGE:**
```
# CORRECT - looks in current project:
Read refactor/state.json
LS refactor

# WRONG - these will fail:
Read ../../../refactor/state.json
Read $HOME/.claude/refactor/state.json
```

## Phase 1: Initial Setup & Analysis with Thinking

### Extended Thinking for Complex Refactoring

<complex_refactoring_thinking>
For complex refactoring scenarios, I'll use deep thinking to develop comprehensive strategies:

<architectural_thinking>
When faced with complex architectural refactoring:
- Multi-step transformation paths: [analyze sequences]
- Risk mitigation: [strategy for each step]
- Dependency graph: [analyze and order updates]
- Performance implications: [assess each approach]
- Backwards compatibility: [requirements analysis]
- Testing strategies: [validation at each step]

Complexity assessment result:
- If score > 3: Trigger Sequential Thinking MCP
- If score <= 3: Continue with structured blocks
</architectural_thinking>

<pattern_thinking>
Pattern transformation strategy:
- Current patterns: [identify all]
- Target patterns: [define desired state]
- Migration path: [step-by-step plan]
- Validation points: [checkpoints defined]
</pattern_thinking>
</complex_refactoring_thinking>

**Triggers for Extended Analysis:**
- Large-scale architectural changes
- Complex dependency untangling
- Performance-critical refactoring
- Legacy system modernization

**MANDATORY FIRST STEPS FOR SESSION CHECK:**
```
Step 1: Check for refactor directory in CURRENT directory
Command: LS refactor

Step 2: If refactor exists, read session files:
Command: Read refactor/state.json
Command: Read refactor/plan.md

DO NOT USE THESE WRONG PATHS:
- ../../../refactor/  (WRONG - goes up directories)
- $HOME/refactor/  (WRONG - home directory)
- ~/refactor/  (WRONG - home directory)

ONLY USE: refactor/ (current directory)
```

**CRITICAL:** The refactor folder is created in the CURRENT WORKING DIRECTORY where user is running the command. NOT in home, NOT in parent directories.

<analysis_phase_thinking>
I'll examine your codebase with intelligent reasoning:

**Analysis Focus with Thinking:**
<analysis_thinking>
- Code complexity hotspots: [reasoning about patterns]
- Duplication detection: [similarity analysis]
- Architecture inconsistencies: [pattern violations]
- Test coverage: [safety assessment]
- Performance bottlenecks: [optimization opportunities]
</analysis_thinking>

**Smart Scoping Decisions:**
<scoping_thinking>
- Input analysis: "$ARGUMENTS"
- Scope decision: [focused/recursive/project-wide]
- Reasoning: [why this scope is optimal]
- Risk areas: [what to examine closely]
</scoping_thinking>
</analysis_phase_thinking>

## Phase 2: Refactoring Planning with Strategic Thinking

<planning_phase_thinking>
Based on analysis, I'll create a thoughtful plan:

**Refactoring Categories with Prioritization:**
<categorization_thinking>
- **Quick Wins**: [why these first - build confidence]
- **Structural**: [dependency order reasoning]
- **Architectural**: [impact analysis and sequencing]
- **Performance**: [benchmark-driven decisions]

Prioritization logic:
- Risk vs reward: [assessment]
- Dependencies: [order determination]
- Testing strategy: [validation approach]
</categorization_thinking>
</planning_phase_thinking>

**Plan Structure:**
I'll create a detailed plan in `refactor/plan.md`:

```markdown
# Refactor Plan - [timestamp]

## Initial State Analysis
- **Current Architecture**: [description of existing patterns]
- **Problem Areas**: [specific issues found]
- **Dependencies**: [external/internal dependencies]
- **Test Coverage**: [current coverage %]

## Refactoring Tasks
[Prioritized list with risk levels]

## Validation Checklist
- [ ] All old patterns removed
- [ ] No broken imports
- [ ] All tests passing
- [ ] Build successful
- [ ] Type checking clean
- [ ] No orphaned code
- [ ] Documentation updated

## De-Para Mapping
| Before | After | Status |
|--------|-------|--------|
| OldService.method() | NewService.method() | Pending |
| /api/v1/* | /api/v2/* | Pending |
```

## Phase 3: Incremental Execution with Continuous Thinking

<execution_phase_thinking>
I'll apply refactorings with reasoning at each step:

**Execution Order with Decision Points:**
<execution_thinking>
1. Git checkpoint: [reasoning - safety first]
2. Low-risk first: [why - build confidence]
3. Validation gates: [what to check and why]
4. Progress decision: [when to advance]
5. Status tracking: [continuous assessment]

At each step:
- Decision: [what to do]
- Reasoning: [why this approach]
- Validation: [success criteria]
- Recovery: [if something fails]
</execution_thinking>
</execution_phase_thinking>

**Continuous Validation & Refinement with Thinking:**
<validation_thinking>
After EVERY refactoring change, my validation thinking:
1. **Immediate Testing:**
   - Run unit tests for modified files
   - Execute integration tests if applicable
   - Verify no test regressions
   
2. **Deep Comparison:**
   - Compare function outputs before/after
   - Validate API contracts maintained
   - Check for missing edge cases
   - Verify error handling preserved
   
3. **Automated Fixes:**
   - Update broken imports automatically
   - Fix reference errors
   - Adjust type definitions
   - Resolve linting issues
   
4. **Quality Gates:**
   - STOP if tests fail - fix immediately
   - STOP if behavior changes - investigate
   - STOP if performance degrades - optimize
   - Only proceed when 100% validated

5. **Continuous Refinement:**
   <refinement_thinking>
   - Re-scan reasoning: [why needed]
   - Update strategy: [which files and why]
   - Cleanup decisions: [what's orphaned]
   - Documentation: [what to capture]
   </refinement_thinking>
</validation_thinking>

## Phase 4: Pattern Application with Intelligent Recognition

<pattern_application_thinking>
I'll apply patterns with reasoning:

**Pattern Recognition and Decision:**
<pattern_decision_thinking>
- Existing patterns: [identified with purpose]
- Anti-patterns: [why they're problematic]
- Design patterns: [when beneficial vs over-engineering]
- Consistency: [architectural decisions]

Pattern selection logic:
- Problem fit: [does it solve the issue?]
- Complexity cost: [is it worth it?]
- Team familiarity: [will it be maintainable?]
</pattern_decision_thinking>
</pattern_application_thinking>

**Code Improvements:**
- Extract duplicated code into utilities
- Simplify complex functions
- Improve naming for clarity
- Reduce coupling between modules

## Phase 5: Quality Metrics with Impact Analysis

<metrics_thinking>
I'll track refactoring impact with analysis:

**Measurable Improvements with Reasoning:**
<impact_thinking>
- Complexity reduction: [target vs achieved]
- Duplication eliminated: [impact on maintenance]
- Test coverage: [safety validation]
- Performance: [benchmarks comparison]
- Readability: [team benefit assessment]

Success evaluation:
- Goals met: [assessment]
- Unexpected benefits: [discovered]
- Trade-offs made: [documented]
</impact_thinking>
</metrics_thinking>

## Context Continuity

**Session Management:**
When you return and run `/refactor` or `/refactor resume`:
- I'll load existing plan and state
- Display progress summary
- Continue from last checkpoint
- Maintain all refactoring decisions

**Progress Example:**
```
RESUMING REFACTORING SESSION
├── Session: refactor_2025_08_02_1430
├── Progress: 12 of 20 tasks complete
├── Last Action: Extract UserService methods
└── Next: Simplify PaymentProcessor logic

Continuing from checkpoint...
```

## Practical Examples

**Start Refactoring:**
```
/refactor                    # Analyze entire project
/refactor src/components/    # Focus on specific directory
/refactor UserService.ts     # Target single file
```

**Session Control:**
```
/refactor resume    # Continue existing session
/refactor status    # Check progress without continuing
/refactor new       # Start fresh (archives existing)
/refactor validate  # Validate completeness and find loose ends
```

**Deep Validation & Enhancement Commands:**
```
/refactor finish    # Complete with full validation & behavior comparison
/refactor enhance   # Deep analysis comparing original vs refactored
/refactor verify    # Run original code, capture behavior, compare with new
/refactor complete  # Ensure 100% migration with behavior preservation
```

## Phase 6: Automatic Final Validation & Refinement with Complete Thinking

**AUTOMATIC EXECUTION:** This phase runs automatically after all refactorings are complete. You can also trigger it manually with `/refactor validate`.

**Final Validation Process:**

**Deep Validation Analysis with Reasoning:**
<final_validation_thinking>
1. **Coverage Check**
   <coverage_thinking>
   - Search strategy: [how to find all patterns]
   - Completeness verification: [ensuring nothing missed]
   </coverage_thinking>

2. **Import Verification**
   <import_thinking>
   - Dependency graph: [analysis approach]
   - Orphan detection: [identification method]
   </import_thinking>

3. **Build & Test**
   <test_thinking>
   - Test strategy: [comprehensive validation]
   - Failure analysis: [root cause identification]
   </test_thinking>

4. **Type Checking**
   <type_thinking>
   - Type safety: [verification approach]
   - Contract preservation: [ensuring compatibility]
   </type_thinking>

5. **Dead Code Detection**
   <cleanup_thinking>
   - Reachability analysis: [what's truly dead]
   - Safe removal: [impact assessment]
   </cleanup_thinking>
</final_validation_thinking>

**De-Para Mapping:**
```
MIGRATION STATUS REPORT
├── Patterns Migrated: 45/48 (94%)
├── Files Updated: 67/70
├── Tests Status: 3 failing
└── Build Status: Passing

PENDING MIGRATIONS:
- src/legacy/UserHelper.js → Still using old pattern
- api/v1/routes.js → Mixed patterns detected
- tests/old-api.test.js → Needs update

SUGGESTED REFINEMENTS:
1. Remove 12 orphaned files
2. Consolidate duplicate utilities
3. Update 3 missed import paths
4. Optimize bundle size (-15KB possible)
```

**Validation Actions:**
- Generate comprehensive de-para documentation
- Create migration guide for team
- Fix remaining issues automatically
- Ensure 100% pattern consistency

## Deep Validation Commands (All-in-One Process)

**ALL these commands (`finish`, `enhance`, `verify`, `complete`) execute the SAME comprehensive validation process:**

### Complete Validation & Enhancement Process
When you run ANY of these: `/refactor finish`, `/refactor enhance`, `/refactor verify`, or `/refactor complete`

**I will AUTOMATICALLY execute ALL these steps:**

1. **Deep Original Code Analysis**
   - Analyze EVERY function, method and class in detail
   - Document ALL behaviors, patterns and logic flows
   - Map complete code structure and dependencies
   - Create comprehensive understanding in `refactor/original-analysis.md`

2. **Complete Migration**
   - Apply ALL remaining refactorings
   - Find and fix ALL instances of old patterns
   - Update ALL imports and references
   - Clean up ALL orphaned code

3. **Deep Code-to-Code Comparison**
   - Analyze refactored code line by line
   - Verify EVERY behavior is preserved
   - Check ALL logic paths match original
   - Ensure error handling is identical

4. **Comprehensive Analysis**
   - Line-by-line code comparison
   - Complexity metrics (before/after)
   - Performance benchmarks
   - Memory usage analysis
   - Test coverage verification

5. **Automatic Fixes**
   - Fix ANY behavioral discrepancies
   - Update broken references
   - Resolve type issues
   - Correct import paths

6. **Final Validation**
   - Run full test suite
   - Execute integration tests
   - Verify build passes
   - Ensure 100% behavior preservation

7. **Complete Report**
   - De-para mapping of ALL changes
   - Migration guide for team
   - Risk assessment
   - Rollback instructions if needed

**The result:** 100% guarantee that NOTHING was broken, NOTHING was left behind, and the application behaves EXACTLY the same as before refactoring.

## Safety Guarantees

**Protection Measures:**
- Git checkpoints before changes
- Incremental commits at logical points
- Test validation after each step
- Clear rollback strategy

**Important:** I will NEVER:
- Add AI attribution or signatures
- Modify git configuration
- Break working functionality
- Make changes without validation
- Use emojis in commits, PRs, or git-related content

## Command Integration

When appropriate, I may suggest using other commands:
- `/test` - After major refactoring to verify functionality
- `/commit` - At logical checkpoints in the refactoring process

## Execution Guarantee with Thinking-First Approach

**My workflow ALWAYS follows this thinking-first order:**

<workflow_guarantee_thinking>
1. **Setup session** - Check/create state files FIRST
   <setup_thinking>Reasoning: Context continuity essential</setup_thinking>

2. **Deep analysis** - Use extended thinking for complex scenarios
   <analysis_thinking>Complexity > 3: Trigger MCP sequential thinking</analysis_thinking>

3. **Write plan** - Document all changes in `refactor/plan.md`
   <plan_thinking>Every change needs reasoning documented</plan_thinking>

4. **Get confirmation** - Show plan summary before starting
   <confirmation_thinking>User understanding critical for success</confirmation_thinking>

5. **Execute incrementally** - Follow plan with checkpoints
   <execution_thinking>Each step validated before proceeding</execution_thinking>

6. **Validate completeness** - Run validation phase when requested
   <validation_thinking>100% coverage verification with reasoning</validation_thinking>
</workflow_guarantee_thinking>

**I will NEVER:**
- Start refactoring without a written plan
- Make changes before complete analysis
- Skip session file creation
- Proceed without showing the plan first

I'll ensure perfect continuity between sessions, always resuming exactly where we left off with full context and decision history.