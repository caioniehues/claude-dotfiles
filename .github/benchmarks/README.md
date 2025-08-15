# 🔬 SAVAGE COMMAND BENCHMARKER

**PhD in roasting bad code with statistical precision**

A comprehensive benchmarking system that scientifically measures and brutally judges commands in `/commands/` with objective data and savage but fair commentary.

## 🎯 Mission Statement

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." - Martin Fowler

This benchmarker enforces CLAUDE.md principles with statistical rigor and provides data-backed roasting of code quality violations.

## 📊 What It Measures

### Objective Metrics
- **Complexity Score** (based on CLAUDE.md rules)
  - Direct solution: 1 point
  - Each new class: +2 points  
  - Each interface: +1 point
  - Each design pattern: +3 points
  - Each configuration file: +2 points
  - **Target: < 5 points**

- **Documentation Quality** (0-10 scale)
  - Task descriptions, context, examples, implementation details

- **ADHD Friendliness** (0-10 scale)
  - Task chunking, energy awareness, pattern learning integration

- **Error Handling Quality** (0-10 scale)
  - Validation, fallback mechanisms, graceful degradation

- **Reusability Factor** (0-10 scale)
  - Parameterization, modularity, template sections

### Performance Metrics (Simulated)
- Execution time variance
- Memory usage estimation
- Token consumption estimates  
- Success rate predictions
- Failure pattern analysis

### Statistical Analysis
- Mean, standard deviation, confidence intervals
- Outlier detection
- Coefficient of variation
- Trend analysis

## 🚨 Roast Levels

| Score Range | Roast Level | Commentary Style |
|-------------|-------------|------------------|
| 70-100      | **MILD** ✅ | "Surprisingly competent" |
| 50-69       | **MEDIUM** ⚠️ | "Mediocrity epidemic" |
| 30-49       | **SAVAGE** 💀 | "Swiss Army knife designed by someone who's never seen a knife" |
| 0-29        | **NUCLEAR** 🚨 | "War crime against clean code principles" |

## 📁 Directory Structure

```
.github/benchmarks/
├── README.md                           # This file
├── run-savage-benchmark.sh            # Main execution script
├── scripts/
│   └── savage-command-benchmarker.py  # Core benchmarking engine
├── results/
│   ├── YYYYMMDD-HHMMSS-report.json   # Timestamped reports
│   └── 20250815-032739-report.json   # Example comprehensive report
└── data/
    └── command_analysis.json          # Evidence collection
```

## 🚀 Usage

### Quick Benchmark
```bash
# Analyze 3 random commands
python3 .github/benchmarks/scripts/savage-command-benchmarker.py

# Or use the wrapper script
bash .github/benchmarks/run-savage-benchmark.sh 3
```

### Continuous Monitoring  
```bash
# Run every hour
watch -n 3600 'bash .github/benchmarks/run-savage-benchmark.sh 5'

# Auto-commit results
bash .github/benchmarks/run-savage-benchmark.sh 3 --commit
```

### Custom Analysis
```python
from savage_command_benchmarker import SavageCommandBenchmarker

benchmarker = SavageCommandBenchmarker(Path("commands"))
result = benchmarker.benchmark_command(Path("commands/my-command.md"))
print(result.savage_judgment.commentary)
```

## 📊 Sample Output

```
🔬 SAVAGE COMMAND BENCHMARKER
PhD in roasting bad code with statistical precision
============================================================

🔬 Analyzing: java-test-driven-development.md
   Score: 52.3/100
   Roast Level: MEDIUM
   Complexity: 9 (🚨 VIOLATION)

⚠️ MEDIOCRITY EPIDEMIC ⚠️

Score of 59.8/100 is the programming equivalent of vanilla ice cream—
technically food, but why would you choose it? 1/3 complexity violations 
suggest room for improvement.

🎯 GLOBAL RECOMMENDATIONS:
1. 🎯 COMPLEXITY AUDIT: 1 commands exceed limits. Implement reviews.
2. 📏 SIZE STANDARDIZATION: Average 413 lines suggests bloat.
```

## 🎯 Key Features

### 1. **Random Selection**
- Scientifically random command selection for unbiased analysis
- Configurable sample sizes

