# Safe Code Beautifier - Zero Behavior Change Beautification

<task>
Beautifies code with guaranteed zero behavior changes and risk assessment: $ARGUMENTS
</task>

<context>
This command transforms working code into beautiful, maintainable code through safe refactoring that guarantees zero behavior changes while improving readability.

Thinking-driven beautification approach:
- Safety-first refactoring analysis
- Risk assessment for each change
- Intelligent naming improvements
- Structure optimization
- Type safety enhancements
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate beautification scope for "$ARGUMENTS":
- Code size (files/lines/functions): _____
- Complexity level (simple/moderate/complex/legacy): _____
- Risk assessment (cosmetic/structural/architectural): _____
- Test coverage availability: _____
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Multi-phase refactoring strategy below
If complexity <= 3:
  USE: Direct beautification with safety thinking checkpoints
</complexity_detection>

## Pre-Refactoring Thinking
<pre_refactoring_thinking>
Before making any changes:

1. What makes this code "ugly" or unmaintainable?
   - Explicit issues: [identify specific problems]
   - Hidden complexity: [detect obscure patterns]
   - Maintenance burden: [assess long-term costs]

2. What are the safety boundaries?
   - Pure cosmetic changes: [safe to make]
   - Structural changes: [require careful testing]
   - Breaking changes: [must avoid completely]

3. What's the optimal improvement strategy?
   - High-impact/low-risk first: [prioritize]
   - Incremental approach: [step-by-step plan]
   - Validation checkpoints: [verification strategy]

4. How to ensure zero behavior change?
   - Test validation: [existing test strategy]
   - Manual verification: [critical paths to check]
   - Rollback plan: [if something goes wrong]
</pre_refactoring_thinking>

## Safety Analysis Thinking
<safety_thinking>
Risk categorization for each potential change:
- Naming changes: [variable/function/class renames]
- Structure changes: [code organization/extraction]  
- Logic changes: [simplification without behavior change]
- Type changes: [improving type safety]

Risk assessment:
<thinking>
For "$ARGUMENTS":
- Safest improvements: [zero-risk changes]
- Medium-risk improvements: [require validation]
- High-risk areas to avoid: [potential behavior changes]
</thinking>
</safety_thinking>
</thinking_orchestration>

<input_handling>
## Intelligent Scope Detection
<input_thinking>
Target: "$ARGUMENTS"

Scope analysis:
<thinking>
- Format detected: [single file/multiple files/directory/pattern]
- Language/framework: [identify from context]
- Complexity indicators: [nested structures/repeated patterns/unclear naming]
- Risk factors: [legacy code/external dependencies/lack of tests]
</thinking>
</input_thinking>

Expected inputs with reasoning:
- Specific file: `path/to/file.ext`
  <thinking>Focused beautification, deep analysis of single component</thinking>
- Multiple files: `file1 file2 file3`
  <thinking>Coordinated refactoring, maintain consistency across files</thinking>
- Directory: `path/to/module/`
  <thinking>Module-wide beautification, ensure architectural consistency</thinking>
- Pattern: `*.component.ts` or similar
  <thinking>Pattern-based improvements, apply consistent standards</thinking>
- Empty: Analyze current context
  <thinking>Infer from recent changes or current directory structure</thinking>

Intelligent scope expansion:
<scope_thinking>
- Related files to include: [tests/configs/dependencies]
- Boundary detection: [where to stop refactoring]
- Consistency requirements: [patterns to maintain]
- External impact assessment: [what might break]
</scope_thinking>
</input_handling>

<execution>
## Thinking-Driven Beautification Process

### 1. Safety Preparation Phase
<preparation_thinking>
Before any code changes:
- Backup strategy: [git checkpoint/file copies]
- Validation approach: [tests/manual checks]
- Rollback plan: [how to undo if needed]
- Change tracking: [systematic documentation]
</preparation_thinking>

**Safety Infrastructure:**
- Create git checkpoint before changes
  <thinking>Preserve current state for rollback capability</thinking>
- Analyze test coverage and identify critical paths
  <thinking>Understand what needs validation after changes</thinking>
- Document current behavior for validation
  <thinking>Baseline for ensuring no behavior changes</thinking>

### 2. Analysis and Planning Phase
<analysis_thinking>
What needs beautification:
- Naming inconsistencies: [variables/functions/classes]
- Structural issues: [nesting/organization/duplication]
- Type safety gaps: [missing/loose types]
- Code clarity problems: [complex expressions/unclear logic]
</analysis_thinking>

