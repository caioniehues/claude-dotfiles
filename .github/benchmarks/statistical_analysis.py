#!/usr/bin/env python3
import json
import statistics
import math
from datetime import datetime

def calculate_statistics(data_points):
    """Calculate comprehensive statistics"""
    mean = statistics.mean(data_points)
    median = statistics.median(data_points)
    std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0
    variance = statistics.variance(data_points) if len(data_points) > 1 else 0
    
    # Confidence interval (95%)
    n = len(data_points)
    if n > 1:
        t_value = 2.776  # t-distribution for n=5, 95% confidence
        margin_error = t_value * (std_dev / math.sqrt(n))
        ci_lower = mean - margin_error
        ci_upper = mean + margin_error
    else:
        ci_lower = ci_upper = mean
    
    return {
        'mean': round(mean, 2),
        'median': median,
        'std_dev': round(std_dev, 2),
        'variance': round(variance, 2),
        'min': min(data_points),
        'max': max(data_points),
        'range': max(data_points) - min(data_points),
        'confidence_interval_95': {
            'lower': round(ci_lower, 2),
            'upper': round(ci_upper, 2),
            'margin_error': round(margin_error, 2) if n > 1 else 0
        },
        'coefficient_variation': round((std_dev / mean) * 100, 1) if mean > 0 else 0
    }

def generate_savage_analysis(results):
    """Generate savage but statistically accurate analysis"""
    
    # Extract data for analysis
    complexity_scores = [r['scores']['complexity_score'] for r in results]
    quality_scores = [r['scores']['quality_score'] for r in results]
    lines_counts = [r['metrics']['lines_count'] for r in results]
    tokens = [r['metrics']['estimated_tokens'] for r in results]
    thinking_blocks = [r['metrics']['thinking_blocks'] for r in results]
    
    # Calculate statistics
    complexity_stats = calculate_statistics(complexity_scores)
    quality_stats = calculate_statistics(quality_scores)
    lines_stats = calculate_statistics(lines_counts)
    token_stats = calculate_statistics(tokens)
    thinking_stats = calculate_statistics(thinking_blocks)
    
    # Generate savage commentary
    savage_insights = []
    
    # Complexity analysis
    if complexity_stats['mean'] > 7:
        savage_insights.append(f"COMPLEXITY CATASTROPHE: Average complexity {complexity_stats['mean']}/10. That's not 'sophisticated', that's incompetent.")
    elif complexity_stats['mean'] > 5:
        savage_insights.append(f"OVER-ENGINEERED MEDIOCRITY: Average complexity {complexity_stats['mean']}/10. Someone confused 'clever' with 'complex'.")
    
    # Size analysis  
    if lines_stats['mean'] > 400:
        savage_insights.append(f"SIZE VIOLATION: Average {lines_stats['mean']} lines. War and Peace was shorter.")
    
    # Thinking block abuse
    if thinking_stats['max'] > 50:
        savage_insights.append(f"ANALYSIS PARALYSIS: One command has {thinking_stats['max']} thinking blocks. That's not thorough, that's therapy.")
    
    # Token consumption
    if token_stats['mean'] > 1000:
        savage_insights.append(f"TOKEN BANKRUPTCY: Average {token_stats['mean']} tokens per command. Your wallet is crying.")
    
    # Quality spread
    if quality_stats['std_dev'] > 2:
        savage_insights.append(f"QUALITY CHAOS: Quality variance {quality_stats['std_dev']:.1f}. Consistency? What's that?")
    
    # Performance predictions
    failure_rate = sum(1 for r in results if r['scores']['complexity_score'] > 6) / len(results)
    savage_insights.append(f"FAILURE PREDICTION: {failure_rate*100:.0f}% of commands are complexity disasters. That's worse than a coin flip.")
    
    return {
        'timestamp': datetime.now().isoformat(),
        'sample_size': len(results),
        'statistical_summary': {
            'complexity': complexity_stats,
            'quality': quality_stats,
            'lines': lines_stats,
            'tokens': token_stats,
            'thinking_blocks': thinking_stats
        },
        'savage_insights': savage_insights,
        'performance_metrics': {
            'average_complexity': complexity_stats['mean'],
            'complexity_failure_rate': f"{failure_rate*100:.1f}%",
            'token_efficiency': f"{token_stats['mean']:.0f} tokens/command",
            'bloat_factor': f"{lines_stats['mean'] / 100:.1f}x (baseline: 100 lines)",
            'thinking_obsession': f"{thinking_stats['mean']:.1f} blocks/command"
        },
        'recommendations': generate_recommendations(complexity_stats, quality_stats, results)
    }

def generate_recommendations(complexity_stats, quality_stats, results):
    """Generate actionable recommendations"""
    recommendations = []
    
    if complexity_stats['mean'] > 6:
        recommendations.append("IMMEDIATE: Refactor complex commands. Complexity > 6 is unacceptable.")
    
    if quality_stats['mean'] < 7:
        recommendations.append("URGENT: Quality improvement needed. Average quality < 7 indicates systemic issues.")
    
    # Find worst offenders
    worst_complexity = max(results, key=lambda x: x['scores']['complexity_score'])
    worst_quality = min(results, key=lambda x: x['scores']['quality_score'])
    
    recommendations.append(f"DELETE OR REBUILD: {worst_complexity['filename']} (complexity {worst_complexity['scores']['complexity_score']}/10)")
    recommendations.append(f"QUALITY DISASTER: {worst_quality['filename']} (quality {worst_quality['scores']['quality_score']}/10)")
    
    return recommendations

# Sample data for testing
if __name__ == "__main__":
    # This would normally load from the analysis results
    test_data = [
        {"filename": "test1", "scores": {"complexity_score": 5, "quality_score": 8}, 
         "metrics": {"lines_count": 200, "estimated_tokens": 500, "thinking_blocks": 5}},
        {"filename": "test2", "scores": {"complexity_score": 8, "quality_score": 6}, 
         "metrics": {"lines_count": 400, "estimated_tokens": 1000, "thinking_blocks": 20}}
    ]
    
    analysis = generate_savage_analysis(test_data)
    print(json.dumps(analysis, indent=2))