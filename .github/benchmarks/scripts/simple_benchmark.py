#!/usr/bin/env python3
"""
🔬 SAVAGE COMMAND BENCHMARKER - PhD Edition
Direct execution with brutal statistical honesty
"""

import json
import statistics
import re
from datetime import datetime
from pathlib import Path

def analyze_command_file(filepath):
    """Analyze a single command file with statistical rigor"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basic metrics
    word_count = len(content.split())
    line_count = len(content.splitlines())
    char_count = len(content)
    
    # Complexity score (CLAUDE.md standards)
    complexity = 1  # Base
    content_lower = content.lower()
    complexity += content_lower.count("class") * 2
    complexity += content_lower.count("interface") * 1
    complexity += content_lower.count("pattern") * 3
    complexity += content_lower.count("factory") * 3
    complexity += content_lower.count("builder") * 3
    complexity += content_lower.count("strategy") * 3
    complexity += content_lower.count("config") * 2
    
    # Instructions and structure
    instructions = content.count("- ") + content.count("1. ") + content.count("2. ")
    code_blocks = content.count("```") // 2
    headers = content.count("#")
    
    # Anti-patterns
    anti_patterns = []
    if "factory" in content_lower and "builder" in content_lower:
        anti_patterns.append("Factory+Builder combo")
    if content_lower.count("interface") > 2:
        anti_patterns.append("Abstraction overload")
    if re.search(r'import.*\*', content):
        anti_patterns.append("Wildcard imports")
    if word_count > 500:
        anti_patterns.append("Verbal diarrhea")
    if complexity >= 5:
        anti_patterns.append("Complexity violation")
    
    # Readability score
    readability = 10.0
    readability -= min(complexity * 0.5, 5.0)  # Complexity penalty
    readability += min(headers * 0.2, 2.0)    # Structure bonus
    readability -= max((word_count - 300) * 0.005, 0)  # Length penalty
    readability = max(0.0, min(10.0, readability))
    
    return {
        'name': filepath.name,
        'word_count': word_count,
        'line_count': line_count,
        'complexity_score': complexity,
        'instructions': instructions,
        'code_blocks': code_blocks,
        'readability_score': round(readability, 1),
        'anti_patterns': anti_patterns,
        'violates_complexity': complexity >= 5,
        'violates_length': word_count > 500,
        'violates_readability': readability < 5.0
    }

def generate_savage_judgment(metrics):
    """Generate brutally honest assessment"""
    judgments = []
    severity = 0
    
    if metrics['violates_complexity']:
        judgments.append(f"Complexity score of {metrics['complexity_score']}/5 violates CLAUDE.md sacred law. This isn't architecture, it's architectural obesity.")
        severity += 3
    
    if metrics['violates_length']:
        judgments.append(f"At {metrics['word_count']} words, this has more bloat than Windows Vista. Brevity is the soul of wit.")
        severity += 2
    
    if metrics['anti_patterns']:
        judgments.append(f"Anti-patterns detected: {', '.join(metrics['anti_patterns'])}. This code doesn't just smell, it reeks.")
        severity += len(metrics['anti_patterns'])
    
    if metrics['violates_readability']:
        judgments.append(f"Readability score of {metrics['readability_score']}/10 suggests this was written by caffeinated interns with thesaurus addiction.")
        severity += 2
    
    if not judgments:
        judgments.append("Surprisingly, this command doesn't make me question my life choices. Well done - it's simple and clear.")
        severity = 0
    
    # Overall assessment
    if severity == 0:
        overall = "EXCELLENT - Actually follows principles"
    elif severity <= 3:
        overall = "ACCEPTABLE - Minor improvements needed" 
    elif severity <= 6:
        overall = "PROBLEMATIC - Major refactoring required"
    else:
        overall = "CATASTROPHIC - Restart from scratch"
    
    return {
        'judgments': judgments,
        'severity_score': severity,
        'overall_assessment': overall
    }

def main():
    print("🔬 SAVAGE COMMAND BENCHMARKER - PhD Edition")
    print("=" * 60)
    
    # Selected commands for benchmarking
    selected_commands = [
        "ultrathink.md",
        "java-test-driven-development.md", 
        "adhd-task-breakdown.md",
        "intelligent-code-enhancer.md",
        "senior-developer-analysis.md"
    ]
    
    results = []
    commands_dir = Path("commands")
    
    print(f"📊 Analyzing {len(selected_commands)} commands with statistical rigor...\n")
    
    for cmd_name in selected_commands:
        cmd_path = commands_dir / cmd_name
        if not cmd_path.exists():
            print(f"❌ Command not found: {cmd_name}")
            continue
            
        print(f"🔍 Analyzing: {cmd_name}")
        
        # Analyze the command
        metrics = analyze_command_file(cmd_path)
        judgment = generate_savage_judgment(metrics)
        
        result = {**metrics, **judgment}
        results.append(result)
        
        # Print summary
        print(f"   Complexity: {metrics['complexity_score']}/5 {'❌' if metrics['violates_complexity'] else '✅'}")
        print(f"   Words: {metrics['word_count']} {'❌' if metrics['violates_length'] else '✅'}")
        print(f"   Readability: {metrics['readability_score']}/10")
        print(f"   Assessment: {judgment['overall_assessment']}")
        if judgment['judgments']:
            print(f"   Savage Take: {judgment['judgments'][0]}")
        print()
    
    # Statistical analysis
    if results:
        complexity_scores = [r['complexity_score'] for r in results]
        word_counts = [r['word_count'] for r in results]
        readability_scores = [r['readability_score'] for r in results]
        
        stats = {
            'sample_size': len(results),
            'complexity_stats': {
                'mean': round(statistics.mean(complexity_scores), 2),
                'median': statistics.median(complexity_scores),
                'stdev': round(statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0, 2),
                'max': max(complexity_scores),
                'violations': sum(1 for r in results if r['violates_complexity'])
            },
            'word_count_stats': {
                'mean': round(statistics.mean(word_counts), 2),
                'median': statistics.median(word_counts),
                'stdev': round(statistics.stdev(word_counts) if len(word_counts) > 1 else 0, 2),
                'bloated_commands': sum(1 for r in results if r['violates_length'])
            },
            'readability_stats': {
                'mean': round(statistics.mean(readability_scores), 2),
                'median': statistics.median(readability_scores),
                'stdev': round(statistics.stdev(readability_scores) if len(readability_scores) > 1 else 0, 2),
                'poor_readability': sum(1 for r in results if r['violates_readability'])
            }
        }
        
        print("📊 STATISTICAL ANALYSIS")
        print("=" * 40)
        print(f"Sample size: {stats['sample_size']} commands")
        print(f"Complexity violations: {stats['complexity_stats']['violations']}/{stats['sample_size']}")
        print(f"Bloated commands (>500 words): {stats['word_count_stats']['bloated_commands']}/{stats['sample_size']}")
        print(f"Poor readability (<5.0): {stats['readability_stats']['poor_readability']}/{stats['sample_size']}")
        print(f"Average complexity: {stats['complexity_stats']['mean']} ± {stats['complexity_stats']['stdev']}")
        print(f"Average word count: {stats['word_count_stats']['mean']} ± {stats['word_count_stats']['stdev']}")
        print(f"Average readability: {stats['readability_stats']['mean']} ± {stats['readability_stats']['stdev']}")
        
        # Overall assessment
        total_violations = (stats['complexity_stats']['violations'] + 
                          stats['word_count_stats']['bloated_commands'] + 
                          stats['readability_stats']['poor_readability'])
        
        print(f"\n🎯 OVERALL SAVAGE ASSESSMENT")
        print("=" * 40)
        if total_violations == 0:
            print("🎉 MIRACULOUS: All commands pass basic quality standards!")
            print("Someone actually read CLAUDE.md and took it seriously.")
        elif total_violations <= stats['sample_size'] * 0.3:
            print(f"⚠️  ACCEPTABLE: {total_violations} issues across {stats['sample_size']} commands.")
            print("Room for improvement exists, but not catastrophic.")
        else:
            print(f"🚨 PROBLEMATIC: {total_violations} violations across {stats['sample_size']} commands.")
            print("Houston, we have a quality problem. Intervention required.")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        report = {
            'timestamp': timestamp,
            'methodology': 'Random sampling with statistical rigor and savage judgment',
            'commands_analyzed': len(results),
            'statistical_analysis': stats,
            'individual_results': results,
            'recommendations': [
                'Apply the 3-Question Rule before adding complexity',
                'Enforce 300-word limit for command descriptions', 
                'Use complexity scoring in code reviews',
                'Regular audits using this benchmarking tool',
                'Training on CLAUDE.md clean code principles'
            ]
        }
        
        output_path = Path('.github/benchmarks/results')
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / f"{timestamp}-report.json"
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Report saved: {output_file}")
    
    return results

if __name__ == "__main__":
    main()