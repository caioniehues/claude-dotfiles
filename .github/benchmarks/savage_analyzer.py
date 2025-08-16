#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
PhD in roasting bad code with SCIENTIFIC PRECISION
"""
import json
import math
import statistics
from datetime import datetime

class SavageAnalyzer:
    def __init__(self, data):
        self.data = data
        self.commands = data['commands']
        self.roasts = []
        
    def calculate_statistics(self):
        """Calculate proper statistical metrics with confidence intervals"""
        
        # Extract metrics for statistical analysis
        tokens = [cmd['estimated_tokens'] for cmd in self.commands.values() if 'estimated_tokens' in cmd]
        complexity = [cmd['complexity_score'] for cmd in self.commands.values() if 'complexity_score' in cmd]
        issues = [cmd['severity_score'] for cmd in self.commands.values() if 'severity_score' in cmd]
        lines = [cmd['lines'] for cmd in self.commands.values() if 'lines' in cmd]
        
        stats = {
            'tokens': {
                'mean': statistics.mean(tokens),
                'median': statistics.median(tokens),
                'stdev': statistics.stdev(tokens) if len(tokens) > 1 else 0,
                'min': min(tokens),
                'max': max(tokens),
                'range': max(tokens) - min(tokens),
                'cv': statistics.stdev(tokens) / statistics.mean(tokens) if len(tokens) > 1 else 0
            },
            'complexity': {
                'mean': statistics.mean(complexity),
                'median': statistics.median(complexity),
                'stdev': statistics.stdev(complexity) if len(complexity) > 1 else 0,
                'min': min(complexity),
                'max': max(complexity),
                'range': max(complexity) - min(complexity),
                'cv': statistics.stdev(complexity) / statistics.mean(complexity) if len(complexity) > 1 else 0
            },
            'severity': {
                'mean': statistics.mean(issues),
                'median': statistics.median(issues),
                'stdev': statistics.stdev(issues) if len(issues) > 1 else 0,
                'total_issues': sum(len(cmd.get('issues', [])) for cmd in self.commands.values()),
                'failure_rate': sum(1 for cmd in self.commands.values() if len(cmd.get('issues', [])) > 0) / len(self.commands)
            },
            'lines': {
                'mean': statistics.mean(lines),
                'median': statistics.median(lines),
                'stdev': statistics.stdev(lines) if len(lines) > 1 else 0,
                'min': min(lines),
                'max': max(lines)
            }
        }
        
        # Calculate confidence intervals (95%)
        n = len(tokens)
        t_stat = 2.776 if n == 5 else 1.96  # t-distribution for small sample
        
        for metric in ['tokens', 'complexity', 'severity', 'lines']:
            if stats[metric]['stdev'] > 0:
                margin_error = t_stat * (stats[metric]['stdev'] / math.sqrt(n))
                stats[metric]['ci_lower'] = stats[metric]['mean'] - margin_error
                stats[metric]['ci_upper'] = stats[metric]['mean'] + margin_error
            else:
                stats[metric]['ci_lower'] = stats[metric]['mean']
                stats[metric]['ci_upper'] = stats[metric]['mean']
                
        return stats
    
    def savage_token_analysis(self, stats):
        """BRUTAL token consumption analysis"""
        roast = "🔥 TOKEN CONSUMPTION SAVAGERY\n"
        roast += "=" * 40 + "\n\n"
        
        avg_tokens = stats['tokens']['mean']
        stdev_tokens = stats['tokens']['stdev']
        cv_tokens = stats['tokens']['cv']
        
        if avg_tokens > 3000:
            roast += f"💸 AVERAGE TOKEN CONSUMPTION: {avg_tokens:.0f} tokens\n"
            roast += f"That's like paying ${avg_tokens * 0.000003:.2f} per execution in Claude API calls.\n"
            roast += f"Your 'rapid' commands are financially slower than hiring an intern.\n\n"
        
        if cv_tokens > 0.5:
            roast += f"📊 COEFFICIENT OF VARIATION: {cv_tokens:.2f}\n"
            roast += f"That's a {cv_tokens*100:.0f}% variance. Your commands are more inconsistent\n"
            roast += f"than a broken random number generator.\n\n"
        
        # Identify the worst offender
        worst_cmd = max(self.commands.items(), key=lambda x: x[1].get('estimated_tokens', 0))
        roast += f"🏆 WORST OFFENDER: {worst_cmd[0]}\n"
        roast += f"Token consumption: {worst_cmd[1]['estimated_tokens']:,} tokens\n"
        roast += f"That's {worst_cmd[1]['estimated_tokens']/avg_tokens:.1f}x the average. Congratulations,\n"
        roast += f"you've created the Hummer of AI commands.\n\n"
        
        return roast
    
    def savage_complexity_analysis(self, stats):
        """BRUTAL complexity analysis"""
        roast = "🧠 COMPLEXITY BRUTALITY REPORT\n"
        roast += "=" * 40 + "\n\n"
        
        avg_complexity = stats['complexity']['mean']
        max_complexity = stats['complexity']['max']
        
        if avg_complexity > 50:
            roast += f"🌪️ AVERAGE COMPLEXITY SCORE: {avg_complexity:.1f}\n"
            roast += f"Your commands have more moving parts than a Swiss watch\n"
            roast += f"designed by someone having a mental breakdown.\n\n"
        
        # Complexity analysis per command
        complexity_crimes = []
        for name, cmd in self.commands.items():
            score = cmd.get('complexity_score', 0)
            if score > 100:
                complexity_crimes.append((name, score, "ARCHITECTURAL DISASTER"))
            elif score > 50:
                complexity_crimes.append((name, score, "OVER-ENGINEERED"))
            elif score > 30:
                complexity_crimes.append((name, score, "UNNECESSARILY COMPLEX"))
        
        if complexity_crimes:
            roast += "🚨 COMPLEXITY HALL OF SHAME:\n"
            for name, score, crime in complexity_crimes:
                roast += f"   • {name}: {score:.1f} ({crime})\n"
            roast += "\n"
        
        # Thinking block analysis
        thinking_blocks = [cmd['patterns'].get('thinking_blocks', 0) for cmd in self.commands.values()]
        avg_thinking = statistics.mean(thinking_blocks) if thinking_blocks else 0
        
        if avg_thinking > 10:
            roast += f"🤔 AVERAGE THINKING BLOCKS: {avg_thinking:.1f}\n"
            roast += f"Your commands think more than Hamlet contemplating suicide.\n"
            roast += f"Sometimes a simple 'if' statement is better than an existential crisis.\n\n"
        
        return roast
    
    def savage_quality_analysis(self, stats):
        """BRUTAL quality assessment"""
        roast = "⚠️ QUALITY ASSESSMENT CARNAGE\n"
        roast += "=" * 40 + "\n\n"
        
        failure_rate = stats['severity']['failure_rate']
        total_issues = stats['severity']['total_issues']
        
        roast += f"💀 FAILURE RATE: {failure_rate*100:.0f}%\n"
        if failure_rate > 0.6:
            roast += f"That's worse than my success rate at predicting cryptocurrency.\n"
            roast += f"More than half your commands have structural issues.\n\n"
        
        roast += f"🐛 TOTAL ISSUES DETECTED: {total_issues}\n"
        roast += f"That averages to {total_issues/len(self.commands):.1f} issues per command.\n"
        if total_issues > 5:
            roast += f"Your code has more red flags than a communist parade.\n\n"
        
        # Specific issue analysis
        all_issues = []
        for cmd in self.commands.values():
            all_issues.extend(cmd.get('issues', []))
        
        if 'EXTREME_COMPLEXITY' in all_issues:
            count = all_issues.count('EXTREME_COMPLEXITY')
            roast += f"🌋 EXTREME COMPLEXITY: {count} commands\n"
            roast += f"You've achieved complexity levels that would make enterprise Java jealous.\n\n"
        
        if 'OVER_THINKING' in all_issues:
            count = all_issues.count('OVER_THINKING')
            roast += f"🧠 OVER-THINKING: {count} commands\n"
            roast += f"Your commands have analysis paralysis worse than a PhD student\n"
            roast += f"choosing a dissertation topic.\n\n"
        
        if 'TOKEN_BLOAT' in all_issues:
            count = all_issues.count('TOKEN_BLOAT')
            roast += f"💰 TOKEN BLOAT: {count} commands\n"
            roast += f"Your prompts are more bloated than a Thanksgiving turkey.\n\n"
        
        return roast
    
    def savage_efficiency_analysis(self):
        """BRUTAL efficiency comparison"""
        roast = "⚡ EFFICIENCY BRUTALITY INDEX\n"
        roast += "=" * 40 + "\n\n"
        
        # Calculate efficiency metrics
        efficiency_scores = []
        for name, cmd in self.commands.items():
            tokens = cmd.get('estimated_tokens', 1)
            complexity = cmd.get('complexity_score', 1)
            issues = len(cmd.get('issues', []))
            
            # Efficiency = 1 / (tokens * complexity * (issues + 1))
            efficiency = 1000000 / (tokens * complexity * (issues + 1))
            efficiency_scores.append((name, efficiency))
        
        # Sort by efficiency (lower is worse)
        efficiency_scores.sort(key=lambda x: x[1])
        
        roast += "🏅 EFFICIENCY RANKING (Higher = Better):\n"
        for i, (name, score) in enumerate(efficiency_scores):
            if i == 0:
                roast += f"   🥇 {name}: {score:.2f} (LEAST TERRIBLE)\n"
            elif i == len(efficiency_scores) - 1:
                roast += f"   💩 {name}: {score:.2f} (EFFICIENCY DISASTER)\n"
            else:
                roast += f"   {i+1}. {name}: {score:.2f}\n"
        
        roast += "\n"
        worst_efficiency = efficiency_scores[0][1]
        best_efficiency = efficiency_scores[-1][1]
        ratio = best_efficiency / worst_efficiency if worst_efficiency > 0 else float('inf')
        
        roast += f"📊 EFFICIENCY RANGE: {ratio:.1f}x difference\n"
        roast += f"Your best command is {ratio:.1f}x more efficient than your worst.\n"
        roast += f"That's like comparing a Tesla to a coal-powered steam engine.\n\n"
        
        return roast
    
    def savage_maintainability_analysis(self):
        """BRUTAL maintainability assessment"""
        roast = "🔧 MAINTAINABILITY APOCALYPSE\n"
        roast += "=" * 40 + "\n\n"
        
        maintainability_scores = [(name, cmd.get('maintainability_score', 0)) 
                                 for name, cmd in self.commands.items()]
        maintainability_scores.sort(key=lambda x: x[1])
        
        avg_maintainability = statistics.mean([score for _, score in maintainability_scores])
        
        roast += f"🔧 AVERAGE MAINTAINABILITY: {avg_maintainability:.1f}/10\n"
        if avg_maintainability < 7:
            roast += f"Your code is less maintainable than a 1987 Yugo.\n"
            roast += f"Future developers will curse your name in languages that don't exist yet.\n\n"
        
        # Worst maintainability offenders
        worst_maintainable = [item for item in maintainability_scores if item[1] < 8]
        if worst_maintainable:
            roast += "🚫 MAINTENANCE NIGHTMARES:\n"
            for name, score in worst_maintainable:
                roast += f"   • {name}: {score:.1f}/10 - "
                if score < 6:
                    roast += "ABANDON HOPE\n"
                elif score < 7:
                    roast += "HAZMAT SUIT REQUIRED\n"
                else:
                    roast += "PROCEED WITH CAUTION\n"
        
        return roast
    
    def generate_recommendations(self):
        """Generate data-backed improvement recommendations"""
        recommendations = "💡 SCIENTIFICALLY-BACKED RECOMMENDATIONS\n"
        recommendations += "=" * 50 + "\n\n"
        
        # Token optimization
        high_token_commands = [name for name, cmd in self.commands.items() 
                              if cmd.get('estimated_tokens', 0) > 3000]
        if high_token_commands:
            recommendations += "🔨 TOKEN DIET REQUIRED:\n"
            for cmd in high_token_commands:
                recommendations += f"   • {cmd}: Reduce by 30% minimum\n"
            recommendations += "\n"
        
        # Complexity reduction
        complex_commands = [name for name, cmd in self.commands.items() 
                           if cmd.get('complexity_score', 0) > 50]
        if complex_commands:
            recommendations += "✂️ COMPLEXITY SURGERY NEEDED:\n"
            for cmd in complex_commands:
                recommendations += f"   • {cmd}: Split into sub-commands\n"
            recommendations += "\n"
        
        # Thinking block optimization
        over_thinking = [name for name, cmd in self.commands.items() 
                        if cmd.get('patterns', {}).get('thinking_blocks', 0) > 10]
        if over_thinking:
            recommendations += "🧠 THINKING DETOX PROGRAM:\n"
            for cmd in over_thinking:
                recommendations += f"   • {cmd}: Reduce thinking blocks by 50%\n"
            recommendations += "\n"
        
        recommendations += "🎯 PRIORITY ACTIONS:\n"
        recommendations += "1. Commands with >3000 tokens: IMMEDIATE diet\n"
        recommendations += "2. Commands with >50 complexity: Split or simplify\n"
        recommendations += "3. Commands with >10 thinking blocks: Streamline logic\n"
        recommendations += "4. Any command with issues: Fix before deployment\n\n"
        
        return recommendations
    
    def calculate_cost_analysis(self, stats):
        """Calculate actual operational costs"""
        cost_analysis = "💰 COST ANALYSIS (PREPARE FOR SHOCK)\n"
        cost_analysis += "=" * 40 + "\n\n"
        
        # Claude pricing (approximate)
        cost_per_token = 0.000003  # $3 per million tokens
        avg_tokens = stats['tokens']['mean']
        
        # Assume 100 executions per month
        monthly_executions = 100
        monthly_cost = avg_tokens * cost_per_token * monthly_executions
        annual_cost = monthly_cost * 12
        
        cost_analysis += f"💸 MONTHLY COST (100 executions): ${monthly_cost:.2f}\n"
        cost_analysis += f"💸 ANNUAL COST: ${annual_cost:.2f}\n"
        cost_analysis += f"💸 COST PER EXECUTION: ${avg_tokens * cost_per_token:.4f}\n\n"
        
        # Compare to manual work
        manual_time_minutes = 30  # Assume 30 minutes manual work
        developer_hourly_rate = 100  # $100/hour
        manual_cost = (manual_time_minutes / 60) * developer_hourly_rate
        
        cost_analysis += f"⏱️ MANUAL ALTERNATIVE: ${manual_cost:.2f} per task\n"
        if avg_tokens * cost_per_token < manual_cost:
            savings = manual_cost - (avg_tokens * cost_per_token)
            cost_analysis += f"✅ SAVINGS: ${savings:.2f} per execution\n"
        else:
            loss = (avg_tokens * cost_per_token) - manual_cost
            cost_analysis += f"❌ LOSS: ${loss:.2f} per execution (worse than manual)\n"
        
        return cost_analysis
    
    def generate_savage_report(self):
        """Generate the complete savage analysis report"""
        stats = self.calculate_statistics()
        
        report = f"""
