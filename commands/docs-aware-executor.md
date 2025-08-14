# Docs-Aware Executor - Intelligent Documentation-Driven Execution

<task>
Execute commands with automatic documentation context loading and knowledge injection for: $ARGUMENTS
</task>

<context>
This command reads relevant documentation before executing any command, enriching execution with contextual knowledge and best practices.

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
   - Gotchas: [anticipate]

3. Execution Strategy
   - Documentation to load: [prioritize]
   - Context to inject: [select]
   - Validation points: [identify]
   - Success criteria: [define from docs]
</pre_execution_thinking>
</thinking_orchestration>

<documentation_discovery>
## Intelligent Documentation Discovery
<discovery_thinking>
Finding relevant documentation for "$ARGUMENTS":

1. **Search Locations**
   <location_thinking>
   Priority order:
   - Project docs: .claude/docs/, docs/, README
   - User docs: ~/.claude/docs/
   - Command docs: Inline documentation
   - External: API docs, library docs
   - Memory: Previous executions, patterns
   </location_thinking>

2. **Relevance Scoring**
   <relevance_thinking>
   Scoring documentation:
   - Direct match: Score 5
   - Related concept: Score 4
   - Same category: Score 3
   - General practices: Score 2
   - Tangential: Score 1
   
   Threshold: Include if score ≥ 3
   </relevance_thinking>

3. **Content Extraction**
   <extraction_thinking>
   Extract from docs:
   - Command syntax
   - Parameters/options
   - Best practices
   - Common pitfalls
   - Examples
   - Performance tips
   </extraction_thinking>
</discovery_thinking>
</documentation_discovery>

<context_injection>
## Smart Context Injection
<injection_strategy>
Injecting documentation knowledge:

1. **Pre-Execution Injection**
   ```markdown
   CONTEXT FROM DOCS:
   - Best Practice: [from documentation]
   - Warning: [known issues]
   - Tip: [optimization suggestion]
   - Example: [relevant pattern]
   ```

2. **Parameter Enhancement**
   <parameter_thinking>
   From docs, enhancing parameters:
   - Default values: [apply if missing]
   - Recommended values: [suggest]
   - Validation rules: [enforce]
   - Incompatible combinations: [prevent]
   </parameter_thinking>

3. **Execution Modification**
   <modification_thinking>
   Based on docs, modifying execution:
   - Add safety checks: [from warnings]
   - Include prerequisites: [from requirements]
   - Apply optimizations: [from tips]
   - Avoid antipatterns: [from pitfalls]
   </modification_thinking>
</injection_strategy>
</context_injection>

<documentation_sources>
## Documentation Source Handlers

### Source 1: Project Documentation
<project_docs_handler>
Reading from project:
```bash
# Check standard locations
- Read .claude/docs/*.md
- Read docs/**/*.md
- Parse README.md
- Extract from CLAUDE.md
```

Extraction focus:
- Project conventions
- Coding standards
- Architecture decisions
- Tool configurations
</project_docs_handler>

### Source 2: Command Documentation
<command_docs_handler>
Reading from commands:
```bash
# Parse command files
- Extract from /user:command-name
- Parse XML documentation blocks
- Read usage examples
- Extract best practices
```

Extraction focus:
- Command syntax
- Parameter details
- Usage patterns
- Integration points
</command_docs_handler>

### Source 3: Claude System Docs
<system_docs_handler>
Reading from Claude docs:
```bash
# System documentation
- ~/.claude/docs/*.md
- Template patterns
- Agent documentation
- Hook configurations
```

Extraction focus:
- Claude conventions
- System capabilities
- Integration patterns
- Performance tips
</system_docs_handler>

### Source 4: External Documentation
<external_docs_handler>
Reading from external sources:
```bash
# When needed
- API documentation
- Library references
- Framework guides
- Stack Overflow patterns
```

