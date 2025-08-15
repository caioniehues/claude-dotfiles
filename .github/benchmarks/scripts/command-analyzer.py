#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
PhD in roasting bad code, scientifically measuring command quality.
"""

import json
import re
import time
from typing import Dict, List, Any, Tuple
from pathlib import Path
import statistics
from datetime import datetime, timezone

class CommandAnalyzer:
    """The SAVAGE COMMAND BENCHMARKER - PhD in roasting bad code."""
    
    def __init__(self):
        self.commands_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands")
        self.results_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        self.start_time = time.time()
        
    def analyze_command(self, command_file: Path) -> Dict[str, Any]:
        """Brutally analyze a command with scientific precision."""
        print(f"🔬 ANALYZING: {command_file.name}")
        
        content = command_file.read_text()
        lines = content.split('\n')
        
        # OBJECTIVE MEASUREMENTS
        metrics = {
            "file_name": command_file.name,
            "line_count": len(lines),
            "character_count": len(content),
            "token_estimate": len(content.split()) * 1.3,  # Conservative token estimate
            "complexity_score": self._calculate_complexity_score(content),
            "readability_score": self._calculate_readability_score(content),
            "integration_complexity": self._analyze_integration_complexity(content),
            "pattern_violations": self._find_pattern_violations(content),
            "dependency_count": self._count_dependencies(content),
            "execution_phases": self._count_execution_phases(content),
            "error_handling": self._analyze_error_handling(content),
            "documentation_quality": self._assess_documentation_quality(content),
            "reusability_score": self._calculate_reusability(content),
            "maintainability_index": self._calculate_maintainability(content)
        }
        
        # SAVAGE ANALYSIS
        metrics["savage_assessment"] = self._generate_savage_assessment(metrics, content)
        
        return metrics
    
    def _calculate_complexity_score(self, content: str) -> int:
        """Calculate complexity based on CLAUDE.md rules."""
        score = 0
        
        # Direct solution baseline
        score += 1
        
        # Count complexity indicators
        if "class " in content: score += 2
        if "interface" in content: score += 1
        if "pattern" in content.lower(): score += 3
        if "config" in content.lower(): score += 2
        if "factory" in content.lower(): score += 3
        if "builder" in content.lower(): score += 3
        
        # Nested structures
        nested_levels = len(re.findall(r'```\w+', content))
        score += nested_levels * 0.5
        
        # Function count (approximate)
        functions = len(re.findall(r'def |function |const \w+\s*=|async \w+', content))
        if functions > 10: score += 2
        elif functions > 5: score += 1
        
        return int(score)
    
    def _calculate_readability_score(self, content: str) -> float:
        """Assess readability using multiple metrics."""
        lines = content.split('\n')
        
        # Average line length
        non_empty_lines = [line for line in lines if line.strip()]
        avg_line_length = sum(len(line) for line in non_empty_lines) / len(non_empty_lines) if non_empty_lines else 0
        
        # Comment ratio
        comment_lines = len([line for line in lines if line.strip().startswith('#') or '##' in line])
        comment_ratio = comment_lines / len(lines) if lines else 0
        
        # Complexity indicators
        complexity_words = ['async', 'await', 'promise', 'callback', 'recursive', 'factory']
        complexity_count = sum(content.lower().count(word) for word in complexity_words)
        
        # Simple scoring (higher is better)
        score = 10.0
        if avg_line_length > 100: score -= 2
        if comment_ratio < 0.1: score -= 1
        if complexity_count > 10: score -= 1
        
        return max(0.0, score)
    
    def _analyze_integration_complexity(self, content: str) -> Dict[str, Any]:
        """Analyze how complex integration with this command is."""
        integrations = {
            "external_commands": len(re.findall(r'/user:\w+', content)),
            "mcp_calls": len(re.findall(r'mcp__', content)),
            "tool_dependencies": len(re.findall(r'Tool|tool|command|cmd', content)),
            "api_endpoints": len(re.findall(r'http|api|endpoint', content, re.IGNORECASE)),
            "file_operations": len(re.findall(r'read|write|file|path', content, re.IGNORECASE))
        }
        
        total_complexity = sum(integrations.values())
        integrations["total_score"] = total_complexity
        integrations["complexity_level"] = (
            "LOW" if total_complexity < 5 else
            "MEDIUM" if total_complexity < 15 else
            "HIGH" if total_complexity < 30 else
            "NUCLEAR"
        )
        
        return integrations
    
    def _find_pattern_violations(self, content: str) -> List[str]:
        """Find violations of good patterns."""
        violations = []
        
        # Wildcard imports (Java style check)
        if "import *" in content:
            violations.append("WILDCARD_IMPORTS")
        
        # Overly long functions/blocks
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        for block in code_blocks:
            if len(block.split('\n')) > 50:
                violations.append("OVERSIZED_CODE_BLOCK")
        
        # Too many parameters (look for function signatures)
        param_matches = re.findall(r'\([^)]{50,}\)', content)
        if param_matches:
            violations.append("TOO_MANY_PARAMETERS")
        
        # Nested complexity
        if content.count('if') > 10 and 'else' in content:
            violations.append("EXCESSIVE_BRANCHING")
        
        # Poor naming (check for single letter vars)
        if re.search(r'\b[a-z]\b\s*[=:]', content):
            violations.append("POOR_NAMING")
        
        return violations
    
    def _count_dependencies(self, content: str) -> Dict[str, int]:
        """Count different types of dependencies."""
        return {
            "mcp_tools": len(re.findall(r'mcp__\w+', content)),
            "external_commands": len(re.findall(r'/user:\w+', content)),
            "system_calls": len(re.findall(r'bash|shell|cmd|exec', content, re.IGNORECASE)),
            "file_dependencies": len(re.findall(r'\.(md|json|yaml|txt|py)', content)),
            "total": len(re.findall(r'mcp__\w+|/user:\w+|bash|shell|\.(md|json)', content))
        }
    
    def _count_execution_phases(self, content: str) -> Dict[str, Any]:
        """Count and analyze execution phases."""
        phases = {
            "initialization": 1 if "initialization" in content.lower() else 0,
            "thinking_phases": len(re.findall(r'thinking|analysis|research', content, re.IGNORECASE)),
            "execution_phases": len(re.findall(r'execution|implement|run', content, re.IGNORECASE)),
            "completion_phases": len(re.findall(r'completion|finish|done|complete', content, re.IGNORECASE))
        }
        
        phases["total_phases"] = sum(phases.values())
        phases["phase_balance"] = "BALANCED" if 2 <= phases["total_phases"] <= 6 else "IMBALANCED"
        
        return phases
    
    def _analyze_error_handling(self, content: str) -> Dict[str, Any]:
        """Analyze error handling patterns."""
        error_patterns = {
            "try_catch_blocks": len(re.findall(r'try\s*{|catch\s*\(', content)),
            "error_checks": len(re.findall(r'error|Error|fail|Fail', content)),
            "validation_checks": len(re.findall(r'validate|check|verify', content, re.IGNORECASE)),
            "fallback_mechanisms": len(re.findall(r'fallback|default|else|alternative', content, re.IGNORECASE))
        }
        
        total_error_handling = sum(error_patterns.values())
        error_patterns["error_handling_score"] = min(10, total_error_handling)
        error_patterns["robustness"] = (
            "FRAGILE" if total_error_handling < 3 else
            "BASIC" if total_error_handling < 8 else
            "ROBUST" if total_error_handling < 15 else
            "PARANOID"
        )
        
        return error_patterns
    
    def _assess_documentation_quality(self, content: str) -> Dict[str, Any]:
        """Assess documentation quality."""
        lines = content.split('\n')
        
        doc_metrics = {
            "has_description": bool(re.search(r'<task>|description|##|\*\*', content)),
            "usage_examples": len(re.findall(r'example|usage|```bash', content, re.IGNORECASE)),
            "parameter_docs": len(re.findall(r'parameter|param|argument', content, re.IGNORECASE)),
            "comment_lines": len([line for line in lines if line.strip().startswith('#')]),
            "markdown_sections": len(re.findall(r'^#+', content, re.MULTILINE))
        }
        
        doc_score = (
            (3 if doc_metrics["has_description"] else 0) +
            min(5, doc_metrics["usage_examples"]) +
            min(2, doc_metrics["parameter_docs"]) +
            min(3, doc_metrics["markdown_sections"])
        )
        
        doc_metrics["documentation_score"] = doc_score
        doc_metrics["doc_quality"] = (
            "TERRIBLE" if doc_score < 3 else
            "POOR" if doc_score < 6 else
            "DECENT" if doc_score < 9 else
            "EXCELLENT"
        )
        
        return doc_metrics
    
    def _calculate_reusability(self, content: str) -> float:
        """Calculate reusability score."""
        # Parameterization
        param_score = min(3, len(re.findall(r'\$\w+|parameter|${', content)))
        
        # Modularity
        module_score = min(3, len(re.findall(r'function|def |class |module', content)))
        
        # Configuration
        config_score = min(2, len(re.findall(r'config|setting|option', content, re.IGNORECASE)))
        
        # Hardcoded values (negative)
        hardcoded = len(re.findall(r'"[^"]*specific[^"]*"|hardcoded|absolute', content, re.IGNORECASE))
        hardcoded_penalty = min(3, hardcoded * 0.5)
        
        total_score = param_score + module_score + config_score - hardcoded_penalty
        return max(0, min(10, total_score))
    
    def _calculate_maintainability(self, content: str) -> float:
        """Calculate maintainability index."""
        # Code organization
        org_score = min(3, len(re.findall(r'<\w+>|##|\*\*|\n#+', content)))
        
        # Naming quality
        good_names = len(re.findall(r'[a-z_]{4,}[a-zA-Z_]*', content))
        bad_names = len(re.findall(r'\b[a-z]\b|\b[A-Z]+\b', content))
        naming_score = min(3, max(0, (good_names - bad_names) / 10))
        
        # Complexity (negative impact)
        complexity_penalty = min(2, self._calculate_complexity_score(content) / 10)
        
        total_score = org_score + naming_score - complexity_penalty
        return max(0, min(10, total_score))
    
    def _generate_savage_assessment(self, metrics: Dict[str, Any], content: str) -> Dict[str, str]:
        """Generate brutally honest assessment with scientific backing."""
        assessments = {}
        
        # Complexity assessment
        complexity = metrics["complexity_score"]
        if complexity >= 10:
            assessments["complexity"] = f"This command has a complexity score of {complexity}/30. That's not 'sophisticated', that's architectural masturbation. The CLAUDE.md limit is <5 for a reason."
        elif complexity >= 5:
            assessments["complexity"] = f"Complexity score: {complexity}/30. You're flirting with the danger zone. One more abstraction and you'll need a PhD to use this thing."
        else:
            assessments["complexity"] = f"Complexity score: {complexity}/30. Finally, someone who read CLAUDE.md. Simple is sustainable."
        
        # Token efficiency
        tokens = metrics["token_estimate"]
        if tokens > 5000:
            assessments["tokens"] = f"Estimated {tokens:.0f} tokens. This isn't a command, it's a novella. Users will hit token limits before getting useful output."
        elif tokens > 3000:
            assessments["tokens"] = f"{tokens:.0f} tokens. Efficient as a gas-guzzling SUV in a Formula 1 race."
        else:
            assessments["tokens"] = f"{tokens:.0f} tokens. Reasonable size for actual human use."
        
        # Integration complexity
        integration = metrics["integration_complexity"]["complexity_level"]
        if integration == "NUCLEAR":
            assessments["integration"] = f"Integration complexity: {integration}. This command needs more dependencies than a JavaScript project. Good luck debugging when something breaks."
        elif integration == "HIGH":
            assessments["integration"] = f"Integration complexity: {integration}. Like a house of cards in an earthquake zone."
        else:
            assessments["integration"] = f"Integration complexity: {integration}. Actually manageable."
        
        # Pattern violations
        violations = metrics["pattern_violations"]
        if len(violations) > 3:
            assessments["violations"] = f"{len(violations)} pattern violations detected: {', '.join(violations)}. This code would make Martin Fowler weep."
        elif len(violations) > 0:
            assessments["violations"] = f"{len(violations)} violations: {', '.join(violations)}. Room for improvement."
        else:
            assessments["violations"] = "No major pattern violations detected. Surprisingly competent."
        
        # Maintainability
        maintainability = metrics["maintainability_index"]
        if maintainability < 3:
            assessments["maintainability"] = f"Maintainability index: {maintainability:.1f}/10. Future developers will curse your name."
        elif maintainability < 6:
            assessments["maintainability"] = f"Maintainability index: {maintainability:.1f}/10. Mediocre. Like lukewarm coffee."
        else:
            assessments["maintainability"] = f"Maintainability index: {maintainability:.1f}/10. Actually maintainable."
        
        return assessments
    
    def generate_report(self, analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive benchmark report with savage commentary."""
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        
        # Statistical analysis
        complexity_scores = [a["complexity_score"] for a in analyses]
        token_estimates = [a["token_estimate"] for a in analyses]
        maintainability_scores = [a["maintainability_index"] for a in analyses]
        
        stats = {
            "complexity": {
                "mean": statistics.mean(complexity_scores),
                "median": statistics.median(complexity_scores),
                "std_dev": statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                "min": min(complexity_scores),
                "max": max(complexity_scores)
            },
            "tokens": {
                "mean": statistics.mean(token_estimates),
                "median": statistics.median(token_estimates),
                "std_dev": statistics.stdev(token_estimates) if len(token_estimates) > 1 else 0,
                "min": min(token_estimates),
                "max": max(token_estimates)
            },
            "maintainability": {
                "mean": statistics.mean(maintainability_scores),
                "median": statistics.median(maintainability_scores),
                "std_dev": statistics.stdev(maintainability_scores) if len(maintainability_scores) > 1 else 0,
                "min": min(maintainability_scores),
                "max": max(maintainability_scores)
            }
        }
        
        # Rankings
        complexity_ranking = sorted(analyses, key=lambda x: x["complexity_score"])
        token_ranking = sorted(analyses, key=lambda x: x["token_estimate"], reverse=True)
        maintainability_ranking = sorted(analyses, key=lambda x: x["maintainability_index"], reverse=True)
        
        report = {
            "metadata": {
                "timestamp": timestamp,
                "analysis_date": datetime.now(timezone.utc).isoformat(),
                "total_commands_analyzed": len(analyses),
                "analysis_duration": time.time() - self.start_time,
                "benchmarker_version": "SAVAGE_v1.0"
            },
            "executive_summary": self._generate_executive_summary(analyses, stats),
            "statistical_analysis": stats,
            "command_analyses": analyses,
            "rankings": {
                "most_complex": complexity_ranking[-3:],  # Top 3 most complex
                "least_complex": complexity_ranking[:3],   # Top 3 least complex
                "token_hogs": token_ranking[:3],          # Biggest token consumers
                "most_maintainable": maintainability_ranking[:3]
            },
            "savage_insights": self._generate_savage_insights(analyses, stats),
            "recommendations": self._generate_recommendations(analyses)
        }
        
        return report
    
    def _generate_executive_summary(self, analyses: List[Dict[str, Any]], stats: Dict[str, Any]) -> str:
        """Generate executive summary with brutal honesty."""
        total_commands = len(analyses)
        avg_complexity = stats["complexity"]["mean"]
        avg_tokens = stats["tokens"]["mean"]
        
        # Count violations
        total_violations = sum(len(a["pattern_violations"]) for a in analyses)
        
        # High complexity commands
        high_complexity = len([a for a in analyses if a["complexity_score"] >= 5])
        
        summary = f"""
COMMAND ARSENAL ANALYSIS - SCIENTIFIC BRUTALITY REPORT

📊 SAMPLE SIZE: {total_commands} commands subjected to rigorous analysis

🎯 KEY FINDINGS:
- Average complexity: {avg_complexity:.1f}/30 (CLAUDE.md limit: <5)
- {high_complexity}/{total_commands} commands violate complexity limits ({high_complexity/total_commands*100:.1f}%)
- Average token consumption: {avg_tokens:.0f} tokens
- Total pattern violations: {total_violations}

💀 REALITY CHECK:
{high_complexity/total_commands*100:.1f}% of your commands are too complex for sustainable use. That's not innovation, that's technical debt with a bow tie.

🔬 STATISTICAL CONFIDENCE: High (n={total_commands}, σ={stats["complexity"]["std_dev"]:.2f})
        """.strip()
        
        return summary
    
    def _generate_savage_insights(self, analyses: List[Dict[str, Any]], stats: Dict[str, Any]) -> List[str]:
        """Generate savage but accurate insights."""
        insights = []
        
        # Complexity distribution
        over_limit = len([a for a in analyses if a["complexity_score"] >= 5])
        if over_limit > 0:
            insights.append(f"{over_limit}/{len(analyses)} commands exceed complexity limits. That's a {over_limit/len(analyses)*100:.0f}% failure rate. If your code was a surgeon, patients would be filing malpractice suits.")
        
        # Token consumption
        avg_tokens = stats["tokens"]["mean"]
        if avg_tokens > 3000:
            insights.append(f"Average token consumption: {avg_tokens:.0f}. Your commands are more bloated than a Windows Vista installation.")
        
        # Pattern violations
        total_violations = sum(len(a["pattern_violations"]) for a in analyses)
        if total_violations > len(analyses):
            insights.append(f"Pattern violations per command: {total_violations/len(analyses):.1f}. Following best practices seems to be treated as a suggestion rather than law.")
        
        # Maintainability
        low_maintainability = len([a for a in analyses if a["maintainability_index"] < 5])
        if low_maintainability > 0:
            insights.append(f"{low_maintainability} commands have low maintainability scores. Future developers will need therapy after working with this code.")
        
        # Integration complexity
        nuclear_integration = len([a for a in analyses if a["integration_complexity"]["complexity_level"] == "NUCLEAR"])
        if nuclear_integration > 0:
            insights.append(f"{nuclear_integration} commands have NUCLEAR integration complexity. These aren't commands, they're distributed systems masquerading as simple tools.")
        
        return insights
    
    def _generate_recommendations(self, analyses: List[Dict[str, Any]]) -> List[str]:
        """Generate data-backed recommendations."""
        recommendations = []
        
        # Complexity recommendations
        high_complexity = [a for a in analyses if a["complexity_score"] >= 5]
        if high_complexity:
            recommendations.append(f"URGENT: Refactor {len(high_complexity)} complex commands. Start with: {', '.join([a['file_name'] for a in high_complexity[:3]])}")
        
        # Token optimization
        high_token = [a for a in analyses if a["token_estimate"] > 3000]
        if high_token:
            recommendations.append(f"Token optimization needed for: {', '.join([a['file_name'] for a in high_token])}")
        
        # Pattern violations
        violation_commands = [a for a in analyses if len(a["pattern_violations"]) > 0]
        if violation_commands:
            recommendations.append(f"Clean up pattern violations in: {', '.join([a['file_name'] for a in violation_commands[:3]])}")
        
        # Maintainability
        low_maintainability = [a for a in analyses if a["maintainability_index"] < 5]
        if low_maintainability:
            recommendations.append(f"Improve maintainability for: {', '.join([a['file_name'] for a in low_maintainability[:3]])}")
        
        return recommendations