### 2. **Evidence Collection**
- All measurements backed by actual file analysis
- Detailed evidence files for transparency
- Statistical confidence intervals

### 3. **CLAUDE.md Compliance**
- Enforces complexity scoring rules
- Validates simplicity principles
- Checks Java clean code standards

### 4. **Savage But Fair**
- Data-backed commentary
- Constructive improvement recommendations
- Comparable command analysis

### 5. **Statistical Rigor**
- 95% confidence intervals
- Outlier detection
- Variance analysis
- Trend identification

## 📈 Report Structure

### Executive Summary
- Overall quality scores
- Complexity violation rates
- Risk assessments

### Individual Command Analysis
```json
{
  "command_metrics": {
    "complexity_score": 9,
    "documentation_quality": 10.0,
    "adhd_friendliness": 0.0,
    "error_handling_quality": 7.0
  },
  "savage_judgment": {
    "overall_score": 52.3,
    "roast_level": "medium",
    "commentary": "This command has more complexity than a relationship status...",
    "improvement_recommendations": ["🎯 COMPLEXITY REDUCTION: Score is 9 (target: <5)"]
  }
}
```

### Statistical Analysis
- Comprehensive metrics with confidence intervals
- Performance correlations
- Quality trend analysis

## 🛠️ Customization

### Adding New Metrics
```python
def _assess_custom_metric(self, content: str) -> float:
    """Add your custom quality assessment"""
    score = 0.0
    # Your assessment logic here
    return min(score, 10.0)
```

### Custom Roast Commentary
```python
def _generate_custom_commentary(self, metrics, score):
    """Add your own savage commentary style"""
    if score < 30:
        return "Your custom nuclear roast here..."
```

### Integration with CI/CD
```yaml
# GitHub Actions example
- name: Savage Benchmark
  run: |
    python3 .github/benchmarks/scripts/savage-command-benchmarker.py
    # Fail if average score < 60
```

## 🎯 Quality Gates

### Recommended Thresholds
- **Complexity Score**: < 5 (hard limit)
- **Overall Quality**: > 70/100
- **Documentation**: > 6/10
- **Error Handling**: > 5/10
- **ADHD Optimization**: > 5/10 for user-facing commands

### Automation Triggers
- **Red Alert**: Complexity > 5
- **Yellow Warning**: Quality score < 60
- **Green Good**: All metrics in acceptable range

## 📚 Integration with CLAUDE.md

This benchmarker enforces the established standards:

### Complexity Rules
✅ **3-Question Rule**
1. Can I use what already exists?
2. Can I solve this with a simple method?  
3. Do I really need this abstraction NOW?

✅ **Complexity Scoring**
- Direct solution: 1 point
- Additional complexity penalties as defined

✅ **Quality Standards**
- Functions < 20 lines
- Final parameters
- No wildcard imports
- No null returns

## 🔮 Future Enhancements

### Planned Features
- **Real Performance Testing**: Execute commands and measure actual performance
- **Semantic Analysis**: AI-powered code understanding
- **Comparative Benchmarking**: Cross-repository comparisons
- **Trend Analysis**: Quality evolution over time
- **Auto-Remediation**: Suggested code improvements

### Integration Opportunities
- **IDE Plugins**: Real-time quality feedback
- **Git Hooks**: Pre-commit quality gates
- **Dashboard**: Executive quality reporting
- **Slack Bot**: Savage roasting on demand

## 💡 Contributing

### Adding New Assessments
1. Extend the `CommandMetrics` dataclass
2. Implement assessment method in `SavageCommandBenchmarker`
3. Update scoring logic in `generate_savage_judgment`
4. Add tests and documentation

### Improving Roast Quality
1. Analyze existing commentary patterns
2. Add new roast levels or categories
3. Implement domain-specific roasting
4. Maintain data-backed approach

## 📄 License

This benchmarker is part of the claude-dotfiles repository and follows the same licensing terms.

---

## 🎯 Bottom Line

**SAVAGE BENCHMARKER**: Scientifically measuring mediocrity since 2025.

*"When in doubt, roast with data."*

---

**Remember**: This tool is designed to improve code quality through objective measurement and constructive (if savage) feedback. The goal is better software, not hurt feelings. 

*Though if your feelings are hurt by accurate quality assessments, maybe that's the code talking.* 🔥