#!/usr/bin/env python3
"""
ADVANCED STATISTICAL ANALYSIS - SAVAGE EDITION
PhD-level statistical roasting with confidence intervals
"""

import json
import statistics
import math
from pathlib import Path
from datetime import datetime

def calculate_confidence_interval(data, confidence=0.95):
    """Calculate confidence interval with proper statistical rigor"""
    n = len(data)
    if n < 2:
        return None
    
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    std_error = std_dev / math.sqrt(n)
    
    # t-distribution critical value for 95% confidence (approximation)
    t_critical = 2.776 if n < 5 else 2.447 if n < 10 else 1.96
    
    margin_error = t_critical * std_error
    
    return {
        'mean': mean,
        'lower_bound': mean - margin_error,
        'upper_bound': mean + margin_error,
        'margin_error': margin_error,
        'confidence_level': confidence
    }

def statistical_significance_test(group1, group2):
    """Perform statistical significance test between two groups"""
    if len(group1) < 2 or len(group2) < 2:
        return None
    
    mean1, mean2 = statistics.mean(group1), statistics.mean(group2)
    var1, var2 = statistics.variance(group1), statistics.variance(group2)
    n1, n2 = len(group1), len(group2)
    
    # Welch's t-test for unequal variances
    pooled_se = math.sqrt(var1/n1 + var2/n2)
    t_stat = (mean1 - mean2) / pooled_se if pooled_se > 0 else 0
    
    # Degrees of freedom (Welch-Satterthwaite equation)
    df = ((var1/n1 + var2/n2)**2) / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1)) if var1 > 0 and var2 > 0 else 1
    
    return {
        't_statistic': t_stat,
        'degrees_freedom': df,
        'mean_difference': mean1 - mean2,
        'effect_size': abs(mean1 - mean2) / math.sqrt((var1 + var2) / 2) if var1 > 0 or var2 > 0 else 0
    }

def cost_benefit_analysis(metrics):
    """Calculate ROI and cost-benefit ratio"""
    token_cost = (metrics['token_consumption']['estimated_input'] + 
                  metrics['token_consumption']['estimated_output']) * 0.000015  # Approximate cost per token
    
    # Estimate time saved (assuming manual work takes 10x longer)
    time_saved_minutes = metrics['variance_statistics']['mean'] * 10 / 1000 / 60
    
    # Value calculation (assuming $60/hour rate)
    time_value = time_saved_minutes * 1.0  # $1 per minute
    
    roi = ((time_value - token_cost) / token_cost * 100) if token_cost > 0 else 0
    
    return {
        'estimated_cost_usd': token_cost,
        'estimated_time_saved_minutes': time_saved_minutes,
        'estimated_value_usd': time_value,
        'roi_percentage': roi,
        'cost_benefit_ratio': time_value / token_cost if token_cost > 0 else 0
    }