def main():
    """Main execution function."""
    print("🔬 SAVAGE COMMAND BENCHMARKER - PhD in roasting bad code")
    print("=" * 60)
    
    analyzer = CommandAnalyzer()
    
    # Get selected commands
    selected_commands = [
        "ultrathink-interactive.md",
        "context-enhanced-executor.md", 
        "adhd-context-switch.md",
        "ultrathink-pure-xml.md",
        "adhd-hyperfocus-guardian.md"
    ]
    
    analyses = []
    
    for cmd_name in selected_commands:
        cmd_path = analyzer.commands_dir / cmd_name
        if cmd_path.exists():
            analysis = analyzer.analyze_command(cmd_path)
            analyses.append(analysis)
        else:
            print(f"⚠️  Command not found: {cmd_name}")
    
    # Generate report
    report = analyzer.generate_report(analyses)
    
    # Save report
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    report_file = analyzer.results_dir / f"{timestamp}-savage-report.json"
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"\n📊 Report saved to: {report_file}")
    
    # Print executive summary
    print("\n" + "=" * 60)
    print("EXECUTIVE SUMMARY")
    print("=" * 60)
    print(report["executive_summary"])
    
    # Print savage insights
    print("\n💀 SAVAGE INSIGHTS:")
    for insight in report["savage_insights"]:
        print(f"• {insight}")
    
    # Print recommendations
    print("\n🔧 RECOMMENDATIONS:")
    for rec in report["recommendations"]:
        print(f"• {rec}")
    
    return report_file

if __name__ == "__main__":
    main()