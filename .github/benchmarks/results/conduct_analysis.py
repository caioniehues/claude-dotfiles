#!/usr/bin/env python3

import os
import json
import re
import time
from datetime import datetime
from pathlib import Path

# Read the command files and conduct savage analysis
def load_command_content(filename):
    try:
        with open(f"commands/{filename}", 'r') as f:
            return f.read()
    except Exception as e:
        return f"ERROR: Could not read {filename}: {str(e)}"

def calculate_claude_md_violations(content):
    """Calculate violations of CLAUDE.md standards"""
    violations = []
    score = 0
    
    # Rule: Complexity score must be < 5
    lines = len(content.split('\n'))
    if lines > 200:
        score += 2
    if lines > 500:
        score += 3
    if lines > 1000:
        score += 5  # This is insane
    
    # Count abstractions
    abstractions = len(re.findall(r'abstract|interface|pattern|strategy|factory|builder', content, re.IGNORECASE))
    score += abstractions * 0.5
    
    # MCP dependency hell
    mcp_calls = len(re.findall(r'mcp__\w+', content))
    if mcp_calls > 5:
        score += 2
    if mcp_calls > 10:
        score += 3
    
    if score >= 5:
        violations.append(f"CLAUDE.md complexity violation: {score:.1f}/5")
    
    return score, violations

def analyze_performance_characteristics(content, filename):
    """Estimate performance impact"""
    perf_data = {
        'estimated_tokens': len(content.split()) * 1.3,  # Rough token estimate
        'response_time_category': 'UNKNOWN',
        'memory_usage': 'UNKNOWN',
        'complexity_operations': 0
    }
    
    # Count expensive operations
    expensive_ops = len(re.findall(r'mcp__|search|build_context|write_note', content))
    perf_data['complexity_operations'] = expensive_ops
    
    # Estimate response time category
    if perf_data['estimated_tokens'] < 1000 and expensive_ops < 3:
        perf_data['response_time_category'] = 'FAST'
    elif perf_data['estimated_tokens'] < 3000 and expensive_ops < 8:
        perf_data['response_time_category'] = 'MODERATE' 
    else:
        perf_data['response_time_category'] = 'SLOW'
        
    return perf_data

def generate_savage_assessment(filename, content, complexity_score, violations, perf_data):
    """Generate brutally honest scientific assessment"""
    
    roasts = []
    quality_score = 100
    
    # Complexity roast
    if complexity_score >= 8:
        roasts.append(f"🔥 {filename} achieves a complexity score of {complexity_score:.1f}. This violates CLAUDE.md by {complexity_score-5:.1f} points. That's not 'advanced', that's architectural malpractice.")
        quality_score -= 40
    elif complexity_score >= 5:
        roasts.append(f"⚠️ {filename} hits {complexity_score:.1f} complexity. CLAUDE.md says < 5. Close call, but still a violation.")
        quality_score -= 20
    
    # Size roast
    lines = len(content.split('\n'))
    if lines > 800:
        roasts.append(f"📏 At {lines} lines, {filename} is longer than the source code of some operating systems from the 1980s.")
        quality_score -= 25
    elif lines > 500:
        roasts.append(f"📄 {lines} lines for a single command? Someone confused 'comprehensive' with 'comprehensive failure'.")
        quality_score -= 15
    
    # Performance roast  
    if perf_data['response_time_category'] == 'SLOW':
        roasts.append(f"🐌 Performance category: SLOW. Users will have time to make coffee while waiting for this command.")
        quality_score -= 20
    
    # MCP dependency roast
    mcp_count = perf_data['complexity_operations']
    if mcp_count > 10:
        roasts.append(f"🔗 {mcp_count} MCP dependencies. This isn't a command, it's a distributed system.")
        quality_score -= 15
    
    # Calculate final grade
    if quality_score >= 85:
        grade = "A"
    elif quality_score >= 70:
        grade = "B" 
    elif quality_score >= 55:
        grade = "C"
    elif quality_score >= 40:
        grade = "D"
    else:
        grade = "F"
    
    return {
        'quality_score': max(0, quality_score),
        'grade': grade,
        'roasts': roasts,
        'violations': violations
    }

# Conduct the analysis
print("🔬 CONDUCTING SAVAGE SCIENTIFIC ANALYSIS")
print("=" * 60)

