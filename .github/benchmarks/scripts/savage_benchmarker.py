#!/usr/bin/env python3
"""
🔬 SAVAGE COMMAND BENCHMARKER - PhD Edition
Statistical rigor meets brutal honesty in command analysis

Dr. Savage McBenchmark, PhD in Computational Roasting
"""

import json
import time
import random
import statistics
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass

@dataclass
class CommandMetrics:
    """Statistical measurements for command performance"""
    name: str
    word_count: int
    line_count: int
    character_count: int
    complexity_score: int
    instruction_density: float
    code_block_ratio: float
    abstraction_level: int
    readability_score: float
    maintainability_issues: List[str]
    anti_patterns: List[str]
    bloat_indicators: List[str]

class SavageBenchmarker:
    """PhD-level command analysis with statistical rigor"""
    
    def __init__(self):
        self.commands_dir = Path("commands")
        self.results = {}
        self.raw_metrics = []
        
        # ADHD Time multipliers from CLAUDE.md standards
        self.adhd_multipliers = {
            "base": 1.5,
            "perfectionism": 1.3,
            "task_switching": 1.25
        }
        
        # Complexity scoring based on CLAUDE.md rules
        self.complexity_weights = {
            "class": 2,
            "interface": 1,
            "pattern": 3,
            "factory": 3,
            "builder": 3,
            "strategy": 3,
            "config": 2,
            "abstract": 2
        }

    def calculate_complexity_score(self, content: str) -> Tuple[int, List[str]]:
        """Calculate complexity score using CLAUDE.md standards"""
        score = 1  # Base implementation
        violations = []
        
        content_lower = content.lower()
        
        for term, weight in self.complexity_weights.items():
            count = content_lower.count(term)
            score += count * weight
            if count > 0:
                violations.append(f"{count} instances of '{term}' (+{count * weight} complexity)")
        
        # Additional complexity indicators
        if content_lower.count("inheritance") > 0:
            score += 2
            violations.append("Inheritance detected (+2 complexity)")
        
        if content_lower.count("dependency injection") > 1:
            score += 1
            violations.append("Multiple DI references (+1 complexity)")
            
        return score, violations

    def detect_anti_patterns(self, content: str) -> List[str]:
        """Detect anti-patterns that violate clean code principles"""
        anti_patterns = []
        content_lower = content.lower()
        
        # Factory madness
        if "factory" in content_lower and "builder" in content_lower:
            anti_patterns.append("Factory + Builder combo detected - architectural obesity alert!")
        
        # Premature abstraction
        abstract_count = content_lower.count("interface") + content_lower.count("abstract")
        if abstract_count > 2:
            anti_patterns.append(f"Abstraction overload: {abstract_count} abstractions for unknown implementations")
        
        # Exception swallowing
        if "catch" in content_lower and ("return null" in content_lower or "ignore" in content_lower):
            anti_patterns.append("Exception swallowing detected - hiding failures like a Windows error dialog")
        
        # Verbose naming
        if re.search(r'\b\w{20,}\b', content):
            anti_patterns.append("Hungarian notation survivors detected - names longer than German compound words")
        
        # Wildcard imports (Java)
        if "import.*" in content or "import com.example.*" in content:
            anti_patterns.append("Wildcard imports - the coding equivalent of 'sure, whatever'")
        
        return anti_patterns

    def detect_bloat_indicators(self, content: str) -> List[str]:
        """Detect bloat that violates simplicity principles"""
        bloat = []
        
        # Word count analysis
        word_count = len(content.split())
        if word_count > 500:
            bloat.append(f"Verbal diarrhea: {word_count} words (optimal: <300)")
        
        # Instruction density
        instructions = content.count("- ") + content.count("1. ") + content.count("2. ")
        if instructions > 20:
            bloat.append(f"Instruction overload: {instructions} steps (IKEA manual complexity)")
        
        # Code block ratio
        code_blocks = content.count("```")
        if code_blocks > 10:
            bloat.append(f"Code block spam: {code_blocks // 2} examples (quantity ≠ quality)")
        
        # Nested thinking blocks
        thinking_blocks = content.count("<thinking") + content.count("<reasoning")
        if thinking_blocks > 5:
            bloat.append(f"Meta-cognition recursion: {thinking_blocks} thinking blocks (inception syndrome)")
        
        return bloat

    def calculate_readability_score(self, content: str) -> float:
        """Calculate readability based on structure and clarity"""
        score = 10.0  # Start with perfect score
        
        # Penalize complexity
        complexity, _ = self.calculate_complexity_score(content)
        score -= min(complexity * 0.5, 5.0)
        
        # Reward structure
        headers = content.count("#")
        if headers > 0:
            score += min(headers * 0.2, 2.0)
        
        # Penalize excessive length
        word_count = len(content.split())
        if word_count > 300:
            score -= (word_count - 300) * 0.005
        
        # Penalize bloat
        bloat_indicators = self.detect_bloat_indicators(content)
        score -= len(bloat_indicators) * 0.8
        
        return max(0.0, min(10.0, score))

    def analyze_command(self, command_path: Path) -> CommandMetrics:
        """Perform comprehensive analysis of a single command"""
        with open(command_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        complexity_score, complexity_violations = self.calculate_complexity_score(content)
        anti_patterns = self.detect_anti_patterns(content)
        bloat_indicators = self.detect_bloat_indicators(content)
        readability_score = self.calculate_readability_score(content)
        
        # Calculate metrics
        word_count = len(content.split())
        line_count = len(content.splitlines())
        character_count = len(content)
        
        instructions = content.count("- ") + content.count("1. ") + content.count("2. ")
        instruction_density = instructions / word_count if word_count > 0 else 0
        
        code_blocks = content.count("```")
        code_block_ratio = (code_blocks // 2) / line_count if line_count > 0 else 0
        
        # Determine abstraction level
        abstraction_level = 1
        if "interface" in content.lower():
            abstraction_level += 1
        if "abstract" in content.lower():
            abstraction_level += 1
        if "pattern" in content.lower():
            abstraction_level += 2
        
        return CommandMetrics(
            name=command_path.name,
            word_count=word_count,
            line_count=line_count,
            character_count=character_count,
            complexity_score=complexity_score,
            instruction_density=instruction_density,
            code_block_ratio=code_block_ratio,
            abstraction_level=abstraction_level,
            readability_score=readability_score,
            maintainability_issues=complexity_violations,
            anti_patterns=anti_patterns,
            bloat_indicators=bloat_indicators
        )

    def generate_savage_judgment(self, metrics: CommandMetrics) -> Dict[str, Any]:
        """Generate brutally honest but data-backed judgment"""
        judgments = []
        severity_score = 0
        
        # Complexity violations
        if metrics.complexity_score >= 5:
            judgments.append(f"Complexity score of {metrics.complexity_score}/5 violates the sacred CLAUDE.md rule. "
                           f"This isn't architecture, it's architectural obesity requiring liposuction.")
            severity_score += 3
        
        # Word count violations
        if metrics.word_count > 500:
            judgments.append(f"At {metrics.word_count} words, this command has more bloat than a Windows Vista install. "
                           f"Brevity is the soul of wit, verbosity is the soul of confusion.")
            severity_score += 2
        
        # Anti-pattern detection
        if metrics.anti_patterns:
            judgments.append(f"Anti-patterns detected: {len(metrics.anti_patterns)} violations of clean code. "
                           f"This code doesn't just smell, it reeks like a fish market in July.")
            severity_score += len(metrics.anti_patterns)
        
        # Bloat indicators
        if metrics.bloat_indicators:
            judgments.append(f"Bloat indicators: {len(metrics.bloat_indicators)} signs of code obesity. "
                           f"This command needs a diet plan, not more features.")
            severity_score += 1
        
        # Readability issues
        if metrics.readability_score < 5.0:
            judgments.append(f"Readability score of {metrics.readability_score:.1f}/10 suggests this was written "
                           f"by a committee of caffeinated interns with a thesaurus addiction.")
            severity_score += 2
        
        # Positive feedback when deserved
        if not judgments:
            judgments.append("Surprisingly, this command doesn't make me question my life choices. "
                           "Well done - it's simple, clear, and respects the reader's time.")
            severity_score = 0
        
        # Overall assessment
        if severity_score == 0:
            overall = "EXCELLENT - Actually follows principles"
        elif severity_score <= 3:
            overall = "ACCEPTABLE - Minor improvements needed"
        elif severity_score <= 6:
            overall = "PROBLEMATIC - Major refactoring required"
        else:
            overall = "CATASTROPHIC - Restart from scratch recommended"
        
        return {
            "judgments": judgments,
            "severity_score": severity_score,
            "overall_assessment": overall,
            "recommendations": self.generate_recommendations(metrics)
        }

    def generate_recommendations(self, metrics: CommandMetrics) -> List[str]:
        """Generate specific, actionable recommendations"""
        recommendations = []
        
        if metrics.complexity_score >= 5:
            recommendations.append(f"CRITICAL: Reduce complexity from {metrics.complexity_score} to <5. "
                                 f"Apply the 3-Question Rule from CLAUDE.md")
        
        if metrics.word_count > 500:
            recommendations.append(f"Cut {metrics.word_count - 300} words. Every word should earn its place or get deleted.")
        
        if metrics.instruction_density > 0.1:
            recommendations.append("Reduce instruction density. Replace steps with clear outcomes.")
        
        if metrics.anti_patterns:
            recommendations.append("Eliminate anti-patterns: " + ", ".join(metrics.anti_patterns[:3]))
        
        if metrics.readability_score < 7.0:
            recommendations.append("Improve readability: use headers, bullets, shorter sentences")
        
        return recommendations

    def calculate_statistical_analysis(self, all_metrics: List[CommandMetrics]) -> Dict[str, Any]:
        """Perform statistical analysis across all commands"""
        if not all_metrics:
            return {}
        
        # Extract numeric values for statistics
        complexity_scores = [m.complexity_score for m in all_metrics]
        word_counts = [m.word_count for m in all_metrics]
        readability_scores = [m.readability_score for m in all_metrics]
        
        return {
            "sample_size": len(all_metrics),
            "complexity_stats": {
                "mean": statistics.mean(complexity_scores),
                "median": statistics.median(complexity_scores),
                "stdev": statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                "max": max(complexity_scores),
                "violations": len([s for s in complexity_scores if s >= 5])
            },
            "word_count_stats": {
                "mean": statistics.mean(word_counts),
                "median": statistics.median(word_counts),
                "stdev": statistics.stdev(word_counts) if len(word_counts) > 1 else 0,
                "bloated_commands": len([w for w in word_counts if w > 500])
            },
            "readability_stats": {
                "mean": statistics.mean(readability_scores),
                "median": statistics.median(readability_scores),
                "stdev": statistics.stdev(readability_scores) if len(readability_scores) > 1 else 0,
                "poor_readability": len([r for r in readability_scores if r < 5.0])
            }
        }

    def run_benchmark(self, selected_commands: List[str] = None) -> Dict[str, Any]:
        """Execute the complete benchmarking suite"""
        print("🔬 SAVAGE COMMAND BENCHMARKER - PhD Edition")
        print("=" * 60)
        print("Statistical rigor meets brutal honesty in command analysis")
        print("Dr. Savage McBenchmark, PhD in Computational Roasting")
        print("=" * 60)
        
        # Select commands to analyze
        if not selected_commands:
            all_commands = list(self.commands_dir.glob("*.md"))
            selected_commands = [cmd.name for cmd in random.sample(all_commands, min(5, len(all_commands)))]
        
        print(f"\n📊 Analyzing {len(selected_commands)} randomly selected commands...")
        
        all_metrics = []
        command_results = {}
        
        for cmd_name in selected_commands:
            cmd_path = self.commands_dir / cmd_name
            if not cmd_path.exists():
                print(f"❌ Command not found: {cmd_name}")
                continue
            
            print(f"\n🔍 Analyzing: {cmd_name}")
            
            # Analyze command
            metrics = self.analyze_command(cmd_path)
            all_metrics.append(metrics)
            
            # Generate savage judgment
            judgment = self.generate_savage_judgment(metrics)
            
            command_results[cmd_name] = {
                "metrics": {
                    "word_count": metrics.word_count,
                    "line_count": metrics.line_count,
                    "complexity_score": metrics.complexity_score,
                    "readability_score": metrics.readability_score,
                    "instruction_density": metrics.instruction_density,
                    "code_block_ratio": metrics.code_block_ratio,
                    "abstraction_level": metrics.abstraction_level
                },
                "quality_assessment": judgment,
                "maintainability_issues": metrics.maintainability_issues,
                "anti_patterns": metrics.anti_patterns,
                "bloat_indicators": metrics.bloat_indicators
            }
            
            # Print quick summary
            print(f"   Complexity: {metrics.complexity_score}/5 {'❌' if metrics.complexity_score >= 5 else '✅'}")
            print(f"   Words: {metrics.word_count} {'❌' if metrics.word_count > 500 else '✅'}")
            print(f"   Readability: {metrics.readability_score:.1f}/10")
            print(f"   Assessment: {judgment['overall_assessment']}")
        
        # Statistical analysis
        stats = self.calculate_statistical_analysis(all_metrics)
        
        # Compile results
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        results = {
            "benchmark_metadata": {
                "timestamp": timestamp,
                "version": "1.0-PhD-Edition",
                "methodology": "Random sampling with statistical rigor and savage judgment",
                "standards_reference": "CLAUDE.md clean code principles",
                "analyzer": "Dr. Savage McBenchmark, PhD"
            },
            "statistical_analysis": stats,
            "command_analysis": command_results,
            "overall_findings": self.generate_overall_findings(stats, all_metrics)
        }
        
        # Save results
        output_file = f".github/benchmarks/results/{timestamp}-savage-report.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n📊 Savage analysis complete! Results saved to {output_file}")
        return results

    def generate_overall_findings(self, stats: Dict, metrics: List[CommandMetrics]) -> Dict[str, Any]:
        """Generate overall findings and recommendations"""
        findings = {
            "summary": "",
            "critical_issues": [],
            "trends": [],
            "recommendations": []
        }
        
        if not stats:
            return findings
        
        complexity_violations = stats["complexity_stats"]["violations"]
        bloated_commands = stats["word_count_stats"]["bloated_commands"]
        poor_readability = stats["readability_stats"]["poor_readability"]
        
        # Summary
        total_commands = stats["sample_size"]
        issues_found = complexity_violations + bloated_commands + poor_readability
        
        if issues_found == 0:
            findings["summary"] = f"Miraculously, all {total_commands} commands pass basic quality standards. Someone actually read CLAUDE.md!"
        elif issues_found <= total_commands * 0.3:
            findings["summary"] = f"Generally acceptable quality with {issues_found} issues across {total_commands} commands. Room for improvement exists."
        else:
            findings["summary"] = f"Houston, we have a problem. {issues_found} quality violations across {total_commands} commands. Time for intervention."
        
        # Critical issues
        if complexity_violations > 0:
            findings["critical_issues"].append(f"{complexity_violations} commands violate complexity limits (≥5). Immediate refactoring required.")
        
        if bloated_commands > 0:
            findings["critical_issues"].append(f"{bloated_commands} commands exceed 500-word limit. Verbal obesity epidemic detected.")
        
        if poor_readability > total_commands * 0.5:
            findings["critical_issues"].append(f"{poor_readability} commands have poor readability (<5.0). Clarity crisis.")
        
        # Recommendations
        findings["recommendations"] = [
            "Apply the 3-Question Rule before adding complexity",
            "Enforce 300-word limit for command descriptions",
            "Use complexity scoring in code reviews",
            "Regular audits using this benchmarking tool",
            "Training on CLAUDE.md clean code principles"
        ]
        
        return findings

def main():
    """Run the savage benchmarking suite"""
    benchmarker = SavageBenchmarker()
    
    # Randomly select 5 commands for this benchmark
    random.seed(42)  # For reproducible results
    selected = [
        "ultrathink.md",
        "java-test-driven-development.md", 
        "adhd-task-breakdown.md",
        "intelligent-code-enhancer.md",
        "senior-developer-analysis.md"
    ]
    
    results = benchmarker.run_benchmark(selected)
    return results

if __name__ == "__main__":
    main()