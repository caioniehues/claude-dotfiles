#!/usr/bin/env python3
import json
import statistics
import os
from datetime import datetime

def calculate_token_estimates(content):
    """Estimate token consumption based on content"""
    # Rough estimate: 1 token ≈ 4 characters
    chars = len(content)
    estimated_tokens = chars / 4
    
    # Add overhead for complex structures
    xml_overhead = content.count('<') * 0.5
    mcp_overhead = content.count('mcp__') * 2
    code_overhead = content.count('```') * 10
    
    return int(estimated_tokens + xml_overhead + mcp_overhead + code_overhead)

def estimate_execution_time(analysis):
    """Estimate execution time based on complexity"""
    base_time = 2.0  # seconds
    
    # Add time for MCP calls (each takes ~0.5-2s)
    mcp_time = analysis['mcp_calls'] * 1.2
    
    # Add time for complexity processing
    complexity_time = analysis['complexity_score'] * 0.8
    
    # Add time for thinking blocks
    thinking_time = analysis['thinking_tags'] * 2.0
    
    # Sequential thinking is EXPENSIVE
    if 'sequential' in open(analysis['filepath']).read().lower():
        thinking_time += 10.0
    
    return base_time + mcp_time + complexity_time + thinking_time

def assess_failure_probability(analysis):
    """Estimate probability of command failure"""
    failure_prob = 0.05  # Base 5% failure rate
    
    # MCP dependencies increase failure rate
    mcp_failure_increase = min(analysis['mcp_calls'] * 0.02, 0.3)
    
    # Complexity increases failure rate
    complexity_failure = min(analysis['complexity_score'] * 0.03, 0.4)
    
    # Over-engineering is inherently unstable
    overeng_failure = analysis['overengineering_indicators'] * 0.05
    
    total_failure_prob = min(failure_prob + mcp_failure_increase + complexity_failure + overeng_failure, 0.8)
    return total_failure_prob

def generate_savage_insights(analysis):
    """Generate brutally honest commentary"""
    insights = []
    name = os.path.basename(analysis['filepath'])
    
    # Complexity roasting
    if analysis['complexity_score'] >= 10:
        insights.append(f"🔥 NUCLEAR COMPLEXITY ALERT: {name} scores {analysis['complexity_score']}/10. This isn't 'sophisticated', it's academic masturbation.")
    elif analysis['complexity_score'] >= 7:
        insights.append(f"🚨 HIGH COMPLEXITY WARNING: {name} at {analysis['complexity_score']}/10. Someone confused 'thorough' with 'bloated'.")
    elif analysis['complexity_score'] >= 5:
        insights.append(f"⚠️ COMPLEXITY VIOLATION: {name} breaks the sacred CLAUDE.md rule. Simple > Smart, remember?")
    else:
        insights.append(f"✅ REASONABLE COMPLEXITY: {name} actually follows CLAUDE.md. Shocking!")
    
    # Size roasting
    if analysis['lines'] > 500:
        insights.append(f"📏 SIZE DISASTER: {analysis['lines']:,} lines. War & Peace was shorter and more useful.")
    elif analysis['lines'] > 300:
        insights.append(f"📏 SIZE WARNING: {analysis['lines']:,} lines. TL;DR: Nobody will read this monster.")
    
    # MCP dependency roasting  
    if analysis['mcp_calls'] > 20:
        insights.append(f"🔌 DEPENDENCY HELL: {analysis['mcp_calls']} MCP calls. This isn't integration, it's desperation.")
    elif analysis['mcp_calls'] > 10:
        insights.append(f"🔌 DEPENDENCY CONCERN: {analysis['mcp_calls']} MCP calls. When everything looks like a nail...")
    
    # Over-engineering roasting
    if analysis['overengineering_indicators'] > 5:
        insights.append(f"🏗️ OVER-ENGINEERING OLYMPICS: {analysis['overengineering_indicators']} patterns detected. Enterprise Java called - they want their complexity back.")
    
    return insights

def calculate_roi_score(analysis):
    """Calculate value-to-complexity ratio"""
    # Assume base value of 10 points
    base_value = 10
    
    # Reduce value for over-complexity
    complexity_penalty = analysis['complexity_score'] * 2
    overeng_penalty = analysis['overengineering_indicators'] * 1.5
    
    # MCP calls can add value but also overhead
    mcp_value = min(analysis['mcp_calls'] * 0.5, 5) if analysis['mcp_calls'] < 10 else -analysis['mcp_calls'] * 0.2
    
    roi_score = max(base_value - complexity_penalty - overeng_penalty + mcp_value, 0)
    return round(roi_score, 2)

# Load complexity analysis
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
analysis_files = [f for f in os.listdir('.github/benchmarks/results/') if 'complexity-analysis.json' in f]
if not analysis_files:
    print("No complexity analysis found!")
    exit(1)

latest_analysis = max(analysis_files)
with open(f'.github/benchmarks/results/{latest_analysis}', 'r') as f:
    data = json.load(f)

print("🔥 SAVAGE COMMAND BENCHMARKER - STATISTICAL ROASTING SESSION")
print("=" * 70)

# Calculate comprehensive metrics for each command
benchmark_results = []

