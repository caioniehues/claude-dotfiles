# SAVAGE COMMAND BENCHMARKING FRAMEWORK
## Scientific Measurement Protocol

### OBJECTIVE METRICS (No BS Allowed)

#### Performance Metrics
- **Token Consumption**: Input + Output tokens per execution
- **Execution Time**: Mean, median, σ, 95th percentile
- **Success Rate**: % successful completions (strict definition)
- **Memory Usage**: Peak memory during execution
- **Error Frequency**: Types and patterns of failures

#### Quality Metrics  
- **Complexity Score**: Based on CLAUDE.md rules (must be < 5)
- **Maintainability Index**: Cyclomatic complexity of generated code
- **Coherence Score**: Output quality consistency
- **Composition Compatibility**: Can it chain with other commands?

#### Cost-Benefit Analysis
- **ROI Calculation**: Time saved vs token cost
- **Baseline Comparison**: Manual execution time vs command time
- **Value Proposition**: Does it actually solve a problem?

### EVIDENCE COLLECTION STANDARDS

#### Sample Size Requirements
- Minimum 5 test runs per command
- Different input scenarios (simple, medium, complex)
- Edge case testing (malformed inputs, missing dependencies)
- Cross-validation with different contexts

#### Documentation Requirements
- Screenshot equivalent outputs
- Full execution logs
- Error stack traces
- Performance telemetry
- User experience notes

### STATISTICAL RIGOR

#### Analysis Methods
- Standard deviation calculation
- Confidence intervals (95%)
- Outlier identification (z-score > 2)
- Trend analysis over multiple runs
- Comparative ranking against baselines

#### Failure Classification
- **Type 1**: Complete execution failure
- **Type 2**: Partial success with errors
- **Type 3**: Success but poor quality output
- **Type 4**: Success but violated complexity rules

### SAVAGE JUDGMENT CRITERIA

#### Excellence Thresholds
- Success rate > 95%
- Complexity score < 3
- Token efficiency > baseline * 0.8
- Error rate < 5%
- Composition compatibility: YES

#### Mediocrity Indicators  
- Success rate 80-95%
- Complexity score 3-5
- Token efficiency 0.5-0.8 baseline
- Error rate 5-15%
- Composition compatibility: PARTIAL

#### Garbage Bin Qualifiers
- Success rate < 80%
- Complexity score ≥ 5
- Token efficiency < 0.5 baseline  
- Error rate > 15%
- Composition compatibility: NO

### ROASTING PROTOCOLS

#### Evidence-Based Savagery
- Every criticism MUST be backed by data
- Include statistical significance tests
- Reference specific failure examples
- Compare against industry standards
- Provide constructive improvement paths

#### Forbidden Statements
- "It doesn't work" → Show failure rate: X% with evidence
- "It's slow" → Show execution time: X±σ vs baseline
- "It's complex" → Show complexity score: X/5 with breakdown
- "It's bad" → Show specific metric violations with data

This framework ensures we roast with SCIENCE, not just opinions.