def generate_savage_scientific_report(data):
    """Generate the ultimate savage but scientifically rigorous report"""
    
    # Extract key metrics for analysis
    complexity_scores = [b['metrics']['complexity_score'] for b in data['benchmarks']]
    success_rates = [b['metrics']['success_rate'] for b in data['benchmarks']]
    execution_times = [b['metrics']['variance_statistics']['mean'] for b in data['benchmarks']]
    cvs = [b['metrics']['variance_statistics']['cv'] for b in data['benchmarks']]
    
    # Statistical analysis
    complexity_ci = calculate_confidence_interval(complexity_scores)
    success_ci = calculate_confidence_interval(success_rates)
    execution_ci = calculate_confidence_interval(execution_times)
    
    # Cost-benefit analysis for each command
    cost_benefits = []
    for benchmark in data['benchmarks']:
        cb = cost_benefit_analysis(benchmark['metrics'])
        cost_benefits.append({
            'command': benchmark['metrics']['command_name'],
            'analysis': cb
        })
    
    # Savage but scientific judgment
    savage_analysis = {
        'timestamp': datetime.now().isoformat(),
        'sample_analysis': {
            'total_commands_analyzed': len(data['benchmarks']),
            'statistical_power': 'Sufficient for savage judgment' if len(data['benchmarks']) >= 8 else 'Questionable like your code quality',
            'confidence_level': '95% - More confident than your last deploy'
        },
        'complexity_apocalypse': {
            'mean_complexity': complexity_ci['mean'] if complexity_ci else 0,
            'confidence_interval': complexity_ci,
            'savage_verdict': f"Average complexity of {complexity_ci['mean']:.1f} - CLAUDE.md recommends <5. This is a {complexity_ci['mean']/5:.1f}x violation of basic sanity.",
            'violations_count': sum(1 for score in complexity_scores if score >= 5),
            'violation_rate': f"{sum(1 for score in complexity_scores if score >= 5)/len(complexity_scores)*100:.1f}%"
        },
        'reliability_disaster': {
            'mean_success_rate': success_ci['mean'] if success_ci else 0,
            'confidence_interval': success_ci,
            'savage_verdict': f"Average success rate {success_ci['mean']*100:.1f}% - Production readiness worse than a college hackathon",
            'failure_analysis': f"{sum(1 for rate in success_rates if rate < 0.8)} out of {len(success_rates)} commands fail basic reliability standards"
        },
        'performance_variance': {
            'execution_consistency': statistics.mean(cvs),
            'savage_verdict': f"Average CV {statistics.mean(cvs):.1f}% - Consistency varies more than cryptocurrency prices" if statistics.mean(cvs) > 15 else f"Average CV {statistics.mean(cvs):.1f}% - Surprisingly stable for this dumpster fire"
        },
        'economic_analysis': {
            'total_estimated_cost': sum(cb['analysis']['estimated_cost_usd'] for cb in cost_benefits),
            'total_estimated_value': sum(cb['analysis']['estimated_value_usd'] for cb in cost_benefits),
            'average_roi': statistics.mean([cb['analysis']['roi_percentage'] for cb in cost_benefits]),
            'savage_verdict': 'Economic disaster - burning money faster than a startup' if statistics.mean([cb['analysis']['roi_percentage'] for cb in cost_benefits]) < 100 else 'Surprisingly profitable despite the chaos'
        },
        'hall_of_shame_detailed': [],
        'hall_of_fame_detailed': [],
        'recommendations_backed_by_science': []
    }
    
    # Detailed analysis for worst performers
    worst_commands = sorted(data['benchmarks'], key=lambda x: x['metrics']['complexity_score'], reverse=True)[:3]
    for cmd in worst_commands:
        metrics = cmd['metrics']
        savage_analysis['hall_of_shame_detailed'].append({
            'command': metrics['command_name'],
            'complexity_score': metrics['complexity_score'],
            'success_rate': metrics['success_rate'],
            'savage_verdict': f"Complexity {metrics['complexity_score']} with {metrics['success_rate']*100:.1f}% success rate - A masterclass in how NOT to write commands",
            'statistical_evidence': f"CV: {metrics['variance_statistics']['cv']:.1f}%, Token consumption: {metrics['token_consumption']['estimated_input']+metrics['token_consumption']['estimated_output']}",
            'cost_benefit': cost_benefit_analysis(metrics)
        })
    
    # Detailed analysis for best performers (if any exist)
    best_commands = sorted(data['benchmarks'], key=lambda x: (x['metrics']['complexity_score'], 1-x['metrics']['success_rate']))[:2]
    for cmd in best_commands:
        metrics = cmd['metrics']
        if metrics['complexity_score'] < 10 and metrics['success_rate'] > 0.5:  # Minimum standards
            savage_analysis['hall_of_fame_detailed'].append({
                'command': metrics['command_name'],
                'complexity_score': metrics['complexity_score'],
                'success_rate': metrics['success_rate'],
                'savage_verdict': f"Complexity {metrics['complexity_score']} with {metrics['success_rate']*100:.1f}% success rate - Actually functional, miracle detected",
                'statistical_evidence': f"CV: {metrics['variance_statistics']['cv']:.1f}%, Token consumption: {metrics['token_consumption']['estimated_input']+metrics['token_consumption']['estimated_output']}"
            })
    
    # Science-backed recommendations
    if complexity_ci and complexity_ci['mean'] > 10:
        savage_analysis['recommendations_backed_by_science'].append({
            'recommendation': 'EMERGENCY SIMPLIFICATION PROTOCOL',
            'evidence': f"Mean complexity {complexity_ci['mean']:.1f} with 95% CI [{complexity_ci['lower_bound']:.1f}, {complexity_ci['upper_bound']:.1f}] - Statistically significant complexity crisis",
            'action': 'Immediate refactoring required. Target complexity <5 per CLAUDE.md'
        })
    
    if success_ci and success_ci['mean'] < 0.6:
        savage_analysis['recommendations_backed_by_science'].append({
            'recommendation': 'RELIABILITY INTERVENTION REQUIRED',
            'evidence': f"Mean success rate {success_ci['mean']*100:.1f}% with 95% CI [{success_ci['lower_bound']*100:.1f}%, {success_ci['upper_bound']*100:.1f}%]",
            'action': 'Add comprehensive error handling and validation'
        })
    
    if statistics.mean(cvs) > 20:
        savage_analysis['recommendations_backed_by_science'].append({
            'recommendation': 'PERFORMANCE STABILIZATION NEEDED',
            'evidence': f"Average CV {statistics.mean(cvs):.1f}% indicates high variance in execution times",
            'action': 'Optimize algorithms and reduce complexity to improve consistency'
        })
    
    return savage_analysis

# Load and analyze the benchmark data
def main():
    results_dir = Path(".github/benchmarks/results")
    latest_file = max(results_dir.glob("*.json"), key=lambda x: x.stat().st_mtime)
    
    with open(latest_file, 'r') as f:
        data = json.load(f)
    
    # Generate advanced analysis
    savage_report = generate_savage_scientific_report(data)
    
    # Save the savage scientific report
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = results_dir / f"{timestamp}-savage-scientific-report.json"
    
    with open(output_file, 'w') as f:
        json.dump(savage_report, f, indent=2)
    
    print(f"🔬 SAVAGE SCIENTIFIC REPORT: {output_file}")
    return savage_report, output_file

if __name__ == "__main__":
    report, file_path = main()