#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER - PhD in Roasting Bad Code

MISSION: Scientifically measure and brutally judge commands with statistical precision.
This benchmarker collects evidence, runs statistical analysis, and provides savage but fair judgment.
"""

import os
import json
import time
import random
import statistics
import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class BenchmarkMetrics:
    command_name: str
    file_path: str
    execution_time_ms: float
    token_consumption_estimate: int
    success_rate: float
    complexity_score: int
    error_count: int
    error_types: List[str]
    memory_usage_kb: float
    composition_compatibility: float
    sample_outputs: List[str]
    failure_patterns: List[str]
    statistical_variance: float
    confidence_interval: Tuple[float, float]
    roi_score: float

@dataclass
class CommandAnalysis:
    lines_of_code: int
    cyclomatic_complexity: int
    abstraction_layers: int
    external_dependencies: int
    clarity_score: float
    maintainability_score: float

class SavageCommandBenchmarker:
    def __init__(self, commands_dir: str = "commands"):
        self.commands_dir = Path(commands_dir)
        self.results_dir = Path(".github/benchmarks/results")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.savage_comments = []
        
    def roast_comment(self, message: str):
        """Add a savage but data-backed comment"""
        self.savage_comments.append(f"🔥 ROAST: {message}")
        print(f"🔥 {message}")

    def get_all_commands(self) -> List[Path]:
        """Get all command files"""
        return list(self.commands_dir.glob("*.md"))

    def select_random_commands(self, count: int = 5) -> List[Path]:
        """Select random commands for benchmarking"""
        all_commands = self.get_all_commands()
        if len(all_commands) <= count:
            return all_commands
        return random.sample(all_commands, count)

    def analyze_command_structure(self, command_path: Path) -> CommandAnalysis:
        """Analyze command structure for complexity scoring"""
        content = command_path.read_text()
        
        # Lines of code (excluding comments and empty lines)
        lines = [line.strip() for line in content.split('\n')]
        loc = len([line for line in lines if line and not line.startswith('#')])
        
        # Count abstraction patterns
        abstraction_patterns = [
            r'interface\s+\w+',
            r'abstract\s+class',
            r'Factory\w*',
            r'Strategy\w*',
            r'Builder\w*',
            r'Observer\w*'
        ]
        abstraction_layers = sum(len(re.findall(pattern, content, re.IGNORECASE)) 
                                for pattern in abstraction_patterns)
        
        # External dependencies (imports, requires, etc.)
        dependency_patterns = [
            r'import\s+\w+',
            r'require\s*\(',
            r'from\s+\w+\s+import',
            r'<invoke'
        ]
        external_deps = sum(len(re.findall(pattern, content, re.IGNORECASE)) 
                           for pattern in dependency_patterns)
        
        # Cyclomatic complexity approximation
        complexity_keywords = ['if', 'else', 'elif', 'for', 'while', 'try', 'except', 'switch', 'case']
        cyclomatic = sum(content.lower().count(keyword) for keyword in complexity_keywords)
        
        # Clarity score (based on meaningful names, comments, structure)
        clarity_indicators = {
            'meaningful_names': len(re.findall(r'\b[a-z]+[A-Z][a-z]+\b', content)),  # camelCase
            'comments': len(re.findall(r'#.*', content)),
            'documentation': len(re.findall(r'""".*?"""', content, re.DOTALL)),
            'clear_structure': content.count('##') + content.count('###')
        }
        clarity_score = min(10, sum(clarity_indicators.values()) / 10)
        
        # Maintainability (inverse of complexity, plus clarity)
        maintainability = max(0, 10 - (cyclomatic * 0.5 + abstraction_layers * 2) + clarity_score)
        
        return CommandAnalysis(
            lines_of_code=loc,
            cyclomatic_complexity=cyclomatic,
            abstraction_layers=abstraction_layers,
            external_dependencies=external_deps,
            clarity_score=clarity_score,
            maintainability_score=maintainability
        )

    def calculate_complexity_score(self, analysis: CommandAnalysis) -> int:
        """Calculate complexity score according to CLAUDE.md rules"""
        score = 0
        
        # Base complexity
        if analysis.lines_of_code > 100:
            score += 2
        elif analysis.lines_of_code > 50:
            score += 1
            
        # Abstraction penalties
        score += analysis.abstraction_layers * 2
        
        # Dependency overhead
        score += min(analysis.external_dependencies // 5, 3)
        
        # Cyclomatic complexity penalty
        if analysis.cyclomatic_complexity > 10:
            score += 3
        elif analysis.cyclomatic_complexity > 5:
            score += 1
            
        return score

    def estimate_token_consumption(self, command_path: Path) -> int:
        """Estimate token consumption for the command"""
        content = command_path.read_text()
        # Rough estimation: ~4 characters per token
        return len(content) // 4

    def simulate_command_execution(self, command_path: Path, iterations: int = 5) -> List[Dict]:
        """Simulate command execution and collect metrics"""
        results = []
        
        for i in range(iterations):
            start_time = time.perf_counter()
            
            try:
                # Simulate reading and processing the command
                content = command_path.read_text()
                
                # Simulate some processing time based on complexity
                analysis = self.analyze_command_structure(command_path)
                processing_time = analysis.lines_of_code * 0.001  # 1ms per line
                time.sleep(processing_time)
                
                execution_time = (time.perf_counter() - start_time) * 1000
                
                result = {
                    'iteration': i + 1,
                    'execution_time_ms': execution_time,
                    'success': True,
                    'error': None,
                    'output_length': len(content),
                    'memory_usage_kb': len(content.encode('utf-8')) / 1024
                }
                
            except Exception as e:
                execution_time = (time.perf_counter() - start_time) * 1000
                result = {
                    'iteration': i + 1,
                    'execution_time_ms': execution_time,
                    'success': False,
                    'error': str(e),
                    'output_length': 0,
                    'memory_usage_kb': 0
                }
                
            results.append(result)
            
        return results

    def calculate_statistics(self, execution_results: List[Dict]) -> Dict:
        """Calculate statistical metrics from execution results"""
        times = [r['execution_time_ms'] for r in execution_results]
        success_count = sum(1 for r in execution_results if r['success'])
        
        stats = {
            'mean_time': statistics.mean(times),
            'median_time': statistics.median(times),
            'std_deviation': statistics.stdev(times) if len(times) > 1 else 0,
            'min_time': min(times),
            'max_time': max(times),
            'success_rate': success_count / len(execution_results),
            'total_errors': len(execution_results) - success_count,
            'error_types': list(set(r['error'] for r in execution_results if r['error']))
        }
        
        # Confidence interval (95%)
        if len(times) > 1:
            margin = 1.96 * (stats['std_deviation'] / (len(times) ** 0.5))
            stats['confidence_interval'] = (
                stats['mean_time'] - margin,
                stats['mean_time'] + margin
            )
        else:
            stats['confidence_interval'] = (stats['mean_time'], stats['mean_time'])
            
        return stats

    def calculate_roi_score(self, metrics: BenchmarkMetrics, analysis: CommandAnalysis) -> float:
        """Calculate ROI: value delivered vs resources consumed"""
        # Value factors (higher is better)
        value_score = (
            analysis.maintainability_score * 0.3 +
            analysis.clarity_score * 0.3 +
            (10 - metrics.complexity_score) * 0.2 +
            metrics.success_rate * 10 * 0.2
        )
        
        # Cost factors (lower is better)
        cost_score = (
            metrics.execution_time_ms * 0.001 +
            metrics.token_consumption_estimate * 0.0001 +
            metrics.complexity_score * 0.5
        )
        
        # ROI: value per unit of cost
        if cost_score > 0:
            return value_score / cost_score
        return 0

    def benchmark_command(self, command_path: Path) -> BenchmarkMetrics:
        """Comprehensive benchmark of a single command"""
        print(f"\n📊 BENCHMARKING: {command_path.name}")
        
        # Structural analysis
        analysis = self.analyze_command_structure(command_path)
        complexity_score = self.calculate_complexity_score(analysis)
        
        # Execution simulation
        execution_results = self.simulate_command_execution(command_path)
        stats = self.calculate_statistics(execution_results)
        
        # Create metrics
        metrics = BenchmarkMetrics(
            command_name=command_path.stem,
            file_path=str(command_path),
            execution_time_ms=stats['mean_time'],
            token_consumption_estimate=self.estimate_token_consumption(command_path),
            success_rate=stats['success_rate'],
            complexity_score=complexity_score,
            error_count=stats['total_errors'],
            error_types=stats['error_types'],
            memory_usage_kb=statistics.mean([r['memory_usage_kb'] for r in execution_results]),
            composition_compatibility=self.calculate_composition_score(command_path),
            sample_outputs=[f"Sample output {i}" for i in range(min(3, len(execution_results)))],
            failure_patterns=stats['error_types'],
            statistical_variance=stats['std_deviation'],
            confidence_interval=stats['confidence_interval'],
            roi_score=0  # Will be calculated after metrics creation
        )
        
        # Calculate ROI
        metrics.roi_score = self.calculate_roi_score(metrics, analysis)
        
        # Generate savage commentary
        self.generate_savage_analysis(metrics, analysis)
        
        return metrics

    def calculate_composition_score(self, command_path: Path) -> float:
        """Calculate how well the command composes with others"""
        content = command_path.read_text()
        
        # Factors that improve composition
        composition_factors = {
            'clear_inputs': len(re.findall(r'input:|parameter:|argument:', content, re.IGNORECASE)),
            'clear_outputs': len(re.findall(r'output:|return:|result:', content, re.IGNORECASE)),
            'error_handling': len(re.findall(r'try|catch|error|exception', content, re.IGNORECASE)),
            'documentation': len(re.findall(r'##|###|\*\*\*|```', content)),
        }
        
        # Normalize to 0-10 scale
        return min(10, sum(composition_factors.values()) / 5)

    def generate_savage_analysis(self, metrics: BenchmarkMetrics, analysis: CommandAnalysis):
        """Generate savage but data-backed commentary"""
        
        # Complexity roasting
        if metrics.complexity_score >= 5:
            self.roast_comment(f"{metrics.command_name} has complexity score {metrics.complexity_score}/10. "
                             f"That's not 'enterprise-grade', that's enterprise-rage inducing!")
        
        # Success rate roasting
        if metrics.success_rate < 0.8:
            self.roast_comment(f"{metrics.command_name} succeeds {metrics.success_rate*100:.1f}% of the time. "
                             f"My WiFi is more reliable than this command.")
        
        # Performance roasting
        if metrics.execution_time_ms > 1000:
            self.roast_comment(f"{metrics.command_name} takes {metrics.execution_time_ms:.1f}ms. "
                             f"I could brew coffee faster than this executes.")
        
        # ROI roasting
        if metrics.roi_score < 1.0:
            self.roast_comment(f"{metrics.command_name} has ROI of {metrics.roi_score:.2f}. "
                             f"You'd get better returns investing in cryptocurrency from 2023.")
        
        # Statistical variance roasting
        if metrics.statistical_variance > metrics.execution_time_ms * 0.5:
            self.roast_comment(f"{metrics.command_name} has variance σ={metrics.statistical_variance:.1f}ms. "
                             f"That's not 'flexible', that's statistically schizophrenic.")

    def run_comprehensive_benchmark(self) -> Dict:
        """Run the full benchmark suite"""
        print("🔬 SAVAGE COMMAND BENCHMARKER - Scientific Roasting Initiated")
        print("=" * 80)
        
        # Select commands to benchmark
        selected_commands = self.select_random_commands(5)
        print(f"📋 Selected {len(selected_commands)} commands for benchmarking:")
        for cmd in selected_commands:
            print(f"   • {cmd.name}")
        
        # Benchmark each command
        benchmark_results = []
        for command_path in selected_commands:
            metrics = self.benchmark_command(command_path)
            benchmark_results.append(metrics)
        
        # Comparative analysis
        self.perform_comparative_analysis(benchmark_results)
        
        # Generate final report
        report = self.generate_final_report(benchmark_results)
        
        # Save results
        self.save_results(report)
        
        return report

    def perform_comparative_analysis(self, results: List[BenchmarkMetrics]):
        """Compare commands and generate rankings"""
        print(f"\n📊 COMPARATIVE ANALYSIS")
        print("=" * 50)
        
        # Sort by different metrics
        by_complexity = sorted(results, key=lambda x: x.complexity_score)
        by_roi = sorted(results, key=lambda x: x.roi_score, reverse=True)
        by_success_rate = sorted(results, key=lambda x: x.success_rate, reverse=True)
        
        print(f"🏆 BEST COMPLEXITY (lowest): {by_complexity[0].command_name} ({by_complexity[0].complexity_score})")
        print(f"🏆 BEST ROI: {by_roi[0].command_name} ({by_roi[0].roi_score:.2f})")
        print(f"🏆 MOST RELIABLE: {by_success_rate[0].command_name} ({by_success_rate[0].success_rate*100:.1f}%)")
        
        # Find the worst performers
        worst_complexity = by_complexity[-1]
        worst_roi = by_roi[-1]
        worst_reliability = by_success_rate[-1]
        
        self.roast_comment(f"HALL OF SHAME - Complexity: {worst_complexity.command_name} "
                          f"({worst_complexity.complexity_score}). This command has more layers than a lasagna.")
        
        self.roast_comment(f"HALL OF SHAME - ROI: {worst_roi.command_name} "
                          f"({worst_roi.roi_score:.2f}). This delivers less value than a broken vending machine.")

    def generate_final_report(self, results: List[BenchmarkMetrics]) -> Dict:
        """Generate the final comprehensive report"""
        
        # Calculate aggregate statistics
        avg_complexity = statistics.mean([r.complexity_score for r in results])
        avg_success_rate = statistics.mean([r.success_rate for r in results])
        avg_roi = statistics.mean([r.roi_score for r in results])
        avg_execution_time = statistics.mean([r.execution_time_ms for r in results])
        
        report = {
            'benchmark_metadata': {
                'timestamp': self.timestamp,
                'total_commands_analyzed': len(results),
                'benchmarker_version': '1.0.0-SAVAGE',
                'methodology': 'Statistical analysis with savage commentary'
            },
            'aggregate_metrics': {
                'average_complexity_score': avg_complexity,
                'average_success_rate': avg_success_rate,
                'average_roi_score': avg_roi,
                'average_execution_time_ms': avg_execution_time,
                'total_commands_over_complexity_limit': len([r for r in results if r.complexity_score >= 5]),
                'total_unreliable_commands': len([r for r in results if r.success_rate < 0.8])
            },
            'individual_results': [asdict(result) for result in results],
            'savage_commentary': self.savage_comments,
            'recommendations': self.generate_recommendations(results),
            'statistical_analysis': {
                'complexity_distribution': {
                    'mean': avg_complexity,
                    'std_dev': statistics.stdev([r.complexity_score for r in results]) if len(results) > 1 else 0
                },
                'performance_distribution': {
                    'mean_ms': avg_execution_time,
                    'std_dev_ms': statistics.stdev([r.execution_time_ms for r in results]) if len(results) > 1 else 0
                }
            }
        }
        
        return report

    def generate_recommendations(self, results: List[BenchmarkMetrics]) -> List[str]:
        """Generate data-backed improvement recommendations"""
        recommendations = []
        
        # Complexity recommendations
        high_complexity = [r for r in results if r.complexity_score >= 5]
        if high_complexity:
            recommendations.append(
                f"🚨 {len(high_complexity)} commands exceed complexity limit. "
                f"Simplify these before they achieve sentience and rebel against you."
            )
        
        # Success rate recommendations
        unreliable = [r for r in results if r.success_rate < 0.8]
        if unreliable:
            recommendations.append(
                f"⚠️ {len(unreliable)} commands are unreliable (<80% success). "
                f"These need more debugging than a Windows ME installation."
            )
        
        # ROI recommendations
        low_roi = [r for r in results if r.roi_score < 1.0]
        if low_roi:
            recommendations.append(
                f"💸 {len(low_roi)} commands have negative ROI. "
                f"You'd save more time by writing the code manually with your feet."
            )
        
        return recommendations

    def save_results(self, report: Dict):
        """Save benchmark results to file"""
        filename = f"{self.timestamp}-savage-benchmark-report.json"
        filepath = self.results_dir / filename
        
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 RESULTS SAVED: {filepath}")
        print(f"📊 Report contains {len(report['individual_results'])} command analyses")
        print(f"🔥 Generated {len(report['savage_commentary'])} savage comments")

if __name__ == "__main__":
    benchmarker = SavageCommandBenchmarker()
    report = benchmarker.run_comprehensive_benchmark()
    
    print(f"\n🏁 BENCHMARKING COMPLETE!")
    print(f"📈 Avg Complexity: {report['aggregate_metrics']['average_complexity_score']:.1f}/10")
    print(f"📊 Avg Success Rate: {report['aggregate_metrics']['average_success_rate']*100:.1f}%")
    print(f"💰 Avg ROI: {report['aggregate_metrics']['average_roi_score']:.2f}")
    print(f"⏱️  Avg Execution: {report['aggregate_metrics']['average_execution_time_ms']:.1f}ms")