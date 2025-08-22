#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER v3.0 - PhD Edition
Scientific measurement and brutal assessment of Claude commands
"""

import json
import os
import re
import statistics
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any
import subprocess
import hashlib

class SavageBenchmarker:
    def __init__(self, commands_dir: str):
        self.commands_dir = Path(commands_dir)
        self.timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.results = {}
        
        # CLAUDE.md compliance thresholds
        self.MAX_COMPLEXITY = 5
        self.MAX_FUNCTION_LINES = 20
        self.MAX_PARAMS = 3
        self.ADHD_TIME_MULTIPLIER = 1.5
        
        # Performance thresholds (from historical data)
        self.TOKEN_EFFICIENCY_THRESHOLD = 4000
        self.EXECUTION_TIME_THRESHOLD = 4.0
        self.SUCCESS_RATE_THRESHOLD = 85.0
        
    def analyze_command_structure(self, file_path: Path) -> Dict[str, Any]:
        """Parse command structure with savage precision"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Count structural elements
        thinking_blocks = len(re.findall(r'<thinking>.*?</thinking>', content, re.DOTALL))
        xml_blocks = len(re.findall(r'<[^/!][^>]*>.*?</[^>]*>', content, re.DOTALL))
        code_blocks = len(re.findall(r'```.*?```', content, re.DOTALL))
        headers = len(re.findall(r'^#+\s+', content, re.MULTILINE))
        
        # Complexity analysis (CLAUDE.md formula)
        abstractions = xml_blocks + thinking_blocks
        patterns = len(re.findall(r'(factory|builder|strategy|observer|singleton)', content, re.IGNORECASE))
        configs = len(re.findall(r'(\.json|\.yaml|\.yml|\.toml|config)', content, re.IGNORECASE))
        
        complexity_score = len(non_empty_lines) / 20 + abstractions * 2 + patterns * 3 + configs * 2
        
        # Token estimation (more accurate)
        estimated_tokens = len(content) / 3.5  # Updated based on GPT tokenization
        
        # Quality metrics
        unique_concepts = len(set(re.findall(r'\b[A-Z][a-z]+(?:[A-Z][a-z]*)*\b', content)))
        abstract_terms = len(re.findall(r'(abstract|interface|pattern|strategy|framework)', content, re.IGNORECASE))
        
        # ADHD-specific analysis
        cognitive_load = thinking_blocks * 2 + xml_blocks * 0.5 + headers * 0.1
        context_switches = len(re.findall(r'(switch|change|context|focus)', content, re.IGNORECASE))
        
        return {
            'total_lines': len(lines),
            'non_empty_lines': len(non_empty_lines),
            'thinking_blocks': thinking_blocks,
            'xml_blocks': xml_blocks,
            'code_blocks': code_blocks,
            'markdown_headers': headers,
            'complexity_score': round(complexity_score, 2),
            'estimated_tokens': round(estimated_tokens),
            'unique_concepts': unique_concepts,
            'abstract_terms': abstract_terms,
            'cognitive_load': round(cognitive_load, 2),
            'context_switches': context_switches,
            'density_score': len(non_empty_lines) / len(lines) if lines else 0
        }
    
    def calculate_savage_metrics(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate metrics with PhD-level statistical rigor"""
        
        # Complexity violation severity
        complexity_violation = max(0, data['complexity_score'] - self.MAX_COMPLEXITY)
        complexity_risk = "CRITICAL" if complexity_violation > 3 else "HIGH" if complexity_violation > 1 else "LOW"
        
        # Token efficiency (tokens per useful concept)
        token_efficiency = data['estimated_tokens'] / max(1, data['unique_concepts'])
        
        # Cognitive load assessment (ADHD-specific)
        adhd_adjusted_time = data['cognitive_load'] * self.ADHD_TIME_MULTIPLIER
        
        # Maintainability nightmare probability
        nightmare_factors = [
            complexity_violation > 2,  # Too complex
            data['abstract_terms'] > data['unique_concepts'] * 0.3,  # Too abstract
            data['thinking_blocks'] > 3,  # Overthinking
            data['xml_blocks'] > 20  # XML hell
        ]
        nightmare_probability = sum(nightmare_factors) / len(nightmare_factors) * 100
        
        # ROI calculation (arbitrary but scientifically arbitrary)
        maintenance_cost = complexity_violation * 100 + data['abstract_terms'] * 10
        utility_value = data['code_blocks'] * 50 + data['unique_concepts'] * 5
        roi = (utility_value - maintenance_cost) / max(1, maintenance_cost) * 100
        
        return {
            'complexity_violation': complexity_violation,
            'complexity_risk': complexity_risk,
            'token_efficiency': round(token_efficiency, 2),
            'adhd_adjusted_time': round(adhd_adjusted_time, 2),
            'nightmare_probability': round(nightmare_probability, 2),
            'roi_percentage': round(roi, 2),
            'grade': self.calculate_grade(data, complexity_violation, token_efficiency, nightmare_probability)
        }
    
    def calculate_grade(self, data: Dict, complexity_violation: float, token_efficiency: float, nightmare_prob: float) -> str:
        """Assign brutal but fair grades"""
        score = 100
        
        # Deductions
        score -= complexity_violation * 20  # -20 per complexity point over limit
        score -= min(30, nightmare_prob)    # Up to -30 for nightmare probability
        score -= max(0, (token_efficiency - 50) / 5)  # Penalty for inefficiency
        
        # Bonuses
        if data['code_blocks'] > data['thinking_blocks']:
            score += 10  # Bonus for doing vs thinking
        if data['density_score'] > 0.8:
            score += 5   # Bonus for conciseness
        
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"
    
    def generate_savage_commentary(self, name: str, metrics: Dict) -> str:
        """Generate brutal but data-backed commentary"""
        comments = []
        
        if metrics['complexity_violation'] > 0:
            comments.append(f"Violates CLAUDE.md complexity limit by {metrics['complexity_violation']:.1f} points. That's not 'intelligent design', that's engineering malpractice.")
        
        if metrics['nightmare_probability'] > 50:
            comments.append(f"{metrics['nightmare_probability']:.1f}% chance this becomes a maintenance nightmare. Those aren't odds, that's a guarantee with statistical confidence.")
        
        if metrics['token_efficiency'] > 100:
            comments.append(f"Burns {metrics['token_efficiency']:.0f} tokens per concept. A junior developer with a thesaurus would be more efficient.")
        
        if metrics['adhd_adjusted_time'] > 10:
            comments.append(f"ADHD-adjusted cognitive load: {metrics['adhd_adjusted_time']:.1f}. This command is basically ADHD kryptonite.")
        
        if metrics['roi_percentage'] < 0:
            comments.append(f"Negative ROI of {metrics['roi_percentage']:.0f}%. This command costs more brain cells than it saves.")
        
        if not comments:
            comments.append("Surprisingly, this doesn't completely suck. Low bar achieved.")
        
        return " ".join(comments)
    
    def benchmark_all_commands(self) -> Dict[str, Any]:
        """Execute full benchmarking suite"""
        print("🔬 SAVAGE BENCHMARKER v3.0 - PhD Edition")
        print("=" * 60)
        
        command_files = list(self.commands_dir.glob("*.md"))
        total_commands = len(command_files)
        
        print(f"Found {total_commands} commands to scientifically roast...")
        
        all_complexity_scores = []
        all_token_counts = []
        all_nightmare_probs = []
        
        for i, cmd_file in enumerate(command_files, 1):
            print(f"Analyzing {cmd_file.name} [{i}/{total_commands}]...")
            
            # Structural analysis
            structure = self.analyze_command_structure(cmd_file)
            
            # Savage metrics
            savage = self.calculate_savage_metrics(structure)
            
            # Commentary
            commentary = self.generate_savage_commentary(cmd_file.name, savage)
            
            # Combine all data
            self.results[cmd_file.name] = {
                'structure': structure,
                'metrics': savage,
                'commentary': commentary,
                'timestamp': self.timestamp
            }
            
            # Collect for statistical analysis
            all_complexity_scores.append(structure['complexity_score'])
            all_token_counts.append(structure['estimated_tokens'])
            all_nightmare_probs.append(savage['nightmare_probability'])
        
        # Calculate statistical summaries
        self.results['_statistical_summary'] = {
            'total_commands': total_commands,
            'complexity_stats': {
                'mean': round(statistics.mean(all_complexity_scores), 2),
                'median': round(statistics.median(all_complexity_scores), 2),
                'stdev': round(statistics.stdev(all_complexity_scores) if len(all_complexity_scores) > 1 else 0, 2),
                'violations': sum(1 for score in all_complexity_scores if score > self.MAX_COMPLEXITY),
                'violation_rate': round(sum(1 for score in all_complexity_scores if score > self.MAX_COMPLEXITY) / total_commands * 100, 1)
            },
            'token_stats': {
                'mean': round(statistics.mean(all_token_counts), 0),
                'median': round(statistics.median(all_token_counts), 0),
                'stdev': round(statistics.stdev(all_token_counts) if len(all_token_counts) > 1 else 0, 0),
                'range': [min(all_token_counts), max(all_token_counts)]
            },
            'nightmare_stats': {
                'mean': round(statistics.mean(all_nightmare_probs), 1),
                'median': round(statistics.median(all_nightmare_probs), 1),
                'high_risk_commands': sum(1 for prob in all_nightmare_probs if prob > 50)
            }
        }
        
        return self.results
    
    def save_results(self, output_file: str = None):
        """Save results with scientific precision"""
        if not output_file:
            output_file = f".github/benchmarks/results/{self.timestamp}-savage-report.json"
        
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n🎯 Savage benchmark report saved to: {output_path}")
        return output_path

if __name__ == "__main__":
    commands_dir = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
    
    benchmarker = SavageBenchmarker(commands_dir)
    results = benchmarker.benchmark_all_commands()
    
    # Print summary stats
    stats = results['_statistical_summary']
    print("\n📊 STATISTICAL SUMMARY - THE BRUTAL TRUTH")
    print("=" * 50)
    print(f"Commands Analyzed: {stats['total_commands']}")
    print(f"Complexity Violations: {stats['complexity_stats']['violations']} ({stats['complexity_stats']['violation_rate']}%)")
    print(f"Mean Complexity: {stats['complexity_stats']['mean']}/5.0 (σ={stats['complexity_stats']['stdev']})")
    print(f"Token Range: {stats['token_stats']['range'][0]} - {stats['token_stats']['range'][1]}")
    print(f"High-Risk Commands: {stats['nightmare_stats']['high_risk_commands']}")
    
    # Save results
    output_path = benchmarker.save_results()
    print(f"\nFull savage analysis available at: {output_path}")