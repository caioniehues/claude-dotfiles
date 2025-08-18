#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER - PhD in Roasting Bad Code
Scientific measurement and brutal judgment of Claude commands.
"""

import json
import time
import statistics
import random
import os
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class CommandMetrics:
    name: str
    file_path: str
    token_count: int
    line_count: int
    complexity_score: float
    composition_compatibility: int
    execution_time: float
    success_rate: float
    error_frequency: float
    memory_usage: int
    readability_score: float
    savage_judgment: str
    
class ScientificBenchmarker:
    def __init__(self):
        self.commands_dir = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
        self.baseline_metrics = {}
        self.statistical_thresholds = {
            "complexity_danger": 5.0,
            "token_bloat": 2000,
            "line_excess": 500,
            "failure_tolerance": 0.05  # 5% failure rate max
        }
    
    def measure_token_consumption(self, content: str) -> int:
        """Estimate token count using rough approximation"""
        # Rough estimation: 4 chars per token average
        return len(content) // 4
    
    def calculate_complexity_score(self, content: str) -> float:
        """Calculate complexity using CLAUDE.md rules"""
        score = 1.0  # Base solution
        
        # XML tags complexity
        xml_patterns = content.count('<') + content.count('>')
        score += xml_patterns * 0.1
        
        # MCP tool calls
        mcp_calls = content.count('mcp__')
        score += mcp_calls * 0.5
        
        # Thinking blocks
        thinking_blocks = content.count('<thinking')
        score += thinking_blocks * 0.3
        
        # Nested structures
        nested_levels = content.count('##') + content.count('###')
        score += nested_levels * 0.1
        
        return score
    
    def measure_readability(self, content: str) -> float:
        """Savage readability assessment"""
        lines = content.split('\n')
        total_lines = len(lines)
        
        # Penalty for overly long lines
        long_lines = sum(1 for line in lines if len(line) > 120)
        
        # Penalty for unclear naming
        unclear_vars = content.count('$ARGUMENTS') + content.count('${')
        
        # Bonus for clear structure
        structure_bonus = content.count('##') * 0.1
        
        base_score = 10.0
        base_score -= (long_lines / total_lines) * 3
        base_score -= unclear_vars * 0.2
        base_score += structure_bonus
        
        return max(0, min(10, base_score))
    
    def assess_composition_compatibility(self, content: str) -> int:
        """How well does this compose with other commands?"""
        compatibility_score = 5  # Base score
        
        # Bonus for tool usage
        if 'mcp__basic-memory' in content:
            compatibility_score += 2
        
        # Bonus for clear inputs/outputs
        if '$ARGUMENTS' in content:
            compatibility_score += 1
        
        # Penalty for hardcoded paths/assumptions
        if '/Users/' in content or 'hardcoded' in content.lower():
            compatibility_score -= 2
        
        return max(0, min(10, compatibility_score))
    
    def generate_savage_judgment(self, metrics: CommandMetrics) -> str:
        """Brutally honest but data-backed assessment"""
        judgments = []
        
        if metrics.complexity_score > 8:
            judgments.append(f"Complexity score of {metrics.complexity_score:.1f} suggests this command has commitment issues - it can't decide what it wants to be when it grows up.")
        
        if metrics.token_count > 3000:
            judgments.append(f"At {metrics.token_count} estimated tokens, this command is more bloated than a startup's Series A pitch deck.")
        
        if metrics.line_count > 800:
            judgments.append(f"{metrics.line_count} lines? War and Peace was shorter and more focused.")
        
        if metrics.readability_score < 5:
            judgments.append(f"Readability score of {metrics.readability_score:.1f}/10. Even the author needs a therapist to understand what they wrote.")
        
        if metrics.composition_compatibility < 4:
            judgments.append(f"Composition compatibility of {metrics.composition_compatibility}/10. This command plays well with others like a honey badger in a petting zoo.")
        
        if not judgments:
            judgments.append("Surprisingly decent. Like finding a unicorn in a field of donkeys.")
        
        return " ".join(judgments)
    
    def benchmark_command(self, command_file: str) -> CommandMetrics:
        """Full scientific analysis of a single command"""
        start_time = time.time()
        
        with open(command_file, 'r') as f:
            content = f.read()
        
        name = os.path.basename(command_file).replace('.md', '')
        
        metrics = CommandMetrics(
            name=name,
            file_path=command_file,
            token_count=self.measure_token_consumption(content),
            line_count=len(content.split('\n')),
            complexity_score=self.calculate_complexity_score(content),
            composition_compatibility=self.assess_composition_compatibility(content),
            execution_time=time.time() - start_time,
            success_rate=random.uniform(0.7, 0.95),  # Simulated for now
            error_frequency=random.uniform(0.05, 0.25),  # Simulated
            memory_usage=len(content),  # Proxy for memory
            readability_score=self.measure_readability(content),
            savage_judgment=""
        )
        
        metrics.savage_judgment = self.generate_savage_judgment(metrics)
        return metrics
    
    def run_statistical_analysis(self, all_metrics: List[CommandMetrics]) -> Dict:
        """Rigorous statistical analysis"""
        complexity_scores = [m.complexity_score for m in all_metrics]
        token_counts = [m.token_count for m in all_metrics]
        readability_scores = [m.readability_score for m in all_metrics]
        
        analysis = {
            "sample_size": len(all_metrics),
            "complexity_stats": {
                "mean": statistics.mean(complexity_scores),
                "median": statistics.median(complexity_scores),
                "std_dev": statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                "min": min(complexity_scores),
                "max": max(complexity_scores),
                "danger_zone_count": sum(1 for score in complexity_scores if score > 5.0)
            },
            "token_stats": {
                "mean": statistics.mean(token_counts),
                "median": statistics.median(token_counts),
                "bloat_candidates": sum(1 for count in token_counts if count > 2000)
            },
            "readability_stats": {
                "mean": statistics.mean(readability_scores),
                "unreadable_count": sum(1 for score in readability_scores if score < 5.0)
            },
            "overall_health": "CRITICAL" if any(m.complexity_score > 8 for m in all_metrics) else "STABLE"
        }
        
        return analysis
    
    def generate_benchmark_report(self, metrics_list: List[CommandMetrics], analysis: Dict) -> Dict:
        """Generate comprehensive savage report"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Rank commands by various metrics
        ranked_by_complexity = sorted(metrics_list, key=lambda x: x.complexity_score, reverse=True)
        ranked_by_bloat = sorted(metrics_list, key=lambda x: x.token_count, reverse=True)
        
        report = {
            "timestamp": timestamp,
            "metadata": {
                "benchmarker_version": "1.0-SAVAGE",
                "total_commands_analyzed": len(metrics_list),
                "analysis_duration": sum(m.execution_time for m in metrics_list),
                "savage_mode": "ENABLED"
            },
            "statistical_analysis": analysis,
            "command_rankings": {
                "complexity_offenders": [
                    {
                        "name": m.name,
                        "score": m.complexity_score,
                        "savage_verdict": f"Complexity {m.complexity_score:.1f}/10 - " + m.savage_judgment
                    }
                    for m in ranked_by_complexity[:5]
                ],
                "token_bloat_champions": [
                    {
                        "name": m.name,
                        "tokens": m.token_count,
                        "efficiency_ratio": m.token_count / max(1, m.readability_score)
                    }
                    for m in ranked_by_bloat[:5]
                ]
            },
            "detailed_metrics": [
                {
                    "name": m.name,
                    "file_path": m.file_path,
                    "metrics": {
                        "complexity_score": m.complexity_score,
                        "token_count": m.token_count,
                        "line_count": m.line_count,
                        "readability_score": m.readability_score,
                        "composition_compatibility": m.composition_compatibility
                    },
                    "savage_judgment": m.savage_judgment,
                    "recommendation": self._generate_recommendation(m)
                }
                for m in metrics_list
            ],
            "savage_summary": self._generate_savage_summary(analysis, metrics_list)
        }
        
        return report
    
    def _generate_recommendation(self, metrics: CommandMetrics) -> str:
        """Evidence-based improvement recommendations"""
        if metrics.complexity_score > 7:
            return f"URGENT: Refactor immediately. Complexity {metrics.complexity_score:.1f} exceeds human comprehension limits."
        elif metrics.token_count > 2500:
            return f"Consider splitting into smaller commands. {metrics.token_count} tokens is approaching novella territory."
        elif metrics.readability_score < 5:
            return "Readability intervention needed. Current state requires a PhD in archaeology to understand."
        else:
            return "Acceptable quality. Minor optimizations could improve user experience."
    
    def _generate_savage_summary(self, analysis: Dict, metrics_list: List[CommandMetrics]) -> str:
        """Overall savage but fair assessment"""
        total_commands = len(metrics_list)
        danger_zone = analysis["complexity_stats"]["danger_zone_count"]
        bloated_count = analysis["token_stats"]["bloat_candidates"]
        unreadable_count = analysis["readability_stats"]["unreadable_count"]
        
        summary = f"SCIENTIFIC SAVAGE SUMMARY:\n\n"
        summary += f"Out of {total_commands} commands analyzed:\n"
        summary += f"- {danger_zone} commands ({danger_zone/total_commands*100:.1f}%) exceed complexity safety limits\n"
        summary += f"- {bloated_count} commands ({bloated_count/total_commands*100:.1f}%) suffer from token obesity\n"
        summary += f"- {unreadable_count} commands ({unreadable_count/total_commands*100:.1f}%) require translation services\n\n"
        
        if danger_zone > total_commands * 0.3:
            summary += "VERDICT: This command collection has more issues than a therapy group. "
            summary += "Immediate intervention required before someone gets hurt.\n\n"
        elif bloated_count > total_commands * 0.2:
            summary += "VERDICT: Moderate complexity debt detected. Like technical debt, but with more regret.\n\n"
        else:
            summary += "VERDICT: Surprisingly manageable. Someone actually read the documentation.\n\n"
        
        summary += f"Average complexity: {analysis['complexity_stats']['mean']:.2f} "
        summary += f"(σ={analysis['complexity_stats']['std_dev']:.2f})\n"
        summary += f"That's not 'intelligent automation', that's statistical chaos with delusions of grandeur."
        
        return summary

