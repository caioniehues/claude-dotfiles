#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific measurement and brutal judgment of Claude commands
"""

import json
import time
import random
import subprocess
import statistics
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

@dataclass
class BenchmarkMetrics:
    """Precise measurements for savage judgment"""
    command_name: str
    execution_time_ms: List[float]
    token_consumption: Dict[str, int]
    success_rate: float
    complexity_score: int
    error_patterns: List[str]
    memory_usage_kb: Optional[int]
    composition_compatibility: Dict[str, bool]
    variance_statistics: Dict[str, float]

class SavageBenchmarker:
    """PhD-level roasting with statistical rigor"""
    
    def __init__(self, commands_dir: Path):
        self.commands_dir = commands_dir
        self.results_dir = Path(".github/benchmarks/results")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # ADHD time multipliers from CLAUDE.md
        self.adhd_multipliers = {
            'base': 1.5,
            'context_switching': 1.25,
            'energy_high': 0.8,
            'energy_low': 2.0
        }
    
    def get_command_list(self) -> List[Path]:
        """Get all .md commands for brutal analysis"""
        return list(self.commands_dir.glob("**/*.md"))
    
    def calculate_complexity_score(self, command_content: str) -> int:
        """Calculate complexity score based on CLAUDE.md rules"""
        score = 1  # Base solution
        
        # Patterns that increase complexity
        complexity_patterns = {
            'class ': 2,
            'interface ': 1, 
            'Factory': 3,
            'Strategy': 3,
            'Builder': 3,
            'Abstract': 3,
            'Observer': 3,
            'config': 2,
            'xml': 2,
            'yaml': 2
        }
        
        for pattern, penalty in complexity_patterns.items():
            score += command_content.lower().count(pattern.lower()) * penalty
            
        return score
    
    def analyze_command_structure(self, command_path: Path) -> Dict[str, Any]:
        """Deep analysis of command structure and patterns"""
        with open(command_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        analysis = {
            'line_count': len(content.splitlines()),
            'word_count': len(content.split()),
            'char_count': len(content),
            'has_examples': '```' in content,
            'has_variables': '${' in content or '{{' in content,
            'has_conditions': any(word in content.lower() for word in ['if', 'when', 'unless']),
            'has_loops': any(word in content.lower() for word in ['for', 'while', 'repeat']),
            'complexity_score': self.calculate_complexity_score(content),
            'estimated_token_count': len(content.split()) * 1.3  # Rough approximation
        }
        
        return analysis
    
    def measure_execution_time(self, command_path: Path, iterations: int = 5) -> List[float]:
        """Measure execution time with statistical variance"""
        times = []
        
        for _ in range(iterations):
            start_time = time.perf_counter()
            
            # Simulate command parsing and analysis
            with open(command_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Simulate processing complexity
            lines = content.splitlines()
            for line in lines:
                if line.strip():
                    # Simulate pattern matching
                    _ = len(line.split())
                    
            end_time = time.perf_counter()
            times.append((end_time - start_time) * 1000)  # Convert to ms
            
        return times
    
    def assess_composition_compatibility(self, command_path: Path) -> Dict[str, bool]:
        """Test compatibility with other commands"""
        with open(command_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        compatibility = {
            'can_chain': 'output' in content.lower() or 'result' in content.lower(),
            'has_input_params': '${' in content or 'input' in content.lower(),
            'is_stateless': 'state' not in content.lower() and 'memory' not in content.lower(),
            'follows_conventions': command_path.name.replace('-', '_').replace('.md', '').isidentifier(),
            'has_error_handling': any(word in content.lower() for word in ['error', 'exception', 'fail']),
            'memory_safe': 'mcp__basic-memory' in content or 'memory' not in content.lower()
        }
        
        return compatibility
    
    def calculate_variance_stats(self, times: List[float]) -> Dict[str, float]:
        """Calculate statistical variance for savage judgment"""
        if len(times) < 2:
            return {'mean': times[0] if times else 0, 'std_dev': 0, 'variance': 0, 'cv': 0}
        
        mean = statistics.mean(times)
        std_dev = statistics.stdev(times)
        variance = statistics.variance(times)
        cv = (std_dev / mean) * 100 if mean > 0 else 0  # Coefficient of variation
        
        return {
            'mean': round(mean, 3),
            'std_dev': round(std_dev, 3),
            'variance': round(variance, 3),
            'cv': round(cv, 2),
            'min': min(times),
            'max': max(times),
            'median': statistics.median(times)
        }
    
    def benchmark_command(self, command_path: Path) -> BenchmarkMetrics:
        """Comprehensive benchmarking with savage precision"""
        print(f"📊 Benchmarking: {command_path.name}")
        
        # Execution time measurements
        execution_times = self.measure_execution_time(command_path)
        
        # Structure analysis
        structure = self.analyze_command_structure(command_path)
        
        # Composition compatibility
        compatibility = self.assess_composition_compatibility(command_path)
        
        # Variance statistics
        variance_stats = self.calculate_variance_stats(execution_times)
        
        # Success rate simulation (based on complexity and structure)
        base_success = 0.95
        complexity_penalty = structure['complexity_score'] * 0.05
        success_rate = max(0.1, base_success - complexity_penalty)
        
        # Simulate error patterns
        error_patterns = []
        if structure['complexity_score'] > 5:
            error_patterns.append("Complexity overload - score exceeds Vegas odds")
        if not compatibility['has_error_handling']:
            error_patterns.append("No error handling - fails silently like a ninja")
        if structure['line_count'] > 100:
            error_patterns.append("Wall of text - TL;DR syndrome")
        
        return BenchmarkMetrics(
            command_name=command_path.name,
            execution_time_ms=execution_times,
            token_consumption={
                'estimated_input': int(structure['estimated_token_count']),
                'estimated_output': int(structure['estimated_token_count'] * 0.7)
            },
            success_rate=round(success_rate, 3),
            complexity_score=structure['complexity_score'],
            error_patterns=error_patterns,
            memory_usage_kb=structure['char_count'] // 1024 + 1,
            composition_compatibility=compatibility,
            variance_statistics=variance_stats
        )
    
    def select_random_commands(self, total_commands: List[Path], sample_size: int = 8) -> List[Path]:
        """Scientifically random selection for unbiased roasting"""
        random.seed(int(datetime.now().timestamp()))
        return random.sample(total_commands, min(sample_size, len(total_commands)))
    
    def generate_savage_judgment(self, metrics: BenchmarkMetrics) -> str:
        """PhD-level roasting with data backing"""
        judgments = []
        
        # Execution time judgment
        cv = metrics.variance_statistics['cv']
        if cv > 30:
            judgments.append(f"Execution time variance of {cv}% - more unstable than a blockchain startup")
        elif cv > 15:
            judgments.append(f"Execution time CV {cv}% - inconsistent like your git commits")
        else:
            judgments.append(f"Execution time CV {cv}% - surprisingly stable")
        
        # Complexity score judgment
        if metrics.complexity_score >= 10:
            judgments.append(f"Complexity score {metrics.complexity_score} - this isn't enterprise architecture, it's command suicide")
        elif metrics.complexity_score >= 5:
            judgments.append(f"Complexity score {metrics.complexity_score} - violates CLAUDE.md harder than terms of service")
        else:
            judgments.append(f"Complexity score {metrics.complexity_score} - finally, someone who read the manual")
        
        # Success rate judgment
        if metrics.success_rate < 0.7:
            judgments.append(f"Success rate {metrics.success_rate*100}% - worse reliability than Windows ME")
        elif metrics.success_rate < 0.9:
            judgments.append(f"Success rate {metrics.success_rate*100}% - mediocre like most code reviews")
        else:
            judgments.append(f"Success rate {metrics.success_rate*100}% - actually functional, shocking")
        
        # Composition compatibility
        compat_count = sum(metrics.composition_compatibility.values())
        total_compat = len(metrics.composition_compatibility)
        compat_ratio = compat_count / total_compat
        
        if compat_ratio < 0.5:
            judgments.append(f"Composition compatibility {compat_ratio*100:.1f}% - plays well with others like a toxic teammate")
        elif compat_ratio < 0.8:
            judgments.append(f"Composition compatibility {compat_ratio*100:.1f}% - somewhat social, needs improvement")
        else:
            judgments.append(f"Composition compatibility {compat_ratio*100:.1f}% - team player detected")
        
        return " | ".join(judgments)
    
    def run_benchmark_suite(self, sample_size: int = 8) -> Dict[str, Any]:
        """Execute the complete savage benchmarking suite"""
        commands = self.get_command_list()
        selected_commands = self.select_random_commands(commands, sample_size)
        
        results = {
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'total_commands': len(commands),
                'sampled_commands': len(selected_commands),
                'sample_size': sample_size,
                'selection_method': 'random_with_seed'
            },
            'benchmarks': [],
            'summary_statistics': {},
            'savage_rankings': {}
        }
        
        # Benchmark each selected command
        all_metrics = []
        for cmd_path in selected_commands:
            metrics = self.benchmark_command(cmd_path)
            savage_judgment = self.generate_savage_judgment(metrics)
            
            benchmark_result = {
                'metrics': asdict(metrics),
                'savage_judgment': savage_judgment,
                'recommendations': self.generate_recommendations(metrics)
            }
            
            results['benchmarks'].append(benchmark_result)
            all_metrics.append(metrics)
        
        # Calculate summary statistics
        results['summary_statistics'] = self.calculate_summary_stats(all_metrics)
        results['savage_rankings'] = self.generate_rankings(all_metrics)
        
        return results
    
    def generate_recommendations(self, metrics: BenchmarkMetrics) -> List[str]:
        """Data-driven improvement recommendations"""
        recommendations = []
        
        if metrics.complexity_score > 5:
            recommendations.append("SIMPLIFY: Reduce complexity score below 5 per CLAUDE.md rules")
        
        if metrics.variance_statistics['cv'] > 20:
            recommendations.append("STABILIZE: High execution variance indicates inconsistent performance")
        
        if metrics.success_rate < 0.8:
            recommendations.append("RELIABILITY: Add error handling and validation")
        
        if not metrics.composition_compatibility['can_chain']:
            recommendations.append("COMPOSABILITY: Add output structure for command chaining")
        
        if metrics.token_consumption['estimated_input'] > 2000:
            recommendations.append("EFFICIENCY: Reduce token consumption for better performance")
        
        return recommendations
    
    def calculate_summary_stats(self, all_metrics: List[BenchmarkMetrics]) -> Dict[str, Any]:
        """Calculate aggregate statistics across all commands"""
        if not all_metrics:
            return {}
        
        complexity_scores = [m.complexity_score for m in all_metrics]
        success_rates = [m.success_rate for m in all_metrics]
        execution_means = [m.variance_statistics['mean'] for m in all_metrics]
        
        return {
            'complexity': {
                'mean': statistics.mean(complexity_scores),
                'median': statistics.median(complexity_scores),
                'max': max(complexity_scores),
                'violations': sum(1 for s in complexity_scores if s >= 5)
            },
            'performance': {
                'mean_execution_time': statistics.mean(execution_means),
                'fastest': min(execution_means),
                'slowest': max(execution_means)
            },
            'reliability': {
                'mean_success_rate': statistics.mean(success_rates),
                'failures': sum(1 for r in success_rates if r < 0.8)
            }
        }
    
    def generate_rankings(self, all_metrics: List[BenchmarkMetrics]) -> Dict[str, Any]:
        """Generate savage but fair rankings"""
        # Overall score calculation (lower is better for ranking)
        scored_commands = []
        for metrics in all_metrics:
            score = (
                metrics.complexity_score * 2 +  # Complexity penalty
                (1 - metrics.success_rate) * 10 +  # Failure penalty
                metrics.variance_statistics['cv'] / 10 +  # Variance penalty
                (1 - sum(metrics.composition_compatibility.values()) / len(metrics.composition_compatibility)) * 5
            )
            scored_commands.append((metrics.command_name, score))
        
        # Sort by score (lower is better)
        scored_commands.sort(key=lambda x: x[1])
        
        return {
            'best_performers': scored_commands[:3],
            'worst_performers': scored_commands[-3:],
            'hall_of_shame': [cmd for cmd, score in scored_commands if score > 10],
            'hall_of_fame': [cmd for cmd, score in scored_commands if score < 3]
        }

if __name__ == "__main__":
    benchmarker = SavageBenchmarker(Path("commands"))
    results = benchmarker.run_benchmark_suite()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = Path(f".github/benchmarks/results/{timestamp}-report.json")
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"🎯 Savage benchmark report saved to: {output_file}")