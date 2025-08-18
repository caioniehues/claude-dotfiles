#!/usr/bin/env python3
import json
import os
import re
from datetime import datetime

def analyze_command_complexity(filepath):
    """Analyze a command file for complexity metrics"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Basic metrics
    lines = len(content.split('\n'))
    chars = len(content)
    words = len(content.split())
    
    # Pattern counting
    xml_blocks = content.count('<') + content.count('>')
    code_blocks = content.count('```')
    mcp_calls = content.count('mcp__')
    thinking_tags = content.count('<thinking>')
    bash_commands = len(re.findall(r'```bash.*?```', content, re.DOTALL))
    
    # Calculate complexity score based on CLAUDE.md rules
    complexity_score = 0
    complexity_factors = []
    
    # Size complexity
    if lines > 500:
        complexity_score += 3
        complexity_factors.append("Ultra-long file (>500 lines)")
    elif lines > 200:
        complexity_score += 2
        complexity_factors.append("Long file (>200 lines)")
    elif lines > 100:
        complexity_score += 1
        complexity_factors.append("Medium file (>100 lines)")
    
    # MCP dependency complexity
    if mcp_calls > 15:
        complexity_score += 3
        complexity_factors.append("Heavy MCP dependency (>15 calls)")
    elif mcp_calls > 10:
        complexity_score += 2
        complexity_factors.append("Moderate MCP dependency (>10 calls)")
    elif mcp_calls > 5:
        complexity_score += 1
        complexity_factors.append("Light MCP dependency (>5 calls)")
    
    # Structure complexity
    if xml_blocks > 100:
        complexity_score += 2
        complexity_factors.append("Heavy XML structure (>100 tags)")
    elif xml_blocks > 50:
        complexity_score += 1
        complexity_factors.append("Moderate XML structure (>50 tags)")
    
    # Design pattern penalties (CLAUDE.md anti-patterns)
    if 'sequential' in content.lower() and 'thinking' in content.lower():
        complexity_score += 3
        complexity_factors.append("Sequential thinking pattern (high complexity)")
    
    if code_blocks > 15:
        complexity_score += 1
        complexity_factors.append("Many code examples (>15 blocks)")
    
    # Check for over-engineering indicators
    overengineered_patterns = [
        'factory', 'builder', 'strategy', 'orchestration', 
        'delegation', 'coordination', 'comprehensive'
    ]
    
    overengineering_count = sum(1 for pattern in overengineered_patterns 
                               if pattern in content.lower())
    if overengineering_count > 5:
        complexity_score += 2
        complexity_factors.append(f"Over-engineering indicators ({overengineering_count})")
    
    return {
        'filepath': filepath,
        'lines': lines,
        'characters': chars,
        'words': words,
        'mcp_calls': mcp_calls,
        'xml_blocks': xml_blocks,
        'code_blocks': code_blocks,
        'thinking_tags': thinking_tags,
        'bash_commands': bash_commands,
        'complexity_score': complexity_score,
        'complexity_factors': complexity_factors,
        'violates_claude_rule': complexity_score >= 5,
        'overengineering_indicators': overengineering_count
    }

# Analyze selected commands
commands = [
    'commands/ultrathink-full-mcp.md',
    'commands/analyze-project-architecture.md',
    'commands/adhd-hyperfocus-guardian.md',
    'commands/adhd-task-breakdown.md',
    'commands/ultrathink.md'
]

results = []
print("📊 SAVAGE COMMAND COMPLEXITY ANALYSIS")
print("=" * 60)

for cmd in commands:
    if os.path.exists(cmd):
        analysis = analyze_command_complexity(cmd)
        results.append(analysis)
        
        name = os.path.basename(cmd)
        print(f"\n🎯 {name}")
        print(f"   Lines: {analysis['lines']:,}")
        print(f"   Characters: {analysis['characters']:,}")
        print(f"   Words: {analysis['words']:,}")
        print(f"   MCP calls: {analysis['mcp_calls']}")
        print(f"   XML blocks: {analysis['xml_blocks']}")
        print(f"   Code blocks: {analysis['code_blocks']}")
        print(f"   COMPLEXITY SCORE: {analysis['complexity_score']}/10")
        
        if analysis['violates_claude_rule']:
            print(f"   🚨 COMPLEXITY VIOLATION! (≥5) - CLAUDE.md Rule BROKEN")
            for factor in analysis['complexity_factors']:
                print(f"      - {factor}")
        else:
            print(f"   ✅ Within complexity limits")
            
        if analysis['overengineering_indicators'] > 3:
            print(f"   ⚠️  Over-engineering detected: {analysis['overengineering_indicators']} indicators")

# Save results for statistical analysis
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
with open(f'.github/benchmarks/results/{timestamp}-complexity-analysis.json', 'w') as f:
    json.dump({
        'timestamp': timestamp,
        'analysis_type': 'complexity',
        'results': results
    }, f, indent=2)

print(f"\n💾 Results saved to .github/benchmarks/results/{timestamp}-complexity-analysis.json")