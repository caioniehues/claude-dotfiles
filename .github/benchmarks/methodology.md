# SAVAGE COMMAND BENCHMARKER - SCIENTIFIC METHODOLOGY

## MEASUREMENT FRAMEWORK

### 1. OBJECTIVE METRICS (The Numbers Don't Lie)

#### Performance Metrics
- **Token Consumption**: Input + Output tokens per execution
- **Execution Time**: Wall clock time with statistical variance (σ)
- **Success Rate**: Well-defined success criteria with confidence intervals
- **Memory Usage**: Peak memory consumption during execution
- **Error Frequency**: Failure types and patterns

#### Quality Metrics (Based on CLAUDE.md Standards)
- **Complexity Score**: Per CLAUDE.md rules (must be < 5)
- **Function Length**: Lines of code (must be < 20)
- **Parameter Count**: Max 3 parameters rule compliance
- **Import Quality**: No wildcard imports score
- **Abstraction Level**: Premature abstraction detection

#### Composition Metrics
- **Chainability**: Can command output feed into other commands
- **Dependency Graph**: Required tools and external dependencies
- **Context Preservation**: Memory and state handling efficiency

### 2. TEST PROTOCOL

#### Statistical Requirements
- **Sample Size**: Minimum 5 executions per command
- **Confidence Level**: 95% confidence intervals
- **Outlier Detection**: Grubbs' test for anomalous results
- **Baseline Comparison**: Manual execution as control group

#### Test Categories
1. **Isolated Execution**: Command alone
2. **Composition Test**: Chained with other commands  
3. **Error Injection**: Malformed inputs and edge cases
4. **Load Test**: Repeated executions for consistency
5. **Context Switch**: Different project environments

### 3. SAVAGE JUDGMENT CRITERIA

#### Grade Scale (Evidence-Based)
- **A (90-100%)**: Consistently excellent, statistically superior
- **B (80-89%)**: Good performance with minor statistical variations
- **C (70-79%)**: Acceptable but shows measurable inefficiencies
- **D (60-69%)**: Poor performance, statistically significant problems
- **F (<60%)**: Empirically terrible, delete immediately

#### Roast Categories
- **Token Glutton**: >2σ above mean token consumption
- **Speed Demon/Slug**: Execution time outliers
- **Reliability Nightmare**: <80% success rate
- **Complexity Criminal**: Violates CLAUDE.md simplicity rules
- **Composition Catastrophe**: Breaks when combined with others

### 4. DATA COLLECTION PROTOCOL

#### Before Each Test
1. Clear caches and reset environment
2. Record baseline system metrics
3. Timestamp and environment snapshot

#### During Each Test
1. Monitor token consumption in real-time
2. Track execution phases and bottlenecks
3. Capture all outputs and errors
4. Measure memory usage patterns

#### After Each Test
1. Calculate statistical measures (mean, σ, CI)
2. Compare against baseline and peer commands
3. Document failure modes and edge cases
4. Archive raw data for reproducibility

### 5. REPORTING FORMAT

```json
{
  "command_name": "string",
  "test_timestamp": "ISO-8601",
  "metrics": {
    "performance": {
      "avg_tokens": number,
      "token_std_dev": number,
      "avg_execution_time_ms": number,
      "time_std_dev": number,
      "success_rate": number,
      "confidence_interval": [number, number]
    },
    "quality": {
      "complexity_score": number,
      "claude_md_compliance": number,
      "maintainability_index": number
    },
    "composition": {
      "chainability_score": number,
      "dependency_count": number,
      "context_preservation": number
    }
  },
  "savage_judgment": {
    "grade": "A-F",
    "roast_category": ["token_glutton", "speed_slug", ...],
    "evidence": "Statistical proof of why this command sucks/rocks",
    "recommendation": "Data-driven improvement suggestions"
  }
}
```

## RANDOM SELECTION ALGORITHM

Using cryptographically secure randomness to prevent bias:
1. Generate random seed from current timestamp
2. Apply Fisher-Yates shuffle to command list
3. Select top N commands for testing
4. Document selection process for reproducibility

## STATISTICAL ANALYSIS REQUIREMENTS

- **Normality Testing**: Shapiro-Wilk test for data distribution
- **Variance Analysis**: F-test for homogeneity 
- **Correlation Analysis**: Pearson/Spearman for metric relationships
- **Regression Analysis**: Identify performance predictors
- **Outlier Detection**: Modified Z-score method

## QUALITY ASSURANCE

- **Reproducible Results**: All tests must be repeatable
- **Version Control**: Test data and methodology versioned
- **Peer Review**: Results validated against manual execution
- **Bias Mitigation**: Blind testing where possible