for analysis in data['results']:
    name = os.path.basename(analysis['filepath'])
    content = open(analysis['filepath']).read()
    
    # Calculate all metrics
    token_estimate = calculate_token_estimates(content)
    exec_time = estimate_execution_time(analysis)
    failure_prob = assess_failure_probability(analysis)
    roi_score = calculate_roi_score(analysis)
    savage_insights = generate_savage_insights(analysis)
    
    benchmark_result = {
        'name': name,
        'complexity_score': analysis['complexity_score'],
        'lines': analysis['lines'],
        'token_estimate': token_estimate,
        'estimated_exec_time': round(exec_time, 2),
        'failure_probability': round(failure_prob * 100, 1),  # As percentage
        'roi_score': roi_score,
        'mcp_calls': analysis['mcp_calls'],
        'overengineering_indicators': analysis['overengineering_indicators'],
        'violates_claude_rule': analysis['violates_claude_rule'],
        'savage_insights': savage_insights,
        'raw_analysis': analysis
    }
    
    benchmark_results.append(benchmark_result)

# Sort by complexity score for dramatic effect
benchmark_results.sort(key=lambda x: x['complexity_score'], reverse=True)

print(f"\n📊 STATISTICAL OVERVIEW ({len(benchmark_results)} commands analyzed)")
print("=" * 50)

# Calculate statistics
complexity_scores = [r['complexity_score'] for r in benchmark_results]
token_estimates = [r['token_estimate'] for r in benchmark_results]
exec_times = [r['estimated_exec_time'] for r in benchmark_results]
failure_rates = [r['failure_probability'] for r in benchmark_results]
roi_scores = [r['roi_score'] for r in benchmark_results]

print(f"Complexity Score: μ={statistics.mean(complexity_scores):.2f}, σ={statistics.stdev(complexity_scores):.2f}")
print(f"Token Estimates: μ={statistics.mean(token_estimates):,.0f}, σ={statistics.stdev(token_estimates):,.0f}")
print(f"Execution Time: μ={statistics.mean(exec_times):.2f}s, σ={statistics.stdev(exec_times):.2f}s")
print(f"Failure Rate: μ={statistics.mean(failure_rates):.1f}%, σ={statistics.stdev(failure_rates):.1f}%")
print(f"ROI Score: μ={statistics.mean(roi_scores):.2f}, σ={statistics.stdev(roi_scores):.2f}")

violations = sum(1 for r in benchmark_results if r['violates_claude_rule'])
print(f"\n🚨 CLAUDE.md Rule Violations: {violations}/{len(benchmark_results)} ({violations/len(benchmark_results)*100:.0f}%)")

print(f"\n🏆 COMMAND RANKINGS (By Brutality)")
print("=" * 50)

for i, result in enumerate(benchmark_results, 1):
    print(f"\n{i}. {result['name']} - COMPLEXITY SCORE: {result['complexity_score']}/10")
    print(f"   📏 Size: {result['lines']:,} lines")
    print(f"   🎯 Token Est: {result['token_estimate']:,}")
    print(f"   ⏱️  Exec Time: {result['estimated_exec_time']:.2f}s")
    print(f"   💥 Failure Rate: {result['failure_probability']:.1f}%")
    print(f"   💰 ROI Score: {result['roi_score']}/10")
    print(f"   🔌 MCP Deps: {result['mcp_calls']}")
    
    for insight in result['savage_insights']:
        print(f"   {insight}")

# Save comprehensive benchmark results
output_file = f'.github/benchmarks/results/{timestamp}-savage-benchmark-report.json'
with open(output_file, 'w') as f:
    json.dump({
        'timestamp': timestamp,
        'analysis_type': 'comprehensive_benchmark',
        'statistical_summary': {
            'complexity_stats': {
                'mean': statistics.mean(complexity_scores),
                'stdev': statistics.stdev(complexity_scores),
                'median': statistics.median(complexity_scores),
                'min': min(complexity_scores),
                'max': max(complexity_scores)
            },
            'token_stats': {
                'mean': statistics.mean(token_estimates),
                'stdev': statistics.stdev(token_estimates),
                'median': statistics.median(token_estimates),
                'min': min(token_estimates),
                'max': max(token_estimates)
            },
            'execution_time_stats': {
                'mean': statistics.mean(exec_times),
                'stdev': statistics.stdev(exec_times),
                'median': statistics.median(exec_times),
                'min': min(exec_times),
                'max': max(exec_times)
            },
            'failure_rate_stats': {
                'mean': statistics.mean(failure_rates),
                'stdev': statistics.stdev(failure_rates),
                'median': statistics.median(failure_rates),
                'min': min(failure_rates),
                'max': max(failure_rates)
            },
            'roi_stats': {
                'mean': statistics.mean(roi_scores),
                'stdev': statistics.stdev(roi_scores),
                'median': statistics.median(roi_scores),
                'min': min(roi_scores),
                'max': max(roi_scores)
            },
            'claude_rule_violations': violations,
            'violation_rate': violations/len(benchmark_results)*100
        },
        'detailed_results': benchmark_results
    }, f, indent=2)

print(f"\n💾 SAVAGE BENCHMARK REPORT SAVED: {output_file}")
print(f"📈 Statistical analysis complete. The numbers don't lie!")