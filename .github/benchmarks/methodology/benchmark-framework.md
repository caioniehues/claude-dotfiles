# SAVAGE COMMAND BENCHMARKER - Scientific Methodology

## Objective Metrics Framework

### 1. Token Consumption Analysis
- **Input Tokens**: Command template length + variable substitution
- **Output Tokens**: Generated response length (avg, min, max, std dev)
- **Total Cost**: Based on current Claude pricing model
- **Token Efficiency**: Output quality per token (subjective scoring)

### 2. Execution Performance
- **Response Time**: End-to-end latency (5 samples minimum)
- **Processing Phases**: Template parsing, generation, validation
- **Memory Footprint**: Peak RAM usage during execution
- **CPU Utilization**: Resource consumption profile

### 3. Success Rate Metrics
- **Completion Rate**: Commands that finish without error
- **Accuracy Rate**: Commands that produce correct/useful output
- **Consistency Rate**: Reproducible results across runs
- **Error Types**: Classification of failure modes

### 4. Complexity Scoring (CLAUDE.md Rules)
- **Template Complexity**: Nested blocks, conditional logic, loops
- **Cognitive Load**: Human comprehension difficulty (1-10 scale)
- **Maintenance Burden**: Lines of code, dependencies, abstractions
- **Pattern Violations**: Deviations from simplicity principles

### 5. Composition Compatibility
- **Chain-ability**: Can output feed into other commands?
- **Context Preservation**: State maintenance across command chains
- **Error Propagation**: Graceful failure handling in pipelines
- **Interface Consistency**: Standardized input/output formats

## Statistical Analysis Framework

### Sample Size Requirements
- **Minimum**: 5 executions per command for basic statistics
- **Preferred**: 20 executions for confidence intervals
- **Stress Test**: 100 executions for edge case detection

### Statistical Measures
- **Central Tendency**: Mean, median, mode for all metrics
- **Variability**: Standard deviation, variance, range
- **Distribution**: Normality tests, outlier detection
- **Confidence Intervals**: 95% CI for performance metrics

### Comparative Analysis
- **Baseline**: Manual execution time/quality
- **Peer Comparison**: Commands with similar functionality
- **Historical Trends**: Performance over time
- **Best-in-Class**: Top 10% performance benchmarks

## Evidence Collection Protocol

### Automated Data Collection
```bash
# Performance measurement wrapper
time -p [command] > output.log 2> error.log
# Memory usage tracking
/usr/bin/time -v [command] > memory.log 2>&1
# Token counting via Claude API
curl -X POST api/count-tokens -d @input.json
```

### Qualitative Assessment
- **Output Quality**: Expert review (1-10 scale)
- **Usefulness**: Real-world applicability rating
- **Clarity**: Communication effectiveness score
- **Completeness**: Task fulfillment percentage

### Edge Case Testing
- **Large Inputs**: 10KB+ argument strings
- **Empty Inputs**: Null/empty argument handling
- **Invalid Inputs**: Malformed/hostile input resistance
- **Concurrent Usage**: Multiple simultaneous executions

## Benchmark Test Scenarios

### Scenario 1: Simple Code Generation
- **Input**: "Create a Java class for user authentication"
- **Expected**: Clean, simple, testable code
- **Metrics**: Code quality, compilation success, test coverage

### Scenario 2: Complex Analysis Task  
- **Input**: "Analyze the architecture of this 50-file project"
- **Expected**: Comprehensive architectural insights
- **Metrics**: Accuracy, completeness, actionability

### Scenario 3: ADHD Task Management
- **Input**: "Plan my day with 15 competing priorities"
- **Expected**: Realistic, actionable daily plan
- **Metrics**: Time estimation accuracy, cognitive load

### Scenario 4: Error Handling
- **Input**: Deliberately broken/ambiguous requests
- **Expected**: Graceful failure with helpful guidance
- **Metrics**: Error clarity, recovery suggestions

## Savage but Fair Judgment Criteria

### Excellence (9-10/10)
- Sub-second response time
- >95% success rate  
- Complexity score ≤2
- Output indistinguishable from expert human

### Good (7-8/10)
- <3 second response time
- >85% success rate
- Complexity score ≤5
- Useful output with minor issues

### Acceptable (5-6/10)
- <10 second response time
- >70% success rate
- Complexity score ≤8
- Functional but requires refinement

### Poor (3-4/10)
- <30 second response time
- >50% success rate
- Complexity score ≤12
- Often fails or produces low-quality output

### Terrible (1-2/10)
- >30 second response time
- <50% success rate
- Complexity score >12
- Consistently fails or produces garbage

## Roasting Guidelines

### Data-Driven Criticism
❌ "This command sucks"
✅ "This command has a 34% failure rate with σ=12.3%, making it statistically indistinguishable from a random number generator"

### Constructive Brutality
❌ "Complete garbage"  
✅ "Response time exceeds human patience threshold by 247%, suggesting the command was optimized for geological rather than human timescales"

### Evidence-Based Recommendations
❌ "Fix everything"
✅ "Primary bottleneck: template parsing (73% of execution time). Recommend: pre-compiled templates, caching, or switching to interpretive dance"

## Output Format Standards

### JSON Schema
```json
{
  "command_name": "string",
  "test_date": "ISO-8601",
  "metrics": {
    "performance": {
      "avg_response_time": "number",
      "std_dev": "number", 
      "success_rate": "percentage",
      "token_consumption": "number"
    },
    "quality": {
      "output_score": "1-10",
      "complexity_score": "number",
      "maintainability": "1-10"
    }
  },
  "statistical_analysis": {
    "confidence_intervals": {},
    "outliers": [],
    "distribution_type": "string"
  },
  "savage_commentary": "string",
  "recommendations": ["array"]
}
```

### Report Structure
1. **Executive Summary**: Brutal one-liner judgment
2. **Quantitative Metrics**: Hard numbers with error bars
3. **Statistical Analysis**: Confidence intervals, outliers
4. **Comparative Ranking**: vs. peers and baseline
5. **Savage Commentary**: Data-backed roasting
6. **Improvement Roadmap**: Specific, measurable recommendations

This framework ensures every roast is backed by cold, hard statistics rather than subjective opinion.