# Execution
if __name__ == "__main__":
    benchmarker = ScientificBenchmarker()
    
    # Get all command files
    command_files = [
        os.path.join(benchmarker.commands_dir, f)
        for f in os.listdir(benchmarker.commands_dir)
        if f.endswith('.md') and f != 'readme.md'
    ]
    
    # Randomly select 3 for detailed analysis
    selected_commands = random.sample(command_files, min(3, len(command_files)))
    
    print("🔬 SAVAGE COMMAND BENCHMARKER - Scientific Analysis Initiated")
    print(f"📊 Analyzing {len(selected_commands)} randomly selected commands...")
    
    # Benchmark each command
    all_metrics = []
    for cmd_file in selected_commands:
        print(f"⚡ Analyzing: {os.path.basename(cmd_file)}")
        metrics = benchmarker.benchmark_command(cmd_file)
        all_metrics.append(metrics)
    
    # Statistical analysis
    analysis = benchmarker.run_statistical_analysis(all_metrics)
    
    # Generate savage report
    report = benchmarker.generate_benchmark_report(all_metrics, analysis)
    
    # Save results
    report_file = f".github/benchmarks/results/{report['timestamp']}-savage-report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n🎯 SAVAGE ANALYSIS COMPLETE!")
    print(f"📄 Report saved to: {report_file}")
    print("\n" + report["savage_summary"])