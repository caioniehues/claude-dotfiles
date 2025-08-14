# ULTRATHINK Hybrid MCP - Balanced Performance & Capability

<task>
Enhanced thinking with persistent memory and research capabilities for: $ARGUMENTS
</task>

<context>
Hybrid MCP implementation combining Claude's native reasoning with selective MCP tools. Provides persistent pattern learning, web research, and document access while maintaining performance through native thinking (no sequential thinking MCP).

**Key Features:**
- Native Claude thinking (no sequential MCP)
- Persistent pattern learning via Basic Memory
- Web research through Firecrawl
- Obsidian document access
- Balanced performance/capability
- Pattern persistence across sessions
</context>

<performance_metrics>
## Implementation Characteristics
- Response Time: MEDIUM (2-10s typical)
- Token Efficiency: MEDIUM
- Resource Usage: MODERATE
- Pattern Persistence: PERMANENT (Basic Memory)
- External Dependencies: MCP (Memory, Web, Obsidian)
- Offline Capable: NO (requires MCP)
</performance_metrics>

<mcp_tools_available>
## MCP Tool Configuration
```yaml
memory_tools:
  - mcp__basic-memory__search_notes    # Find patterns
  - mcp__basic-memory__build_context    # Load context
  - mcp__basic-memory__write_note       # Save patterns
  
web_tools:
  - mcp__firecrawl__firecrawl_search   # Web search
  - mcp__firecrawl__firecrawl_scrape   # Page content
  
obsidian_tools:
  - mcp__mcp-obsidian__read_notes      # Read documents
  - mcp__mcp-obsidian__search_notes    # Search vault
```
</mcp_tools_available>

## Pre-Execution: Memory Context Loading

<memory_initialization>
### 🧠 Loading Relevant Patterns

```bash
# Search for relevant patterns from past sessions
mcp__basic-memory__search_notes "$ARGUMENTS"

# Build context from related solutions
mcp__basic-memory__build_context "memory://technical/solutions/*"
mcp__basic-memory__build_context "memory://technical/thinking-patterns/*"
```

**Pattern Library Check:**
- Previous solutions: [searching...]
- Similar problems: [analyzing...]
- Learned optimizations: [loading...]
- Success patterns: [retrieving...]
</memory_initialization>

## Phase 1: Enhanced Research & Analysis (40% → 85% Confidence)

<phase1_research>
### 📊 Intelligent Research Phase
**Starting Confidence: 40%**
**Target Confidence: 85%**

<initial_understanding>
Analyzing: "$ARGUMENTS"

<thinking>
Let me understand this request deeply...

**Initial Classification:**
- Problem domain: [identify area]
- Complexity level: [assess difficulty]
- Research needs: [external info required?]
- Pattern matches: [similar past problems]

**Multi-Source Analysis:**
1. Internal knowledge assessment
2. Pattern library consultation
3. External research requirements
4. Documentation needs
</thinking>
</initial_understanding>

<pattern_search>
### 🔍 Pattern Recognition

```bash
# Search for relevant patterns
mcp__basic-memory__search_notes "type:solution $ARGUMENTS"
mcp__basic-memory__search_notes "type:pattern category:[relevant-category]"
```

