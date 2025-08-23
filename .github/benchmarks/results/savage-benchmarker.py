#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER v2.0 - The PhD Roaster

Scientifically measures and brutally judges Claude commands.
No feelings spared, only cold hard data and savage truths.
"""

import json
import re
import statistics
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass 
class CommandMetrics:
    name: str
    file_size_bytes: int
    line_count: int
    thinking_blocks: int
    complexity_score: float
    readability_score: float
    pattern_compliance: float
    mcp_integration: bool
    error_recovery: bool
    documentation_quality: float
    reusability_score: float
    token_estimate: int
    performance_class: str
    savage_rating: str
    improvement_potential: float

class SavageBenchmarker:
    def __init__(self):
        self.commands_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands")
        
        self.savage_ratings_explanation = {
            "LEGENDARY": "This command is so good it makes other commands cry with shame.",
            "EXCELLENT": "Solid work. Your future self won't hate you for writing this.", 
            "GOOD": "Not terrible, but there's room for growth. Like a lot of room.",
            "MEDIOCRE": "This command exists. That's about all the praise I can muster.",
            "POOR": "I've seen better code written by caffeinated squirrels.",
            "CATASTROPHIC": "This isn't code, it's a crime against humanity. Delete it. Now."
        }
    
    def analyze_command(self, filepath: Path) -> CommandMetrics:
        """Surgically analyze a command file"""
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic metrics
        file_size = len(content.encode('utf-8'))
        line_count = len(content.splitlines())
        
        # Thinking architecture analysis
        thinking_blocks = len(re.findall(r'<.*?thinking.*?>', content, re.IGNORECASE))
        
        # Complexity scoring (based on CLAUDE.md rules)
        complexity_score = 1.0  # Base score
        if 'mcp__' in content: complexity_score += 0.5
        if 'sequential' in content.lower(): complexity_score += 1.0
        if thinking_blocks == 0: complexity_score += 3.0  # Huge penalty
        elif thinking_blocks > 10: complexity_score += 1.0  # Over-engineering
        
        pattern_count = len(re.findall(r'orchestration|detection|routing|wrapper', content, re.IGNORECASE))
        complexity_score += pattern_count * 0.3
        
        if line_count > 500: complexity_score += 1.5
        elif line_count > 300: complexity_score += 0.8
        
        # Readability assessment
        readability_score = 10.0
        if '<task>' not in content: readability_score -= 2.0
        if '<context>' not in content: readability_score -= 2.0
        if 'example' not in content.lower(): readability_score -= 1.5
        
        # Pattern compliance (CLAUDE.md adherence)
        pattern_compliance = 0.0
        required_patterns = {
            r'<task>.*?\$ARGUMENTS': 2.5,
            r'<context>': 2.0,
            r'thinking.*orchestration': 2.5,
            r'complexity.*detection': 2.0,
            r'usage.*example': 1.0
        }
        
        for pattern, points in required_patterns.items():
            if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                pattern_compliance += points
        
        # MCP integration
        mcp_integration = 'mcp__' in content
        
        # Error recovery mechanisms
        error_recovery = any(term in content.lower() for term in [
            'error', 'recovery', 'fallback', 'validation', 'exception'
        ])
        
        # Documentation quality
        doc_quality = 0.0
        if '<context>' in content: doc_quality += 2.0
        if 'example' in content.lower(): doc_quality += 2.5
        if 'usage' in content.lower(): doc_quality += 2.0
        doc_sections = ['description', 'parameters', 'notes', 'integration']
        doc_quality += sum(1.0 for section in doc_sections if section in content.lower())
        
        # Reusability assessment
        reusability = 5.0
        if '$ARGUMENTS' in content: reusability += 1.5
        param_count = len(re.findall(r'\$\{[^}]+\}|\$[A-Z_]+|--\w+', content))
        reusability += min(param_count * 0.3, 2.0)
        hardcoded_count = len(re.findall(r'https?://|/[a-z/]+|"[^"]*"', content))
        reusability -= min(hardcoded_count * 0.2, 2.5)
        
        # Token estimation (rough)
        token_estimate = len(content) // 4
        
        # Performance classification
        if thinking_blocks == 0:
            performance_class = "BRAINDEAD"
        elif thinking_blocks < 3 and complexity_score > 5:
            performance_class = "OVERTHOUGHT" 
        elif pattern_compliance < 3:
            performance_class = "NONCOMPLIANT"
        elif complexity_score < 3 and pattern_compliance > 7:
            performance_class = "OPTIMIZED"
        else:
            performance_class = "STANDARD"
        
        # Savage rating calculation
        weights = {'complexity': 0.15, 'readability': 0.25, 'compliance': 0.30, 'documentation': 0.15, 'reusability': 0.15}
        normalized_complexity = max(0, 10 - complexity_score)
        
        weighted_score = (
            normalized_complexity * weights['complexity'] +
            readability_score * weights['readability'] +
            pattern_compliance * weights['compliance'] +
            doc_quality * weights['documentation'] +
            reusability * weights['reusability']
        )
        
        if weighted_score >= 9.0: savage_rating = "LEGENDARY"
        elif weighted_score >= 7.5: savage_rating = "EXCELLENT"  
        elif weighted_score >= 6.0: savage_rating = "GOOD"
        elif weighted_score >= 4.0: savage_rating = "MEDIOCRE"
        elif weighted_score >= 2.0: savage_rating = "POOR"
        else: savage_rating = "CATASTROPHIC"
        
        # Improvement potential
        current_quality = (readability_score + pattern_compliance + doc_quality) / 3
        improvement_potential = max(0, (10 - current_quality) * 10)
        
        return CommandMetrics(
            name=filepath.stem,
            file_size_bytes=file_size,
            line_count=line_count,
            thinking_blocks=thinking_blocks,
            complexity_score=complexity_score,
            readability_score=readability_score,
            pattern_compliance=pattern_compliance,
            mcp_integration=mcp_integration,
            error_recovery=error_recovery,
            documentation_quality=doc_quality,
            reusability_score=reusability,
            token_estimate=token_estimate,
            performance_class=performance_class,
            savage_rating=savage_rating,
            improvement_potential=improvement_potential
        )
    
    def generate_savage_commentary(self, metrics: CommandMetrics) -> str:
        """Generate PhD-level brutal commentary"""
        
        base_comment = self.savage_ratings_explanation[metrics.savage_rating]
        comments = [f"**{metrics.savage_rating}**: {base_comment}"]
        
        # Specific roasting
        if metrics.thinking_blocks == 0:
            comments.append("🧠 **BRAINDEAD**: Zero thinking blocks. This has the intelligence of a brick.")
        
        if metrics.pattern_compliance < 5.0:
            comments.append(f"📋 **NONCOMPLIANT**: {metrics.pattern_compliance:.1f}/10 pattern compliance. Did you read CLAUDE.md or just pretend to?")
        
        if metrics.complexity_score > 6.0:
            comments.append(f"🔥 **OVERCOMPLICATED**: {metrics.complexity_score:.1f}/10 complexity. Simplicity died for your sins.")
        
        if metrics.documentation_quality < 4.0:
            comments.append(f"📚 **UNDOCUMENTED**: {metrics.documentation_quality:.1f}/10 documentation. Future you will hunt present you down.")
        
        if metrics.token_estimate > 2000:
            comments.append(f"💸 **TOKEN WASTE**: {metrics.token_estimate} estimated tokens. Efficiency is apparently optional.")
        
        return " ".join(comments)
    
    def benchmark_commands(self, command_files: List[str]) -> Dict[str, Any]:
        """Run the complete savage benchmark suite"""
        
        print("🚨 SAVAGE BENCHMARKER v2.0 - Preparing for Scientific Roasting")
        print("=" * 70)
        
        results = []
        start_time = datetime.now()
        
        for cmd_file in command_files:
            cmd_path = self.commands_dir / cmd_file
            if cmd_path.exists():
                print(f"🔬 Analyzing {cmd_file}...")
                metrics = self.analyze_command(cmd_path)
                savage_commentary = self.generate_savage_commentary(metrics)
                
                # Calculate confidence score
                confidence = (
                    (10 - metrics.complexity_score) * 0.15 +
                    metrics.readability_score * 0.25 +
                    metrics.pattern_compliance * 0.30 +
                    metrics.documentation_quality * 0.15 +
                    metrics.reusability_score * 0.15
                ) * 10
                
                results.append({
                    "command_name": metrics.name,
                    "metrics": asdict(metrics),
                    "savage_commentary": savage_commentary,
                    "confidence_score": confidence,
                    "recommendations": self._get_recommendations(metrics)
                })
        
        # Calculate aggregate stats
        if results:
            complexity_scores = [r["metrics"]["complexity_score"] for r in results]
            confidence_scores = [r["confidence_score"] for r in results] 
            thinking_blocks = [r["metrics"]["thinking_blocks"] for r in results]
            
            stats = {
                "complexity": {
                    "mean": statistics.mean(complexity_scores),
                    "stdev": statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                    "median": statistics.median(complexity_scores)
                },
                "confidence": {
                    "mean": statistics.mean(confidence_scores),
                    "stdev": statistics.stdev(confidence_scores) if len(confidence_scores) > 1 else 0,
                    "median": statistics.median(confidence_scores)
                },
                "thinking_blocks": {
                    "mean": statistics.mean(thinking_blocks),
                    "total": sum(thinking_blocks)
                }
            }
            
            # Generate savage summary
            avg_confidence = stats["confidence"]["mean"]
            if avg_confidence >= 70:
                summary = f"🎉 DECENT: {avg_confidence:.1f}% average confidence. Surprisingly not terrible."
            elif avg_confidence >= 50:
                summary = f"😐 MEDIOCRE: {avg_confidence:.1f}% average confidence. Peak averageness achieved."
            else:
                summary = f"💀 DISASTER: {avg_confidence:.1f}% average confidence. This is a quality catastrophe."
        else:
            stats = {}
            summary = "No commands analyzed. Coward."
        
        duration = (datetime.now() - start_time).total_seconds()
        
        return {
            "benchmark_metadata": {
                "timestamp": start_time.isoformat(),
                "version": "2.0-savage",
                "duration_seconds": duration,
                "commands_analyzed": len(results)
            },
            "results": results,
            "aggregate_statistics": stats,
            "savage_summary": summary,
            "rankings": self._generate_rankings(results)
        }
    
    def _get_recommendations(self, metrics: CommandMetrics) -> List[str]:
        """Generate brutal but helpful recommendations"""
        recs = []
        
        if metrics.thinking_blocks < 3:
            recs.append("Add more thinking blocks. Thinking-first is mandatory, not optional.")
        
        if metrics.pattern_compliance < 7:
            recs.append("Follow CLAUDE.md patterns. They exist for a reason.")
        
        if metrics.complexity_score > 5:
            recs.append("Simplify. Apply the 3-Question Rule ruthlessly.")
        
        if metrics.documentation_quality < 6:
            recs.append("Write documentation. Your future self will thank you.")
        
        if not metrics.mcp_integration and metrics.complexity_score > 4:
            recs.append("Consider MCP integration for complex operations.")
        
        if metrics.improvement_potential > 50:
            recs.append("Major refactoring needed. Current quality is unacceptable.")
        
        return recs
    
    def _generate_rankings(self, results: List[Dict]) -> Dict[str, List[str]]:
        """Generate command rankings by various metrics"""
        if not results:
            return {}
        
        return {
            "best_overall": [r["command_name"] for r in sorted(results, key=lambda x: x["confidence_score"], reverse=True)],
            "most_complex": [r["command_name"] for r in sorted(results, key=lambda x: x["metrics"]["complexity_score"], reverse=True)],
            "most_compliant": [r["command_name"] for r in sorted(results, key=lambda x: x["metrics"]["pattern_compliance"], reverse=True)],
            "best_documented": [r["command_name"] for r in sorted(results, key=lambda x: x["metrics"]["documentation_quality"], reverse=True)]
        }

def main():
    """Execute the savage benchmark"""
    selected_commands = [
        "intelligent-code-enhancer.md",
        "ultrathink-hybrid-mcp.md", 
        "java-rapid-implementation.md",
        "ultrathink-interactive.md",
        "generate-thinking-command.md"
    ]
    
    benchmarker = SavageBenchmarker()
    results = benchmarker.benchmark_commands(selected_commands)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{timestamp}-savage-report.json"
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🔥 SAVAGE BENCHMARKING COMPLETE")
    print(f"📁 Report saved: {output_file}")
    print(f"📊 Commands analyzed: {len(selected_commands)}")
    
    return output_file

if __name__ == "__main__":
    main()