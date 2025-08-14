<task>
Implement Java code following SIMPLICITY FIRST principle with Clean Code standards through thinking-first validation. Check complexity score and reasoning before writing any code.
</task>

<context>
Quick Java implementation command with thinking-first architecture that enforces the 3-Question Rule and complexity scoring before any implementation. This is a simplicity-focused shorthand for java-clean-implementer with mandatory reasoning validation and MCP integration for complex scenarios.
</context>

<thinking_orchestration>
## Rapid Complexity Assessment
<complexity_detection>
Instant evaluation of request "$ARGUMENTS":
- Implementation type: [direct method / class creation / pattern usage]
- Abstraction need: [none / minimal / significant]
- Integration complexity: [simple / moderate / complex]
- Estimated complexity score: _____

Complexity Scoring (Rapid):
- Direct solution: 1 point
- Each new class: +2 points  
- Each interface: +1 point
- Each design pattern: +3 points
- Each config file: +2 points

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  REASON: Complex implementations need systematic thinking
  FALLBACK: Use full java-clean-implementer command
If complexity <= 3:
  PROCEED: With rapid thinking validation below
</complexity_detection>

## Rapid Pre-Implementation Thinking
<rapid_thinking>
Quick but thorough analysis before any code:

1. **Real Problem Identification**
   <thinking>
   What's actually being asked?
   - Surface request: "$ARGUMENTS"
   - Core need: [identify essential functionality]
   - Complexity drivers: [what might make this hard]
   Decision: [problem understanding] guides [solution approach]
   </thinking>

2. **Solution Landscape Scan**
   <thinking>
   What already exists that I can use?
   - Spring Boot: [quick scan for applicable features]
   - Java stdlib: [identify relevant utilities]  
   - Project code: [check for existing patterns]
   Choice: [use existing / build new] because [quick cost-benefit]
   </thinking>

3. **Simplicity Validation**
   <thinking>
   Is this the simplest approach?
   - Direct method possible? [yes/no with reason]
   - Patterns actually needed? [justify or reject]
   - Abstractions necessary now? [evidence-based decision]
   Approach: [selected strategy] maintains [simplicity goal]
   </thinking>
</rapid_thinking>
</thinking_orchestration>

<pre_implementation_check>
## STOP! Before Writing Code, Answer with Reasoning:

1. **Can I use what already exists?**
   <thinking_checkpoint>
   Quick scan results:
   - Spring Boot features: [found/not applicable]
   - Java standard library: [relevant utilities identified]
   - Existing project code: [reusable components located]
   
   Decision: [use existing / create new] 
   Reasoning: [cost-benefit in one sentence]
   </thinking_checkpoint>
   
2. **Can I solve this with a simple method?**
   <thinking_checkpoint>
   Simplicity assessment:
   - Direct implementation feasible? [yes/no]
   - Pattern complexity justified? [evidence check]
   - Method-level solution sufficient? [scope validation]
   
   Decision: [simple method / complex solution]
   Reasoning: [why this approach fits best]
   </thinking_checkpoint>
   
3. **Do I really need this abstraction NOW?**
   <thinking_checkpoint>
   Abstraction necessity check:
   - Current concrete implementations: [actual count, not theoretical]
   - YAGNI principle application: [strict evaluation]
   - Future needs predictability: [realistic assessment]
   
   Decision: [concrete implementation / abstraction]
   Reasoning: [evidence-based justification]
   </thinking_checkpoint>

### Calculate Complexity Score with Justification:
<complexity_reasoning>
Score breakdown with reasoning:
- Direct solution: [1 point] - [what makes this direct]
- New classes: [+N points] - [why each class is necessary]  
- Interfaces: [+N points] - [justification for each interface]
- Design patterns: [+N points] - [evidence for pattern necessity]
- Config files: [+N points] - [configuration complexity reasoning]

Total Score: [sum] points
Threshold Check: [≥ 5? STOP / < 5? PROCEED]
Reasoning: [why this complexity level is appropriate]
</complexity_reasoning>

**Score ≥ 5? STOP AND SIMPLIFY!**
</pre_implementation_check>

<implementation>
## Thinking-Driven Implementation Strategy

