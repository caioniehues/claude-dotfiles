#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
PhD in Roasting Bad Code, Statistical Precision Division

Scientifically measures and brutally judges commands with zero tolerance for mediocrity.
"""

import json
import re
import time
import statistics
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Tuple

class SavageCommandBenchmarker:
    """Brutally honest benchmarker with PhD-level standards"""
    
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.session_id = f"20250817-{int(time.time())}"
        self.commands_dir = Path("commands")
        self.results = {
            'session_info': {
                'timestamp': self.timestamp,
                'session_id': self.session_id,
                'benchmarker_version': '1.0-SAVAGE',
                'standards': 'PhD-level statistical analysis with zero BS tolerance'
            },
            'commands_analyzed': [],
            'metrics': {},
            'statistical_analysis': {},
            'savage_commentary': {},
            'rankings': {},
            'recommendations': {}
        }
    
    def measure_command_metrics(self, command_file: str) -> Dict[str, Any]:
        """Measure objective metrics with statistical precision"""
        file_path = self.commands_dir / command_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic metrics
        lines = content.split('\n')
        words = content.split()
        
        # Complexity analysis
        xml_blocks = len(re.findall(r'<[^/][^>]*>', content))
        thinking_blocks = len(re.findall(r'<thinking[^>]*>', content))
        complexity_indicators = len(re.findall(r'(complexity|pattern|abstraction|interface)', content, re.IGNORECASE))
        
        # Structure analysis
        markdown_headers = len(re.findall(r'^#+\s', content, re.MULTILINE))
        code_blocks = len(re.findall(r'```', content)) // 2
        
        # Cognitive load indicators
        nested_structures = len(re.findall(r'(\s{4,}|\t+)', content))
        conditionals = len(re.findall(r'(if|when|case|switch)', content, re.IGNORECASE))
        
        # ADHD-specific analysis (for ADHD commands)
        is_adhd_command = 'adhd' in command_file.lower()
        adhd_features = 0
        if is_adhd_command:
            adhd_features = len(re.findall(r'(energy|hyperfocus|break|pattern|time|multiplier)', content, re.IGNORECASE))
        
        # Java-specific analysis (for Java commands)
        is_java_command = 'java' in command_file.lower()
        java_features = 0
        if is_java_command:
            java_features = len(re.findall(r'(class|interface|method|pattern|spring|clean)', content, re.IGNORECASE))
        
        return {
            'file_size_bytes': len(content.encode('utf-8')),
            'total_lines': len(lines),
            'non_empty_lines': len([l for l in lines if l.strip()]),
            'total_words': len(words),
            'xml_blocks': xml_blocks,
            'thinking_blocks': thinking_blocks,
            'complexity_indicators': complexity_indicators,
            'markdown_headers': markdown_headers,
            'code_blocks': code_blocks,
            'nested_structures': nested_structures,
            'conditionals': conditionals,
            'is_adhd_command': is_adhd_command,
            'adhd_features': adhd_features,
            'is_java_command': is_java_command,
            'java_features': java_features,
            'estimated_read_time_minutes': len(words) / 200,  # Average reading speed
            'cognitive_load_score': (nested_structures + conditionals + complexity_indicators) / 10
        }
    
    def calculate_complexity_score(self, metrics: Dict[str, Any]) -> Tuple[float, str]:
        """Calculate complexity score based on CLAUDE.md rules with savage assessment"""
        
        # Base complexity calculation
        base_score = 1  # Direct solution baseline
        
        # Add complexity based on structure
        if metrics['xml_blocks'] > 10:
            base_score += 1  # Complex structure
        if metrics['thinking_blocks'] > 5:
            base_score += 1  # Heavy thinking overhead
        if metrics['nested_structures'] > 50:
            base_score += 1  # Nesting hell
        if metrics['total_lines'] > 500:
            base_score += 2  # Bloated command
            
        # Domain-specific penalties
        if metrics['is_java_command'] and metrics['java_features'] < 10:
            base_score += 1  # Weak Java integration
        if metrics['is_adhd_command'] and metrics['adhd_features'] < 15:
            base_score += 1  # Poor ADHD optimization
            
        # Determine assessment
        if base_score >= 5:
            assessment = "BLOATED MESS"
        elif base_score >= 4:
            assessment = "OVER-ENGINEERED"
        elif base_score >= 3:
            assessment = "ACCEPTABLE"
        elif base_score >= 2:
            assessment = "WELL-DESIGNED"
        else:
            assessment = "SIMPLE ELEGANCE"
            
        return base_score, assessment
    
    def calculate_execution_risk(self, metrics: Dict[str, Any]) -> Tuple[float, str]:
        """Calculate execution risk with statistical backing"""
        
        risk_factors = []
        
        # Size-based risk
        if metrics['total_lines'] > 800:
            risk_factors.append(0.3)  # Large commands are harder to execute
            
        # Complexity-based risk
        if metrics['cognitive_load_score'] > 5:
            risk_factors.append(0.25)  # High cognitive load = higher failure rate
            
        # Structure-based risk
        if metrics['xml_blocks'] > 20:
            risk_factors.append(0.2)  # Too many XML blocks = parsing issues
            
        # Domain-specific risk
        if metrics['is_java_command'] and metrics['java_features'] > 50:
            risk_factors.append(0.15)  # Over-optimized for Java
            
        risk_score = sum(risk_factors)
        
        if risk_score >= 0.7:
            risk_level = "EXTREMELY HIGH"
        elif risk_score >= 0.5:
            risk_level = "HIGH"
        elif risk_score >= 0.3:
            risk_level = "MODERATE"
        elif risk_score >= 0.1:
            risk_level = "LOW"
        else:
            risk_level = "MINIMAL"
            
        return risk_score, risk_level
    
    def estimate_token_consumption(self, metrics: Dict[str, Any]) -> Dict[str, float]:
        """Estimate token consumption with statistical modeling"""
        
        # Conservative token estimation (1 token ≈ 4 characters)
        input_tokens = metrics['file_size_bytes'] / 4
        
        # Output estimation based on command complexity
        output_multiplier = 1.0
        if metrics['is_java_command']:
            output_multiplier = 2.5  # Java commands generate more code
        elif metrics['is_adhd_command']:
            output_multiplier = 1.8  # ADHD commands generate structured output
        else:
            output_multiplier = 1.5  # Generic commands
            
        estimated_output_tokens = input_tokens * output_multiplier
        total_tokens = input_tokens + estimated_output_tokens
        
        # Cost estimation (rough, based on model pricing)
        estimated_cost_usd = total_tokens * 0.000015  # Approximate cost per token
        
        return {
            'input_tokens': input_tokens,
            'estimated_output_tokens': estimated_output_tokens,
            'total_tokens': total_tokens,
            'estimated_cost_usd': estimated_cost_usd,
            'cost_efficiency_score': metrics['total_words'] / total_tokens  # Words per token
        }
    
    def generate_savage_commentary(self, command_file: str, metrics: Dict[str, Any], 
                                 complexity_score: float, risk_score: float) -> str:
        """Generate brutally honest commentary with statistical backing"""
        
        commentary = []
        
        # Size roasting
        if metrics['total_lines'] > 800:
            commentary.append(f"📏 This command has {metrics['total_lines']} lines. "
                            f"War and Peace was shorter and more useful.")
        elif metrics['total_lines'] < 50:
            commentary.append(f"📏 At {metrics['total_lines']} lines, this command is more "
                            f"concise than my patience for mediocrity.")
        
        # Complexity roasting
        if complexity_score >= 5:
            commentary.append(f"🎯 Complexity score: {complexity_score}/5. "
                            f"You've created a masterpiece of over-engineering. "
                            f"Even Rube Goldberg would be impressed.")
        elif complexity_score <= 2:
            commentary.append(f"🎯 Complexity score: {complexity_score}/5. "
                            f"Refreshingly simple. Your future self will actually thank you.")
        
        # Structure analysis
        if metrics['xml_blocks'] > 20:
            commentary.append(f"📦 {metrics['xml_blocks']} XML blocks detected. "
                            f"This isn't markup, it's a cry for help.")
        
        # Cognitive load
        if metrics['cognitive_load_score'] > 7:
            commentary.append(f"🧠 Cognitive load score: {metrics['cognitive_load_score']:.1f}. "
                            f"Reading this command requires a PhD in Mind Reading.")
        
        # Domain-specific roasting
        if metrics['is_java_command']:
            if metrics['java_features'] < 10:
                commentary.append("☕ Java command with weak Java integration. "
                               "It's like ordering a latte and getting hot water.")
            elif metrics['java_features'] > 50:
                commentary.append("☕ This command mentions Java more than Oracle's marketing team.")
        
        if metrics['is_adhd_command']:
            if metrics['adhd_features'] < 15:
                commentary.append("🧩 ADHD command that forgot about ADHD. "
                               "The irony is palpable.")
            else:
                commentary.append("🧩 Actually understands ADHD patterns. "
                               "Miracles do happen.")
        
        # Token efficiency
        tokens = self.estimate_token_consumption(metrics)
        if tokens['cost_efficiency_score'] < 0.1:
            commentary.append(f"💰 Token efficiency: {tokens['cost_efficiency_score']:.3f} words/token. "
                            f"This command costs more per word than a divorce lawyer.")
        
        # Risk assessment
        if risk_score > 0.5:
            commentary.append(f"⚠️ Execution risk: {risk_score:.1f}. "
                            f"Higher failure rate than a startup's first product launch.")
        
        return "\n".join(commentary)
    
    def analyze_command(self, command_file: str) -> Dict[str, Any]:
        """Complete analysis of a single command"""
        
        print(f"🔬 Analyzing {command_file} with scientific precision...")
        
        metrics = self.measure_command_metrics(command_file)
        complexity_score, complexity_assessment = self.calculate_complexity_score(metrics)
        risk_score, risk_level = self.calculate_execution_risk(metrics)
        token_analysis = self.estimate_token_consumption(metrics)
        savage_commentary = self.generate_savage_commentary(
            command_file, metrics, complexity_score, risk_score
        )
        
        analysis = {
            'command_file': command_file,
            'raw_metrics': metrics,
            'complexity': {
                'score': complexity_score,
                'assessment': complexity_assessment,
                'threshold_violated': complexity_score >= 5
            },
            'risk': {
                'score': risk_score,
                'level': risk_level
            },
            'token_analysis': token_analysis,
            'performance_score': self.calculate_performance_score(metrics, complexity_score, risk_score),
            'savage_commentary': savage_commentary,
            'recommendations': self.generate_recommendations(metrics, complexity_score, risk_score)
        }
        
        return analysis
    
    def calculate_performance_score(self, metrics: Dict[str, Any], 
                                  complexity_score: float, risk_score: float) -> float:
        """Calculate overall performance score (0-100)"""
        
        # Start with base score
        score = 100
        
        # Penalize complexity
        score -= (complexity_score - 1) * 15  # -15 points per complexity point above 1
        
        # Penalize risk
        score -= risk_score * 30  # -30 points per risk point
        
        # Penalize cognitive load
        score -= metrics['cognitive_load_score'] * 5
        
        # Penalize bloat
        if metrics['total_lines'] > 500:
            score -= ((metrics['total_lines'] - 500) / 100) * 10
        
        # Bonus for domain optimization
        if metrics['is_adhd_command'] and metrics['adhd_features'] >= 20:
            score += 10
        if metrics['is_java_command'] and metrics['java_features'] >= 15:
            score += 10
        
        return max(0, min(100, score))
    
    def generate_recommendations(self, metrics: Dict[str, Any], 
                               complexity_score: float, risk_score: float) -> List[str]:
        """Generate evidence-based recommendations"""
        
        recommendations = []
        
        if complexity_score >= 5:
            recommendations.append("🚨 CRITICAL: Complexity score exceeds threshold. "
                                 "Break this command into smaller, focused commands.")
        
        if metrics['total_lines'] > 800:
            recommendations.append("📏 Command is too long. Split into multiple files or "
                                 "reduce redundant content.")
        
        if metrics['cognitive_load_score'] > 6:
            recommendations.append("🧠 High cognitive load. Simplify nested structures "
                                 "and reduce conditional complexity.")
        
        if risk_score > 0.4:
            recommendations.append("⚠️ High execution risk. Add more validation checkpoints "
                                 "and error handling.")
        
        if metrics['xml_blocks'] > 25:
            recommendations.append("📦 Excessive XML structure. Consider using templates "
                                 "or simpler formatting.")
        
        # Domain-specific recommendations
        if metrics['is_java_command'] and metrics['java_features'] < 10:
            recommendations.append("☕ Weak Java integration. Add more Java-specific "
                                 "patterns and best practices.")
        
        if metrics['is_adhd_command'] and metrics['adhd_features'] < 15:
            recommendations.append("🧩 Insufficient ADHD optimization. Add more "
                                 "pattern-based features and time management.")
        
        return recommendations
    
    def run_full_benchmark(self, commands: List[str]) -> Dict[str, Any]:
        """Run complete benchmark analysis on selected commands"""
        
        print("🔬 SAVAGE COMMAND BENCHMARKER INITIATED")
        print("PhD in Roasting Bad Code - Statistical Precision Division")
        print("=" * 60)
        
        analyses = []
        
        for command_file in commands:
            analysis = self.analyze_command(command_file)
            analyses.append(analysis)
            self.results['commands_analyzed'].append(command_file)
        
        # Calculate comparative statistics
        performance_scores = [a['performance_score'] for a in analyses]
        complexity_scores = [a['complexity']['score'] for a in analyses]
        risk_scores = [a['risk']['score'] for a in analyses]
        
        self.results['statistical_analysis'] = {
            'performance_statistics': {
                'mean': statistics.mean(performance_scores),
                'median': statistics.median(performance_scores),
                'stdev': statistics.stdev(performance_scores) if len(performance_scores) > 1 else 0,
                'min': min(performance_scores),
                'max': max(performance_scores)
            },
            'complexity_statistics': {
                'mean': statistics.mean(complexity_scores),
                'median': statistics.median(complexity_scores),
                'stdev': statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                'threshold_violations': sum(1 for s in complexity_scores if s >= 5),
                'violation_rate': sum(1 for s in complexity_scores if s >= 5) / len(complexity_scores)
            },
            'risk_statistics': {
                'mean': statistics.mean(risk_scores),
                'median': statistics.median(risk_scores),
                'stdev': statistics.stdev(risk_scores) if len(risk_scores) > 1 else 0,
                'high_risk_count': sum(1 for s in risk_scores if s >= 0.5)
            }
        }
        
        # Generate rankings
        sorted_by_performance = sorted(analyses, key=lambda x: x['performance_score'], reverse=True)
        sorted_by_complexity = sorted(analyses, key=lambda x: x['complexity']['score'])
        sorted_by_risk = sorted(analyses, key=lambda x: x['risk']['score'])
        
        self.results['rankings'] = {
            'best_performance': [a['command_file'] for a in sorted_by_performance],
            'lowest_complexity': [a['command_file'] for a in sorted_by_complexity],
            'lowest_risk': [a['command_file'] for a in sorted_by_risk]
        }
        
        # Store individual analyses
        self.results['individual_analyses'] = analyses
        
        return self.results
    
    def save_results(self, filename: str = None):
        """Save benchmark results to JSON file"""
        
        if filename is None:
            filename = f".github/benchmarks/results/{self.session_id}-savage-report.json"
        
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"💾 Savage benchmark report saved to: {filename}")
        return filename

if __name__ == "__main__":
    # Commands selected for savage analysis
    commands_to_test = [
        'java-rapid-implementation.md',
        'adhd-hyperfocus-guardian.md', 
        'java-clean-code-generator.md',
        'adhd-morning-assistant.md',
        'safe-code-beautifier.md'
    ]
    
    benchmarker = SavageCommandBenchmarker()
    results = benchmarker.run_full_benchmark(commands_to_test)
    report_file = benchmarker.save_results()
    
    print("\n" + "=" * 60)
    print("🎯 SAVAGE BENCHMARK COMPLETE")
    print(f"📊 Report saved: {report_file}")
    print("=" * 60)