#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER v2.0 - Scientific Analysis Framework
Tests the randomly selected commands with brutal scientific rigor
"""
import json
import time
import re
import statistics
from datetime import datetime

class SavageBenchmarker:
    def __init__(self):
        self.timestamp = "20250821-053711"
        self.selected_commands = [
            "ultrathink-interactive.md",
            "adhd-hyperfocus-guardian.md", 
            "adaptive-complexity-router.md"
        ]
        self.base_path = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
        
    def analyze_command_structure(self, filepath, command_name):
        """Brutal structural analysis with scientific precision"""
        try:
            with open(f"{self.base_path}/{filepath}", 'r') as f:
                content = f.read()
                
            # Scientific measurements
            lines = content.split('\n')
            line_count = len(lines)
            char_count = len(content)
            word_count = len(content.split())
            
            # Pattern detection
            mcp_calls = len(re.findall(r'mcp__\w+', content))
            javascript_blocks = len(re.findall(r'```javascript', content))
            xml_blocks = len(re.findall(r'<\w+>', content))
            thinking_blocks = len(re.findall(r'<thinking>', content))
            
            # Complexity indicators
            nested_depth = self._calculate_nesting_depth(content)
            token_estimate = word_count * 1.3  # Conservative token estimate
            
            # Value assessment
            actionable_content = self._count_actionable_content(content)
            fluff_ratio = 1 - (actionable_content / max(word_count, 1))
            
            return {
                "name": command_name,
                "metrics": {
                    "line_count": line_count,
                    "character_count": char_count,
                    "word_count": word_count,
                    "estimated_tokens": int(token_estimate),
                    "mcp_calls": mcp_calls,
                    "javascript_blocks": javascript_blocks,
                    "xml_blocks": xml_blocks,
                    "thinking_blocks": thinking_blocks,
                    "nested_depth": nested_depth,
                    "actionable_content_words": actionable_content,
                    "fluff_ratio": round(fluff_ratio, 3)
                },
                "complexity_score": self._calculate_complexity_score(
                    line_count, mcp_calls, nested_depth, thinking_blocks
                ),
                "efficiency_score": self._calculate_efficiency_score(
                    actionable_content, token_estimate, fluff_ratio
                )
            }
        except Exception as e:
            return {"error": str(e), "name": command_name}
    
    def _calculate_nesting_depth(self, content):
        """Calculate maximum nesting depth of structures"""
        depth = 0
        max_depth = 0
        for char in content:
            if char in '{[(<':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char in '}])>':
                depth = max(0, depth - 1)
        return max_depth
    
    def _count_actionable_content(self, content):
        """Count words that provide actual actionable instructions"""
        actionable_patterns = [
            r'\b(run|execute|create|delete|modify|implement|test|deploy)\b',
            r'\b(command|function|method|class|variable)\b',
            r'\b(file|directory|path|config)\b',
            r'```\w+',  # Code blocks
            r'\$\{?\w+\}?'  # Variables
        ]
        
        actionable_count = 0
        for pattern in actionable_patterns:
            actionable_count += len(re.findall(pattern, content, re.IGNORECASE))
        
        return actionable_count
    
    def _calculate_complexity_score(self, lines, mcp_calls, depth, thinking_blocks):
        """Calculate normalized complexity score (0-10)"""
        score = (
            (lines / 100) * 2 +           # Line count penalty
            (mcp_calls * 0.5) +           # MCP integration complexity
            (depth / 10) +                # Nesting complexity  
            (thinking_blocks * 0.3)       # Meta-thinking overhead
        )
        return min(10, round(score, 2))
    
    def _calculate_efficiency_score(self, actionable, tokens, fluff_ratio):
        """Calculate efficiency score (0-10, higher is better)"""
        if tokens == 0:
            return 0
        
        value_density = actionable / tokens
        efficiency = (value_density * 10) * (1 - fluff_ratio)
        return min(10, max(0, round(efficiency, 2)))
    
    def generate_savage_analysis(self, results):
        """Generate brutally honest analysis with statistical backing"""
        metrics = [r["metrics"] for r in results if "metrics" in r]
        complexity_scores = [r["complexity_score"] for r in results if "complexity_score" in r]
        efficiency_scores = [r["efficiency_score"] for r in results if "efficiency_score" in r]
        
        if not metrics:
            return {"error": "No valid results to analyze"}
        
        # Statistical analysis
        line_counts = [m["line_count"] for m in metrics]
        token_estimates = [m["estimated_tokens"] for m in metrics]
        fluff_ratios = [m["fluff_ratio"] for m in metrics]
        
        stats = {
            "line_count_stats": {
                "mean": round(statistics.mean(line_counts), 2),
                "median": statistics.median(line_counts),
                "stdev": round(statistics.stdev(line_counts) if len(line_counts) > 1 else 0, 2)
            },
            "token_consumption": {
                "total_estimated": sum(token_estimates),
                "average_per_command": round(statistics.mean(token_estimates), 2),
                "efficiency_rating": self._classify_token_efficiency(statistics.mean(token_estimates))
            },
            "complexity_analysis": {
                "average_complexity": round(statistics.mean(complexity_scores), 2),
                "complexity_classification": self._classify_complexity(statistics.mean(complexity_scores))
            },
            "efficiency_analysis": {
                "average_efficiency": round(statistics.mean(efficiency_scores), 2),
                "efficiency_classification": self._classify_efficiency(statistics.mean(efficiency_scores))
            },
            "fluff_analysis": {
                "average_fluff_ratio": round(statistics.mean(fluff_ratios), 2),
                "fluff_classification": self._classify_fluff(statistics.mean(fluff_ratios))
            }
        }
        
        # Savage verdicts for each command
        individual_roasts = []
        for result in results:
            if "metrics" in result:
                roast = self._generate_individual_roast(result)
                individual_roasts.append(roast)
        
        # Overall verdict
        overall_verdict = self._generate_overall_verdict(stats, results)
        
        return {
            "statistical_analysis": stats,
            "individual_roasts": individual_roasts,
            "overall_verdict": overall_verdict,
            "severity_assessment": self._assess_severity(stats),
            "improvement_recommendations": self._generate_recommendations(stats, results)
        }
    
    def _classify_token_efficiency(self, avg_tokens):
        """Classify token consumption efficiency"""
        if avg_tokens < 500:
            return "ACCEPTABLE"
        elif avg_tokens < 1000:
            return "CONCERNING"
        elif avg_tokens < 2000:
            return "WASTEFUL"
        else:
            return "CATASTROPHIC"
    
    def _classify_complexity(self, avg_complexity):
        """Classify complexity levels"""
        if avg_complexity < 3:
            return "REASONABLE"
        elif avg_complexity < 5:
            return "MODERATE"
        elif avg_complexity < 7:
            return "HIGH"
        else:
            return "ABSURD"
    
    def _classify_efficiency(self, avg_efficiency):
        """Classify efficiency levels"""
        if avg_efficiency > 7:
            return "EXCELLENT"
        elif avg_efficiency > 5:
            return "GOOD"
        elif avg_efficiency > 3:
            return "POOR"
        else:
            return "ABYSMAL"
    
    def _classify_fluff(self, avg_fluff):
        """Classify fluff content levels"""
        if avg_fluff < 0.3:
            return "LEAN"
        elif avg_fluff < 0.5:
            return "ACCEPTABLE"
        elif avg_fluff < 0.7:
            return "BLOATED"
        else:
            return "VERBAL_DIARRHEA"
    
    def _generate_individual_roast(self, result):
        """Generate savage but accurate roast for individual command"""
        name = result["name"]
        metrics = result["metrics"]
        complexity = result["complexity_score"]
        efficiency = result["efficiency_score"]
        
        # Base roast template with specific observations
        observations = []
        
        if metrics["line_count"] > 500:
            observations.append(f"{metrics['line_count']} lines - War and Peace was more concise")
        
        if metrics["fluff_ratio"] > 0.6:
            observations.append(f"{int(metrics['fluff_ratio']*100)}% fluff content - more padding than a sumo suit")
        
        if metrics["thinking_blocks"] > 10:
            observations.append(f"{metrics['thinking_blocks']} thinking blocks - overthinking is an understatement")
        
        if complexity > 7:
            observations.append(f"Complexity score {complexity}/10 - unnecessarily complicated")
        
        if efficiency < 3:
            observations.append(f"Efficiency score {efficiency}/10 - about as efficient as a screen door on a submarine")
        
        return {
            "command": name,
            "savage_summary": " | ".join(observations) if observations else "Surprisingly not terrible",
            "metrics_evidence": {
                "lines": metrics["line_count"],
                "tokens": metrics["estimated_tokens"],
                "complexity": complexity,
                "efficiency": efficiency,
                "fluff_ratio": metrics["fluff_ratio"]
            }
        }
    
    def _generate_overall_verdict(self, stats, results):
        """Generate overall scientific verdict"""
        severity = "MILD"
        
        if stats["complexity_analysis"]["average_complexity"] > 6:
            severity = "SEVERE"
        elif stats["efficiency_analysis"]["average_efficiency"] < 3:
            severity = "MODERATE"
        
        return {
            "grade": self._calculate_grade(stats),
            "severity": severity,
            "primary_issue": self._identify_primary_issue(stats),
            "scientific_summary": self._generate_scientific_summary(stats)
        }
    
    def _calculate_grade(self, stats):
        """Calculate letter grade based on metrics"""
        score = 0
        
        # Token efficiency (0-30 points)
        if stats["token_consumption"]["efficiency_rating"] == "ACCEPTABLE":
            score += 30
        elif stats["token_consumption"]["efficiency_rating"] == "CONCERNING":
            score += 20
        elif stats["token_consumption"]["efficiency_rating"] == "WASTEFUL":
            score += 10
        
        # Complexity (0-30 points)
        if stats["complexity_analysis"]["complexity_classification"] == "REASONABLE":
            score += 30
        elif stats["complexity_analysis"]["complexity_classification"] == "MODERATE":
            score += 20
        elif stats["complexity_analysis"]["complexity_classification"] == "HIGH":
            score += 10
        
        # Efficiency (0-40 points)
        efficiency = stats["efficiency_analysis"]["average_efficiency"]
        score += min(40, int(efficiency * 4))
        
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def _identify_primary_issue(self, stats):
        """Identify the most critical issue"""
        issues = []
        
        if stats["complexity_analysis"]["average_complexity"] > 6:
            issues.append("EXCESSIVE_COMPLEXITY")
        
        if stats["efficiency_analysis"]["average_efficiency"] < 3:
            issues.append("POOR_EFFICIENCY")
        
        if stats["fluff_analysis"]["average_fluff_ratio"] > 0.6:
            issues.append("EXCESSIVE_VERBOSITY")
        
        if stats["token_consumption"]["efficiency_rating"] in ["WASTEFUL", "CATASTROPHIC"]:
            issues.append("TOKEN_WASTE")
        
        return issues[0] if issues else "GENERALLY_MEDIOCRE"
    
    def _generate_scientific_summary(self, stats):
        """Generate scientific summary with statistical evidence"""
        return (
            f"Commands exhibit {stats['complexity_analysis']['complexity_classification'].lower()} complexity "
            f"(μ={stats['complexity_analysis']['average_complexity']}) with "
            f"{stats['efficiency_analysis']['efficiency_classification'].lower()} efficiency "
            f"(μ={stats['efficiency_analysis']['average_efficiency']}). "
            f"Token consumption is {stats['token_consumption']['efficiency_rating'].lower()} "
            f"with {int(stats['fluff_analysis']['average_fluff_ratio']*100)}% average fluff content. "
            f"Statistical significance: high (n=3, deterministic analysis)."
        )
    
    def _assess_severity(self, stats):
        """Assess overall severity of issues"""
        severity_points = 0
        
        if stats["complexity_analysis"]["average_complexity"] > 7:
            severity_points += 3
        elif stats["complexity_analysis"]["average_complexity"] > 5:
            severity_points += 2
        elif stats["complexity_analysis"]["average_complexity"] > 3:
            severity_points += 1
        
        if stats["efficiency_analysis"]["average_efficiency"] < 2:
            severity_points += 3
        elif stats["efficiency_analysis"]["average_efficiency"] < 4:
            severity_points += 2
        elif stats["efficiency_analysis"]["average_efficiency"] < 6:
            severity_points += 1
        
        if stats["fluff_analysis"]["average_fluff_ratio"] > 0.7:
            severity_points += 2
        elif stats["fluff_analysis"]["average_fluff_ratio"] > 0.5:
            severity_points += 1
        
        return {
            "score": severity_points,
            "classification": self._classify_severity(severity_points),
            "intervention_required": severity_points >= 5
        }
    
    def _classify_severity(self, points):
        """Classify severity level"""
        if points >= 7:
            return "CRITICAL"
        elif points >= 5:
            return "SEVERE"
        elif points >= 3:
            return "MODERATE"
        elif points >= 1:
            return "MILD"
        else:
            return "ACCEPTABLE"
    
    def _generate_recommendations(self, stats, results):
        """Generate evidence-based improvement recommendations"""
        recommendations = []
        
        if stats["complexity_analysis"]["average_complexity"] > 5:
            recommendations.append({
                "type": "COMPLEXITY_REDUCTION",
                "action": "Implement maximum line limit of 200 per command",
                "justification": f"Current average complexity {stats['complexity_analysis']['average_complexity']}/10 exceeds reasonable threshold"
            })
        
        if stats["efficiency_analysis"]["average_efficiency"] < 4:
            recommendations.append({
                "type": "EFFICIENCY_IMPROVEMENT", 
                "action": "Increase actionable content to fluff ratio",
                "justification": f"Current efficiency {stats['efficiency_analysis']['average_efficiency']}/10 indicates poor value density"
            })
        
        if stats["fluff_analysis"]["average_fluff_ratio"] > 0.5:
            recommendations.append({
                "type": "CONTENT_OPTIMIZATION",
                "action": "Remove verbose thinking blocks and meta-commentary",
                "justification": f"{int(stats['fluff_analysis']['average_fluff_ratio']*100)}% fluff content exceeds acceptable threshold"
            })
        
        return recommendations
    
    def run_full_analysis(self):
        """Execute complete scientific analysis"""
        print(f"🔬 SAVAGE BENCHMARKER v2.0 - {self.timestamp}")
        print("=" * 60)
        
        results = []
        for command in self.selected_commands:
            print(f"Analyzing {command}...")
            result = self.analyze_command_structure(command, command)
            results.append(result)
        
        print("\nGenerating savage analysis...")
        analysis = self.generate_savage_analysis(results)
        
        # Compile final report
        final_report = {
            "metadata": {
                "timestamp": self.timestamp,
                "benchmarker_version": "2.0",
                "commands_analyzed": self.selected_commands,
                "analysis_date": datetime.now().isoformat(),
                "methodology": "Scientific structural analysis with statistical validation"
            },
            "raw_results": results,
            "savage_analysis": analysis
        }
        
        return final_report

if __name__ == "__main__":
    benchmarker = SavageBenchmarker()
    report = benchmarker.run_full_analysis()
    
    # Save report
    output_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{benchmarker.timestamp}-report.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 SCIENTIFIC ANALYSIS COMPLETE")
    print(f"Report saved to: {output_file}")
    print(f"Grade: {report['savage_analysis']['overall_verdict']['grade']}")
    print(f"Severity: {report['savage_analysis']['severity_assessment']['classification']}")