<implementation_decision>
Based on complexity score [value] and thinking analysis:

**If Score < 3** (Simple): Rapid implementation with thinking annotations
**If Score 3** (Moderate): Structured implementation with decision points  
**If Score > 3** (Complex): Delegate to full java-clean-implementer or MCP tools

Selected path: [chosen approach] because [reasoning summary]
</implementation_decision>

### Rapid Implementation (Score < 3)
<rapid_implementation_thinking>
For simple implementations:
1. **Direct solution approach**
   <thinking>
   Implementation strategy:
   - Method signature: [designed with reasoning]
   - Logic flow: [step-by-step with justification]
   - Return handling: [Optional vs direct with reason]
   </thinking>

2. **Quality checkpoints** 
   <thinking>
   Inline quality validation:
   - Parameters final? [enforced because immutability]
   - Function < 20 lines? [checked for single responsibility]
   - No wildcards? [explicit imports for clarity]
   - Meaningful names? [searchable and clear]
   </thinking>
</rapid_implementation_thinking>

### Structured Implementation (Score = 3)
<structured_implementation_thinking>
For moderate complexity:
1. **Pattern decision reasoning**
   <thinking>
   Why this pattern is needed:
   - Problem it solves: [specific issue addressed]
   - Simpler alternatives considered: [what was rejected and why]
   - Future benefit: [concrete advantage provided]
   </thinking>

2. **Incremental validation**
   <thinking>
   At each step, verify:
   - Still meeting simplicity goals? [checkpoint]
   - Complexity justified by value? [benefit validation]
   - Could this be simpler? [continuous simplification check]
   </thinking>
</structured_implementation_thinking>

### Complex Implementation (Score > 3)
Use the full java-clean-implementer command for detailed implementation:
`/user:java-clean-implementer`

Or invoke MCP sequential thinking for systematic analysis:
`mcp__mcp-sequentialthinking-tools__sequentialthinking_tools`

<delegation_reasoning>
Delegating because:
- Complexity score [value] exceeds rapid implementation threshold
- Multiple decision points require systematic thinking
- Quality assurance needs comprehensive validation
- Risk of over-engineering without structured guidance
</delegation_reasoning>
</implementation>

<rapid_error_recovery>
## Quick Error Recovery with Reasoning
<error_recovery_thinking>
If rapid implementation hits issues:

**Complexity Creep** (Score climbing during implementation)
<thinking>
- What's adding complexity? [identify source]
- Can it be simplified? [reduction options]
- Is complexity justified? [value validation]
Recovery: [simplification strategy] because [maintains goal]
</thinking>

**Pattern Mismatch** (Chosen approach not working)
<thinking>
- Why isn't it fitting? [root cause]
- What was missed in analysis? [oversight identification]  
- Simpler alternative available? [fallback options]
Recovery: [pivot strategy] because [better fits actual need]
</thinking>

**Quality Standard Violation** (Clean code rules broken)
<thinking>
- Which rule was violated? [specific standard]
- Why did it happen? [cause analysis]
- How to fix without adding complexity? [solution approach]
Recovery: [correction strategy] because [maintains quality and simplicity]
</thinking>
</error_recovery_thinking>
</rapid_error_recovery>

<output_commitment>
## Implementation Commitment

For this rapid implementation, I will:

1. **Think first**: Every decision backed by reasoning
2. **Validate complexity**: Score must stay < 5
3. **Use existing solutions**: Leverage what's already available  
4. **Write minimal code**: No unnecessary abstractions
5. **Apply clean standards**: Final parameters, meaningful names, small functions
6. **Test if needed**: Quick validation of behavior
7. **Document reasoning**: Show why choices were made

The code will be:
- **Simple** - Understandable immediately
- **Clean** - Following established standards  
- **Justified** - Every complexity point earned
- **Pragmatic** - Solving actual problems

<thinking_foundation>
This rapid command maintains the thinking-first principle while optimizing for speed:
- Complexity assessment prevents over-engineering upfront
- Reasoning checkpoints catch issues early
- Clear delegation thresholds for complex scenarios
- Error recovery maintains quality under pressure

When complexity > 3: Graceful escalation to systematic thinking tools
</thinking_foundation>
</output_commitment>