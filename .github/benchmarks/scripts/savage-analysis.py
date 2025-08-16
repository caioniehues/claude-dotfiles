#!/usr/bin/env python3
"""
SAVAGE STATISTICAL ANALYSIS
"""

import json
import math

# Load our brutal data
with open('.github/benchmarks/results/20250816-223801-report.json', 'r') as f:
    data = json.load(f)

print('🔬 SAVAGE STATISTICAL ANALYSIS')
print('=' * 50)

# Advanced statistical analysis
raw_metrics = data['raw_metrics']
stats = data['statistical_analysis']

# Calculate ROI efficiency
print('📊 EFFICIENCY ANALYSIS:')
for cmd in raw_metrics:
    efficiency = cmd['reasoning_depth'] / cmd['tokens'] * 1000 if cmd['tokens'] > 0 else 0
    roi = cmd['maintainability'] / (cmd['complexity'] + 1) * 100
    print(f"{cmd['command']:<30} | Efficiency: {efficiency:.2f} | ROI: {roi:.1f}%")

print('\n📈 COMPLEXITY DISTRIBUTION ANALYSIS:')
complexities = [m['complexity'] for m in raw_metrics]
print(f"Standard deviation: {stats['complexity_scores']['std_dev']:.2f}")
print(f"Coefficient of variation: {stats['complexity_scores']['std_dev'] / stats['complexity_scores']['mean'] * 100:.1f}%")

# Performance cost analysis
print('\n💰 TOKEN COST ANALYSIS:')
token_costs = [m['tokens'] for m in raw_metrics]
total_tokens = sum(token_costs)
avg_per_command = total_tokens / len(token_costs)
print(f'Total tokens across 5 commands: {total_tokens:,}')
print(f'Average per command: {avg_per_command:.0f}')
print(f'Estimated cost @ $0.003/1K tokens: ${total_tokens * 0.003 / 1000:.2f}')

# Thinking block effectiveness
print('\n🧠 THINKING BLOCK EFFECTIVENESS:')
for cmd in raw_metrics:
    if cmd['thinking_blocks'] > 0:
        effectiveness = cmd['reasoning_depth'] / cmd['thinking_blocks']
        print(f"{cmd['command']:<30} | {cmd['thinking_blocks']} blocks → {effectiveness:.1f} depth/block")
    else:
        print(f"{cmd['command']:<30} | NO THINKING BLOCKS (FAILURE)")

# Savage rankings with detailed analysis
print('\n🏆 SAVAGE PERFORMANCE RANKINGS:')
print('\nMOST OVER-ENGINEERED:')
for cmd in sorted(raw_metrics, key=lambda x: x['complexity'], reverse=True)[:3]:
    print(f"  {cmd['command']} - Complexity {cmd['complexity']}/10 (YIKES!)")

print('\nMOST THINKING-HEAVY:')
for cmd in sorted(raw_metrics, key=lambda x: x['thinking_blocks'], reverse=True)[:3]:
    ratio = cmd['thinking_blocks'] / cmd['lines'] * 100
    print(f"  {cmd['command']} - {cmd['thinking_blocks']} thinking blocks ({ratio:.1f}% of lines)")

print('\nMOST TOKEN-HUNGRY:')
for cmd in sorted(raw_metrics, key=lambda x: x['tokens'], reverse=True)[:3]:
    cost = cmd['tokens'] * 0.003 / 1000
    print(f"  {cmd['command']} - {cmd['tokens']} tokens (${cost:.3f} per execution)")

# Correlation analysis
print('\n🔗 CORRELATION ANALYSIS:')
complexities = [m['complexity'] for m in raw_metrics]
tokens = [m['tokens'] for m in raw_metrics]
maintainability = [m['maintainability'] for m in raw_metrics]

def correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(a * b for a, b in zip(x, y))
    sum_x2 = sum(a * a for a in x)
    sum_y2 = sum(b * b for b in y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y))
    
    return numerator / denominator if denominator != 0 else 0

complexity_token_corr = correlation(complexities, tokens)
complexity_maintainability_corr = correlation(complexities, maintainability)

print(f'Complexity vs Tokens correlation: {complexity_token_corr:.3f}')
print(f'Complexity vs Maintainability correlation: {complexity_maintainability_corr:.3f}')

if abs(complexity_token_corr) > 0.7:
    print('VERDICT: Strong correlation - complexity drives token usage!')
else:
    print('VERDICT: Weak correlation - complexity and size are independent!')

# Final savage verdict
print('\n⚖️ FINAL SAVAGE VERDICT:')
total_score = sum(m['maintainability'] for m in raw_metrics) / len(raw_metrics) * 100
print(f'Average maintainability: {total_score:.1f}%')

if total_score > 95:
    print('VERDICT: Surprisingly decent code quality. I am mildly impressed.')
elif total_score > 85:
    print('VERDICT: Acceptable but room for improvement. Not terrible.')
else:
    print('VERDICT: This code needs serious intervention. Call the refactoring squad!')