**Intelligent Code Analysis:**
- **Read tool** to examine code structure and identify improvement opportunities
  <thinking>Understanding current patterns and identifying beautification targets</thinking>
- **Grep tool** to find naming inconsistencies and repeated patterns
  <thinking>Discovering system-wide patterns that need consistency</thinking>
- **Glob tool** to understand broader context and related files
  <thinking>Ensuring beautification maintains architectural consistency</thinking>

### 3. Strategic Beautification Execution
<execution_thinking>
Improvement priority order:
1. Zero-risk naming improvements
2. Structure organization without logic changes  
3. Type safety enhancements
4. Complexity reduction through extraction

Risk validation at each step:
- Does this change behavior? NO → Proceed
- Does this affect external interfaces? Consider carefully
- Can this be easily reverted? Ensure YES
</execution_thinking>

**Phase-by-Phase Improvements:**

#### Phase 1: Safe Naming Improvements
<naming_thinking>
Naming improvements with zero behavior risk:
- Variable clarity: [make names self-documenting]
- Function naming: [verb-noun clarity]
- Constant naming: [descriptive and discoverable]
- File/module naming: [consistent with content]
</naming_thinking>

- Variable and function names for clarity
  <thinking>Self-documenting names reduce cognitive load</thinking>
- Consistent naming conventions across files
  <thinking>Reduces mental context switching</thinking>
- Remove abbreviations and unclear shortcuts
  <thinking>Explicit is better than implicit</thinking>

#### Phase 2: Structural Organization  
<structure_thinking>
Organization improvements without logic changes:
- Group related functionality together
- Extract common patterns into functions
- Remove dead/unused code
- Simplify complex nested structures
</structure_thinking>

- Code organization and logical grouping
  <thinking>Related code should live together</thinking>
- Extract repeated patterns into reusable functions
  <thinking>DRY principle application without behavior changes</thinking>
- Remove unused imports and dead code
  <thinking>Reduce cognitive overhead and maintenance burden</thinking>

#### Phase 3: Type Safety Enhancements
<type_thinking>
Type improvements for better development experience:
- Add missing type annotations
- Make loose types more specific
- Improve interface definitions
- Add generic constraints where helpful
</type_thinking>

- Fix loose or generic type declarations
  <thinking>Better types catch errors at compile time</thinking>
- Add missing type annotations where supported
  <thinking>Explicit types improve code documentation</thinking>
- Make types more specific based on actual usage
  <thinking>Precise types enable better tooling support</thinking>

#### Phase 4: Complexity Reduction
<complexity_thinking>
Simplification without behavior changes:
- Break down complex expressions
- Reduce nesting through early returns
- Simplify conditional logic
- Extract complex calculations
</complexity_thinking>

- Simplify complex expressions while preserving logic
  <thinking>Simpler expressions are easier to understand and debug</thinking>
- Reduce nesting through guard clauses and early returns
  <thinking>Flatter structure reduces cognitive complexity</thinking>
- Group related functionality into well-named functions
  <thinking>Functions as documentation of intent</thinking>
</execution>

<beautification_strategies>
## Intelligent Improvement Patterns

### Naming Enhancement Strategy
<naming_strategy>
Smart naming improvements:
- Self-documenting variables: `data` → `userAccountData`
- Clear function names: `process()` → `validateAndTransformUserInput()`
- Descriptive constants: `MAX_SIZE` → `MAX_FILE_UPLOAD_SIZE_MB`
- Consistent terminology: Align with domain language
</naming_strategy>

### Structure Optimization Strategy
<structure_strategy>
Organization improvements:
- Related functions grouped together
- Clear separation of concerns
- Consistent indentation and formatting
- Logical flow from high-level to implementation details
</structure_strategy>

### Type Safety Strategy
<type_strategy>
Type improvements:
- Replace `any` with specific types
- Add union types for valid value sets
- Use generics for reusable type-safe functions
- Interface definitions for complex objects
</type_strategy>

### Complexity Reduction Strategy
<complexity_strategy>
Simplification approaches:
- Extract complex conditions into well-named functions
- Use early returns to reduce nesting
- Break down large functions into smaller, focused ones
- Replace magic numbers with named constants
</complexity_strategy>
</beautification_strategies>

<validation>
## Thinking-Driven Quality Assurance