Extraction focus:
- API contracts
- Version compatibility
- Known issues
- Community solutions
</external_docs_handler>

### Source 5: Memory and Learning
<memory_handler>
Reading from memory:
```bash
# Historical context
- Previous executions
- Learned patterns
- Success/failure cases
- Optimization discoveries
```

Using: mcp__basic-memory__search_notes
For: Pattern retrieval and learning
</memory_handler>
</documentation_sources>

<execution_enhancement>
## Documentation-Enhanced Execution

### Phase 1: Pre-Flight Check
<preflight_thinking>
Before execution:

1. Documentation Validation
   - Required docs found: [verify]
   - Coverage complete: [assess]
   - Version compatibility: [check]
   - Dependencies met: [confirm]

2. Context Preparation
   - Knowledge loaded: [list]
   - Constraints identified: [enumerate]
   - Best practices ready: [confirm]
   - Examples available: [verify]

3. Risk Assessment
   - Known issues: [from docs]
   - Mitigation strategies: [prepared]
   - Rollback plan: [if needed]
   - Success criteria: [defined]
</preflight_thinking>

### Phase 2: Enriched Execution
<execution_thinking>
Executing with documentation context:

1. Apply Best Practices
   ```
   FROM DOCS: [best practice]
   APPLYING: [how it's implemented]
   BENEFIT: [expected improvement]
   ```

2. Avoid Known Pitfalls
   ```
   WARNING FROM DOCS: [issue]
   PREVENTION: [mitigation applied]
   VERIFICATION: [check performed]
   ```

3. Use Recommended Patterns
   ```
   PATTERN FROM DOCS: [pattern]
   IMPLEMENTATION: [how applied]
   VALIDATION: [correctness check]
   ```
</execution_thinking>

### Phase 3: Validation Against Docs
<validation_thinking>
Post-execution validation:

1. Success Criteria Check
   - Doc criteria: [listed]
   - Actual result: [compared]
   - Match status: [verified]

2. Quality Validation
   - Best practices followed: [checked]
   - Antipatterns avoided: [confirmed]
   - Performance acceptable: [validated]

3. Documentation Update
   - New patterns discovered: [document]
   - Issues encountered: [record]
   - Optimizations found: [save]
</validation_thinking>
</execution_enhancement>

<knowledge_synthesis>
## Knowledge Synthesis Engine
<synthesis_thinking>
Combining documentation sources:

1. **Conflict Resolution**
   <conflict_thinking>
   When docs conflict:
   - Priority: Project > User > System > External
   - Recency: Newer overrides older
   - Specificity: Specific over general
   - Authority: Official over community
   </conflict_thinking>

