#!/usr/bin/env python3
"""
DIRECT SCIENTIFIC ANALYSIS - NO DEPENDENCIES
Brutal statistical measurement of command effectiveness
"""

import json
import re
import statistics
from datetime import datetime
from pathlib import Path

def analyze_complexity(content):
    """Calculate CLAUDE.md complexity score with evidence"""
    violations = []
    score = 1  # Base score for existing solution
    
    # Direct solution: 1 point (already counted)
    # Each new class: +2 points
    class_count = len(re.findall(r'class\s+\w+', content))
    if class_count > 1:
        score += (class_count - 1) * 2
        violations.append(f"Multiple classes detected ({class_count})")
    
    # Each interface: +1 point
    interface_count = len(re.findall(r'interface\s+\w+|abstract class', content))
    score += interface_count
    if interface_count > 0:
        violations.append(f"Interfaces/abstractions detected ({interface_count})")
    
    # Each design pattern: +3 points
    patterns = ['Factory', 'Builder', 'Strategy', 'Observer', 'Decorator', 'Adapter', 'Proxy']
    pattern_count = sum(1 for p in patterns if p in content)
    score += pattern_count * 3
    if pattern_count > 0:
        violations.append(f"Design patterns detected ({pattern_count})")
    
    # Each configuration file: +2 points
    config_indicators = ['.xml', '.properties', '.yml', '.yaml', '.config']
    config_count = sum(1 for c in config_indicators if c in content.lower())
    score += config_count * 2
    if config_count > 0:
        violations.append(f"Configuration complexity ({config_count})")
    
    # Meta-complexity penalties
    if 'thinking' in content.lower() and 'orchestration' in content.lower():
        score += 2
        violations.append("Meta-thinking complexity")
    
    if 'mcp__' in content:
        score += 2
        violations.append("External MCP dependencies")
    
    return score, violations

def estimate_tokens(content):
    """Rough token estimation (4 chars ≈ 1 token)"""
    return len(content) // 4

def estimate_execution_time(complexity_score, token_count):
    """Estimate execution time based on complexity and tokens"""
    base_time = 1.5  # seconds base
    complexity_overhead = complexity_score * 0.8
    token_overhead = token_count / 10000  # tokens slow things down
    return base_time + complexity_overhead + token_overhead

def main():
    print("🔬 SAVAGE SCIENTIFIC COMMAND ANALYSIS")
    print("=" * 50)
    
    # Our victims
    commands = [
        'reasoning-wrapper.md',
        'ultrathink-pure-xml.md', 
        'analyze-project-architecture.md',
        'context-enhanced-executor.md'
    ]
    
    base_path = '/home/runner/work/claude-dotfiles/claude-dotfiles/commands'
    results = []
    
    for cmd_file in commands:
        file_path = f"{base_path}/{cmd_file}"
        cmd_name = cmd_file.replace('.md', '')
        
        print(f"\n🎯 ANALYZING: {cmd_name}")
        
        # Read and analyze
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Scientific measurements
        complexity_score, violations = analyze_complexity(content)
        input_tokens = estimate_tokens(content)
        output_tokens = input_tokens + (complexity_score * 400)  # Complex commands generate more output
        execution_time = estimate_execution_time(complexity_score, input_tokens)
        
        # Success probability (based on simplicity)
        success_probability = max(0, 100 - (complexity_score - 3) * 20)
        
        result = {
            "command": cmd_name,
            "complexity_score": complexity_score,
            "claude_md_violations": violations,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "estimated_execution_seconds": round(execution_time, 2),
            "success_probability_percent": round(success_probability, 1),
            "cost_per_run_usd": round((input_tokens + output_tokens) * 0.003 / 1000, 4),
            "file_size_bytes": len(content),
            "lines_of_code": len(content.split('\n'))
        }
        
        results.append(result)
        
        # Real-time roasting
        print(f"  💀 Complexity: {complexity_score}/5 {'❌ VIOLATES' if complexity_score > 3 else '✅'}")
        print(f"  💰 Cost: ${result['cost_per_run_usd']:.4f} per run")
        print(f"  🎲 Success Rate: {success_probability:.1f}%")
        if violations:
            print(f"  ⚠️  Violations: {', '.join(violations[:2])}...")
    
    # Statistical analysis
    complexities = [r['complexity_score'] for r in results]
    tokens = [r['total_tokens'] for r in results]
    costs = [r['cost_per_run_usd'] for r in results]
    
    stats = {
        "analysis_timestamp": datetime.now().isoformat(),
        "total_commands": len(results),
        "statistical_summary": {
            "average_complexity": round(statistics.mean(complexities), 2),
            "complexity_std_dev": round(statistics.stdev(complexities) if len(complexities) > 1 else 0, 2),
            "total_token_burn": sum(tokens),
            "average_tokens_per_command": round(statistics.mean(tokens)),
            "total_cost_per_benchmark": round(sum(costs), 4),
            "commands_exceeding_complexity_limit": sum(1 for c in complexities if c > 3)
        },
        "savage_rankings": {
            "most_complex": max(results, key=lambda x: x['complexity_score']),
            "most_expensive": max(results, key=lambda x: x['total_tokens']),
            "least_reliable": min(results, key=lambda x: x['success_probability_percent'])
        },
        "detailed_results": results
    }
    
    # Generate savage commentary
    avg_complexity = stats['statistical_summary']['average_complexity']
    violations = sum(len(r['claude_md_violations']) for r in results)
    total_cost = stats['statistical_summary']['total_cost_per_benchmark']
    
    savage_verdict = []
    
    if avg_complexity > 3:
        savage_verdict.append(f"Average complexity of {avg_complexity} violates CLAUDE.md standards. This isn't clean code, this is digital spaghetti.")
    
    if violations > 8:
        savage_verdict.append(f"Found {violations} CLAUDE.md violations across 4 commands. That's a 2:1 violation-to-command ratio - impressive incompetence.")
    
    if total_cost > 0.05:
        savage_verdict.append(f"These 4 commands cost ${total_cost:.4f} per benchmark. Running this daily would cost ${total_cost * 365:.2f} annually. Expensive mediocrity.")
    
    stats['savage_verdict'] = ' '.join(savage_verdict) if savage_verdict else "Shockingly, these commands show some restraint. Practically a miracle."
    
    # Save scientific evidence
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{timestamp}-report.json"
    
    with open(output_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    print("\n" + "=" * 60)
    print("🔬 SCIENTIFIC ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"📊 Statistics: {len(results)} commands analyzed")
    print(f"💀 Average complexity: {avg_complexity}/5")
    print(f"💰 Total cost: ${total_cost:.4f}")
    print(f"⚠️  Total violations: {violations}")
    print(f"\n💬 SAVAGE VERDICT:")
    print(stats['savage_verdict'])
    print(f"\n📁 Full report: {output_file}")
    
    return stats

if __name__ == "__main__":
    main()