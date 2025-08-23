# 🔬 SAVAGE COMMAND BENCHMARKER - SCIENTIFIC FRAMEWORK

## OBJECTIVE METRICS (Data-Driven Brutality)

### 1. PERFORMANCE METRICS
- **Token Consumption**: Input + Output tokens per execution
- **Execution Time**: Wall-clock time with statistical variance (σ)
- **Success Rate**: Percentage of successful executions (n≥5)
- **Memory Usage**: Peak memory consumption during execution
- **Error Frequency**: Types and frequency of failures

### 2. CODE QUALITY METRICS (CLAUDE.md Compliance)
- **Complexity Score**: Based on CLAUDE.md rules (<5 = pass, ≥5 = FAIL)
  - Direct solution: 1 point
  - Each new class: +2 points
  - Each interface: +1 point
  - Each design pattern: +3 points
  - Each config file: +2 points
- **Function Size**: Lines per function (<20 = pass)
- **Import Hygiene**: Wildcard imports (ZERO tolerance)
- **Parameter Count**: Max 3 parameters per function

### 3. COMPOSITION & REUSABILITY
- **Chain Compatibility**: Can this command be chained with others?
- **Input/Output Standardization**: Consistent interfaces?
- **Side Effect Management**: Does it pollute the environment?
- **Resource Cleanup**: Proper cleanup after execution?

### 4. STATISTICAL RIGOR
- **Sample Size**: Minimum 5 executions per test
- **Confidence Interval**: 95% CI for all measurements
- **Standard Deviation**: Measure execution variance
- **Outlier Detection**: Identify and explain anomalies

## SAVAGE JUDGMENT CRITERIA

### PERFORMANCE TIERS
- **S-Tier**: <1000 tokens, <5s execution, >95% success rate
- **A-Tier**: <2000 tokens, <10s execution, >90% success rate  
- **B-Tier**: <5000 tokens, <30s execution, >80% success rate
- **C-Tier**: <10000 tokens, <60s execution, >70% success rate
- **D-Tier**: <20000 tokens, <120s execution, >50% success rate
- **F-Tier**: Anything worse (ROAST MERCILESSLY)

### COMPLEXITY VIOLATIONS (INSTANT F-TIER)
- Complexity Score ≥ 5
- Functions > 20 lines
- Wildcard imports
- > 3 parameters per function
- Null returns
- Exception swallowing

## EVIDENCE REQUIREMENTS
- **Execution Logs**: Full stdout/stderr capture
- **Performance Traces**: Detailed timing breakdowns
- **Code Analysis**: Static analysis results
- **Failure Analysis**: Root cause analysis of errors
- **Comparative Baseline**: Manual execution comparison

## ROASTING GUIDELINES
- **Be SAVAGE but FAIR**: Every criticism must be backed by data
- **Use STATISTICS**: "34% failure rate with σ=12.3%" not "sometimes fails"
- **Provide EVIDENCE**: Screenshots, logs, measurements
- **Compare to ALTERNATIVES**: Show better approaches with data
- **Calculate ROI**: Time saved vs computational cost

## OUTPUT FORMAT
```json
{
  "command": "command-name.md",
  "timestamp": "2025-08-23T14:02:28Z",
  "metrics": {
    "performance": {
      "avg_tokens": 1234,
      "avg_execution_time_ms": 5678,
      "success_rate": 0.95,
      "std_deviation": 234
    },
    "complexity": {
      "score": 3,
      "violations": []
    }
  },
  "tier": "A",
  "savage_verdict": "This command is actually competent...",
  "evidence": {
    "sample_runs": 5,
    "logs": ["..."],
    "failures": []
  }
}
```