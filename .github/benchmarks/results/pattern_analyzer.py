#!/usr/bin/env python3
import re
import json
import time
from collections import Counter

def analyze_command_patterns(file_path):
    """Analyzes thinking patterns, tool usage, and structural complexity"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Pattern analysis
    patterns = {
        'thinking_tags': len(re.findall(r'<thinking>', content, re.IGNORECASE)),
        'xml_blocks': len(re.findall(r'<\w+[^>]*>', content)),
        'mcp_calls': len(re.findall(r'mcp__\w+', content)),
        'bash_commands': content.count('bash'),
        'code_examples': content.count('```'),
        'if_complexity': len(re.findall(r'if.*complexity.*>', content, re.IGNORECASE)),
        'todo_usage': len(re.findall(r'todo', content, re.IGNORECASE)),
        'nested_structure_depth': max([line.count('  ') for line in content.split('\n')] + [0]),
        'placeholder_count': len(re.findall(r'_____|\[\w+\]|\$\w+', content)),
        'markdown_headers': len(re.findall(r'^#+', content, re.MULTILINE))
    }
    
    # Estimate token count (rough approximation: 4 chars per token)
    estimated_tokens = len(content) // 4
    
    # Calculate maintainability issues
    issues = {
        'excessive_placeholders': patterns['placeholder_count'] > 50,
        'deep_nesting': patterns['nested_structure_depth'] > 6,
        'xml_overuse': patterns['xml_blocks'] > 30,
        'complexity_branching': patterns['if_complexity'] > 3,
        'token_bloat': estimated_tokens > 3000
    }
    
    return patterns, estimated_tokens, issues

# Load previous analysis
with open('/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/initial-analysis.json', 'r') as f:
    data = json.load(f)

print('🧪 DETAILED PATTERN & BLOAT ANALYSIS')
print('=' * 60)

for cmd_name, cmd_data in data['commands'].items():
    print(f'\n🎯 DISSECTING: {cmd_name}')
    
    patterns, tokens, issues = analyze_command_patterns(cmd_data['file_path'])
    
    # Update data with detailed metrics
    cmd_data.update({
        'patterns': patterns,
        'estimated_tokens': tokens,
        'maintainability_issues': issues,
        'issue_count': sum(issues.values())
    })
    
    print(f'   📏 Size: {cmd_data["lines"]} lines, ~{tokens:,} tokens')
    print(f'   🏗️ Structure: {patterns["xml_blocks"]} XML blocks, depth {patterns["nested_structure_depth"]}')
    print(f'   🧠 Thinking: {patterns["thinking_tags"]} explicit thinking tags')
    print(f'   🔧 Tools: {patterns["mcp_calls"]} MCP calls, {patterns["bash_commands"]} bash blocks')
    print(f'   ⚠️  Issues: {cmd_data["issue_count"]}/5 maintainability problems')
    
    if cmd_data['issue_count'] > 2:
        print('   🔥 SAVAGE JUDGMENT: Bloated mess with maintainability debt!')
    elif cmd_data['issue_count'] > 0:
        print('   ⚡ JUDGMENT: Has issues but somewhat manageable')
    else:
        print('   ✅ JUDGMENT: Actually well-structured (rare!)')

# Calculate aggregate bloat metrics
total_tokens = sum(cmd_data['estimated_tokens'] for cmd_data in data['commands'].values())
avg_tokens = total_tokens / len(data['commands'])
bloated_commands = sum(1 for cmd_data in data['commands'].values() if cmd_data['estimated_tokens'] > 3000)

print(f'\n💀 AGGREGATE BLOAT ASSESSMENT:')
print(f'   Total estimated tokens: {total_tokens:,}')
print(f'   Average tokens per command: {avg_tokens:,.0f}')
print(f'   Commands exceeding token sanity limit (3k): {bloated_commands}/{len(data["commands"])}')
print(f'   Repository bloat factor: {total_tokens/10000:.1f}x (>1.0 is bloated)')

# Update the file
with open('/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/initial-analysis.json', 'w') as f:
    data['bloat_metrics'] = {
        'total_tokens': total_tokens,
        'avg_tokens': avg_tokens,
        'bloated_count': bloated_commands,
        'bloat_factor': total_tokens/10000
    }
    json.dump(data, f, indent=2)

print('\n✅ Detailed analysis complete with savage judgments')