#!/usr/bin/env python3
import json
import sys
from collections import defaultdict

# Read the JSON file
with open('.github/benchmarks/results/benchmark-report-20250817-134031.json', 'r') as f:
    data = json.load(f)

# Aggregate data
command_summary = {}
overall_stats = {
    'success_rates': [],
    'complexity_scores': [],
    'roi_scores': [],
    'costs': [],
    'execution_times': []
}

# Process each command
for cmd_name, cmd_data in data.get('commands', {}).items():
    cmd_summary = {
        'complexity': cmd_data['metadata']['complexity_indicators'],
        'scenarios': {},
        'avg_success': 0,
        'avg_roi': 0,
        'avg_cost': 0,
        'total_complexity': sum([
            cmd_data['metadata']['complexity_indicators'].get('mcp_calls', 0) * 2,
            cmd_data['metadata']['complexity_indicators'].get('conditional_logic', 0),
            cmd_data['metadata']['complexity_indicators'].get('loops', 0),
            cmd_data['metadata']['complexity_indicators'].get('function_calls', 0)
        ])
    }
    
    success_rates = []
    roi_scores = []
    costs = []
    
    for scenario_name, scenario_data in cmd_data.get('scenarios', {}).items():
        stats = scenario_data.get('statistics', {})
        if stats:
            cmd_summary['scenarios'][scenario_name] = {
                'success': stats.get('success_mean', 0),
                'roi': stats.get('roi_mean', 0),
                'cost': stats.get('cost_mean', 0),
                'time': stats.get('time_mean', 0)
            }
            success_rates.append(stats.get('success_mean', 0))
            roi_scores.append(stats.get('roi_mean', 0))
            costs.append(stats.get('cost_mean', 0))
            
            overall_stats['success_rates'].append(stats.get('success_mean', 0))
            overall_stats['roi_scores'].append(stats.get('roi_mean', 0))
            overall_stats['costs'].append(stats.get('cost_mean', 0))
            overall_stats['execution_times'].append(stats.get('time_mean', 0))
    
    if success_rates:
        cmd_summary['avg_success'] = sum(success_rates) / len(success_rates)
        cmd_summary['avg_roi'] = sum(roi_scores) / len(roi_scores)
        cmd_summary['avg_cost'] = sum(costs) / len(costs)
    
    command_summary[cmd_name] = cmd_summary

# Calculate overall statistics
print("# BENCHMARK ANALYSIS RESULTS")
print(f"\nTotal Commands: {len(command_summary)}")
print(f"Total Scenarios: {len(overall_stats['success_rates'])}")
print(f"\n## OVERALL STATISTICS")
print(f"Average Success Rate: {sum(overall_stats['success_rates'])/len(overall_stats['success_rates']):.1%}")
print(f"Average ROI: {sum(overall_stats['roi_scores'])/len(overall_stats['roi_scores']):.2f}")
print(f"Average Cost: ${sum(overall_stats['costs'])/len(overall_stats['costs']):.3f}")
print(f"Average Execution Time: {sum(overall_stats['execution_times'])/len(overall_stats['execution_times']):.2f}s")

# Sort commands by ROI
sorted_by_roi = sorted(command_summary.items(), key=lambda x: x[1]['avg_roi'], reverse=True)

print("\n## TOP 5 COMMANDS BY ROI")
for i, (cmd, summary) in enumerate(sorted_by_roi[:5], 1):
    print(f"{i}. {cmd}: ROI={summary['avg_roi']:.2f}, Success={summary['avg_success']:.1%}, Complexity={summary['total_complexity']}")

print("\n## BOTTOM 5 COMMANDS BY ROI")
for i, (cmd, summary) in enumerate(sorted_by_roi[-5:], 1):
    print(f"{i}. {cmd}: ROI={summary['avg_roi']:.2f}, Success={summary['avg_success']:.1%}, Complexity={summary['total_complexity']}")

# Sort by complexity
sorted_by_complexity = sorted(command_summary.items(), key=lambda x: x[1]['total_complexity'], reverse=True)

print("\n## HIGHEST COMPLEXITY COMMANDS")
for i, (cmd, summary) in enumerate(sorted_by_complexity[:5], 1):
    print(f"{i}. {cmd}: Complexity={summary['total_complexity']}, ROI={summary['avg_roi']:.2f}, Success={summary['avg_success']:.1%}")

# Sort by success rate
sorted_by_success = sorted(command_summary.items(), key=lambda x: x[1]['avg_success'])

print("\n## LOWEST SUCCESS RATE COMMANDS")
for i, (cmd, summary) in enumerate(sorted_by_success[:5], 1):
    print(f"{i}. {cmd}: Success={summary['avg_success']:.1%}, ROI={summary['avg_roi']:.2f}, Complexity={summary['total_complexity']}")

# Scenario performance
scenario_performance = defaultdict(list)
for cmd_name, cmd_data in command_summary.items():
    for scenario_name, scenario_stats in cmd_data['scenarios'].items():
        scenario_performance[scenario_name].append(scenario_stats['success'])

print("\n## SCENARIO PERFORMANCE")
for scenario, success_rates in scenario_performance.items():
    avg_success = sum(success_rates) / len(success_rates) if success_rates else 0
    print(f"{scenario}: {avg_success:.1%} average success rate")

print("\n## COMPLEXITY VIOLATIONS (Score > 5)")
violations = [(cmd, summary['total_complexity']) for cmd, summary in command_summary.items() if summary['total_complexity'] > 5]
print(f"Total violations: {len(violations)}/{len(command_summary)} ({len(violations)/len(command_summary)*100:.0f}%)")
print("Worst offenders:")
for cmd, complexity in sorted(violations, key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {cmd}: {complexity} (violation by {(complexity-5)/5*100:.0f}%)")