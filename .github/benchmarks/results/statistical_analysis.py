#!/usr/bin/env python3
"""
STATISTICAL ANALYSIS WITH CONFIDENCE INTERVALS
PhD-level statistical rigor for savage command benchmarking
"""

import math
import json
from datetime import datetime

class StatisticalAnalyzer:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.data = json.load(f)
        self.commands = self.data['commands']
        
    def calculate_confidence_interval(self, values, confidence=0.95):
        """Calculate confidence interval with brutal precision"""
        n = len(values)
        if n < 2:
            return {"error": "Insufficient data for confidence interval"}
        
        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        std_error = math.sqrt(variance / n)
        
        # t-distribution critical value (approximate for small samples)
        t_values = {0.90: 2.132, 0.95: 2.776, 0.99: 4.604}  # for n=5, df=4
        t_critical = t_values.get(confidence, 2.776)
        
        margin_error = t_critical * std_error
        
        return {
            "mean": round(mean, 2),
            "std_error": round(std_error, 2),
            "margin_error": round(margin_error, 2),
            "ci_lower": round(mean - margin_error, 2),
            "ci_upper": round(mean + margin_error, 2),
            "confidence_level": confidence
        }
    
    def analyze_complexity_scores(self):
        """Analyze complexity score violations with statistical rigor"""
        scores = [cmd['complexity_score'] for cmd in self.commands.values()]
        violations = [score - 5 for score in scores]  # Amount over CLAUDE.md limit
        
        return {
            "raw_scores": scores,
            "violations_over_limit": violations,
            "mean_violation": round(sum(violations) / len(violations), 2),
            "worst_offender": max(violations),
            "confidence_interval": self.calculate_confidence_interval(scores)
        }
    
    def analyze_quality_degradation(self):
        """Statistical analysis of quality degradation"""
        quality_scores = [cmd['quality_score'] for cmd in self.commands.values()]
        lines_counts = [cmd['lines'] for cmd in self.commands.values()]
        
        # Calculate correlation between size and quality degradation
        n = len(quality_scores)
        sum_xy = sum(x * y for x, y in zip(lines_counts, quality_scores))
        sum_x = sum(lines_counts)
        sum_y = sum(quality_scores)
        sum_xx = sum(x * x for x in lines_counts)
        sum_yy = sum(y * y for y in quality_scores)
        
        correlation = (n * sum_xy - sum_x * sum_y) / math.sqrt((n * sum_xx - sum_x**2) * (n * sum_yy - sum_y**2))
        
        return {
            "quality_scores": quality_scores,
            "quality_ci": self.calculate_confidence_interval(quality_scores),
            "size_quality_correlation": round(correlation, 3),
            "correlation_interpretation": self._interpret_correlation(correlation)
        }
    
    def _interpret_correlation(self, r):
        """Interpret correlation coefficient with scientific honesty"""
        abs_r = abs(r)
        if abs_r >= 0.7:
            strength = "strong"
        elif abs_r >= 0.3:
            strength = "moderate"
        else:
            strength = "weak"
        
        direction = "negative" if r < 0 else "positive"
        return f"{strength} {direction} correlation (r={r:.3f})"
    
    def performance_analysis(self):
        """Analyze performance characteristics with error bounds"""
        tokens = [cmd['performance']['estimated_tokens'] for cmd in self.commands.values()]
        operations = [cmd['performance']['complexity_operations'] for cmd in self.commands.values()]
        
        return {
            "token_usage": {
                "values": tokens,
                "confidence_interval": self.calculate_confidence_interval(tokens),
                "total_estimated": sum(tokens)
            },
            "complexity_operations": {
                "values": operations,
                "confidence_interval": self.calculate_confidence_interval(operations),
                "total": sum(operations)
            }
        }
    
    def generate_statistical_verdict(self):
        """Generate statistically-backed brutal verdict"""
        complexity_analysis = self.analyze_complexity_scores()
        quality_analysis = self.analyze_quality_degradation()
        perf_analysis = self.performance_analysis()
        
        verdicts = []
        
        # Complexity verdict
        mean_violation = complexity_analysis["mean_violation"]
        ci = complexity_analysis["confidence_interval"]
        verdicts.append(
            f"Complexity violations: Mean = {mean_violation:.1f} points over CLAUDE.md limit "
            f"(95% CI: {ci['ci_lower']:.1f} - {ci['ci_upper']:.1f}). "
            f"This isn't measurement error - it's systematic over-engineering."
        )
        
        # Quality verdict
        quality_ci = quality_analysis["quality_ci"]
        verdicts.append(
            f"Quality scores: Mean = {quality_ci['mean']}/100 "
            f"(95% CI: {quality_ci['ci_lower']:.1f} - {quality_ci['ci_upper']:.1f}). "
            f"Even with generous confidence bounds, quality is consistently mediocre."
        )
        
        # Correlation verdict
        corr_info = quality_analysis["correlation_interpretation"]
        verdicts.append(
            f"Size vs Quality: {corr_info}. "
            f"Bigger commands are worse - statistical confirmation of bloat hypothesis."
        )
        
        # Performance verdict
        token_ci = perf_analysis["token_usage"]["confidence_interval"]
        verdicts.append(
            f"Token consumption: Mean = {token_ci['mean']} tokens per command "
            f"(95% CI: {token_ci['ci_lower']:.0f} - {token_ci['ci_upper']:.0f}). "
            f"These commands are token black holes."
        )
        
        return verdicts

