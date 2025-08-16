#!/usr/bin/env python3
import json
import datetime
import os
import re

def count_tokens_rough(text):
    """Rough token estimation: ~4 chars per token"""
    return len(text) // 4

def analyze_complexity(content):
    """Count complexity indicators and calculate score"""
    patterns = {
        'thinking_blocks': len(re.findall(r'<thinking[^>]*>.*?</thinking>', content, re.DOTALL)),
        'conditional_logic': len(re.findall(r'if\s+\w+.*?:', content)),
        'mcp_calls': len(re.findall(r'mcp__.*?__', content)),
        'xml_tags': len(re.findall(r'<[^/][^>]*>', content)),
        'code_blocks': content.count('```'),
        'variables': len(re.findall(r'\$\w+', content)),
        'orchestration_blocks': content.count('<thinking_orchestration>'),
        'execution_blocks': content.count('<execution>'),
        'error_handlers': content.count('<error_'),
    }
    
    # Calculate complexity score (weighted)
    score = (patterns['thinking_blocks'] * 3 + 
             patterns['conditional_logic'] * 2 +
             patterns['mcp_calls'] * 4 +
             patterns['xml_tags'] * 0.5 +
             patterns['code_blocks'] * 1 +
             patterns['variables'] * 0.5 +
             patterns['orchestration_blocks'] * 5 +
             patterns['execution_blocks'] * 2 +
             patterns['error_handlers'] * 1)
    
    return score, patterns

def assess_quality_issues(content, cmd_name):
    """Identify potential quality and performance issues"""
    issues = []
    warnings = []
    
    # Length issues
    if len(content) > 20000:
        issues.append('EXCESSIVE_LENGTH')
    elif len(content) > 15000:
        warnings.append('HIGH_LENGTH')
    
    # Token issues
    tokens = count_tokens_rough(content)
    if tokens > 4000:
        issues.append('TOKEN_BLOAT')
    elif tokens > 3000:
        warnings.append('HIGH_TOKENS')
    
    # Complexity issues
    complexity_score, patterns = analyze_complexity(content)
    if complexity_score > 30:
        issues.append('EXTREME_COMPLEXITY')
    elif complexity_score > 20:
        warnings.append('HIGH_COMPLEXITY')
    
    # Structural issues
    if patterns['thinking_blocks'] > 15:
        issues.append('OVER_THINKING')
    elif patterns['thinking_blocks'] > 10:
        warnings.append('EXCESSIVE_THINKING')
    
    if patterns['mcp_calls'] == 0 and 'mcp' in cmd_name.lower():
        issues.append('NO_MCP_INTEGRATION')
    
    if '<task>' not in content[:200]:
        issues.append('MISSING_TASK_TAG')
    
    # Maintainability issues
    if patterns['xml_tags'] > 50:
        warnings.append('XML_HEAVY')
    
    if patterns['conditional_logic'] > 20:
        warnings.append('LOGIC_HEAVY')
    
    # Performance issues
    lines = len(content.split('\n'))
    if lines > 600:
        issues.append('EXCESSIVE_LINES')
    elif lines > 400:
        warnings.append('HIGH_LINES')
    
    return issues, warnings

def main():
    # Initialize benchmark analysis
    analysis_data = {
        'benchmark_id': '20250816-220226-savage-analysis',
        'timestamp': datetime.datetime.now().isoformat(),
        'commands_total': 22,
        'commands_analyzed': 5,
        'selection_method': 'random_seed_20250816',
        'savage_analysis': True,
        'commands': {}
    }
    
    # Commands to analyze
    commands = [
        'senior-developer-analysis.md',
        'intelligent-refactor-session.md', 
        'java-rapid-implementation.md',
        'context-enhanced-executor.md',
        'adhd-task-breakdown.md'
    ]
    
    total_tokens = 0
    total_complexity = 0
    all_issues = []
    
    # Analyze each command
    for cmd in commands:
        try:
            filepath = f'commands/{cmd}'
            with open(filepath, 'r') as f:
                content = f.read()
                
            tokens = count_tokens_rough(content)
            complexity_score, patterns = analyze_complexity(content)
            issues, warnings = assess_quality_issues(content, cmd)
            
            # Calculate metrics
            lines = len(content.split('\n'))
            chars = len(content)
            
            # Token density (tokens per line)
            token_density = tokens / lines if lines > 0 else 0
            
            # Complexity per 100 lines
            complexity_density = (complexity_score / lines) * 100 if lines > 0 else 0
            
            analysis_data['commands'][cmd] = {
                'file_size_chars': chars,
                'lines': lines,
                'estimated_tokens': tokens,
                'token_density': round(token_density, 2),
                'complexity_score': round(complexity_score, 2),
                'complexity_density': round(complexity_density, 2),
                'patterns': patterns,
                'issues': issues,
                'warnings': warnings,
                'severity_score': len(issues) * 3 + len(warnings) * 1,
                'maintainability_score': max(0, 10 - len(issues) - len(warnings) * 0.5)
            }
            
            total_tokens += tokens
            total_complexity += complexity_score
            all_issues.extend(issues)
            
        except Exception as e:
            analysis_data['commands'][cmd] = {'error': str(e)}
    
    # Calculate aggregate statistics
    analysis_data['aggregate_stats'] = {
        'total_tokens': total_tokens,
        'avg_tokens': total_tokens / len(commands),
        'total_complexity': round(total_complexity, 2),
        'avg_complexity': round(total_complexity / len(commands), 2),
        'total_issues': len(all_issues),
        'most_common_issues': [issue for issue in set(all_issues) if all_issues.count(issue) > 1]
    }
    
    return analysis_data

if __name__ == '__main__':
    result = main()
    print(json.dumps(result, indent=2))