# 🔥 SAVAGE COMMAND BENCHMARK REPORT 🔥
## Scientific Roasting with PhD-Level Precision

**Benchmark ID**: {self.data['benchmark_id']}
**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Commands Analyzed**: {len(self.commands)}/22 (Random Sample)
**Scientist**: Dr. Savage McBenchmark, PhD in Code Roasting

---

{self.savage_token_analysis(stats)}

{self.savage_complexity_analysis(stats)}

{self.savage_quality_analysis(stats)}

{self.savage_efficiency_analysis()}

{self.savage_maintainability_analysis()}

{self.calculate_cost_analysis(stats)}

{self.generate_recommendations()}

## 📊 STATISTICAL SUMMARY

### Token Consumption
- **Mean**: {stats['tokens']['mean']:.0f} ± {stats['tokens']['stdev']:.0f}
- **95% CI**: [{stats['tokens']['ci_lower']:.0f}, {stats['tokens']['ci_upper']:.0f}]
- **Coefficient of Variation**: {stats['tokens']['cv']:.2f}

### Complexity Metrics
- **Mean Score**: {stats['complexity']['mean']:.1f} ± {stats['complexity']['stdev']:.1f}
- **95% CI**: [{stats['complexity']['ci_lower']:.1f}, {stats['complexity']['ci_upper']:.1f}]
- **Range**: {stats['complexity']['min']:.1f} - {stats['complexity']['max']:.1f}

### Quality Assessment
- **Failure Rate**: {stats['severity']['failure_rate']*100:.0f}%
- **Average Issues per Command**: {stats['severity']['mean']:.1f}
- **Total Issues Detected**: {stats['severity']['total_issues']}

---

## 🎯 VERDICT

Based on rigorous statistical analysis, your command portfolio exhibits:

1. **Token Inefficiency**: Average {stats['tokens']['mean']:.0f} tokens per command
2. **Complexity Disorder**: {stats['severity']['failure_rate']*100:.0f}% of commands have structural issues
3. **Over-Engineering Syndrome**: {len([c for c in self.commands.values() if c.get('complexity_score', 0) > 50])}/{len(self.commands)} commands are unnecessarily complex

**RECOMMENDATION**: Start over. With a simpler approach. And possibly a different career.

---

*Generated by the Savage Command Benchmarker™*
*"Brutally honest since 2025"*
"""
        return report

def main():
    # Load the analysis data
    with open('/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/temp_analysis.json', 'r') as f:
        data = json.load(f)
    
    analyzer = SavageAnalyzer(data)
    return analyzer.generate_savage_report()

if __name__ == '__main__':
    print(main())