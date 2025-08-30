#!/usr/bin/env python3
"""
Manual Command Analysis with Savage Statistical Precision
"""

import re
import json
import statistics
from datetime import datetime
from pathlib import Path

def analyze_command_complexity(content: str, name: str) -> dict:
    """Analyze command complexity with CLAUDE.md scoring"""
    score = 1  # Base score
    
    # Count abstraction layers
    abstractions = len(re.findall(r'interface|abstract|pattern|factory', content, re.IGNORECASE))
    score += abstractions * 3
    
    # Count thinking blocks (cognitive overhead)
    thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content))
    score += thinking_blocks * 0.5
    
    # Count MCP integrations
    mcp_calls = len(re.findall(r'mcp__[a-zA-Z0-9_-]+__[a-zA-Z0-9_-]+', content))
    score += mcp_calls * 0.5
    
    # Count conditional complexity
    conditionals = len(re.findall(r'\bif\b|\bswitch\b|\bcase\b', content, re.IGNORECASE))
    score += conditionals * 0.2
    
    # Template variables (parameter complexity)
    variables = len(re.findall(r'\$\{[^}]+\}', content))
    score += variables * 0.1
    
    return {
        'complexity_score': round(score, 1),
        'abstractions_count': abstractions,
        'thinking_blocks': thinking_blocks,
        'mcp_integrations': mcp_calls,
        'conditional_logic': conditionals,
        'template_variables': variables,
        'total_lines': len(content.split('\n')),
        'character_count': len(content),
        'violates_complexity_rule': score >= 5
    }

def estimate_token_consumption(content: str) -> dict:
    """Estimate token consumption"""
    chars = len(content)
    base_tokens = chars // 4  # Rough approximation
    
    # Dynamic content expansion factor
    variables = len(re.findall(r'\$\{[^}]+\}', content))
    expansion_factor = 1 + (variables * 0.1)  # Each variable adds 10% expansion
    
    return {
        'base_input_tokens': base_tokens,
        'estimated_output_tokens': int(base_tokens * expansion_factor),
        'total_estimated_tokens': int(base_tokens * (1 + expansion_factor)),
        'cost_per_run_usd': int(base_tokens * (1 + expansion_factor)) * 0.00001
    }

def analyze_composition_compatibility(content: str) -> dict:
    """Analyze how well command composes with ecosystem"""
    compatibility_factors = {
        'memory_integration': 'mcp__basic-memory__' in content,
        'sequential_thinking': 'mcp__mcp-sequentialthinking-tools__' in content,
        'argument_passing': '$ARGUMENTS' in content,
        'standard_task_structure': '<task>' in content,
        'integration_documentation': 'Works seamlessly with:' in content or 'Integration Notes' in content,
        'pattern_capture': 'pattern' in content.lower() and 'memory' in content.lower(),
        'error_handling': any(word in content.lower() for word in ['error', 'fail', 'exception']),
        'parameterization': len(re.findall(r'\$\{[^}]+\}', content)) > 0
    }
    
    score = sum(compatibility_factors.values()) / len(compatibility_factors)
    
    return {
        'compatibility_score': round(score, 2),
        'factors': compatibility_factors,
        'integration_readiness': score > 0.6
    }

def detect_error_patterns(content: str, name: str) -> list:
    """Detect potential failure patterns"""
    patterns = []
    
    # Template injection without validation
    if '${' in content and 'validation' not in content.lower():
        patterns.append("INJECTION_RISK: Parameter substitution without validation")
    
    # Complex conditional logic
    if content.count('if ') > 5:
        patterns.append("COGNITIVE_OVERLOAD: Excessive conditional branching")
    
    # MCP calls without error handling
    mcp_calls = len(re.findall(r'mcp__', content))
    error_handling = any(word in content.lower() for word in ['error', 'catch', 'fail'])
    if mcp_calls > 0 and not error_handling:
        patterns.append("CASCADE_FAILURE: MCP calls without error handling")
    
    # Hardcoded assumptions
    if any(hardcode in content for hardcode in ['20 minutes', '5 minutes', 'timeout']) and 'configurable' not in content.lower():
        patterns.append("BRITTLENESS: Hardcoded timing assumptions")
    
    # Overly complex templates
    if len(content) > 10000:
        patterns.append("VERBOSITY_EXPLOSION: Command template exceeds reasonable size")
    
    return patterns