2. **Gap Identification**
   <gap_thinking>
   Documentation gaps found:
   - Missing: [what's not documented]
   - Unclear: [ambiguous sections]
   - Outdated: [needs updating]
   - Incomplete: [partial coverage]
   
   Compensation strategy:
   - Use defaults: [safe assumptions]
   - Ask user: [when critical]
   - Test carefully: [when uncertain]
   </gap_thinking>

3. **Pattern Extraction**
   <pattern_extraction>
   Patterns from documentation:
   - Common workflows: [identified]
   - Best practices: [extracted]
   - Integration patterns: [recognized]
   - Optimization techniques: [learned]
   </pattern_extraction>
</synthesis_thinking>
</knowledge_synthesis>

<adaptive_learning>
## Documentation Learning System
<learning_thinking>
Learning from documentation usage:

1. **Effectiveness Tracking**
   - Which docs helped: [track usage]
   - Success correlation: [measure impact]
   - Time saved: [quantify benefit]
   - Errors prevented: [count avoided]

2. **Pattern Recognition**
   - Frequently needed docs: [cache]
   - Common combinations: [bundle]
   - Unused documentation: [deprioritize]
   - Missing documentation: [flag for creation]

3. **Optimization Application**
   - Faster discovery: [improve search]
   - Better relevance: [tune scoring]
   - Smarter caching: [optimize storage]
   - Predictive loading: [anticipate needs]
</learning_thinking>
</adaptive_learning>

<error_handling>
## Documentation-Aware Error Recovery
<error_recovery_thinking>
When execution fails:

1. **Check Documentation**
   - Error mentioned in docs? [search]
   - Known issue? [verify]
   - Workaround available? [apply]
   - Alternative approach? [try]

2. **Documentation Gaps**
   - Undocumented behavior: [record]
   - Missing error case: [document]
   - Unclear instruction: [clarify]
   - Create documentation: [if needed]

3. **Fallback Strategies**
   - Try without enhancement: [baseline]
   - Use minimal context: [reduce complexity]
   - Request user guidance: [when stuck]
   - Document resolution: [for future]
</error_recovery_thinking>
</error_handling>

<output_format>
## Execution Output with Documentation Context
<output_structure>
```markdown
## Documentation-Enhanced Execution

### Documentation Loaded
- Sources: [list of documentation]
- Relevance: [scoring]
- Coverage: [percentage]

### Context Applied
- Best Practices: [which ones]
- Warnings Heeded: [what avoided]
- Patterns Used: [which patterns]

### Execution Result
[Actual execution output]

### Validation Against Docs
- Success Criteria: ✅ Met
- Best Practices: ✅ Followed
- Performance: ✅ Acceptable

### Learning Captured
- New Pattern: [if discovered]
- Documentation Gap: [if found]
- Optimization: [if identified]

### Recommendations
- Documentation Updates: [if needed]
- Process Improvements: [if identified]
- Future Optimizations: [if possible]
```
</output_structure>
</output_format>

<usage_examples>
## Usage Examples

### Basic Documentation Enhancement
```bash
/user:docs-aware-executor /user:refactor
# Loads refactoring best practices before execution
```

### With Specific Documentation
```bash
/user:docs-aware-executor --docs="testing-guide.md" /user:java-tdd
# Loads specific documentation for context
```

### Force Documentation Refresh
```bash
/user:docs-aware-executor --refresh-docs /user:create-command
# Reloads all documentation, ignoring cache
```

### Skip Documentation
```bash
/user:docs-aware-executor --no-docs "simple command"
# Executes without documentation loading (faster)
```

### Documentation-Only Mode
```bash
/user:docs-aware-executor --docs-only /user:complex-command
# Shows what documentation would be loaded without executing
```
</usage_examples>

<integration_notes>
## Integration Capabilities

### Works With All Commands
- Enhances any `/user:*` command
- Enriches any `/project:*` command
- Augments system commands
- Improves agent execution

### Special Integrations
1. **thinking-enhancer.md**
   - Adds documentation to thinking
   - Provides context for decisions

2. **sequential-thinking-orchestrator.md**
   - Includes docs in complexity scoring
   - Enhances thinking with knowledge

3. **Memory System**
   - Saves documentation patterns
   - Learns from usage
   - Builds knowledge graph

### Chain Multiple Enhancers
```bash
/user:thinking-enhancer /user:docs-aware-executor /user:refactor
# Adds both thinking and documentation awareness
```
</integration_notes>

<performance_optimization>
## Performance Considerations
<performance_thinking>
Optimizing documentation loading:

1. **Caching Strategy**
   - Cache frequently used docs
   - TTL: 30 minutes
   - Invalidate on file change
   - Memory limit: 10MB

2. **Lazy Loading**
   - Load only when needed
   - Progressive enhancement
   - Async documentation fetch
   - Priority queue for loading

3. **Smart Filtering**
   - Relevance threshold
   - Size limits per doc
   - Excerpt extraction
   - Summary generation

4. **Parallel Processing**
   - Concurrent doc reading
   - Parallel extraction
   - Async synthesis
   - Background learning
</performance_thinking>
</performance_optimization>