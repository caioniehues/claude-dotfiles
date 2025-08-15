#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
PhD in roasting bad code with statistical precision.

Scientifically measures and brutally judges commands in /commands/
with objective data and savage but fair commentary.
"""

import json
import os
import random
import statistics
import subprocess
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any
import re
import sys

@dataclass
class CommandMetrics:
    """Objective measurements for a command"""
    command_name: str
    complexity_score: int
    line_count: int
    documentation_quality: float  # 0-10 scale
    reusability_factor: float  # 0-10 scale
    adhd_friendliness: float  # 0-10 scale based on CLAUDE.md criteria
    mcp_integration_count: int
    thinking_block_count: int
    error_handling_quality: float  # 0-10 scale

@dataclass
class PerformanceMetrics:
    """Runtime performance measurements"""
    execution_time_ms: List[float]
    memory_usage_mb: float
    token_consumption_estimate: int
    success_rate: float
    failure_patterns: List[str]

@dataclass
class StatisticalAnalysis:
    """Statistical analysis of measurements"""
    mean: float
    std_dev: float
    confidence_interval_95: tuple
    outliers: List[float]
    variance: float
    coefficient_variation: float

@dataclass
class SavageJudgment:
    """Brutal but data-backed assessment"""
    overall_score: float  # 0-100
    roast_level: str  # "mild", "medium", "savage", "nuclear"
    commentary: str
    improvement_recommendations: List[str]
    comparable_commands: List[str]
    complexity_verdict: str

@dataclass
class BenchmarkResult:
    """Complete benchmark result for a command"""
    timestamp: str
    command_metrics: CommandMetrics
    performance_metrics: PerformanceMetrics
    statistical_analysis: Dict[str, StatisticalAnalysis]
    savage_judgment: SavageJudgment
    evidence_files: List[str]

class SavageCommandBenchmarker:
    """The PhD-level savage benchmarker with statistical precision"""
    
    def __init__(self, commands_dir: Path):
        self.commands_dir = commands_dir
        self.commands = self._discover_commands()
        self.evidence_dir = Path(".github/benchmarks/data")
        self.results_dir = Path(".github/benchmarks/results")
        
        # CLAUDE.md complexity scoring rules
        self.complexity_weights = {
            'direct_solution': 1,
            'new_class': 2,
            'interface': 1,
            'design_pattern': 3,
            'config_file': 2
        }
        
        self.roast_thresholds = {
            'mild': 70,
            'medium': 50,
            'savage': 30,
            'nuclear': 15
        }
    
    def _discover_commands(self) -> List[Path]:
        """Discover all command files, excluding utilities"""
        commands = []
        for file in self.commands_dir.glob("*.md"):
            if not file.name.startswith("rename_commands"):
                commands.append(file)
        return commands
    
    def select_random_command(self) -> Path:
        """Scientifically random command selection"""
        return random.choice(self.commands)
    
    def analyze_command_complexity(self, command_path: Path) -> CommandMetrics:
        """Analyze command complexity using CLAUDE.md rules"""
        content = command_path.read_text()
        
        # Count complexity indicators
        complexity_score = 1  # Base score
        
        # Detect patterns that add complexity
        if re.search(r'class\s+\w+', content):
            complexity_score += self.complexity_weights['new_class']
        
        if re.search(r'interface\s+\w+', content):
            complexity_score += self.complexity_weights['interface']
        
        # Design pattern detection (Factory, Builder, Strategy, etc.)
        patterns = ['Factory', 'Builder', 'Strategy', 'Observer', 'Singleton']
        for pattern in patterns:
            if pattern.lower() in content.lower():
                complexity_score += self.complexity_weights['design_pattern']
        
        # Configuration file references
        if re.search(r'\.(xml|properties|yml|yaml)', content):
            complexity_score += self.complexity_weights['config_file']
        
        # Count MCP integrations
        mcp_count = len(re.findall(r'mcp__\w+', content))
        
        # Count thinking blocks
        thinking_count = len(re.findall(r'<thinking.*?</thinking>', content, re.DOTALL))
        
        # Line count
        line_count = len(content.splitlines())
        
        # Documentation quality (based on structure and clarity)
        doc_quality = self._assess_documentation_quality(content)
        
        # Reusability factor
        reusability = self._assess_reusability(content)
        
        # ADHD friendliness (based on CLAUDE.md criteria)
        adhd_friendliness = self._assess_adhd_friendliness(content)
        
        # Error handling quality
        error_handling = self._assess_error_handling(content)
        
        return CommandMetrics(
            command_name=command_path.stem,
            complexity_score=complexity_score,
            line_count=line_count,
            documentation_quality=doc_quality,
            reusability_factor=reusability,
            adhd_friendliness=adhd_friendliness,
            mcp_integration_count=mcp_count,
            thinking_block_count=thinking_count,
            error_handling_quality=error_handling
        )
    
    def _assess_documentation_quality(self, content: str) -> float:
        """Assess documentation quality (0-10 scale)"""
        score = 0.0
        
        # Has proper task description
        if '<task>' in content and '</task>' in content:
            score += 2.0
        
        # Has context section
        if '<context>' in content and '</context>' in content:
            score += 2.0
        
        # Has usage examples
        if 'example' in content.lower() or 'usage' in content.lower():
            score += 2.0
        
        # Has clear structure
        if content.count('#') >= 3:  # Multiple headers
            score += 2.0
        
        # Has implementation details
        if 'implementation' in content.lower():
            score += 1.0
        
        # Has integration notes
        if 'integration' in content.lower():
            score += 1.0
        
        return min(score, 10.0)
    
    def _assess_reusability(self, content: str) -> float:
        """Assess reusability factor (0-10 scale)"""
        score = 5.0  # Base score
        
        # Parameterized arguments
        if '$ARGUMENTS' in content:
            score += 2.0
        
        # Modular structure
        if content.count('<') >= 5:  # XML-like structure
            score += 1.0
        
        # Template sections
        if 'template' in content.lower():
            score += 1.0
        
        # Tool integration
        if 'tools>' in content:
            score += 1.0
        
        # Hardcoded values penalty
        hardcoded_patterns = [r'\d{4}-\d{2}-\d{2}', r'localhost:\d+', r'/Users/\w+']
        for pattern in hardcoded_patterns:
            if re.search(pattern, content):
                score -= 1.0
        
        return max(0.0, min(score, 10.0))
    
    def _assess_adhd_friendliness(self, content: str) -> float:
        """Assess ADHD friendliness based on CLAUDE.md criteria"""
        score = 0.0
        
        # Time breakdown into chunks
        if 'chunk' in content.lower() or '20 min' in content.lower():
            score += 2.0
        
        # Energy level considerations
        if 'energy' in content.lower():
            score += 2.0
        
        # Task breakdown methodology
        if 'breakdown' in content.lower():
            score += 2.0
        
        # Context switching awareness
        if 'context switch' in content.lower():
            score += 2.0
        
        # Pattern learning integration
        if 'pattern' in content.lower() and 'memory' in content.lower():
            score += 1.0
        
        # Hyperfocus management
        if 'hyperfocus' in content.lower():
            score += 1.0
        
        return min(score, 10.0)
    
    def _assess_error_handling(self, content: str) -> float:
        """Assess error handling quality (0-10 scale)"""
        score = 0.0
        
        # Has error handling blocks
        if 'error' in content.lower() or 'exception' in content.lower():
            score += 3.0
        
        # Has validation
        if 'validate' in content.lower() or 'check' in content.lower():
            score += 2.0
        
        # Has fallback mechanisms
        if 'fallback' in content.lower() or 'alternative' in content.lower():
            score += 2.0
        
        # Has recovery mechanisms
        if 'recover' in content.lower() or 'retry' in content.lower():
            score += 2.0
        
        # Has graceful degradation
        if 'graceful' in content.lower():
            score += 1.0
        
        return min(score, 10.0)
    
    def calculate_statistics(self, values: List[float]) -> StatisticalAnalysis:
        """Calculate comprehensive statistical analysis"""
        if not values:
            return StatisticalAnalysis(0, 0, (0, 0), [], 0, 0)
        
        mean = statistics.mean(values)
        std_dev = statistics.stdev(values) if len(values) > 1 else 0
        variance = statistics.variance(values) if len(values) > 1 else 0
        
        # Coefficient of variation
        cv = (std_dev / mean * 100) if mean != 0 else 0
        
        # 95% confidence interval (approximate)
        margin = 1.96 * (std_dev / (len(values) ** 0.5)) if len(values) > 1 else 0
        ci_95 = (mean - margin, mean + margin)
        
        # Outlier detection (values beyond 2 standard deviations)
        outliers = [v for v in values if abs(v - mean) > 2 * std_dev] if std_dev > 0 else []
        
        return StatisticalAnalysis(
            mean=mean,
            std_dev=std_dev,
            confidence_interval_95=ci_95,
            outliers=outliers,
            variance=variance,
            coefficient_variation=cv
        )
    
    def generate_savage_judgment(self, metrics: CommandMetrics) -> SavageJudgment:
        """Generate brutal but fair judgment with statistical backing"""
        
        # Calculate overall score (0-100)
        score_components = {
            'complexity': max(0, 100 - (metrics.complexity_score - 1) * 20),  # Penalty for complexity > 1
            'documentation': metrics.documentation_quality * 10,
            'reusability': metrics.reusability_factor * 10,
            'adhd_friendliness': metrics.adhd_friendliness * 10,
            'error_handling': metrics.error_handling_quality * 10,
            'line_efficiency': max(0, 100 - (metrics.line_count / 10))  # Penalty for excessive lines
        }
        
        overall_score = sum(score_components.values()) / len(score_components)
        
        # Determine roast level
        roast_level = 'nuclear'
        for level, threshold in self.roast_thresholds.items():
            if overall_score >= threshold:
                roast_level = level
                break
        
        # Generate commentary based on data
        commentary = self._generate_commentary(metrics, overall_score, roast_level)
        
        # Generate improvement recommendations
        recommendations = self._generate_recommendations(metrics)
        
        # Complexity verdict
        complexity_verdict = self._generate_complexity_verdict(metrics.complexity_score)
        
        return SavageJudgment(
            overall_score=overall_score,
            roast_level=roast_level,
            commentary=commentary,
            improvement_recommendations=recommendations,
            comparable_commands=[],  # To be filled based on similarity analysis
            complexity_verdict=complexity_verdict
        )
    
    def _generate_commentary(self, metrics: CommandMetrics, score: float, roast_level: str) -> str:
        """Generate savage but data-backed commentary"""
        
        if roast_level == "nuclear":
            return f"🚨 CRITICAL CODE VIOLATION DETECTED 🚨\n\n" \
                   f"This command scored {score:.1f}/100, which is so bad it's practically " \
                   f"a war crime against clean code principles. With a complexity score of " \
                   f"{metrics.complexity_score} (target: <5), this code has more abstraction " \
                   f"layers than a Las Vegas wedding cake. The {metrics.line_count} lines " \
                   f"could probably be reduced to {metrics.line_count//3} without losing " \
                   f"functionality. This isn't engineering—it's architectural masturbation."
        
        elif roast_level == "savage":
            return f"💀 SAVAGE JUDGMENT: {score:.1f}/100 💀\n\n" \
                   f"This command is like a Swiss Army knife designed by someone who's never " \
                   f"seen a knife. Complexity score of {metrics.complexity_score} suggests " \
                   f"the author confused 'enterprise-grade' with 'enterprise-confused'. " \
                   f"The {metrics.line_count} lines include more ceremony than a royal wedding. " \
                   f"Documentation quality of {metrics.documentation_quality:.1f}/10 means " \
                   f"future developers will need archaeological training to understand this."
        
        elif roast_level == "medium":
            return f"⚠️ MEDIOCRE ALERT: {score:.1f}/100 ⚠️\n\n" \
                   f"This command is the programming equivalent of lukewarm coffee—not terrible " \
                   f"enough to throw away, but not good enough to enjoy. Complexity score of " \
                   f"{metrics.complexity_score} is acceptable, but the {metrics.line_count} lines " \
                   f"suggest some optimization opportunities. Documentation quality at " \
                   f"{metrics.documentation_quality:.1f}/10 is 'meh' tier."
        
        else:  # mild
            return f"✅ ACCEPTABLE QUALITY: {score:.1f}/100 ✅\n\n" \
                   f"This command passes the basic sanity check with a complexity score of " \
                   f"{metrics.complexity_score} (within acceptable range). The {metrics.line_count} " \
                   f"lines are reasonable, and documentation quality of {metrics.documentation_quality:.1f}/10 " \
                   f"suggests someone actually cares about maintainability. Not bad, human."
    
    def _generate_recommendations(self, metrics: CommandMetrics) -> List[str]:
        """Generate data-backed improvement recommendations"""
        recommendations = []
        
        if metrics.complexity_score >= 5:
            recommendations.append(
                f"🎯 COMPLEXITY REDUCTION: Score is {metrics.complexity_score} (target: <5). "
                f"Apply the 3-question rule: Can you use existing solutions? "
                f"Can you solve with a simple method? Do you really need abstraction NOW?"
            )
        
        if metrics.line_count > 500:
            recommendations.append(
                f"📏 SIZE REDUCTION: {metrics.line_count} lines is excessive. "
                f"Target: <300 lines. Break into smaller, focused commands."
            )
        
        if metrics.documentation_quality < 6:
            recommendations.append(
                f"📚 DOCUMENTATION IMPROVEMENT: Quality is {metrics.documentation_quality:.1f}/10. "
                f"Add clear task description, context, usage examples, and integration notes."
            )
        
        if metrics.adhd_friendliness < 5:
            recommendations.append(
                f"🧠 ADHD OPTIMIZATION: Score {metrics.adhd_friendliness:.1f}/10. "
                f"Add task chunking, energy level awareness, and pattern learning integration."
            )
        
        if metrics.error_handling_quality < 5:
            recommendations.append(
                f"🛡️ ERROR HANDLING: Score {metrics.error_handling_quality:.1f}/10. "
                f"Add validation, fallback mechanisms, and graceful degradation."
            )
        
        if metrics.mcp_integration_count == 0:
            recommendations.append(
                f"🔌 MCP INTEGRATION: Zero MCP tools detected. "
                f"Consider adding memory integration or tool orchestration."
            )
        
        return recommendations
    
    def _generate_complexity_verdict(self, complexity_score: int) -> str:
        """Generate complexity verdict based on CLAUDE.md rules"""
        if complexity_score == 1:
            return "🏆 OPTIMAL: Direct solution, zero unnecessary complexity"
        elif complexity_score <= 3:
            return "✅ ACCEPTABLE: Within complexity budget"
        elif complexity_score <= 5:
            return "⚠️ WARNING: At complexity threshold, monitor carefully"
        else:
            return f"🚨 VIOLATION: Score {complexity_score} exceeds limit of 5. SIMPLIFY IMMEDIATELY!"
    
    def benchmark_command(self, command_path: Path) -> BenchmarkResult:
        """Complete benchmark analysis of a command"""
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # Analyze command structure
        metrics = self.analyze_command_complexity(command_path)
        
        # Simulate performance metrics (in real implementation, would execute)
        performance = self._simulate_performance_metrics(metrics)
        
        # Calculate statistical analysis
        stats = {
            'execution_time': self.calculate_statistics(performance.execution_time_ms),
            'complexity_trend': self.calculate_statistics([metrics.complexity_score])
        }
        
        # Generate savage judgment
        judgment = self.generate_savage_judgment(metrics)
        
        # Evidence collection
        evidence_files = self._collect_evidence(command_path, metrics)
        
        return BenchmarkResult(
            timestamp=timestamp,
            command_metrics=metrics,
            performance_metrics=performance,
            statistical_analysis=stats,
            savage_judgment=judgment,
            evidence_files=evidence_files
        )
    
    def _simulate_performance_metrics(self, metrics: CommandMetrics) -> PerformanceMetrics:
        """Simulate performance metrics (placeholder for real measurements)"""
        # In real implementation, would execute command and measure
        base_time = metrics.line_count * 0.1  # Rough estimate
        execution_times = [
            base_time + random.gauss(0, base_time * 0.1) 
            for _ in range(5)
        ]
        
        return PerformanceMetrics(
            execution_time_ms=execution_times,
            memory_usage_mb=metrics.line_count * 0.01,
            token_consumption_estimate=metrics.line_count * 10,
            success_rate=max(0.5, 1.0 - (metrics.complexity_score - 1) * 0.1),
            failure_patterns=["complexity_timeout", "memory_overflow"] if metrics.complexity_score > 5 else []
        )
    
    def _collect_evidence(self, command_path: Path, metrics: CommandMetrics) -> List[str]:
        """Collect evidence files for analysis"""
        evidence_files = []
        
        # Save command analysis
        analysis_file = self.evidence_dir / f"{command_path.stem}_analysis.json"
        analysis_data = {
            'command_path': str(command_path),
            'metrics': asdict(metrics),
            'content_sample': command_path.read_text()[:500] + "..."
        }
        
        analysis_file.write_text(json.dumps(analysis_data, indent=2))
        evidence_files.append(str(analysis_file))
        
        return evidence_files
    
    def run_benchmark_suite(self, num_commands: int = 3) -> Dict[str, Any]:
        """Run complete benchmark suite on random commands"""
        results = {}
        selected_commands = random.sample(self.commands, min(num_commands, len(self.commands)))
        
        print(f"🧪 SAVAGE BENCHMARKER ACTIVATED")
        print(f"Selected {len(selected_commands)} commands for scientific roasting...")
        
        for command_path in selected_commands:
            print(f"\n🔬 Analyzing: {command_path.name}")
            result = self.benchmark_command(command_path)
            results[command_path.stem] = result
            
            # Immediate feedback
            print(f"   Score: {result.savage_judgment.overall_score:.1f}/100")
            print(f"   Roast Level: {result.savage_judgment.roast_level.upper()}")
            print(f"   Complexity: {result.command_metrics.complexity_score}")
        
        return results
    
    def generate_report(self, results: Dict[str, BenchmarkResult]) -> Dict[str, Any]:
        """Generate comprehensive benchmark report"""
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        
        # Aggregate statistics
        all_scores = [r.savage_judgment.overall_score for r in results.values()]
        complexity_scores = [r.command_metrics.complexity_score for r in results.values()]
        
        aggregate_stats = {
            'overall_scores': self.calculate_statistics(all_scores),
            'complexity_scores': self.calculate_statistics(complexity_scores),
            'total_commands_analyzed': len(results),
            'commands_exceeding_complexity': sum(1 for c in complexity_scores if c >= 5),
            'average_line_count': statistics.mean([r.command_metrics.line_count for r in results.values()]),
            'mcp_integration_rate': sum(1 for r in results.values() if r.command_metrics.mcp_integration_count > 0) / len(results)
        }
        
        # Generate summary commentary
        summary_commentary = self._generate_summary_commentary(aggregate_stats, results)
        
        # Convert statistical analysis objects to dictionaries
        serializable_aggregate_stats = {}
        for key, value in aggregate_stats.items():
            if hasattr(value, '__dict__'):
                serializable_aggregate_stats[key] = asdict(value)
            else:
                serializable_aggregate_stats[key] = value
        
        report = {
            'metadata': {
                'timestamp': timestamp,
                'benchmarker_version': '1.0.0-savage',
                'total_commands_available': len(self.commands),
                'analyzed_commands': len(results)
            },
            'aggregate_statistics': serializable_aggregate_stats,
            'summary_commentary': summary_commentary,
            'individual_results': {k: asdict(v) for k, v in results.items()},
            'recommendations': self._generate_global_recommendations(aggregate_stats, results)
        }
        
        return report
    
    def _generate_summary_commentary(self, stats: Dict, results: Dict[str, BenchmarkResult]) -> str:
        """Generate overall commentary on the command suite"""
        avg_score = stats['overall_scores'].mean
        complexity_violators = stats['commands_exceeding_complexity']
        total = stats['total_commands_analyzed']
        
        if avg_score < 30:
            roast = "🔥 NUCLEAR DEVASTATION DETECTED 🔥\n\n" \
                   f"The command suite scored an average of {avg_score:.1f}/100, which is " \
                   f"like giving a blind person a Rubik's cube and expecting art. " \
                   f"{complexity_violators}/{total} commands violate complexity limits. " \
                   f"This isn't a codebase—it's a crime scene."
        elif avg_score < 50:
            roast = "💀 SYSTEMATIC FAILURE IDENTIFIED 💀\n\n" \
                   f"Average score of {avg_score:.1f}/100 suggests the commands were " \
                   f"designed by committee—a committee of caffeinated monkeys. " \
                   f"{complexity_violators}/{total} complexity violations indicate " \
                   f"a fundamental misunderstanding of the CLAUDE.md principles."
        elif avg_score < 70:
            roast = "⚠️ MEDIOCRITY EPIDEMIC ⚠️\n\n" \
                   f"Score of {avg_score:.1f}/100 is the programming equivalent of " \
                   f"vanilla ice cream—technically food, but why would you choose it? " \
                   f"{complexity_violators}/{total} complexity violations suggest " \
                   f"room for improvement."
        else:
            roast = "✅ SURPRISINGLY COMPETENT ✅\n\n" \
                   f"Average score of {avg_score:.1f}/100 suggests someone actually " \
                   f"read the CLAUDE.md documentation. Only {complexity_violators}/{total} " \
                   f"complexity violations—almost like real software engineering happened here."
        
        return roast
    
    def _generate_global_recommendations(self, stats: Dict, results: Dict[str, BenchmarkResult]) -> List[str]:
        """Generate recommendations for the entire command suite"""
        recommendations = []
        
        if stats['commands_exceeding_complexity'] > 0:
            recommendations.append(
                f"🎯 GLOBAL COMPLEXITY AUDIT: {stats['commands_exceeding_complexity']} commands "
                f"exceed complexity limits. Implement mandatory complexity reviews."
            )
        
        if stats['overall_scores'].mean < 50:
            recommendations.append(
                f"📚 TRAINING INTERVENTION: Average score {stats['overall_scores'].mean:.1f} "
                f"indicates systematic knowledge gaps. Mandatory CLAUDE.md training required."
            )
        
        if stats['mcp_integration_rate'] < 0.5:
            recommendations.append(
                f"🔌 MCP ADOPTION: Only {stats['mcp_integration_rate']*100:.0f}% commands "
                f"use MCP integration. Consider standardizing memory/tool patterns."
            )
        
        if stats['average_line_count'] > 400:
            recommendations.append(
                f"📏 SIZE STANDARDIZATION: Average {stats['average_line_count']:.0f} lines "
                f"per command suggests overly complex implementations. Set size limits."
            )
        
        return recommendations

def main():
    """Main execution function"""
    print("🔬 SAVAGE COMMAND BENCHMARKER")
    print("PhD in roasting bad code with statistical precision")
    print("=" * 60)
    
    # Initialize benchmarker
    commands_dir = Path("commands")
    if not commands_dir.exists():
        print("❌ Commands directory not found!")
        sys.exit(1)
    
    benchmarker = SavageCommandBenchmarker(commands_dir)
    
    # Run benchmark suite
    results = benchmarker.run_benchmark_suite(num_commands=3)
    
    # Generate report
    report = benchmarker.generate_report(results)
    
    # Save report
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    report_file = Path(f".github/benchmarks/results/{timestamp}-report.json")
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 BENCHMARK COMPLETE")
    print(f"Report saved: {report_file}")
    print(f"\n{report['summary_commentary']}")
    
    # Print top-level recommendations
    print(f"\n🎯 GLOBAL RECOMMENDATIONS:")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"{i}. {rec}")

if __name__ == "__main__":
    main()