def generate_savage_judgment(name: str, metrics: dict) -> str:
    """Generate data-backed savage judgment"""
    complexity = metrics['complexity']['complexity_score']
    tokens = metrics['tokens']['total_estimated_tokens']
    compatibility = metrics['composition']['compatibility_score']
    errors = len(metrics['error_patterns'])
    
    # Complexity judgment
    if complexity >= 8:
        complexity_roast = f"Complexity score of {complexity} is higher than my expectations for humanity. This isn't architecture, it's abstract art."
    elif complexity >= 5:
        complexity_roast = f"Complexity score of {complexity} violates CLAUDE.md rules harder than a parking ticket in downtown SF."
    else:
        complexity_roast = f"Complexity score of {complexity} shows someone actually read the manual. Shocking."
    
    # Token judgment
    if tokens > 10000:
        token_roast = f"{tokens} estimated tokens per run will burn through your API budget faster than gas prices in 2022."
    elif tokens > 5000:
        token_roast = f"{tokens} tokens is pricey but not bankruptcy-inducing."
    else:
        token_roast = f"{tokens} tokens is reasonable. Fiscal responsibility exists!"
    
    # Compatibility judgment
    if compatibility < 0.3:
        comp_roast = "Composition compatibility suggests this command is lonelier than a JavaScript developer at a Python conference."
    elif compatibility < 0.6:
        comp_roast = f"Compatibility score of {compatibility} means it plays okay with others. Like a decent coworker."
    else:
        comp_roast = f"Compatibility score of {compatibility} means this actually integrates well. Rare ecosystem thinking!"
    
    # Error pattern judgment
    if errors > 3:
        error_roast = f"With {errors} error patterns, this command has more red flags than a Communist parade."
    elif errors > 1:
        error_roast = f"{errors} error patterns detected. Concerning but not catastrophic."
    else:
        error_roast = "Error patterns are minimal. Someone tested their thinking."
    
    return f"{complexity_roast} {token_roast} {comp_roast} {error_roast}"

def analyze_commands():
    """Analyze the three selected commands"""
    commands = {
        'ultrathink': Path('/home/runner/work/claude-dotfiles/claude-dotfiles/commands/ultrathink.md'),
        'java-clean-code-generator': Path('/home/runner/work/claude-dotfiles/claude-dotfiles/commands/java-clean-code-generator.md'),
        'adhd-task-breakdown': Path('/home/runner/work/claude-dotfiles/claude-dotfiles/commands/adhd-task-breakdown.md')
    }
    
    results = {}
    
    for name, path in commands.items():
        if not path.exists():
            print(f"❌ Command not found: {path}")
            continue
            
        content = path.read_text()
        
        # Perform analysis
        complexity_analysis = analyze_command_complexity(content, name)
        token_analysis = estimate_token_consumption(content)
        composition_analysis = analyze_composition_compatibility(content)
        error_patterns = detect_error_patterns(content, name)
        
        # Compile metrics
        metrics = {
            'complexity': complexity_analysis,
            'tokens': token_analysis,
            'composition': composition_analysis,
            'error_patterns': error_patterns,
            'content_length': len(content),
            'estimated_execution_time_ms': max(500, len(content) / 100 + complexity_analysis['complexity_score'] * 200)
        }
        
        # Generate savage judgment
        savage_judgment = generate_savage_judgment(name, metrics)
        
        results[name] = {
            'metrics': metrics,
            'savage_judgment': savage_judgment,
            'overall_score': min(10, max(0, 10 - complexity_analysis['complexity_score'] + composition_analysis['compatibility_score'] * 3))
        }
        
        print(f"\n🔬 {name.upper()} ANALYSIS:")
        print(f"   Complexity Score: {complexity_analysis['complexity_score']} (Limit: <5)")
        print(f"   Token Estimate: {token_analysis['total_estimated_tokens']}")
        print(f"   Compatibility: {composition_analysis['compatibility_score']}")
        print(f"   Error Patterns: {len(error_patterns)}")
        print(f"   Savage Score: {results[name]['overall_score']:.1f}/10")
        print(f"   📝 {savage_judgment}")
    
    return results

if __name__ == "__main__":
    results = analyze_commands()
    
    # Save detailed results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_path = f".github/benchmarks/results/{timestamp}-manual-analysis.json"
    
    with open(report_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📊 Detailed analysis saved to: {report_path}")
    print("🧪 Scientific roasting complete!")