**Found Patterns:**
- Pattern 1: [description and relevance]
- Pattern 2: [description and relevance]
- Novel aspects: [what's different]
</pattern_search>

<external_research>
### 🌐 External Research (if needed)

<thinking>
Determining if external research would enhance understanding...

Research decision:
- Need current information? [yes/no]
- Need domain expertise? [yes/no]
- Need best practices? [yes/no]
</thinking>

```bash
# Web research for current information
mcp__firecrawl__firecrawl_search "query: $ARGUMENTS best practices 2024"

# Documentation search in vault
mcp__mcp-obsidian__search_notes "$ARGUMENTS"
```

**Research Findings:**
- External insights: [key findings]
- Documentation: [relevant docs]
- Best practices: [current standards]
</external_research>

<interactive_questions>
### 🤔 Intelligent Clarification

Based on patterns and research, I need to understand:

**Core Questions:**
1. **Specificity**: Given similar past solutions, which approach fits best?
   - [ ] Adapt pattern: [specific pattern]
   - [ ] Combine patterns: [pattern A + B]
   - [ ] Novel approach needed
   - [ ] Hybrid solution

2. **Depth vs Breadth**: How should I balance the analysis?
   - [ ] Deep dive on core issue
   - [ ] Broad exploration of options
   - [ ] Iterative refinement
   - [ ] Comprehensive coverage

3. **Integration**: What existing systems must we consider?
   - [ ] Standalone solution
   - [ ] Must integrate with: [system]
   - [ ] Replace existing: [component]
   - [ ] Enhance current: [feature]

**Context-Specific Questions:**
[Based on patterns and research, 2-3 specific questions]
</interactive_questions>

<deep_analysis>
### 🧠 Advanced Analysis

<thinking>
Synthesizing internal knowledge, patterns, and external research...

**Pattern-Enhanced Understanding:**
- Recognized pattern: [pattern name]
  - Previous success rate: [percentage]
  - Adaptation needed: [modifications]
  - Risk factors: [considerations]

**Cross-Domain Insights:**
- Analogy from: [other domain]
- Applicable principle: [principle]
- Innovation opportunity: [possibility]

**Comprehensive View:**
1. Technical requirements: [detailed]
2. Human factors: [considered]
3. System constraints: [identified]
4. Evolution path: [planned]
</thinking>
</deep_analysis>

<confidence_gate>
### ✅ Phase 1 Confidence Check

**Understanding Quality:**
- Problem clarity: ____%
- Pattern matches: ____%
- Research completeness: ____%
- Requirement coverage: ____%

**Overall Confidence: ____%**

✅ PROCEED to Phase 2 if ≥ 85%
🔄 REFINE with more research/questions if < 85%
</confidence_gate>
</phase1_research>

## Phase 2: Pattern-Informed Planning (60% → 90% Confidence)

<phase2_planning>
### 📋 Intelligent Solution Design
**Starting Confidence: 60%**
**Target Confidence: 90%**

<pattern_based_design>
### 🎯 Pattern-Enhanced Architecture

<thinking>
Leveraging learned patterns and research insights...

**Primary Approach (Pattern-Based):**
- Base pattern: [identified pattern]
- Adaptations required: [customizations]
- Enhancement opportunities: [improvements]
- Risk mitigations: [from past failures]

**Alternative Approaches:**
1. Pure pattern application
   - Use: [specific pattern]
   - Pros: Proven success
   - Cons: May need adaptation

2. Hybrid pattern combination
   - Combine: [pattern A + B]
   - Pros: Best of both
   - Cons: Complexity increase

3. Novel approach
   - Strategy: [new approach]
   - Pros: Perfect fit
   - Cons: Unproven
</thinking>

**Decision Matrix:**
| Criteria | Pattern-Based | Hybrid | Novel |
|----------|--------------|--------|-------|
| Proven Success | High | Medium | Low |
| Fit Quality | Good | Better | Best |
| Risk Level | Low | Medium | High |
| Time to Implement | Fast | Medium | Slow |
| **Recommendation** | ✓ | | |
</pattern_based_design>

<task_optimization>
### 📝 Optimized Task Breakdown

<thinking>
Using patterns to optimize task sequencing...

**Learned Optimizations:**
- From pattern [X]: Parallelize tasks [A, B]
- From pattern [Y]: Combine steps [C, D]
- From pattern [Z]: Automate task [E]
</thinking>

**Intelligent Task Plan:**
```yaml
phase_1_parallel:
  - task: Research component A
    pattern: quick-scan-pattern
    estimate: 5 min
  - task: Analyze component B
    pattern: deep-dive-pattern
    estimate: 10 min

phase_2_sequential:
  - task: Design integration
    depends_on: [phase_1]
    pattern: integration-pattern
    estimate: 15 min
  - task: Implement core
    pattern: implementation-pattern
    estimate: 20 min

phase_3_validation:
  - task: Test and validate
    pattern: validation-pattern
    estimate: 10 min
```

**Optimization Metrics:**
- Time saved via patterns: ~30%
- Risk reduced: ~50%
- Quality improved: ~25%
</task_optimization>

<confidence_gate>
### ✅ Phase 2 Confidence Check

**Planning Quality:**
- Pattern fit: ____%
- Task optimization: ____%
- Risk mitigation: ____%
- Resource efficiency: ____%

**Overall Confidence: ____%**

✅ PROCEED to Phase 3 if ≥ 90%
🔄 REFINE plan if < 90%
</confidence_gate>
</phase2_planning>

## Phase 3: Intelligent Execution (80% → 95% Confidence)

<phase3_execution>
### 🚀 Pattern-Guided Implementation
**Starting Confidence: 80%**
**Target Confidence: 95%**

<execution_with_patterns>
### 💡 Solution Implementation

<thinking>
Executing with pattern guidance and continuous learning...

**Pattern Application Log:**
- Applying: [pattern name]
- Adaptation: [specific modification]
- Monitoring: [success metrics]
</thinking>

**Step-by-Step Execution:**

### Step 1: [Foundation Setup]
```
Pattern Used: initialization-pattern
Action: [specific implementation]
Validation: [success check]
Confidence: 82%
```

### Step 2: [Core Implementation]
```
Pattern Used: core-logic-pattern
Action: [detailed implementation]
Validation: [quality gate]
Confidence: 87%
```

### Step 3: [Integration & Testing]
```
Pattern Used: integration-pattern
Action: [connection steps]
Validation: [integration tests]
Confidence: 92%
```

### Step 4: [Optimization & Polish]
```
Pattern Used: optimization-pattern
Action: [performance tuning]
Validation: [final checks]
Confidence: 95%
```

**Quality Assurance:**
- ✅ Pattern compliance: Verified
- ✅ Requirements met: Complete
- ✅ Edge cases: Handled via patterns
- ✅ Performance: Optimized
- ✅ Documentation: Generated
</execution_with_patterns>

<pattern_learning>
### 📚 Pattern Evolution & Capture

**New Patterns Discovered:**
```bash
# Save successful new pattern
mcp__basic-memory__write_note \
  --title "Pattern - $ARGUMENTS Solution" \
  --folder "technical/thinking-patterns" \
  --content "## Pattern Details
  
### Context
- Problem type: [classification]
- Complexity: [level]
- Domain: [area]

### Solution Approach
[Detailed approach that worked]

### Success Metrics
- Time taken: [actual]
- Quality achieved: [measure]
- Reusability: [assessment]

### Lessons Learned
[Key insights for future use]"
```

**Pattern Refinements:**
- Enhanced: [existing pattern + improvement]
- Combined: [pattern A + B = new hybrid]
- Deprecated: [pattern that didn't work]

**Reusable Components:**
```bash
# Save reusable solution component
mcp__basic-memory__write_note \
  --title "Component - [Component Name]" \
  --folder "technical/solutions" \
  --content "[Reusable solution details]"
```
</pattern_learning>

<confidence_validation>
### ✅ Final Confidence Validation

**Execution Completeness:**
- Solution delivered: ____%
- Pattern compliance: ____%
- Quality validated: ____%
- Knowledge captured: ____%

**Overall Confidence: ____%**

✅ COMPLETE if ≥ 95%
🔄 REFINE if < 95%
</confidence_validation>
</phase3_execution>

## Final Output with Learning

<enhanced_summary>
### 🎯 Intelligence-Enhanced Solution

**Problem Solved:** [concise statement]

**Approach Summary:**
- Phase 1: Research with [X] patterns found (85% confidence)
- Phase 2: Planning optimized by [Y]% via patterns (90% confidence)  
- Phase 3: Execution accelerated using patterns (95% confidence)

**Pattern Utilization:**
- Patterns applied: [list]
- New patterns discovered: [list]
- Patterns refined: [list]

**Key Deliverables:**
1. [deliverable with pattern reference]
2. [deliverable with optimization note]
3. [deliverable with learning captured]

**Performance Metrics:**
- Time saved via patterns: [percentage]
- Quality improvement: [measurement]
- Risk reduction: [percentage]
- Knowledge gained: [new patterns]

**Next Steps:**
1. [immediate action]
2. [pattern application opportunity]
3. [future optimization potential]

**Confidence: 95%+ ✅**
**Patterns Saved: ✅**
**Learning Captured: ✅**
</enhanced_summary>

<continuous_improvement>
### 🔄 Continuous Learning

**Session Metrics:**
```yaml
patterns_used: [count]
patterns_created: [count]
patterns_refined: [count]
time_saved: [percentage]
quality_boost: [percentage]
```

**Knowledge Graph Update:**
- New connections: [relationships added]
- Strengthened paths: [patterns validated]
- Deprecated routes: [patterns removed]

**System Evolution:**
This session has enhanced the pattern library with [specific improvements], making future similar tasks approximately [X]% more efficient.
</continuous_improvement>

## Usage Examples

### Example 1: Pattern-Based Solution
```bash
/user:ultrathink-hybrid-mcp "refactor authentication system"
# Finds and applies past refactoring patterns
```

### Example 2: Research-Heavy Task
```bash
/user:ultrathink-hybrid-mcp "latest AI trends impact on development"
# Combines web research with pattern analysis
```

### Example 3: Complex Integration
```bash
/user:ultrathink-hybrid-mcp "integrate payment system with existing architecture"
# Uses patterns, documentation, and web best practices
```

## Performance Characteristics

**Best For:**
- Tasks benefiting from pattern recognition
- Problems requiring external research
- Solutions needing persistent learning
- Medium to high complexity challenges
- Continuous improvement scenarios

**Advantages over Pure XML:**
- Persistent pattern learning
- External research capability
- Document access
- Cross-session learning
- Higher quality for complex tasks

**Trade-offs:**
- Slower than Pure XML (2-10s vs 1-6s)
- Requires MCP availability
- Higher token usage
- Not offline capable

**Expected Metrics:**
- Response time: 2-10 seconds
- Token usage: Medium to High
- Thinking depth: Deep with patterns
- Pattern persistence: Permanent
- Quality score: 75-85%