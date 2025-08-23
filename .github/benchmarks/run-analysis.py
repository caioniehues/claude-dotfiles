#!/usr/bin/env python3
"""
SAVAGE COMMAND ANALYSIS - Direct execution
"""

import json
import time
import statistics
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

class CommandAnalyzer:
    """Savage but scientific command analyzer"""
    
    def __init__(self):
        self.commands_dir = Path("commands")
        self.results_dir = Path(".github/benchmarks/results")
        self.results_dir.mkdir(parents=True, exist_ok=True)
    
    def measure_complexity_score(self, command_path: str) -> float:
        """Calculate complexity based on CLAUDE.md rules"""
        with open(command_path, 'r') as f:
            content = f.read()
        
        score = 0
        
        # Direct solution check
        if "<thinking>" in content.lower():
            score += 1
        
        # Each new abstraction layer
        abstractions = len(re.findall(r'<[^/][^>]*>', content))
        score += min(abstractions / 10, 2)  # Cap at 2 points
        
        # MCP tool usage (complexity increase)
        mcp_calls = len(re.findall(r'mcp__[a-zA-Z-_]+__', content))
        score += min(mcp_calls * 0.3, 2)  # Cap at 2 points
        
        # Nested thinking blocks
        nested_thinking = len(re.findall(r'<[^>]*thinking[^>]*>.*?<[^>]*thinking[^>]*>', content, re.DOTALL))
        score += nested_thinking * 0.5
        
        return min(score, 5.0)
    
    def calculate_success_rate(self, command_path: str) -> float:
        """Calculate expected success rate"""
        with open(command_path, 'r') as f:
            content = f.read()
        
        success_factors = 0
        total_factors = 8
        
        # Error handling
        if "error" in content.lower() or "exception" in content.lower():
            success_factors += 1
        
        # Validation steps
        if "validate" in content.lower() or "check" in content.lower():
            success_factors += 1
        
        # Complexity appropriate
        complexity = self.measure_complexity_score(command_path)
        if 1.5 <= complexity <= 3.5:
            success_factors += 2
        elif complexity <= 1.5 or complexity >= 4.5:
            success_factors += 0
        else:
            success_factors += 1
        
        # Clear structure
        if "<task>" in content and "</task>" in content:
            success_factors += 1
        
        # Documentation
        if "##" in content:
            success_factors += 1
        
        # MCP integration
        if "mcp__" in content:
            if "thinking" in content.lower():
                success_factors += 1
            else:
                success_factors += 0.5
        else:
            success_factors += 1
        
        # Reasonable length
        lines = len(content.split('\n'))
        if 100 <= lines <= 600:
            success_factors += 1
        elif lines < 50:
            success_factors += 0
        else:
            success_factors += 0.5
        
        return min(success_factors / total_factors, 1.0)
    
    def estimate_token_usage(self, command_path: str) -> int:
        """Estimate token consumption"""
        with open(command_path, 'r') as f:
            content = f.read()
        
        # Base estimate: ~4 characters per token
        base_tokens = len(content) // 4
        
        # MCP calls increase token usage
        mcp_calls = len(re.findall(r'mcp__[a-zA-Z-_]+__', content))
        mcp_overhead = mcp_calls * 500  # 500 tokens per MCP call
        
        # Thinking blocks add processing overhead
        thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content))
        thinking_overhead = thinking_blocks * 200
        
        return base_tokens + mcp_overhead + thinking_overhead
    
    def calculate_error_frequency(self, command_path: str) -> float:
        """Estimate error probability"""
        with open(command_path, 'r') as f:
            content = f.read()
        
        error_factors = 0
        
        # High complexity
        complexity = self.measure_complexity_score(command_path)
        if complexity > 4:
            error_factors += 0.3
        elif complexity > 3:
            error_factors += 0.15
        
        # MCP dependencies
        mcp_calls = len(re.findall(r'mcp__[a-zA-Z-_]+__', content))
        error_factors += mcp_calls * 0.05
        
        # Lack of error handling
        if "error" not in content.lower():
            error_factors += 0.2
        
        return min(error_factors, 1.0)
    
    def generate_savage_score(self, metrics: Dict) -> Tuple[float, str]:
        """Generate savage but fair score and commentary"""
        score = 5.0  # Base
        commentary_parts = []
        
        # Token efficiency
        tokens = metrics['token_usage']
        if tokens > 20000:
            score -= 2
            commentary_parts.append(f"Token usage: {tokens:,}. Like using a freight train to deliver a pizza.")
        elif tokens > 10000:
            score -= 1
            commentary_parts.append(f"Token usage: {tokens:,}. Moderately bloated.")
        else:
            score += 1
            commentary_parts.append(f"Token usage: {tokens:,}. Actually reasonable.")
        
        # Success rate
        success = metrics['success_rate']
        if success < 0.7:
            score -= 3
            commentary_parts.append(f"Success rate: {success:.1%}. Worse than a coin flip.")
        elif success < 0.85:
            score -= 1
            commentary_parts.append(f"Success rate: {success:.1%}. Mediocre reliability.")
        else:
            score += 1
            commentary_parts.append(f"Success rate: {success:.1%}. Actually reliable.")
        
        # Complexity
        complexity = metrics['complexity_score']
        if complexity > 5:
            score -= 3
            commentary_parts.append(f"Complexity: {complexity:.1f}/5. Violates CLAUDE.md rules spectacularly.")
        elif complexity > 4:
            score -= 2
            commentary_parts.append(f"Complexity: {complexity:.1f}/5. Over-engineered.")
        elif complexity < 1:
            score -= 1
            commentary_parts.append(f"Complexity: {complexity:.1f}/5. Suspiciously simple.")
        else:
            score += 0.5
        
        # Error frequency
        errors = metrics['error_frequency']
        if errors > 0.3:
            score -= 2
            commentary_parts.append(f"Error rate: {errors:.1%}. Fails more than it succeeds.")
        
        score = max(0, min(10, score))
        
        # Overall assessment
        if score < 3:
            overall = "Dumpster fire disguised as code."
        elif score < 5:
            overall = "Functional but uninspiring."
        elif score < 7:
            overall = "Decent with room for improvement."
        elif score < 8.5:
            overall = "Well-designed and competent."
        else:
            overall = "Excellence in command form."
        
        commentary = f"{overall} " + " ".join(commentary_parts)
        return score, commentary
    
    def analyze_command(self, command_file: str) -> Dict:
        """Analyze a single command"""
        command_path = self.commands_dir / command_file
        
        if not command_path.exists():
            return None
        
        print(f"🔬 Analyzing {command_file}...")
        
        metrics = {
            'complexity_score': self.measure_complexity_score(str(command_path)),
            'success_rate': self.calculate_success_rate(str(command_path)),
            'token_usage': self.estimate_token_usage(str(command_path)),
            'error_frequency': self.calculate_error_frequency(str(command_path))
        }
        
        savage_score, commentary = self.generate_savage_score(metrics)
        
        return {
            'command': command_file,
            'metrics': metrics,
            'savage_score': savage_score,
            'commentary': commentary,
            'timestamp': datetime.now().isoformat()
        }
    
    def run_analysis(self, selected_commands: List[str]) -> Dict:
        """Run full analysis on selected commands"""
        print("🔥 SAVAGE COMMAND BENCHMARKER")
        print("=" * 60)
        print("Scientific Analysis with PhD-level Brutality")
        print()
        
        results = {}
        
        for command_file in selected_commands:
            result = self.analyze_command(command_file)
            if result:
                results[command_file] = result
                print(f"📊 {command_file}: {result['savage_score']:.1f}/10")
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive report"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        report_file = self.results_dir / f"{timestamp}-report.json"
        
        # Calculate aggregate stats
        scores = [r['savage_score'] for r in results.values()]
        complexities = [r['metrics']['complexity_score'] for r in results.values()]
        success_rates = [r['metrics']['success_rate'] for r in results.values()]
        token_usage = [r['metrics']['token_usage'] for r in results.values()]
        
        # Rank commands
        ranked = sorted(results.items(), key=lambda x: x[1]['savage_score'], reverse=True)
        
        # Generate insights
        savage_insights = []
        mean_score = statistics.mean(scores) if scores else 0
        
        if mean_score < 5:
            savage_insights.append(f"Average quality: {mean_score:.1f}/10. Your command library needs an intervention.")
        else:
            savage_insights.append(f"Average quality: {mean_score:.1f}/10. Not terrible, surprisingly.")
        
        # Worst and best
        if ranked:
            worst = ranked[-1]
            best = ranked[0]
            savage_insights.append(f"Worst: {worst[0]} ({worst[1]['savage_score']:.1f}/10) - A cautionary tale.")
            savage_insights.append(f"Best: {best[0]} ({best[1]['savage_score']:.1f}/10) - Someone read the docs.")
        
        # CLAUDE.md violations
        violations = [cmd for cmd, result in results.items() if result['metrics']['complexity_score'] > 5]
        if violations:
            savage_insights.append(f"CLAUDE.md violators: {', '.join(violations)}. Rules are apparently optional.")
        
        report_data = {
            'benchmark_timestamp': timestamp,
            'methodology': {
                'commands_analyzed': len(results),
                'metrics': ['complexity_score', 'success_rate', 'token_usage', 'error_frequency'],
                'scoring_range': '0-10 (higher is better)',
                'complexity_limit': '5 (per CLAUDE.md)'
            },
            'aggregate_statistics': {
                'mean_savage_score': mean_score,
                'score_std_dev': statistics.stdev(scores) if len(scores) > 1 else 0,
                'mean_complexity': statistics.mean(complexities) if complexities else 0,
                'mean_success_rate': statistics.mean(success_rates) if success_rates else 0,
                'mean_token_usage': statistics.mean(token_usage) if token_usage else 0
            },
            'command_rankings': [
                {
                    'rank': i + 1,
                    'command': cmd,
                    'savage_score': result['savage_score'],
                    'complexity': result['metrics']['complexity_score'],
                    'success_rate': result['metrics']['success_rate'],
                    'tokens': result['metrics']['token_usage']
                }
                for i, (cmd, result) in enumerate(ranked)
            ],
            'detailed_results': results,
            'savage_insights': savage_insights
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        return str(report_file)

def main():
    selected_commands = [
        "ultrathink-hybrid-mcp.md",
        "adaptive-complexity-router.md", 
        "adhd-context-switch.md",
        "intelligent-code-enhancer.md",
        "intelligent-refactor-session.md"
    ]
    
    analyzer = CommandAnalyzer()
    results = analyzer.run_analysis(selected_commands)
    
    if results:
        print("\n📝 Generating savage report...")
        report_file = analyzer.generate_report(results)
        
        print(f"\n✅ Report generated: {report_file}")
        
        # Show quick summary
        with open(report_file, 'r') as f:
            data = json.load(f)
        
        print("\n💀 SAVAGE INSIGHTS:")
        for insight in data['savage_insights']:
            print(f"  • {insight}")
        
        print("\n🏆 TOP COMMANDS:")
        for ranking in data['command_rankings'][:3]:
            print(f"  {ranking['rank']}. {ranking['command']}: {ranking['savage_score']:.1f}/10")
        
        print(f"\n📄 Full statistical analysis saved to: {report_file}")
        print("💀 Scientific roasting complete!")

if __name__ == "__main__":
    main()