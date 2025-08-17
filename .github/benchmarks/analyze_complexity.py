#!/usr/bin/env python3
import re
import json
import sys
import os
from pathlib import Path

def analyze_command_complexity(content, filename):
    """Analyze command complexity using SAVAGE metrics"""
    lines = len(content.split('\n'))
    words = len(content.split())
    
    # Count various patterns
    thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content, re.IGNORECASE))
    xml_tags = len(re.findall(r'<[^/][^>]*>', content))
    parameter_substitutions = len(re.findall(r'\$\{[^}]+\}', content))
    javascript_blocks = len(re.findall(r'```javascript', content, re.IGNORECASE))
    bash_blocks = len(re.findall(r'```bash', content, re.IGNORECASE))
    
    # CLAUDE.md complexity violations
    violations = []
    
    # Size violations
    if lines > 500:
        violations.append("MASSIVE: 500+ lines - who has time for this novel?")
    elif lines > 300:
        violations.append("BLOATED: 300+ lines - someone got carried away")
    elif lines > 200:
        violations.append("CHUNKY: 200+ lines - approaching danger zone")
    
    # Over-engineering detection
    if thinking_blocks > 15:
        violations.append(f"OVER-THINKING: {thinking_blocks} thinking blocks - analysis paralysis much?")
    
    if xml_tags > 50:
        violations.append(f"XML HELL: {xml_tags} XML tags - this isn't 2005")
    
    # Complexity score calculation (CLAUDE.md violations)
    complexity = 0
    
    # Size penalty
    if lines > 100: complexity += 1
    if lines > 300: complexity += 2 
    if lines > 500: complexity += 4  # Heavy penalty
    
    # Pattern complexity  
    complexity += min(thinking_blocks // 3, 4)  # Max 4 points for thinking overuse
    complexity += min(xml_tags // 20, 3)       # Max 3 points for XML soup
    complexity += min(javascript_blocks, 2)    # Max 2 points for JS
    
    # Features count
    features = 0
    features += 1 if 'mcp__basic-memory__' in content else 0
    features += 1 if 'initialization>' in content else 0
    features += 1 if 'completion_summary>' in content else 0
    features += 1 if 'pattern' in content.lower() else 0
    features += 1 if 'validation' in content.lower() else 0
    
    # Readability metrics
    avg_line_length = sum(len(line) for line in content.split('\n')) / max(lines, 1)
    long_lines = len([line for line in content.split('\n') if len(line) > 120])
    
    # Token consumption estimation (more accurate)
    # Claude tokens are roughly 0.75 words for code/markdown
    estimated_tokens = int(words * 0.75)
    
    # Quality score (inverse of problems)
    quality_score = 10
    if lines > 400: quality_score -= 3
    if thinking_blocks > 20: quality_score -= 2
    if long_lines > lines * 0.3: quality_score -= 2
    if avg_line_length > 100: quality_score -= 1
    quality_score = max(0, quality_score)
    
    return {
        'filename': filename,
        'metrics': {
            'lines_count': lines,
            'words_count': words,
            'avg_line_length': round(avg_line_length, 1),
            'long_lines_count': long_lines,
            'thinking_blocks': thinking_blocks,
            'xml_tags': xml_tags,
            'parameter_substitutions': parameter_substitutions,
            'javascript_blocks': javascript_blocks,
            'bash_blocks': bash_blocks,
            'estimated_tokens': estimated_tokens
        },
        'scores': {
            'complexity_score': min(complexity, 10),  # Cap at 10
            'feature_richness': features,
            'quality_score': quality_score,
            'readability_penalty': long_lines
        },
        'violations': violations,
        'savage_verdict': get_savage_verdict(complexity, quality_score, violations)
    }

def get_savage_verdict(complexity, quality, violations):
    """Generate statistically-backed savage commentary"""
    if complexity >= 8:
        return "ACADEMIC DISASTER: Complexity score 8+. This is a PhD thesis, not a command."
    elif complexity >= 6:
        return "OVER-ENGINEERED NIGHTMARE: Complexity 6+. Someone watched too many architecture videos."
    elif complexity >= 4:
        return "BLOATED BUT FUNCTIONAL: Complexity 4+. Works but at what cost?"
    elif quality >= 8:
        return "SURPRISINGLY DECENT: Actually follows some best practices. Shocking."
    elif quality >= 6:
        return "MEDIOCRE BUT ACCEPTABLE: Gets the job done without causing therapy."
    else:
        return "DUMPSTER FIRE: Quality score < 6. Start over."

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_complexity.py <command_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        result = analyze_command_complexity(content, os.path.basename(filepath))
        print(json.dumps(result, indent=2))
        
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error analyzing {filepath}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()