### Behavior Preservation Validation
<validation_thinking>
How to ensure zero behavior changes:
1. Run existing tests (if available)
2. Manual testing of critical paths
3. Compare outputs before/after changes
4. Validate external interfaces unchanged
</validation_thinking>

**Systematic Verification:**
- All functionality remains identical
  <thinking>Primary requirement - no behavior changes allowed</thinking>
- Tests continue to pass (if available)
  <thinking>Existing tests validate behavior preservation</thinking>
- External interfaces unchanged
  <thinking>No breaking changes for consumers</thinking>
- Performance characteristics maintained
  <thinking>Beautification shouldn't degrade performance</thinking>

### Change Documentation
<documentation_thinking>
Track improvements for:
- Clear commit messages explaining each change
- Documentation of risky changes made
- Performance impact notes (if any)
- Follow-up improvement opportunities identified
</documentation_thinking>
</validation>

<error_handling>
## Intelligent Beautification Error Recovery
<error_thinking>
When beautification encounters issues:
1. Is this a code quality problem that prevents safe refactoring?
2. Are there dependencies that make changes risky?
3. Is the complexity too high for safe automated beautification?
4. Are there test failures indicating behavior changes?
</error_thinking>

Smart error responses:

- **Code too complex for safe refactoring**:
  <thinking>Need manual review and gradual approach</thinking>
  ```
  ⚠️ Complex code detected: [specific complexity indicators]
  💡 Recommended approach: Manual review + incremental refactoring
  🛡️ Safe first steps: [low-risk improvements to start with]
  ```

- **Missing tests create risk**:
  <thinking>Need extra validation or cautious approach</thinking>
  ```
  ⚠️ Limited test coverage detected
  💡 Proceeding with extra caution: [cosmetic changes only]
  🔍 Recommend adding tests before structural changes
  ```

- **External dependencies complicate changes**:
  <thinking>Interface changes could break consumers</thinking>
  ```
  ⚠️ External dependencies detected: [specific interfaces]
  🛡️ Limiting to internal improvements only
  💡 Preserving all public interfaces
  ```
</error_handling>

<output>
## Intelligent Beautification Results
<output_thinking>
Result presentation based on:
- Number and types of changes made
- Risk level of improvements
- Impact on code maintainability
- Follow-up opportunities identified
</output_thinking>

### Adaptive Success Summary
```
✨ Code Beautification Complete

<thinking>
What to highlight:
- Most impactful improvements made
- Risk mitigation strategies used
- Maintainability gains achieved
- Next-step recommendations
</thinking>

📊 Improvements Summary:
- Naming improvements: [count] variables, [count] functions
- Structure optimizations: [specific improvements]
- Type safety enhancements: [types added/improved]
- Complexity reductions: [functions simplified/extracted]
- Lines of code impact: [before/after comparison]

🛡️ Safety Measures:
- All tests passing: [status]
- Behavior preservation: Verified
- External interfaces: Unchanged
- Performance: [maintained/improved]

🎯 Maintainability Gains:
- Readability score: [improvement metric]
- Code complexity: [reduction achieved]
- Documentation value: [self-documenting improvements]

💡 Next Steps:
- [Follow-up improvement opportunities]
- [Test coverage recommendations]
- [Architecture enhancement suggestions]
```
</output>

<learning_system>
## Beautification Pattern Learning
<pattern_learning>
Track and apply:
- Common code smells in codebase
- Effective beautification patterns
- Team style preferences
- Successful refactoring approaches
- Risk factors that require caution

Apply learning:
- Recognize similar patterns across projects
- Apply team-specific style preferences
- Use previously successful improvement strategies
- Avoid patterns that caused issues before
</pattern_learning>

## Code Quality Intelligence
<quality_learning>
Build understanding of:
- Language/framework best practices
- Domain-specific naming conventions
- Performance implications of changes
- Maintainability metrics that matter
- Technical debt patterns

Apply quality knowledge:
- Suggest framework-specific improvements
- Use domain-appropriate terminology
- Maintain or improve performance characteristics
- Prioritize changes with highest maintainability impact
</quality_learning>
</learning_system>

**Important**: I will NEVER:
- Add "Co-authored-by" or any Claude signatures
- Include "Generated with Claude Code" or similar messages
- Modify git config or user credentials
- Add any AI/assistant attribution to commits

This thinking-enhanced approach ensures that code beautification improves maintainability while maintaining absolute safety through systematic risk assessment and validation at every step.