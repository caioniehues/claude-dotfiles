#!/usr/bin/env python3
"""
🔬 SAVAGE COMMAND BENCHMARKER
Scientific measurement and brutal judgment of Claude Code commands.
"""

import json
import time
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import statistics

class CommandBenchmarker:
    def __init__(self):
        self.results = {}
        self.timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
    def analyze_command_complexity(self, command_path: str) -> Dict[str, Any]:
        """Calculate complexity metrics per CLAUDE.md rules"""
        with open(command_path, 'r') as f:
            content = f.read()
        
        # Complexity scoring per CLAUDE.md
        complexity_score = 1  # Base
        
        # Count patterns that add complexity
        patterns = {
            'new_class': len(re.findall(r'class\s+\w+', content, re.IGNORECASE)),
            'interfaces': len(re.findall(r'interface\s+\w+', content, re.IGNORECASE)),
            'design_patterns': len(re.findall(r'(factory|builder|strategy|observer|singleton)', content, re.IGNORECASE)),
            'config_files': len(re.findall(r'\.(xml|json|yaml|properties)', content)),
            'mcp_calls': len(re.findall(r'mcp__', content)),
            'thinking_blocks': len(re.findall(r'<thinking.*?>', content, re.DOTALL)),
            'decision_points': len(re.findall(r'(decision|choice|alternative)', content, re.IGNORECASE))
        }
        
        # Apply CLAUDE.md scoring
        complexity_score += patterns['new_class'] * 2
        complexity_score += patterns['interfaces'] * 1
        complexity_score += patterns['design_patterns'] * 3
        complexity_score += patterns['config_files'] * 2
        
        # Count lines and words for size metrics
        lines = len(content.split('\n'))
        words = len(content.split())
        
        return {
            'complexity_score': complexity_score,
            'lines': lines,
            'words': words,
            'patterns': patterns,
            'violates_rules': complexity_score >= 5
        }
    
    def measure_token_consumption(self, content: str) -> Dict[str, int]:
        """Estimate token consumption (rough approximation)"""
        # Rough token estimation: ~4 chars per token for English
        input_tokens = len(content) // 4
        
        # Estimate output based on command type and complexity
        if 'thinking' in content.lower():
            output_multiplier = 3.5  # Thinking commands generate more output
        elif 'analysis' in content.lower():
            output_multiplier = 2.8
        elif 'adhd' in content.lower():
            output_multiplier = 2.2
        else:
            output_multiplier = 1.8
            
        estimated_output = int(input_tokens * output_multiplier)
        total_tokens = input_tokens + estimated_output
        
        return {
            'input_tokens': input_tokens,
            'estimated_output_tokens': estimated_output,
            'total_estimated_tokens': total_tokens
        }
    
    def analyze_command_structure(self, content: str) -> Dict[str, Any]:
        """Analyze structural quality of the command"""
        structure_score = 0
        issues = []
        
        # Check for required sections
        required_sections = ['<task>', '<context>']
        for section in required_sections:
            if section in content:
                structure_score += 1
            else:
                issues.append(f"Missing {section}")
        
        # Check for thinking orchestration
        if '<thinking_orchestration>' in content:
            structure_score += 2
        else:
            issues.append("No thinking orchestration")
            
        # Check for complexity detection
        if 'complexity_detection' in content:
            structure_score += 1
        else:
            issues.append("No complexity detection")
            
        # Check for MCP integration
        if 'mcp__' in content:
            structure_score += 1
        else:
            issues.append("No MCP integration")
            
        return {
            'structure_score': structure_score,
            'max_score': 5,
            'percentage': (structure_score / 5) * 100,
            'issues': issues
        }
    
    def benchmark_command(self, command_path: str) -> Dict[str, Any]:
        """Comprehensive benchmark of a single command"""
        start_time = time.time()
        
        command_name = Path(command_path).stem
        
        with open(command_path, 'r') as f:
            content = f.read()
        
        # Run all measurements
        complexity = self.analyze_command_complexity(command_path)
        tokens = self.measure_token_consumption(content)
        structure = self.analyze_command_structure(content)
        
        # Calculate composite scores
        quality_score = (
            (5 - min(complexity['complexity_score'], 5)) * 20 +  # Complexity (lower is better)
            structure['percentage'] +  # Structure quality
            min(100, tokens['total_estimated_tokens'] / 100)  # Token efficiency
        ) / 3
        
        execution_time = time.time() - start_time
        
        return {
            'command_name': command_name,
            'file_path': command_path,
            'timestamp': datetime.now().isoformat(),
            'execution_time_ms': execution_time * 1000,
            'complexity': complexity,
            'tokens': tokens,
            'structure': structure,
            'quality_score': quality_score,
            'savage_verdict': self.generate_savage_verdict(complexity, tokens, structure, quality_score)
        }
    
    def generate_savage_verdict(self, complexity, tokens, structure, quality_score) -> str:
        """Generate brutally honest assessment based on data"""
        verdicts = []
        
        # Complexity assessment
        if complexity['complexity_score'] >= 5:
            verdicts.append(f"COMPLEXITY VIOLATION: Score {complexity['complexity_score']}/5. This isn't 'sophisticated', it's BLOATED.")
        elif complexity['complexity_score'] <= 2:
            verdicts.append(f"SIMPLICITY WIN: Score {complexity['complexity_score']}/5. Actually follows the rules!")
        else:
            verdicts.append(f"ACCEPTABLE: Score {complexity['complexity_score']}/5. Teetering on the edge of chaos.")
            
        # Token efficiency
        if tokens['total_estimated_tokens'] > 5000:
            verdicts.append(f"TOKEN VAMPIRE: {tokens['total_estimated_tokens']} tokens. This command drinks tokens like a Vegas slot machine drinks quarters.")
        elif tokens['total_estimated_tokens'] < 1000:
            verdicts.append(f"EFFICIENT: {tokens['total_estimated_tokens']} tokens. Respects your Claude budget.")
        else:
            verdicts.append(f"REASONABLE: {tokens['total_estimated_tokens']} tokens. Not terrible, not great.")
            
        # Structure quality
        if structure['percentage'] >= 80:
            verdicts.append(f"WELL STRUCTURED: {structure['percentage']:.1f}% compliance. Someone read the docs.")
        elif structure['percentage'] < 50:
            verdicts.append(f"STRUCTURAL NIGHTMARE: {structure['percentage']:.1f}% compliance. Did you even TRY to follow the patterns?")
        else:
            verdicts.append(f"MEDIOCRE STRUCTURE: {structure['percentage']:.1f}% compliance. Half-hearted effort detected.")
            
        # Overall verdict
        if quality_score >= 80:
            overall = "🏆 EXEMPLARY: This is how it's done."
        elif quality_score >= 60:
            overall = "✅ DECENT: Gets the job done without embarrassing anyone."
        elif quality_score >= 40:
            overall = "⚠️ PROBLEMATIC: Has issues but not completely hopeless."
        else:
            overall = "💀 DISASTER: This command is a crime against clean code."
            
        return {
            'breakdown': verdicts,
            'overall': overall,
            'numeric_score': quality_score
        }
    
    def run_benchmark_suite(self, command_files: List[str]) -> Dict[str, Any]:
        """Run comprehensive benchmark on selected commands"""
        suite_start = time.time()
        
        results = []
        for cmd_file in command_files:
            print(f"🔬 Benchmarking: {Path(cmd_file).stem}")
            result = self.benchmark_command(cmd_file)
            results.append(result)
        
        # Calculate statistics
        quality_scores = [r['quality_score'] for r in results]
        complexity_scores = [r['complexity']['complexity_score'] for r in results]
        token_counts = [r['tokens']['total_estimated_tokens'] for r in results]
        
        statistics_data = {
            'quality_mean': statistics.mean(quality_scores),
            'quality_stdev': statistics.stdev(quality_scores) if len(quality_scores) > 1 else 0,
            'complexity_mean': statistics.mean(complexity_scores),
            'complexity_stdev': statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
            'token_mean': statistics.mean(token_counts),
            'token_stdev': statistics.stdev(token_counts) if len(token_counts) > 1 else 0,
        }
        
        suite_time = time.time() - suite_start
        
        return {
            'benchmark_id': self.timestamp,
            'suite_execution_time_s': suite_time,
            'commands_analyzed': len(command_files),
            'individual_results': results,
            'statistics': statistics_data,
            'generated_at': datetime.now().isoformat()
        }

def main():
    # Selected commands for benchmarking
    commands = [
        "commands/java-clean-code-generator.md",
        "commands/adhd-morning-assistant.md", 
        "commands/adhd-evening-reflect.md",
        "commands/analyze-project-architecture.md",
        "commands/reasoning-wrapper.md",
        "commands/senior-developer-analysis.md"
    ]
    
    benchmarker = CommandBenchmarker()
    results = benchmarker.run_benchmark_suite(commands)
    
    # Save results
    output_file = f".github/benchmarks/results/{benchmarker.timestamp}-report.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🎯 Benchmark complete! Results saved to: {output_file}")
    print(f"📊 Commands analyzed: {results['commands_analyzed']}")
    print(f"⏱️ Total time: {results['suite_execution_time_s']:.2f}s")
    
    return results

if __name__ == "__main__":
    main()