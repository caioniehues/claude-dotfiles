#!/usr/bin/env python3

import subprocess
import json
import re
from datetime import datetime

def count_patterns(file_path, pattern):
    """Count regex patterns in a file with scientific precision."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return len(re.findall(pattern, content))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def count_xml_blocks(file_path):
    """Count XML-style abstraction blocks like <task>, <context>, etc."""
    return count_patterns(file_path, r'<[^/>][^>]*>')

def count_code_blocks(file_path):
    """Count markdown code blocks (triple backticks)."""
    return count_patterns(file_path, r'```') // 2  # Each block has start and end

def analyze_command_complexity():
    """SAVAGE scientific analysis of command complexity."""
    
    # Our victim commands with basic metrics
    commands = {
        'adhd-evening-reflect': {'lines': 437, 'mcp_calls': 3},
        'intelligent-code-enhancer': {'lines': 441, 'mcp_calls': 1},
        'adhd-task-breakdown': {'lines': 364, 'mcp_calls': 3},
        'ultrathink-interactive': {'lines': 672, 'mcp_calls': 3},
        'safe-code-beautifier': {'lines': 426, 'mcp_calls': 1}
    }

    base_path = '/home/runner/work/claude-dotfiles/claude-dotfiles/commands/'
    
    results = {}
    
    for cmd_name, data in commands.items():
        file_path = f'{base_path}{cmd_name}.md'
        
        # Collect scientific evidence
        data['xml_blocks'] = count_xml_blocks(file_path)
        data['code_blocks'] = count_code_blocks(file_path)
        
        # Calculate SAVAGE COMPLEXITY SCORE using CLAUDE.md rules
        score = 0
        score += data['lines'] / 100  # 1 point per 100 lines (length penalty)
        score += data['mcp_calls'] * 0.5  # 0.5 points per external dependency
        score += data['xml_blocks'] * 0.2  # 0.2 points per abstraction layer
        score += data['code_blocks'] * 0.3  # 0.3 points per embedded code complexity
        
        data['savage_complexity_score'] = round(score, 2)
        data['claude_md_compliant'] = score < 5  # THE SACRED 5-POINT LIMIT
        data['complexity_violation'] = round(max(0, score - 5), 2)
        
        # SAVAGE SCIENTIFIC VERDICT
        if score >= 8:
            data['verdict'] = 'ARCHITECTURAL DISASTER - Rewrite from scratch'
            data['roast_intensity'] = 'NUCLEAR'
        elif score >= 5:
            data['verdict'] = 'BLOATED GARBAGE - Violates CLAUDE.md rules'
            data['roast_intensity'] = 'SAVAGE'
        elif score >= 3:
            data['verdict'] = 'QUESTIONABLE DESIGN - Approaching bloat'
            data['roast_intensity'] = 'MODERATE'
        elif score >= 2:
            data['verdict'] = 'ACCEPTABLE BUT CHUNKY - Could be leaner'
            data['roast_intensity'] = 'GENTLE'
        else:
            data['verdict'] = 'LEAN AND MEAN - Well designed'
            data['roast_intensity'] = 'PRAISE'
        
        # Calculate efficiency metrics
        data['lines_per_abstraction'] = round(data['lines'] / max(1, data['xml_blocks']), 1)
        data['complexity_density'] = round(score / (data['lines'] / 100), 2)  # Complexity per 100 lines
        
        results[cmd_name] = data
    
    return results

if __name__ == "__main__":
    results = analyze_command_complexity()
    print(json.dumps(results, indent=2))