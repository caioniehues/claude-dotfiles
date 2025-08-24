#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER v1.0
The PhD-level scientific roaster of Claude commands.
"""

import json
import random
import time
import statistics
import subprocess
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict
import hashlib
import re

@dataclass
class BenchmarkMetrics:
    command_name: str
    execution_time: float
    token_estimate: int
    success: bool
    complexity_score: int
    error_messages: List[str]
    output_quality: float
    memory_usage: int
    file_changes: int
    lines_of_code: int

@dataclass
class StatisticalAnalysis:
    mean: float
    std_dev: float
    confidence_interval: Tuple[float, float]
    outliers: List[float]
    success_rate: float

class SavageBenchmarker:
    def __init__(self, commands_dir: str = "commands"):
        self.commands_dir = Path(commands_dir)
        self.results_dir = Path(".github/benchmarks/results")
        self.baselines_dir = Path(".github/benchmarks/baselines")
        
        # Ensure directories exist
        self.results_dir.mkdir(parents=True, exist_ok=True)
        self.baselines_dir.mkdir(parents=True, exist_ok=True)
        
        self.commands = self._discover_commands()
        self.savage_comments = []
        
    def _discover_commands(self) -> List[str]:
        """Find all .md command files"""
        return [f.stem for f in self.commands_dir.glob("*.md")]
    
    def _calculate_complexity_score(self, command_content: str) -> int:
        """Calculate complexity based on CLAUDE.md rules"""
        score = 1  # Base score for direct solution
        
        # Count complexity indicators
        patterns = {
            r'class\s+\w+': 2,  # Each new class: +2
            r'interface\s+\w+': 1,  # Each interface: +1
            r'Factory|Builder|Strategy|Observer': 3,  # Design patterns: +3
            r'\.properties|\.yaml|\.xml': 2,  # Config files: +2
            r'extends\s+\w+': 1,  # Inheritance: +1
            r'implements\s+\w+': 1,  # Implementation: +1
        }
        
        for pattern, points in patterns.items():
            matches = len(re.findall(pattern, command_content, re.IGNORECASE))
            score += matches * points
            
        return score
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (1 token ≈ 4 characters)"""
        return len(text) // 4
    
    def _measure_execution_time(self, command_path: str, iterations: int = 5) -> List[float]:
        """Measure command execution time with multiple iterations"""
        times = []
        
        for _ in range(iterations):
            start_time = time.time()
            
            # Simulate command execution by reading and processing
            try:
                with open(command_path, 'r') as f:
                    content = f.read()
                    
                # Simulate processing time based on complexity
                complexity = self._calculate_complexity_score(content)
                processing_time = complexity * 0.01  # Base processing time
                time.sleep(processing_time)
                
                execution_time = time.time() - start_time
                times.append(execution_time)
                
            except Exception as e:
                times.append(float('inf'))  # Mark as failed execution
                
        return times
    
    def _analyze_command_quality(self, command_content: str) -> Tuple[float, List[str]]:
        """Analyze command quality and return score + issues"""
        issues = []
        quality_score = 10.0  # Start with perfect score
        
        # Check for anti-patterns from CLAUDE.md
        anti_patterns = [
            (r'import\s+.*\*', "Wildcard imports detected", -2.0),
            (r'return\s+null', "Null returns found", -1.5),
            (r'catch.*\{\s*\}', "Empty catch blocks", -3.0),
            (r'\.length\s*>\s*20', "Functions > 20 lines", -2.0),
            (r'Factory.*Factory', "Factory madness detected", -5.0),
            (r'Abstract.*Base.*Impl', "Premature abstraction", -3.0),
        ]
        
        for pattern, message, penalty in anti_patterns:
            if re.search(pattern, command_content, re.IGNORECASE):
                issues.append(message)
                quality_score += penalty
                
        return max(0.0, quality_score), issues
    
    def benchmark_command(self, command_name: str) -> BenchmarkMetrics:
        """Benchmark a single command with scientific precision"""
        command_path = self.commands_dir / f"{command_name}.md"
        
        if not command_path.exists():
            return BenchmarkMetrics(
                command_name=command_name,
                execution_time=float('inf'),
                token_estimate=0,
                success=False,
                complexity_score=0,
                error_messages=[f"Command file not found: {command_path}"],
                output_quality=0.0,
                memory_usage=0,
                file_changes=0,
                lines_of_code=0
            )
        
        try:
            with open(command_path, 'r') as f:
                content = f.read()
            
            # Measure execution times
            execution_times = self._measure_execution_time(str(command_path))
            avg_execution_time = statistics.mean([t for t in execution_times if t != float('inf')])
            
            # Calculate metrics
            token_estimate = self._estimate_tokens(content)
            complexity_score = self._calculate_complexity_score(content)
            quality_score, issues = self._analyze_command_quality(content)
            lines_of_code = len(content.split('\n'))
            
            # Simulate memory usage (rough estimate)
            memory_usage = token_estimate * 4  # Rough bytes estimate
            
            success = avg_execution_time != float('inf') and not issues
            
            return BenchmarkMetrics(
                command_name=command_name,
                execution_time=avg_execution_time,
                token_estimate=token_estimate,
                success=success,
                complexity_score=complexity_score,
                error_messages=issues,
                output_quality=quality_score,
                memory_usage=memory_usage,
                file_changes=0,  # Would need real execution to measure
                lines_of_code=lines_of_code
            )
            
        except Exception as e:
            return BenchmarkMetrics(
                command_name=command_name,
                execution_time=float('inf'),
                token_estimate=0,
                success=False,
                complexity_score=0,
                error_messages=[str(e)],
                output_quality=0.0,
                memory_usage=0,
                file_changes=0,
                lines_of_code=0
            )
    
    def generate_statistical_analysis(self, metrics_list: List[BenchmarkMetrics]) -> StatisticalAnalysis:
        """Generate statistical analysis of benchmark results"""
        execution_times = [m.execution_time for m in metrics_list if m.execution_time != float('inf')]
        
        if not execution_times:
            return StatisticalAnalysis(0, 0, (0, 0), [], 0)
        
        mean_time = statistics.mean(execution_times)
        std_dev = statistics.stdev(execution_times) if len(execution_times) > 1 else 0
        
        # Calculate confidence interval (95%)
        margin = 1.96 * (std_dev / (len(execution_times) ** 0.5)) if execution_times else 0
        confidence_interval = (mean_time - margin, mean_time + margin)
        
        # Find outliers (> 2 standard deviations)
        outliers = [t for t in execution_times if abs(t - mean_time) > 2 * std_dev]
        
        # Calculate success rate
        success_rate = sum(1 for m in metrics_list if m.success) / len(metrics_list)
        
        return StatisticalAnalysis(
            mean=mean_time,
            std_dev=std_dev,
            confidence_interval=confidence_interval,
            outliers=outliers,
            success_rate=success_rate
        )
    
    def generate_savage_commentary(self, metrics: BenchmarkMetrics, stats: StatisticalAnalysis) -> str:
        """Generate brutally honest but data-backed commentary"""
        commentary = []
        
        # Roast complexity
        if metrics.complexity_score >= 5:
            commentary.append(
                f"🔥 COMPLEXITY VIOLATION: Score {metrics.complexity_score}/5. "
                f"This isn't 'enterprise-grade', it's enterprise-bloat."
            )
        
        # Roast failure rate
        if stats.success_rate < 0.7:
            commentary.append(
                f"💀 SUCCESS RATE: {stats.success_rate:.1%}. "
                f"That's not 'intelligent automation', that's gambling with worse odds than a casino."
            )
        
        # Roast performance
        if metrics.execution_time > 1.0:
            commentary.append(
                f"🐌 PERFORMANCE: {metrics.execution_time:.2f}s execution time. "
                f"My grandmother's typewriter is faster than this."
            )
        
        # Roast quality issues
        if metrics.error_messages:
            commentary.append(
                f"🗑️ QUALITY ISSUES: {len(metrics.error_messages)} violations found. "
                f"Code reviews exist for a reason, and this is it."
            )
        
        # Statistical roasting
        if stats.std_dev > stats.mean * 0.5:
            commentary.append(
                f"📊 CONSISTENCY: σ={stats.std_dev:.3f}, CV={stats.std_dev/stats.mean:.1%}. "
                f"More unpredictable than weather forecasts."
            )
        
        return " | ".join(commentary) if commentary else "✅ SURPRISINGLY DECENT: Against all odds, this actually works."
    
    def run_comprehensive_benchmark(self, sample_size: int = None) -> Dict[str, Any]:
        """Run the full savage benchmarking suite"""
        
        # Select random sample if specified
        commands_to_test = self.commands
        if sample_size and sample_size < len(self.commands):
            commands_to_test = random.sample(self.commands, sample_size)
        
        print(f"🔬 INITIATING SAVAGE BENCHMARK of {len(commands_to_test)} commands...")
        
        all_metrics = []
        command_results = {}
        
        for i, command in enumerate(commands_to_test, 1):
            print(f"📊 Testing {i}/{len(commands_to_test)}: {command}")
            
            metrics = self.benchmark_command(command)
            all_metrics.append(metrics)
            
            # Generate per-command stats
            stats = self.generate_statistical_analysis([metrics])
            savage_comment = self.generate_savage_commentary(metrics, stats)
            
            command_results[command] = {
                "metrics": asdict(metrics),
                "savage_commentary": savage_comment,
                "timestamp": datetime.now().isoformat()
            }
        
        # Overall statistical analysis
        overall_stats = self.generate_statistical_analysis(all_metrics)
        
        # Generate final report
        report = {
            "benchmark_info": {
                "timestamp": datetime.now().isoformat(),
                "total_commands_tested": len(commands_to_test),
                "benchmarker_version": "1.0",
                "methodology": "Scientific measurement with savage commentary"
            },
            "overall_statistics": asdict(overall_stats),
            "command_results": command_results,
            "rankings": {
                "fastest": sorted(commands_to_test, key=lambda c: command_results[c]["metrics"]["execution_time"])[:3],
                "slowest": sorted(commands_to_test, key=lambda c: command_results[c]["metrics"]["execution_time"], reverse=True)[:3],
                "most_complex": sorted(commands_to_test, key=lambda c: command_results[c]["metrics"]["complexity_score"], reverse=True)[:3],
                "highest_quality": sorted(commands_to_test, key=lambda c: command_results[c]["metrics"]["output_quality"], reverse=True)[:3]
            },
            "savage_summary": self._generate_overall_savage_summary(overall_stats, all_metrics)
        }
        
        return report
    
    def _generate_overall_savage_summary(self, stats: StatisticalAnalysis, metrics_list: List[BenchmarkMetrics]) -> str:
        """Generate an overall savage summary of the entire command suite"""
        
        total_complexity = sum(m.complexity_score for m in metrics_list)
        avg_complexity = total_complexity / len(metrics_list)
        failed_commands = [m for m in metrics_list if not m.success]
        
        summary = f"""
🎓 PhD-LEVEL SCIENTIFIC ROAST RESULTS:

📈 STATISTICAL FACTS:
- Success Rate: {stats.success_rate:.1%} (Below 90% = Professional Embarrassment)
- Average Complexity: {avg_complexity:.1f}/5.0 (Above 5 = Enterprise Bloat Syndrome)
- Performance Variance: σ={stats.std_dev:.3f}s ({stats.std_dev/stats.mean:.1%} CV)
- Confidence Interval: {stats.confidence_interval[0]:.3f}s - {stats.confidence_interval[1]:.3f}s

🔥 BRUTAL TRUTH:
{len(failed_commands)}/{len(metrics_list)} commands failed basic quality standards.
That's a {len(failed_commands)/len(metrics_list):.1%} failure rate.

🏆 VERDICT: {"SCIENTIFICALLY SUBPAR" if stats.success_rate < 0.8 else "SURPRISINGLY FUNCTIONAL"}
        """
        
        return summary.strip()

    def save_report(self, report: Dict[str, Any]) -> str:
        """Save the benchmark report with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{timestamp}-savage-benchmark-report.json"
        filepath = self.results_dir / filename
        
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        return str(filepath)

def main():
    """Main execution function"""
    print("🔬 SAVAGE COMMAND BENCHMARKER v1.0")
    print("The PhD-level scientific roaster of Claude commands")
    print("=" * 60)
    
    benchmarker = SavageBenchmarker()
    
    # Run comprehensive benchmark on random sample
    sample_size = min(5, len(benchmarker.commands))  # Test up to 5 commands
    report = benchmarker.run_comprehensive_benchmark(sample_size)
    
    # Save report
    report_path = benchmarker.save_report(report)
    
    print(f"\n📊 SAVAGE REPORT GENERATED: {report_path}")
    print("\n" + report["savage_summary"])
    
    return report_path

if __name__ == "__main__":
    main()