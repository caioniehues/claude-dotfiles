#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER - The Truth Hurts Edition
"""
import json
import re
from pathlib import Path

def savage_analyze():
    """Brutal analysis with scientific precision"""
    base_path = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/"
    commands = [
        'ultrathink-interactive.md',
        'ultrathink-full-mcp.md', 
        'reasoning-wrapper.md',
        'adhd-hyperfocus-guardian.md',
        'java-clean-code-generator.md'
    ]
    
    results = {}
    total_violations = 0
    
    print("🔬 SAVAGE BENCHMARKING INITIATED")
    print("=" * 50)
    
    for cmd in commands:
        try:
            with open(base_path + cmd, 'r') as f:
                content = f.read()
            
            # BRUTAL TOKEN COUNT
            tokens = len(content) // 4  # Rough estimate
            
            # COMPLEXITY VIOLATIONS
            complexity_violations = 0
            if tokens > 2000:
                complexity_violations += 1
            if content.count('mcp__') > 10:
                complexity_violations += 1
            if len(content) > 15000:
                complexity_violations += 1
            
            # USABILITY SCORE (Harsh but fair)
            usability = 10
            if 'TODO' in content:
                usability -= 3
            if content.count('$') > 20:
                usability -= 2  # Over-templated
            if 'complex' in content.lower():
                usability -= 1
            
            results[cmd] = {
                'tokens': tokens,
                'length': len(content),
                'mcp_dependencies': content.count('mcp__'),
                'complexity_violations': complexity_violations,
                'usability_score': max(0, usability),
                'has_examples': '```' in content,
                'todo_count': content.count('TODO'),
                'template_variables': content.count('$')
            }
            
            total_violations += complexity_violations
            
            print(f"📊 {cmd}")
            print(f"   Tokens: {tokens}")
            print(f"   Length: {len(content):,} chars")
            print(f"   MCP deps: {content.count('mcp__')}")
            print(f"   Violations: {complexity_violations}")
            print(f"   Usability: {usability}/10")
            print()
            
        except Exception as e:
            print(f"❌ {cmd}: FAILED - {e}")
    
    # AGGREGATE SAVAGE STATISTICS
    total_tokens = sum(r['tokens'] for r in results.values())
    avg_tokens = total_tokens / len(results) if results else 0
    
    print("🎯 AGGREGATE ROASTING")
    print("=" * 30)
    print(f"Total commands: {len(results)}")
    print(f"Total tokens: {total_tokens:,}")
    print(f"Average tokens: {avg_tokens:.0f}")
    print(f"Total violations: {total_violations}")
    print(f"Commands over 10k chars: {sum(1 for r in results.values() if r['length'] > 10000)}")
    
    # Save brutal truth
    output = {
        'benchmark_timestamp': '2025-08-29T06:03:32Z',
        'commands_analyzed': len(results),
        'total_violations': total_violations,
        'individual_results': results,
        'savage_summary': {
            'worst_offender': max(results.keys(), key=lambda k: results[k]['complexity_violations']) if results else None,
            'most_bloated': max(results.keys(), key=lambda k: results[k]['tokens']) if results else None,
            'dependency_king': max(results.keys(), key=lambda k: results[k]['mcp_dependencies']) if results else None
        }
    }
    
    with open('/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/20250829-060332-report.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n💀 BRUTAL TRUTH SAVED TO REPORT")
    return output

if __name__ == "__main__":
    savage_analyze()