#!/usr/bin/env python3
"""
DETAILED SAVAGE ANALYSIS with Token Estimation and Performance Metrics
Scientific brutality with statistical rigor
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Any
import statistics

class DetailedBenchmarkAnalyzer:
    """The Advanced Savage - deeper metrics, harsher truths"""
    
    def __init__(self):
        # Token estimation coefficients (based on GPT-4 tokenization patterns)
        self.chars_per_token = 4.0  # Average for English text
        self.xml_token_multiplier = 1.3  # XML adds overhead
        
    def estimate_tokens(self, content: str) -> Dict[str, int]:
        """Estimate input/output token consumption"""
        # Base token estimation
        base_tokens = len(content) / self.chars_per_token
        
        # XML overhead
        xml_tags = len(re.findall(r'<[^/].*?>', content))
        xml_overhead = xml_tags * 2  # Each tag adds ~2 tokens overhead
        
        # Thinking blocks are input-heavy
        thinking_content = ''.join(re.findall(r'<thinking.*?</thinking>', content, re.DOTALL))
        thinking_tokens = len(thinking_content) / self.chars_per_token * 1.2
        
        return {
            'estimated_input_tokens': int(base_tokens + xml_overhead),
            'estimated_thinking_tokens': int(thinking_tokens),
            'estimated_xml_overhead': int(xml_overhead),
            'total_token_burden': int(base_tokens + xml_overhead + thinking_tokens)
        }
        
    def analyze_usability(self, content: str) -> Dict[str, Any]:
        """Assess actual usability and practicality"""
        # Count action-oriented vs thinking-oriented content
        action_patterns = [
            r'Read\s+', r'Write\s+', r'Edit\s+', r'Bash\s+', r'Grep\s+',
            r'Glob\s+', r'Create\s+', r'Delete\s+', r'Move\s+'
        ]
        
        thinking_patterns = [
            r'<thinking>', r'<.*?_thinking>', r'reasoning', r'assessment',
            r'analysis', r'evaluation', r'consideration'
        ]
        
        action_count = sum(len(re.findall(pattern, content, re.IGNORECASE)) 
                          for pattern in action_patterns)
        thinking_count = sum(len(re.findall(pattern, content, re.IGNORECASE)) 
                            for pattern in thinking_patterns)
        
        # Calculate talk-to-action ratio
        total_content = action_count + thinking_count
        action_ratio = (action_count / total_content * 100) if total_content else 0
        
        return {
            'action_directives': action_count,
            'thinking_directives': thinking_count,
            'action_ratio_percent': action_ratio,
            'talk_to_action_ratio': (thinking_count / action_count) if action_count else float('inf'),
            'usability_score': min(100, action_ratio * 2)  # Higher is better
        }
        
    def calculate_complexity_score(self, content: str) -> Dict[str, Any]:
        """Apply CLAUDE.md complexity scoring rules"""
        lines = content.splitlines()
        
        # Count complexity contributors (from CLAUDE.md standards)
        classes = len(re.findall(r'class\s+\w+', content))
        interfaces = len(re.findall(r'interface\s+\w+', content))
        patterns = len(re.findall(r'pattern|Pattern|Factory|Builder|Strategy', content))
        configs = len(re.findall(r'config|Config|\.json|\.yaml|\.xml', content))
        abstractions = len(re.findall(r'abstract|Abstract|extends|implements', content))
        
        # CLAUDE.md scoring
        score = 1  # Base direct solution
        score += classes * 2
        score += interfaces * 1  
        score += patterns * 3
        score += configs * 2
        score += abstractions * 1
        
        return {
            'complexity_score': score,
            'classes': classes,
            'interfaces': interfaces,
            'patterns': patterns,
            'configs': configs,
            'abstractions': abstractions,
            'violates_complexity_rule': score >= 5,
            'simplicity_violation_severity': max(0, score - 4)
        }
        
    def analyze_single_command(self, filepath: str) -> Dict[str, Any]:
        """Comprehensive single-command analysis"""
        with open(filepath, 'r') as f:
            content = f.read()
            
        filename = Path(filepath).name
        
        # Basic metrics
        lines = len(content.splitlines())
        chars = len(content)
        words = len(content.split())
        
        # Advanced analysis
        token_metrics = self.estimate_tokens(content)
        usability_metrics = self.analyze_usability(content)
        complexity_metrics = self.calculate_complexity_score(content)
        
        # Error patterns and anti-patterns
        error_handling = len(re.findall(r'try|catch|except|Error|Exception', content, re.IGNORECASE))
        null_checks = len(re.findall(r'null|None|undefined|optional', content, re.IGNORECASE))
        defensive_patterns = len(re.findall(r'validate|check|verify|assert', content, re.IGNORECASE))
        
        # Documentation vs code ratio
        doc_lines = len([line for line in content.splitlines() if line.strip().startswith('#') or '```' in line])
        doc_ratio = (doc_lines / lines * 100) if lines else 0
        
        return {
            'filename': filename,
            'basic_metrics': {
                'lines': lines,
                'characters': chars,
                'words': words,
                'chars_per_word': chars / words if words else 0
            },
            'token_analysis': token_metrics,
            'usability_analysis': usability_metrics,
            'complexity_analysis': complexity_metrics,
            'quality_metrics': {
                'error_handling_references': error_handling,
                'null_safety_indicators': null_checks,
                'defensive_programming': defensive_patterns,
                'documentation_ratio': doc_ratio
            },
            'efficiency_score': self.calculate_efficiency_score(token_metrics, usability_metrics, complexity_metrics)
        }
        
    def calculate_efficiency_score(self, tokens: Dict, usability: Dict, complexity: Dict) -> float:
        """Calculate overall efficiency score (0-100, higher is better)"""
        # Penalize token bloat
        token_penalty = min(50, tokens['total_token_burden'] / 100)
        
        # Reward high action ratio
        action_bonus = min(30, usability['action_ratio_percent'])
        
        # Penalize complexity violations
        complexity_penalty = complexity['simplicity_violation_severity'] * 10
        
        # Base score
        base_score = 100
        final_score = base_score - token_penalty + action_bonus - complexity_penalty
        
        return max(0, min(100, final_score))
        
    def generate_detailed_roasts(self, analysis: Dict[str, Dict]) -> List[str]:
        """Generate statistically-backed roasts"""
        roasts = []
        
        for filename, data in analysis.items():
            if 'error' in data:
                continue
                
            basic = data['basic_metrics']
            tokens = data['token_analysis'] 
            usability = data['usability_analysis']
            complexity = data['complexity_analysis']
            efficiency = data['efficiency_score']
            
            # Token efficiency roasts
            if tokens['total_token_burden'] > 2000:
                roasts.append(f"🔥 {filename}: {tokens['total_token_burden']} token burden. "
                            f"That's ${tokens['total_token_burden'] * 0.00003:.3f} per execution. "
                            f"Your command costs more than a Starbucks coffee.")
                            
            # Action ratio roasts
            if usability['action_ratio_percent'] < 20:
                roasts.append(f"💬 {filename}: {usability['action_ratio_percent']:.1f}% action ratio. "
                            f"This is a philosophy course, not a command. "
                            f"Talk-to-action ratio: {usability['talk_to_action_ratio']:.1f}:1")
                            
            # Complexity violations
            if complexity['violates_complexity_rule']:
                roasts.append(f"🚨 {filename}: Complexity score {complexity['complexity_score']} "
                            f"(limit: 4). Violates CLAUDE.md standards by "
                            f"{complexity['simplicity_violation_severity']} points. "
                            f"Even your own rules can't contain this chaos.")
                            
            # Efficiency assessment  
            if efficiency < 40:
                roasts.append(f"⚰️ {filename}: Efficiency score {efficiency:.1f}/100. "
                            f"This command is clinically dead. Time of death: "
                            f"{basic['lines']} lines of bloated thinking.")
                            
            # XML bloat
            xml_ratio = (tokens['estimated_xml_overhead'] / tokens['estimated_input_tokens'] * 100)
            if xml_ratio > 20:
                roasts.append(f"🏷️ {filename}: {xml_ratio:.1f}% XML overhead. "
                            f"You've recreated XML configuration hell in markdown. Congratulations.")
                            
        return roasts

def main():
    analyzer = DetailedBenchmarkAnalyzer()
    
    commands = [
        'context-enhanced-executor.md',
        'senior-developer-analysis.md',
        'intelligent-refactor-session.md', 
        'analyze-project-architecture.md',
        'java-rapid-implementation.md'
    ]
    
    results = {}
    
    print("🔬 EXECUTING DETAILED SAVAGE ANALYSIS...")
    
    for cmd in commands:
        filepath = f"/home/runner/work/claude-dotfiles/claude-dotfiles/commands/{cmd}"
        try:
            results[cmd] = analyzer.analyze_single_command(filepath)
        except Exception as e:
            results[cmd] = {'error': str(e)}
            
    # Generate comparative statistics
    valid_results = {k: v for k, v in results.items() if 'error' not in v}
    
    efficiency_scores = [data['efficiency_score'] for data in valid_results.values()]
    token_burdens = [data['token_analysis']['total_token_burden'] for data in valid_results.values()]
    action_ratios = [data['usability_analysis']['action_ratio_percent'] for data in valid_results.values()]
    complexity_scores = [data['complexity_analysis']['complexity_score'] for data in valid_results.values()]
    
    # Statistical analysis
    stats = {
        'efficiency_scores': {
            'mean': statistics.mean(efficiency_scores),
            'median': statistics.median(efficiency_scores),  
            'stdev': statistics.stdev(efficiency_scores) if len(efficiency_scores) > 1 else 0,
            'worst': min(efficiency_scores),
            'best': max(efficiency_scores)
        },
        'token_costs': {
            'mean': statistics.mean(token_burdens),
            'total': sum(token_burdens),
            'worst_offender': max(token_burdens),
            'estimated_cost_per_run_usd': sum(token_burdens) * 0.00003
        },
        'action_effectiveness': {
            'mean': statistics.mean(action_ratios),
            'median': statistics.median(action_ratios),
            'worst_talker': min(action_ratios)
        },
        'complexity_violations': {
            'mean': statistics.mean(complexity_scores),
            'violations': sum(1 for score in complexity_scores if score >= 5),
            'worst_violator': max(complexity_scores)
        }
    }
    
    # Generate roasts
    roasts = analyzer.generate_detailed_roasts(results)
    
    # Output results
    print("\n" + "="*80)
    print("🔥 DETAILED SAVAGE ASSESSMENT RESULTS")
    print("="*80)
    
    for roast in roasts:
        print(roast)
        
    print(f"\n📊 STATISTICAL BRUTALITY:")
    print(f"  💰 Total token cost per full execution: ${stats['token_costs']['estimated_cost_per_run_usd']:.4f}")
    print(f"  ⚡ Average efficiency: {stats['efficiency_scores']['mean']:.1f}/100 (σ={stats['efficiency_scores']['stdev']:.1f})")
    print(f"  🎯 Average action ratio: {stats['action_effectiveness']['mean']:.1f}% (lower = more talk, less action)")
    print(f"  🚨 Complexity violations: {stats['complexity_violations']['violations']}/5 commands exceed CLAUDE.md limits")
    print(f"  🏆 Best performer: {stats['efficiency_scores']['best']:.1f}/100 efficiency")
    print(f"  💀 Worst performer: {stats['efficiency_scores']['worst']:.1f}/100 efficiency")
    
    return {
        'detailed_results': results,
        'comparative_statistics': stats,
        'savage_roasts': roasts,
        'analysis_timestamp': '2025-08-19T13:10:30Z'
    }

if __name__ == "__main__":
    report = main()
    
    # Save detailed results
    with open('.github/benchmarks/results/20250819-131030-detailed-report.json', 'w') as f:
        json.dump(report, f, indent=2)
        
    print(f"\n📋 Detailed report saved to: .github/benchmarks/results/20250819-131030-detailed-report.json")