commands_to_analyze = [
    'adhd-morning-assistant.md',
    'ultrathink-pure-xml.md', 
    'adaptive-complexity-router.md',
    'intelligent-refactor-session.md',
    'adhd-task-breakdown.md'
]

results = {
    'timestamp': datetime.now().isoformat(),
    'methodology': 'SAVAGE_SCIENTIFIC_ANALYSIS',
    'commands': {},
    'statistical_summary': {},
    'harsh_truths': []
}

print("📊 INDIVIDUAL COMMAND ANALYSIS")
print("-" * 40)

for cmd in commands_to_analyze:
    content = load_command_content(cmd)
    if content.startswith("ERROR"):
        print(f"❌ {cmd}: {content}")
        continue
    
    complexity_score, violations = calculate_claude_md_violations(content)
    perf_data = analyze_performance_characteristics(content, cmd)
    assessment = generate_savage_assessment(cmd, content, complexity_score, violations, perf_data)
    
    results['commands'][cmd] = {
        'lines': len(content.split('\n')),
        'size_kb': round(len(content.encode('utf-8')) / 1024, 2),
        'complexity_score': round(complexity_score, 2),
        'claude_md_violations': violations,
        'performance': perf_data,
        'quality_score': assessment['quality_score'],
        'grade': assessment['grade'],
        'savage_assessment': assessment['roasts']
    }
    
    print(f"📝 {cmd}")
    print(f"   Lines: {results['commands'][cmd]['lines']}")
    print(f"   Complexity: {results['commands'][cmd]['complexity_score']}/5")
    print(f"   Grade: {assessment['grade']} ({assessment['quality_score']}/100)")
    if assessment['roasts']:
        print(f"   🔥 {assessment['roasts'][0]}")
    print()

# Statistical summary
all_scores = [cmd_data['quality_score'] for cmd_data in results['commands'].values()]
all_complexity = [cmd_data['complexity_score'] for cmd_data in results['commands'].values()]
all_lines = [cmd_data['lines'] for cmd_data in results['commands'].values()]

results['statistical_summary'] = {
    'sample_size': len(commands_to_analyze),
    'quality_scores': {
        'mean': round(sum(all_scores) / len(all_scores), 2),
        'min': min(all_scores),
        'max': max(all_scores),
        'std_dev': round((sum((x - sum(all_scores)/len(all_scores))**2 for x in all_scores) / len(all_scores))**0.5, 2)
    },
    'complexity_scores': {
        'mean': round(sum(all_complexity) / len(all_complexity), 2),
        'violations': sum(1 for score in all_complexity if score >= 5),
        'violation_rate': round(sum(1 for score in all_complexity if score >= 5) / len(all_complexity) * 100, 1)
    },
    'code_size': {
        'mean_lines': round(sum(all_lines) / len(all_lines)),
        'total_lines': sum(all_lines),
        'largest': max(all_lines)
    }
}

print("📈 STATISTICAL SUMMARY")
print("-" * 20)
print(f"Quality Score Mean: {results['statistical_summary']['quality_scores']['mean']}")
print(f"Complexity Violations: {results['statistical_summary']['complexity_scores']['violations']}/{len(commands_to_analyze)} ({results['statistical_summary']['complexity_scores']['violation_rate']}%)")
print(f"Total Lines of Code: {results['statistical_summary']['code_size']['total_lines']}")
print()

# Generate harsh truths
results['harsh_truths'] = [
    f"Your commands have a {results['statistical_summary']['complexity_scores']['violation_rate']}% CLAUDE.md violation rate. That's not 'comprehensive', that's 'comprehensively broken'.",
    f"Average quality score: {results['statistical_summary']['quality_scores']['mean']}/100. I've seen better code in student homework assignments.",
    f"Total codebase: {results['statistical_summary']['code_size']['total_lines']} lines for 5 commands. The Linux kernel has better code density.",
    f"Standard deviation of {results['statistical_summary']['quality_scores']['std_dev']} indicates inconsistent quality. Pick a standard and stick to it!"
]

print("🔥 HARSH SCIENTIFIC TRUTHS:")
for truth in results['harsh_truths']:
    print(f"   • {truth}")

# Save results
with open('.github/benchmarks/results/20250820-savage-report.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n💾 Report saved to: 20250820-savage-report.json")
print("🎓 SAVAGE BENCHMARKING COMPLETE!")