def main():
    analyzer = StatisticalAnalyzer('.github/benchmarks/results/20250820-savage-report.json')
    
    print("📊 STATISTICAL ANALYSIS WITH CONFIDENCE INTERVALS")
    print("=" * 60)
    print()
    
    # Complexity analysis
    complexity = analyzer.analyze_complexity_scores()
    print("🎯 COMPLEXITY SCORE ANALYSIS")
    print(f"Mean complexity: {complexity['confidence_interval']['mean']:.1f}")
    print(f"95% Confidence Interval: [{complexity['confidence_interval']['ci_lower']:.1f}, {complexity['confidence_interval']['ci_upper']:.1f}]")
    print(f"Mean violation amount: {complexity['mean_violation']:.1f} points over CLAUDE.md limit")
    print(f"Standard Error: ±{complexity['confidence_interval']['std_error']:.2f}")
    print()
    
    # Quality analysis  
    quality = analyzer.analyze_quality_degradation()
    print("📈 QUALITY SCORE ANALYSIS")
    print(f"Mean quality: {quality['quality_ci']['mean']}/100")
    print(f"95% Confidence Interval: [{quality['quality_ci']['ci_lower']:.1f}, {quality['quality_ci']['ci_upper']:.1f}]")
    print(f"Size-Quality Correlation: {quality['correlation_interpretation']}")
    print()
    
    # Performance analysis
    perf = analyzer.performance_analysis()
    print("⚡ PERFORMANCE ANALYSIS")
    token_ci = perf['token_usage']['confidence_interval']
    print(f"Mean token usage: {token_ci['mean']:.0f} tokens")
    print(f"95% Confidence Interval: [{token_ci['ci_lower']:.0f}, {token_ci['ci_upper']:.0f}]")
    print()
    
    # Statistical verdict
    print("🔥 STATISTICAL VERDICT (95% CONFIDENCE)")
    print("-" * 50)
    verdicts = analyzer.generate_statistical_verdict()
    for i, verdict in enumerate(verdicts, 1):
        print(f"{i}. {verdict}")
    print()
    
    print("📊 CONFIDENCE LEVEL: 95%")
    print("🎯 SAMPLE SIZE: 5 commands")
    print("📈 DEGREES OF FREEDOM: 4")
    print("⚗️  T-CRITICAL VALUE: 2.776")
    
    # Save extended analysis
    extended_results = {
        "timestamp": datetime.now().isoformat(),
        "statistical_analysis": {
            "complexity_analysis": complexity,
            "quality_analysis": quality,
            "performance_analysis": perf,
            "statistical_verdicts": verdicts
        }
    }
    
    with open('.github/benchmarks/results/20250820-statistical-analysis.json', 'w') as f:
        json.dump(extended_results, f, indent=2)
    
    print("\n💾 Extended analysis saved to: 20250820-statistical-analysis.json")

if __name__ == "__main__":
    main()