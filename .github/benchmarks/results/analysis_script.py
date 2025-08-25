#!/usr/bin/env python3
import re
import os
import json
from datetime import datetime

def analyze_command_complexity(filepath):
    """Calculate complexity score based on CLAUDE.md rules"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    complexity = 1  # Direct solution baseline
    
    # Count new classes (+2 each)
    class_patterns = [r'class\s+\w+', r'@Component', r'@Service', r'@Repository']
    for pattern in class_patterns:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        complexity += matches * 2
        
    # Count interfaces (+1 each) 
    interface_patterns = [r'interface\s+\w+', r'extends\s+\w+', r'implements\s+\w+']
    for pattern in interface_patterns:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        complexity += matches * 1
    
    # Count design patterns (+3 each)
    pattern_indicators = [
        'Factory', 'Builder', 'Strategy', 'Observer', 'Singleton',
        'Template', 'Command', 'Adapter', 'Decorator', 'Facade',
        'AbstractFactory', 'FactoryImpl', 'StrategyImpl'
    ]
    for indicator in pattern_indicators:
        if indicator.lower() in content.lower():
            complexity += 3
    
    # Count config files (+2 each)
    config_indicators = ['.yml', '.yaml', '.properties', '.xml', '.json', 'application.properties']
    for indicator in config_indicators:
        if indicator in content:
            complexity += 2
            
    return complexity

def count_dependencies(content):
    """Count external tool dependencies"""
    mcp_tools = len(re.findall(r'mcp__\w+__\w+', content))
    bash_commands = len(re.findall(r'bash|shell|command', content, re.IGNORECASE))
    web_requests = len(re.findall(r'http|fetch|curl|wget', content, re.IGNORECASE))
    return mcp_tools + bash_commands + web_requests

def analyze_verbosity(content):
    """Measure verbosity vs value ratio"""
    lines = content.split('\n')
    actual_code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('<!--')]
    comment_lines = [l for l in lines if l.strip().startswith('#') or '##' in l]
    markdown_fluff = [l for l in lines if '```' in l or l.strip().startswith('*') or l.strip().startswith('-')]
    
    return {
        'total_lines': len(lines),
        'code_lines': len(actual_code_lines),
        'comment_lines': len(comment_lines),
        'fluff_lines': len(markdown_fluff),
        'signal_to_noise': len(actual_code_lines) / len(lines) if lines else 0
    }

def calculate_maintenance_burden(content):
    """Calculate how likely this is to break"""
    risk_factors = 0
    
    # External dependencies
    if 'mcp__' in content:
        risk_factors += 3  # High risk - external MCP tools
    if 'firecrawl' in content or 'web' in content.lower():
        risk_factors += 2  # Medium risk - web dependencies
    if 'obsidian' in content.lower():
        risk_factors += 1  # Low risk - local tools
        
    # Complexity indicators
    if content.count('```') > 10:
        risk_factors += 2  # Too many code blocks
    if len(content) > 15000:
        risk_factors += 2  # File too large
        
    # Fragility indicators
    if 'experimental' in content.lower() or 'beta' in content.lower():
        risk_factors += 3
        
    return risk_factors

def rate_user_experience(content, filename):
    """Rate the user experience quality"""
    ux_score = 10  # Start perfect
    
    # Documentation clarity
    if 'usage:' not in content.lower() and 'how to' not in content.lower():
        ux_score -= 2  # No clear usage instructions
        
    # Example quality
    if 'example' not in content.lower():
        ux_score -= 2  # No examples provided
        
    # Over-engineering penalty
    if len(content) > 20000:
        ux_score -= 3  # Intimidatingly large
        
    # Naming clarity
    if 'ultrathink' in filename and 'interactive' in filename:
        ux_score -= 1  # Confusing compound names
        
    return max(0, ux_score)

# Main analysis
commands = [
    'ultrathink-interactive.md',
    'java-rapid-implementation.md', 
    'adhd-morning-assistant.md',
    'adhd-hyperfocus-guardian.md',
    'ultrathink-hybrid-mcp.md'
]

results = {
    'timestamp': datetime.now().isoformat(),
    'methodology': '20250825-230341-methodology.md',
    'commands_analyzed': len(commands),
    'results': {}
}

print('🔬 SAVAGE COMMAND BENCHMARKING - Scientific Analysis')
print('=' * 60)

for cmd in commands:
    filepath = f'/home/runner/work/claude-dotfiles/claude-dotfiles/commands/{cmd}'
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Run all analyses
        complexity = analyze_command_complexity(filepath)
        deps = count_dependencies(content)
        verbosity = analyze_verbosity(content)
        maintenance_risk = calculate_maintenance_burden(content)
        ux_score = rate_user_experience(content, cmd)
        
        # Calculate final grade
        penalty = 0
        if complexity >= 5:
            penalty += 20  # Major complexity penalty
        if deps > 5:
            penalty += 15  # Dependency hell penalty
        if verbosity['signal_to_noise'] < 0.3:
            penalty += 10  # Too much fluff penalty
        if maintenance_risk > 5:
            penalty += 15  # Maintenance nightmare penalty
            
        final_score = max(0, 100 - penalty)
        
        # Determine grade
        if final_score >= 90:
            grade = 'A+'
        elif final_score >= 80:
            grade = 'A'
        elif final_score >= 70:
            grade = 'B'
        elif final_score >= 60:
            grade = 'C'
        elif final_score >= 50:
            grade = 'D'
        else:
            grade = 'F'
            
        # Store results
        results['results'][cmd] = {
            'complexity_score': complexity,
            'dependencies': deps,
            'total_lines': verbosity['total_lines'],
            'signal_noise_ratio': verbosity['signal_to_noise'],
            'maintenance_risk': maintenance_risk,
            'ux_score': ux_score,
            'final_score': final_score,
            'grade': grade,
            'file_size_bytes': len(content),
            'is_over_engineered': complexity >= 5,
            'savage_verdict': 'OVER-ENGINEERED TRASH' if complexity >= 5 else 'Acceptable Complexity'
        }
        
        # Print detailed analysis
        print(f'\n📊 {cmd}:')
        print(f'   Complexity Score: {complexity}/30 {"🚨 DANGER!" if complexity >= 5 else "✅"}')
        print(f'   Dependencies: {deps} external tools {"🚨" if deps > 5 else ""}')
        print(f'   File Size: {len(content):,} bytes ({len(content)/1024:.1f}KB)')
        print(f'   Signal/Noise Ratio: {verbosity["signal_to_noise"]:.1%} {"🚨" if verbosity["signal_to_noise"] < 0.3 else ""}')
        print(f'   Maintenance Risk: {maintenance_risk}/10 {"🚨" if maintenance_risk > 5 else ""}')
        print(f'   User Experience: {ux_score}/10')
        print(f'   📊 FINAL GRADE: {grade} ({final_score}/100)')
        print(f'   🔥 SAVAGE VERDICT: {results["results"][cmd]["savage_verdict"]}')

print(f'\n💾 Saving detailed results to JSON...')

# Save detailed results
with open('/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/20250825-230341-analysis.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f'✅ Analysis complete! {len(commands)} commands scientifically roasted.')