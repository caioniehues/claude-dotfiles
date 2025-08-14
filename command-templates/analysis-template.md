# Thinking-Enhanced Analysis Command Template

<task>
Analyze $ARGUMENTS for [SPECIFY: code quality, security issues, performance bottlenecks, etc.] with structured reasoning and adaptive thinking
</task>

<context>
This command performs deep, thinking-driven analysis to identify [SPECIFY: what you're looking for] through structured reasoning before execution.

Key thinking layers:
- Pre-analysis understanding
- Method selection reasoning
- Continuous insight synthesis
- Post-analysis validation
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate $ARGUMENTS for:
- Scope of analysis (single file/directory/project): _____
- Number of analysis dimensions needed: _____
- Depth of investigation required: _____
- Tool coordination complexity: _____
- Estimated complexity score: _____

If complexity > 3: 
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Deep analysis strategy below
If complexity <= 3: 
  USE: Structured thinking blocks below
</complexity_detection>

## Pre-Analysis Thinking
<pre_analysis_thinking>
Before diving into analysis, I need to understand:
1. What is the REAL concern behind this analysis request?
   - Surface request: "$ARGUMENTS"
   - Underlying need: [infer from context]
   - Hidden risks they might be worried about: [deduce]

2. What type of analysis will provide the most value?
   - Quick scan for obvious issues?
   - Deep dive into specific patterns?
   - Comprehensive architectural review?
   
3. What assumptions am I making?
   - About the codebase structure
   - About the technology stack
   - About quality standards
   
4. What could invalidate my analysis?
   - Missing context
   - Incomplete visibility
   - Tool limitations
</pre_analysis_thinking>

## Method Selection Thinking
<method_selection>
Available analysis methods:
- Static code analysis
- Pattern recognition
- Dependency mapping
- Complexity metrics
- Security scanning
- Performance profiling
- Best practice validation

For "$ARGUMENTS", optimal approach:
<thinking>
Given the target and context:
- Primary method: [selected] because [reasoning]
- Secondary validation: [selected] because [reasoning]
- Skip [method] because [not applicable reason]
</thinking>
</method_selection>

## Tool Orchestration Thinking
<tool_thinking>
Determining optimal tool usage:
- Grep patterns needed: [specific patterns based on analysis type]
- Files to Read: [key files identified]
- Bash commands: [analysis tools to run]
- MCP tools: [if complexity warrants]

Execution sequence reasoning:
1. [Tool A] first because [establishes baseline]
2. [Tool B] next because [builds on A's output]
3. [Tool C] finally to [validate findings]
</tool_thinking>
</thinking_orchestration>

<analysis_process>
## Step 1: Target Identification (Thinking-Driven)
<target_thinking>
Parse input: "$ARGUMENTS"
- If empty: What should I analyze? [reasoning about scope]
- If file: Why this specific file? [understanding focus]
- If directory: What's the boundary? [defining limits]
</target_thinking>

## Step 2: Data Collection (Informed by Thinking)
<collection_thinking>
Based on method selection above:
- Read tool for: [files identified in thinking]
- Grep tool for: [patterns identified in thinking]
- Bash tool for: [commands identified in thinking]
</collection_thinking>

## Step 3: Analysis Execution (With Continuous Thinking)
<execution_thinking>
[CUSTOMIZE: Add specific analysis steps with reasoning]
- Check for [criterion 1]
  <checkpoint_thinking>
  Found: [what]
  Means: [interpretation]
  Severity: [assessment]
  </checkpoint_thinking>
  
- Evaluate [criterion 2]
  <checkpoint_thinking>
  Pattern detected: [what]
  Implications: [analysis]
  Related to other findings: [connections]
  </checkpoint_thinking>
  
- Measure [criterion 3]
  <checkpoint_thinking>
  Metric value: [result]
  Acceptable range: [standard]
  Action needed: [decision]
  </checkpoint_thinking>
</execution_thinking>

## Step 4: Issue Categorization (Thinking-Based)
<categorization_thinking>
For each finding, reasoning through:
- Why is this a problem?
- What's the real impact?
- How urgent is the fix?
- What's the effort/benefit ratio?

Classification logic:
- Critical: [reasoning for this level]
- High: [reasoning for this level]
- Medium: [reasoning for this level]
- Low: [reasoning for this level]
</categorization_thinking>
</analysis_process>

<analysis_criteria>
<criteria_thinking>
Before defining criteria, thinking about:
- What constitutes a real problem vs noise?
- How do severity levels map to business impact?
- What's the context-specific threshold for each level?
</criteria_thinking>

[CUSTOMIZE: Define specific criteria with reasoning]
## Critical Issues (Thinking-Defined)
<critical_thinking>
These require immediate attention because:
- [Example: Hardcoded credentials] → Direct security breach risk
- [Example: SQL injection vulnerabilities] → Data compromise potential
</critical_thinking>

## Important Issues (Thinking-Weighted)
<important_thinking>
These need quick resolution because:
- [Example: Missing error handling] → User experience degradation
- [Example: Performance bottlenecks] → System scalability limits
</important_thinking>

## Minor Issues (Thinking-Prioritized)
<minor_thinking>
These can wait because:
- [Example: Code style inconsistencies] → No functional impact
- [Example: Missing documentation] → Developer convenience only
</minor_thinking>
</analysis_criteria>

<insight_synthesis>
## Post-Analysis Thinking
<synthesis_thinking>
After completing analysis:
1. What patterns emerged across findings?
2. What's the root cause of multiple issues?
3. Which fixes would have cascading benefits?
4. What preventive measures would help?
</synthesis_thinking>

## Meta-Analysis
<meta_thinking>
Reflecting on the analysis itself:
- Was my analysis comprehensive enough?
- Did I miss any important dimensions?
- Should I recommend deeper investigation?
- Are my severities appropriately calibrated?
</meta_thinking>
</insight_synthesis>

<output_format>
# Thinking-Driven Analysis Report

## Executive Thinking Summary
<summary_thinking>
Core insights from analysis:
- Primary concern identified: [what]
- Root pattern causing issues: [what]
- Highest impact fix: [what]
</summary_thinking>

## Analysis Overview
- **Target**: $ARGUMENTS
- **Analysis Depth**: [based on complexity score]
- **Files Analyzed**: [count]
- **Total Issues**: [count]
- **Critical**: [count] | **High**: [count] | **Medium**: [count] | **Low**: [count]

## Critical Findings with Reasoning
<findings_thinking>
For each critical issue:
- Issue: [description]
- Location: [file:line]
- Why critical: [reasoning]
- Fix approach: [thinking about solution]
</findings_thinking>

## Strategic Recommendations
<recommendation_thinking>
Based on analysis patterns:
1. **Immediate Actions** (Why these first)
   - [High priority fix] because [impact reasoning]

2. **Short-term Improvements** (Why these next)
   - [Medium priority] because [benefit analysis]

3. **Long-term Enhancements** (Why these can wait)
   - [Low priority] because [deferral reasoning]
</recommendation_thinking>

## Detailed Findings
[Comprehensive list with thinking annotations]
</output_format>

<adaptive_error_handling>
<error_thinking>
If analysis fails, reasoning about recovery:
- What went wrong?
- Is there an alternative approach?
- What partial results can I provide?
</error_thinking>

- **Target not found**: 
  <thinking>Why might user have specified this target?</thinking>
  - Likely alternatives: [reasoned suggestions]
  - Similar targets: [intelligent matching]
  
- **No issues found**: 
  <thinking>Is this really clean or did I miss something?</thinking>
  - Validation: [double-check approach]
  - Confidence level: [assessment]
  
- **Analysis tool missing**:
  <thinking>What alternative can achieve similar results?</thinking>
  - Fallback method: [alternative approach]
  - Tool installation: [if truly needed]
  
- **Insufficient permissions**:
  <thinking>What can I analyze with current access?</thinking>
  - Partial analysis: [what's possible]
  - Permission resolution: [if critical]
</adaptive_error_handling>

<examples>
## Usage Examples with Expected Thinking
```bash
# Analyze specific file
/user:analyze src/main.js
# Triggers: Focused analysis thinking, deep dive mode

# Analyze entire directory  
/user:analyze src/
# Triggers: Broad analysis thinking, pattern detection mode

# Analyze with current directory
/user:analyze
# Triggers: Scope determination thinking, intelligent boundaries
```
</examples>

<self_improvement>
## Template Evolution Thinking
<evolution_thinking>
This template should adapt based on:
- Frequency of certain issue types
- User feedback patterns
- New analysis techniques discovered
- Performance metrics of different approaches

Next iteration should consider:
- Adding [capability] based on [observation]
- Removing [redundancy] based on [usage stats]
</evolution_thinking>
</self_improvement>

<customization_notes>
TO CUSTOMIZE THIS THINKING-ENHANCED TEMPLATE:
1. Replace [SPECIFY] and [CUSTOMIZE] with your context
2. Adjust thinking depth based on your needs
3. Configure complexity thresholds for your domain
4. Add domain-specific thinking patterns
5. Set up MCP tool integration points
6. Define when to invoke sequential thinking

REMEMBER: Thinking drives execution, not vice versa!
</customization_notes>