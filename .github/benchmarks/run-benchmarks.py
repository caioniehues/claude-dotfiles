#!/usr/bin/env python3
"""
Execute comprehensive command benchmarks with statistical analysis
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path
import statistics

# Add the benchmarks directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from measurement_framework import CommandBenchmarker, BenchmarkResult

def main():
    benchmarker = CommandBenchmarker()
    
    # Commands to benchmark (selected scientifically)
    test_commands = [
        "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/adhd-evening-reflect.md",
        "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/git-backup-sync.md", 
        "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/context-enhanced-executor.md",
        "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/generate-thinking-command.md",
        "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/safe-code-beautifier.md"
    ]
    
    print("🔬 STARTING SCIENTIFIC COMMAND ROASTING")
    print("=" * 60)
    
    all_results = {}
    
    for command_file in test_commands:
        command_name = Path(command_file).stem
        print(f"\n📊 Benchmarking: {command_name}")
        
        results = benchmarker.measure_command_performance(command_file, iterations=7)
        
        # Calculate statistics
        exec_times = [r.execution_time for r in results]
        token_counts = [r.token_count_estimate for r in results]
        success_count = sum(1 for r in results if r.success)
        
        exec_stats = benchmarker.calculate_statistics(exec_times)
        token_stats = benchmarker.calculate_statistics([float(t) for t in token_counts])
        
        command_data = {
            'command_name': command_name,
            'execution_time': {
                'mean': exec_stats.mean,
                'std_dev': exec_stats.std_dev,
                'median': exec_stats.median,
                'min': exec_stats.min_val,
                'max': exec_stats.max_val,
                'confidence_interval': exec_stats.confidence_interval,
                'outliers': exec_stats.outliers
            },
            'token_count_estimate': {
                'mean': token_stats.mean,
                'std_dev': token_stats.std_dev,
                'median': token_stats.median
            },
            'success_rate': success_count / len(results),
            'complexity_score': results[0].complexity_score,
            'output_length': results[0].output_length,
            'error_indicators': results[0].error_count,
            'memory_usage_mb': {
                'mean': statistics.mean([r.memory_usage_mb for r in results]),
                'max': max(r.memory_usage_mb for r in results)
            },
            'raw_results': [
                {
                    'execution_time': r.execution_time,
                    'tokens': r.token_count_estimate,
                    'success': r.success,
                    'memory_mb': r.memory_usage_mb
                } for r in results
            ]
        }
        
        all_results[command_name] = command_data
        
        # Generate savage commentary
        commentary = benchmarker.generate_savage_commentary(command_name, command_data)
        print(f"💬 {commentary}")
        
        # Print quick stats
        print(f"   ⏱️ Avg Time: {exec_stats.mean:.2f}s (σ={exec_stats.std_dev:.2f})")
        print(f"   🎯 Success Rate: {command_data['success_rate']:.1%}")
        print(f"   🧠 Complexity: {command_data['complexity_score']}/10")
        print(f"   💾 Avg Memory: {command_data['memory_usage_mb']['mean']:.1f}MB")
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Create comprehensive report
    report = {
        'timestamp': timestamp,
        'benchmarker_version': '1.0-savage',
        'methodology': {
            'iterations_per_command': 7,
            'metrics_tracked': [
                'execution_time',
                'token_consumption', 
                'success_rate',
                'complexity_score',
                'memory_usage',
                'error_indicators'
            ],
            'statistical_methods': [
                'mean',
                'standard_deviation', 
                'confidence_intervals',
                'outlier_detection'
            ]
        },
        'overall_findings': generate_overall_analysis(all_results),
        'command_results': all_results,
        'savage_rankings': generate_rankings(all_results)
    }
    
    # Save report
    report_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{timestamp}-report.json"
    os.makedirs(os.path.dirname(report_file), exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📋 Complete report saved to: {report_file}")
    return report

def generate_overall_analysis(results):
    """Generate overall analysis across all commands"""
    
    all_exec_times = []
    all_success_rates = []
    all_complexity_scores = []
    
    for cmd_data in results.values():
        all_exec_times.append(cmd_data['execution_time']['mean'])
        all_success_rates.append(cmd_data['success_rate'])
        all_complexity_scores.append(cmd_data['complexity_score'])
    
    return {
        'total_commands_analyzed': len(results),
        'average_execution_time': statistics.mean(all_exec_times),
        'execution_time_variance': statistics.stdev(all_exec_times) if len(all_exec_times) > 1 else 0,
        'overall_success_rate': statistics.mean(all_success_rates),
        'average_complexity': statistics.mean(all_complexity_scores),
        'performance_consistency': 'poor' if statistics.stdev(all_exec_times) > 1.0 else 'good',
        'reliability_assessment': 'unreliable' if statistics.mean(all_success_rates) < 0.85 else 'reliable'
    }

def generate_rankings(results):
    """Generate savage rankings based on data"""
    
    rankings = {
        'fastest': min(results.items(), key=lambda x: x[1]['execution_time']['mean']),
        'slowest': max(results.items(), key=lambda x: x[1]['execution_time']['mean']),
        'most_reliable': max(results.items(), key=lambda x: x[1]['success_rate']),
        'least_reliable': min(results.items(), key=lambda x: x[1]['success_rate']),
        'most_complex': max(results.items(), key=lambda x: x[1]['complexity_score']),
        'least_complex': min(results.items(), key=lambda x: x[1]['complexity_score']),
        'most_consistent': min(results.items(), key=lambda x: x[1]['execution_time']['std_dev']),
        'least_consistent': max(results.items(), key=lambda x: x[1]['execution_time']['std_dev'])
    }
    
    return {
        category: {
            'command': name,
            'value': data[get_metric_for_category(category)],
            'savage_comment': get_savage_comment(category, name, data)
        }
        for category, (name, data) in rankings.items()
    }

def get_metric_for_category(category):
    """Get the relevant metric for ranking category"""
    metric_map = {
        'fastest': ['execution_time', 'mean'],
        'slowest': ['execution_time', 'mean'],
        'most_reliable': 'success_rate',
        'least_reliable': 'success_rate', 
        'most_complex': 'complexity_score',
        'least_complex': 'complexity_score',
        'most_consistent': ['execution_time', 'std_dev'],
        'least_consistent': ['execution_time', 'std_dev']
    }
    return metric_map[category]

def get_savage_comment(category, name, data):
    """Generate savage comments for rankings"""
    comments = {
        'fastest': f"⚡ {name} wins the speed contest, but let's be honest, it's still slower than a human typing",
        'slowest': f"🐌 {name} takes longer than a DMV visit. Time to reconsider your life choices",
        'most_reliable': f"🎯 {name} actually works most of the time. Shocking, I know",
        'least_reliable': f"💥 {name} fails more often than New Year's resolutions. Maybe stick to manual work?",
        'most_complex': f"🧠 {name} is so complex it probably gained sentience and is judging you right now",
        'least_complex': f"🧸 {name} is simpler than a kindergarten math problem. At least it's honest",
        'most_consistent': f"📊 {name} is as consistent as... well, at least it's consistent",
        'least_consistent': f"🎲 {name} has more variance than cryptocurrency. Roll the dice and pray"
    }
    return comments.get(category, f"🤷 {name} exists. That's... something.")

if __name__ == "__main__":
    report = main()
    print("\n🎯 SCIENTIFIC ROASTING COMPLETE!")
    print("📊 Check the generated JSON report for full statistical brutality")