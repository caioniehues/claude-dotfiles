#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
PhD-level roasting with statistical precision
"""

import json
import time
import statistics
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict

@dataclass
class CommandMetrics:
    """Statistical metrics for brutal analysis"""
    name: str
    description: str
    token_count_input: int
    token_count_output: int
    execution_time: float
    success: bool
    error_message: str
    complexity_score: float
    composition_compatibility: int
    memory_usage: int
    pattern_quality: float
    adhd_optimization: float
    thinking_overhead: float

class SavageBenchmarker:
    """Scientific brutality framework"""
    
    def __init__(self):
        self.results = []
        self.baseline_metrics = {}
        self.start_time = datetime.now()
        
    def calculate_complexity_score(self, content: str) -> float:
        """
        Calculate complexity score based on CLAUDE.md rules
        """
        lines = content.split('\n')
        score = 1  # Base solution
        
        # Count complexity factors
        class_count = sum(1 for line in lines if 'class ' in line or '@dataclass' in line)
        interface_count = sum(1 for line in lines if 'interface ' in line or 'Protocol' in line)
        pattern_count = sum(1 for line in lines if any(pattern in line.lower() for pattern in 
                           ['factory', 'strategy', 'observer', 'decorator', 'builder']))
        config_count = sum(1 for line in lines if 'config' in line.lower() or 'yaml' in line.lower())
        
        score += class_count * 2
        score += interface_count * 1
        score += pattern_count * 3
        score += config_count * 2
        
        return score
    
    def analyze_command_content(self, content: str) -> Dict[str, Any]:
        """
        Deep analysis of command structure and quality
        """
        lines = content.split('\n')
        analysis = {
            'has_thinking_blocks': bool([l for l in lines if '<thinking' in l or '</thinking>' in l]),
            'has_mcp_integration': bool([l for l in lines if 'mcp__' in l]),
            'has_complexity_detection': bool([l for l in lines if 'complexity' in l.lower()]),
            'has_error_handling': bool([l for l in lines if 'error' in l.lower() or 'exception' in l.lower()]),
            'has_basic_memory': bool([l for l in lines if 'basic-memory' in l]),
            'line_count': len(lines),
            'xml_block_count': len([l for l in lines if '<' in l and '>' in l]),
            'javascript_blocks': len([l for l in lines if 'javascript' in l or '```js' in l]),
            'bash_blocks': len([l for l in lines if '```bash' in l]),
            'parameter_count': len([l for l in lines if '$ARGUMENTS' in l or '${' in l]),
        }
        return analysis
    
    def rate_adhd_optimization(self, content: str) -> float:
        """
        Rate how well command optimizes for ADHD patterns
        Scale: 0-10 (brutal honesty)
        """
        score = 0.0
        adhd_features = [
            ('time boundaries', 2.0),
            ('break reminder', 2.0), 
            ('context switching', 1.5),
            ('hyperfocus', 2.0),
            ('task breakdown', 1.5),
            ('energy matching', 1.0),
        ]
        
        content_lower = content.lower()
        for feature, points in adhd_features:
            if feature in content_lower:
                score += points
                
        return min(score, 10.0)
    
    def measure_thinking_overhead(self, content: str) -> float:
        """
        Calculate percentage of content devoted to thinking vs action
        Higher = more bloated
        """
        lines = content.split('\n')
        thinking_lines = sum(1 for line in lines if any(marker in line for marker in 
                            ['<thinking', '</thinking>', '<orchestration', 'thinking_thinking']))
        total_lines = len(lines)
        
        return (thinking_lines / total_lines * 100) if total_lines > 0 else 0.0
    
    def benchmark_command(self, file_path: Path) -> CommandMetrics:
        """
        Benchmark a single command with scientific precision
        """
        content = file_path.read_text()
        start_time = time.time()
        
        # Analysis
        complexity = self.calculate_complexity_score(content)
        analysis = self.analyze_command_content(content)
        adhd_score = self.rate_adhd_optimization(content)
        thinking_overhead = self.measure_thinking_overhead(content)
        
        # Token estimation (rough but consistent)
        token_count_input = len(content.split()) * 1.3  # Conservative estimate
        token_count_output = token_count_input * 0.6    # Typical response ratio
        
        execution_time = time.time() - start_time
        
        # Pattern quality assessment
        pattern_quality = self.assess_pattern_quality(analysis, complexity)
        
        return CommandMetrics(
            name=file_path.stem,
            description=self.extract_description(content),
            token_count_input=int(token_count_input),
            token_count_output=int(token_count_output),
            execution_time=execution_time,
            success=True,
            error_message="",
            complexity_score=complexity,
            composition_compatibility=self.rate_composition_compatibility(analysis),
            memory_usage=len(content),  # Proxy for memory usage
            pattern_quality=pattern_quality,
            adhd_optimization=adhd_score,
            thinking_overhead=thinking_overhead
        )
    
    def extract_description(self, content: str) -> str:
        """Extract command description"""
        lines = content.split('\n')
        for line in lines:
            if line.startswith('#') and not line.startswith('##'):
                return line[1:].strip()
        return "No description found"
    
    def assess_pattern_quality(self, analysis: Dict, complexity: float) -> float:
        """
        Assess how well command follows established patterns
        Scale: 0-10 (10 = perfect adherence)
        """
        score = 5.0  # Baseline
        
        # Positive factors
        if analysis['has_thinking_blocks']:
            score += 1.5
        if analysis['has_mcp_integration']:
            score += 1.0
        if analysis['has_complexity_detection']:
            score += 1.5
        if analysis['has_error_handling']:
            score += 1.0
        
        # Negative factors
        if complexity > 5:
            score -= 2.0  # Violates CLAUDE.md complexity rule
        if analysis['line_count'] > 800:
            score -= 1.0  # Too bloated
            
        return max(0.0, min(10.0, score))
    
    def rate_composition_compatibility(self, analysis: Dict) -> int:
        """
        Rate how well command composes with others
        Scale: 1-5 (5 = highly composable)
        """
        score = 3  # Baseline
        
        if analysis['has_mcp_integration']:
            score += 1
        if analysis['has_basic_memory']:
            score += 1
        if analysis['parameter_count'] > 0:
            score += 1
        if analysis['line_count'] > 500:
            score -= 1  # Too complex to compose well
            
        return max(1, min(5, score))
    
    def generate_savage_analysis(self, metrics: List[CommandMetrics]) -> Dict[str, Any]:
        """
        Generate statistically-backed roasting
        """
        if not metrics:
            return {"error": "No metrics to analyze. Did the benchmarker get stage fright?"}
        
        # Statistical calculations
        complexity_scores = [m.complexity_score for m in metrics]
        pattern_scores = [m.pattern_quality for m in metrics]
        thinking_overheads = [m.thinking_overhead for m in metrics]
        adhd_scores = [m.adhd_optimization for m in metrics]
        
        stats = {
            'total_commands': len(metrics),
            'complexity_stats': {
                'mean': statistics.mean(complexity_scores),
                'median': statistics.median(complexity_scores),
                'stdev': statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                'violations': len([s for s in complexity_scores if s >= 5]),  # CLAUDE.md rule
            },
            'pattern_quality_stats': {
                'mean': statistics.mean(pattern_scores),
                'median': statistics.median(pattern_scores),
                'stdev': statistics.stdev(pattern_scores) if len(pattern_scores) > 1 else 0,
            },
            'thinking_overhead_stats': {
                'mean': statistics.mean(thinking_overheads),
                'median': statistics.median(thinking_overheads),
                'max': max(thinking_overheads),
                'bloat_offenders': [m.name for m in metrics if m.thinking_overhead > 50],
            },
            'adhd_optimization_stats': {
                'mean': statistics.mean(adhd_scores),
                'median': statistics.median(adhd_scores),
                'adhd_winners': [m.name for m in metrics if m.adhd_optimization >= 8],
                'adhd_failures': [m.name for m in metrics if m.adhd_optimization < 3],
            }
        }
        
        return stats

def main():
    """Execute the scientific roasting"""
    benchmarker = SavageBenchmarker()
    commands_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands")
    
    print("🔬 SAVAGE COMMAND BENCHMARKER - PhD-Level Scientific Roasting")
    print("=" * 70)
    
    # Benchmark sample commands
    sample_commands = [
        "adaptive-complexity-router.md",
        "adhd-hyperfocus-guardian.md", 
        "java-clean-code-generator.md",
        "ultrathink.md",
        "intelligent-code-enhancer.md"
    ]
    
    all_metrics = []
    for cmd_name in sample_commands:
        cmd_path = commands_dir / cmd_name
        if cmd_path.exists():
            print(f"Benchmarking: {cmd_name}...")
            metrics = benchmarker.benchmark_command(cmd_path)
            all_metrics.append(metrics)
            print(f"  Complexity Score: {metrics.complexity_score:.1f}/5 {'❌ VIOLATION' if metrics.complexity_score >= 5 else '✅'}")
            print(f"  Pattern Quality: {metrics.pattern_quality:.1f}/10")
            print(f"  Thinking Overhead: {metrics.thinking_overhead:.1f}%")
            print()
    
    # Generate analysis
    analysis = benchmarker.generate_savage_analysis(all_metrics)
    
    # Save results
    results = {
        'timestamp': datetime.now().isoformat(),
        'methodology': 'Statistical analysis with CLAUDE.md compliance checking',
        'sample_size': len(all_metrics),
        'metrics': [asdict(m) for m in all_metrics],
        'statistical_analysis': analysis,
        'savage_verdict': 'Analysis complete - prepare for scientific roasting!'
    }
    
    output_path = Path(".github/benchmarks/results/20250818-113326-report.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"📊 Results saved to: {output_path}")
    return results

if __name__ == "__main__":
    results = main()