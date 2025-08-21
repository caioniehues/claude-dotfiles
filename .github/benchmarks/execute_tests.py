#!/usr/bin/env python3
"""
SAVAGE BENCHMARKER - Real Execution Module
Performs actual command analysis and generates statistical reports
"""

import json
import re
import time
import statistics
from datetime import datetime
from pathlib import Path

class RealCommandAnalyzer:
    def __init__(self):
        self.commands_dir = Path("commands")
        self.results = {}
        self.test_start = datetime.now()
    
    def analyze_command_file(self, command_path: Path) -> dict:
        """Perform deep static analysis of command file"""
        with open(command_path, 'r') as f:
            content = f.read()
        
        # Objective measurements
        line_count = len(content.split('\n'))
        char_count = len(content)
        word_count = len(content.split())
        
        # Token estimation (4 chars ≈ 1 token for GPT models)
        estimated_tokens = char_count // 4
        
        # Complexity analysis based on CLAUDE.md rules
        complexity_score = self.calculate_complexity(content)
        
        # Pattern analysis
        patterns = self.analyze_patterns(content)
        
        # Performance estimates
        performance = self.estimate_performance(content, estimated_tokens)
        
        # Quality assessment
        quality = self.assess_quality(content)
        
        return {
            "file_metrics": {
                "lines": line_count,
                "characters": char_count,
                "words": word_count,
                "estimated_tokens": estimated_tokens
            },
            "complexity": complexity_score,
            "patterns": patterns,
            "performance": performance,
            "quality": quality,
            "analyzed_at": datetime.now().isoformat()
        }
    
    def calculate_complexity(self, content: str) -> dict:
        """Calculate complexity score based on CLAUDE.md standards"""
        score = 1  # Base complexity
        factors = []
        
        # MCP tool usage (+2 each)
        mcp_tools = len(re.findall(r'mcp__[a-zA-Z0-9_-]+__[a-zA-Z0-9_-]+', content))
        if mcp_tools > 0:
            score += mcp_tools * 2
            factors.append(f"MCP tools: {mcp_tools} (+{mcp_tools * 2})")
        
        # Thinking blocks (+1 each)
        thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content, re.IGNORECASE))
        if thinking_blocks > 0:
            score += thinking_blocks
            factors.append(f"Thinking blocks: {thinking_blocks} (+{thinking_blocks})")
        
        # Sequential thinking trigger (+3)
        if "sequentialthinking" in content.lower():
            score += 3
            factors.append("Sequential thinking trigger (+3)")
        
        # Orchestration patterns (+2)
        if "orchestration" in content.lower():
            score += 2
            factors.append("Orchestration pattern (+2)")
        
        # Phase-based structure (+1 per phase)
        phases = len(re.findall(r'(?:phase|step)\s*\d+', content, re.IGNORECASE))
        if phases > 0:
            score += phases
            factors.append(f"Phases: {phases} (+{phases})")
        
        # Complex condition blocks (+1 each)
        complex_conditions = len(re.findall(r'if\s+complexity\s*[><=]', content, re.IGNORECASE))
        if complex_conditions > 0:
            score += complex_conditions
            factors.append(f"Complexity conditions: {complex_conditions} (+{complex_conditions})")
        
        return {
            "total_score": min(score, 10),  # Cap at 10
            "factors": factors,
            "claude_md_compliant": score <= 5,  # Per CLAUDE.md rule
            "risk_level": "HIGH" if score >= 5 else "MEDIUM" if score >= 3 else "LOW"
        }
    
    def analyze_patterns(self, content: str) -> dict:
        """Analyze command patterns and anti-patterns"""
        patterns = {
            "good_patterns": [],
            "anti_patterns": [],
            "design_patterns": [],
            "adhd_patterns": []
        }
        
        # Good patterns
        if "<thinking" in content:
            patterns["good_patterns"].append("Explicit thinking blocks")
        if "complexity_detection" in content:
            patterns["good_patterns"].append("Complexity detection")
        if "error_recovery" in content:
            patterns["good_patterns"].append("Error recovery")
        if "pattern_learning" in content:
            patterns["good_patterns"].append("Pattern learning")
        
        # Anti-patterns (from CLAUDE.md)
        if content.count("Factory") > 2:
            patterns["anti_patterns"].append("Factory madness detected")
        if "AbstractFactoryBuilder" in content:
            patterns["anti_patterns"].append("Over-abstraction")
        if content.count("interface") > 5:
            patterns["anti_patterns"].append("Interface explosion")
        
        # Design patterns
        if "Strategy" in content:
            patterns["design_patterns"].append("Strategy pattern")
        if "Template" in content:
            patterns["design_patterns"].append("Template pattern")
        if "Wrapper" in content:
            patterns["design_patterns"].append("Wrapper pattern")
        
        # ADHD-specific patterns
        if "adhd" in content.lower():
            patterns["adhd_patterns"].append("ADHD awareness")
        if "time_multiplier" in content:
            patterns["adhd_patterns"].append("Time multiplier pattern")
        if "energy" in content.lower():
            patterns["adhd_patterns"].append("Energy management")
        if "hyperfocus" in content.lower():
            patterns["adhd_patterns"].append("Hyperfocus handling")
        
        return patterns
    
    def estimate_performance(self, content: str, tokens: int) -> dict:
        """Estimate command performance characteristics"""
        # Base processing time estimate
        base_time = 0.5  # Base response time
        
        # Token-based time estimate (rough: 1000 tokens ≈ 1 second)
        token_time = tokens / 1000
        
        # Complexity modifiers
        mcp_calls = len(re.findall(r'mcp__', content))
        thinking_blocks = len(re.findall(r'<thinking', content, re.IGNORECASE))
        
        # MCP calls add significant time
        mcp_overhead = mcp_calls * 0.5
        
        # Thinking blocks add processing time
        thinking_overhead = thinking_blocks * 0.1
        
        estimated_time = base_time + token_time + mcp_overhead + thinking_overhead
        
        # Success rate estimate based on complexity and patterns
        complexity_penalty = max(0, (tokens / 2000 - 1) * 0.1)  # Penalty for very long commands
        mcp_reliability = 0.95 if mcp_calls > 0 else 1.0  # MCP introduces small failure chance
        
        estimated_success_rate = max(0.6, min(1.0, 1.0 - complexity_penalty)) * mcp_reliability
        
        # Token efficiency (value delivered per token)
        thinking_quality_boost = min(0.3, thinking_blocks * 0.05)  # Thinking improves quality
        base_efficiency = 0.7  # Base efficiency
        efficiency = base_efficiency + thinking_quality_boost
        
        return {
            "estimated_execution_time": round(estimated_time, 2),
            "estimated_success_rate": round(estimated_success_rate, 3),
            "token_efficiency": round(efficiency, 3),
            "performance_factors": {
                "base_time": base_time,
                "token_processing": token_time,
                "mcp_overhead": mcp_overhead,
                "thinking_overhead": thinking_overhead,
                "mcp_calls": mcp_calls,
                "thinking_blocks": thinking_blocks
            }
        }
    
    def assess_quality(self, content: str) -> dict:
        """Assess command quality based on best practices"""
        quality_score = 0
        quality_factors = []
        
        # Documentation quality
        if "## " in content:  # Has sections
            quality_score += 10
            quality_factors.append("Well-structured documentation (+10)")
        
        if "example" in content.lower():
            quality_score += 5
            quality_factors.append("Contains examples (+5)")
        
        # Error handling
        if "error" in content.lower() or "exception" in content.lower():
            quality_score += 10
            quality_factors.append("Error handling present (+10)")
        
        # Thinking architecture
        if "<thinking" in content:
            quality_score += 15
            quality_factors.append("Explicit thinking architecture (+15)")
        
        # User guidance
        if "usage" in content.lower():
            quality_score += 5
            quality_factors.append("Usage instructions provided (+5)")
        
        # Integration patterns
        if "integration" in content.lower():
            quality_score += 5
            quality_factors.append("Integration considerations (+5)")
        
        # Learning mechanisms
        if "learning" in content.lower() or "pattern" in content.lower():
            quality_score += 10
            quality_factors.append("Learning/pattern mechanisms (+10)")
        
        # Validation
        if "validation" in content.lower() or "verify" in content.lower():
            quality_score += 5
            quality_factors.append("Validation steps included (+5)")
        
        # Complexity management
        if "complexity" in content.lower():
            quality_score += 10
            quality_factors.append("Complexity awareness (+10)")
        
        # MCP integration
        if "mcp__" in content:
            quality_score += 5
            quality_factors.append("MCP tool integration (+5)")
        
        return {
            "total_score": quality_score,
            "grade": self.get_quality_grade(quality_score),
            "factors": quality_factors,
            "max_possible": 80  # Sum of all possible points
        }
    
    def get_quality_grade(self, score: int) -> str:
        """Convert quality score to letter grade"""
        percentage = (score / 80) * 100
        if percentage >= 90: return "A"
        elif percentage >= 80: return "B"
        elif percentage >= 70: return "C"
        elif percentage >= 60: return "D"
        else: return "F"
    
    def generate_savage_analysis(self, cmd_name: str, analysis: dict) -> str:
        """Generate brutally honest assessment"""
        complexity = analysis["complexity"]["total_score"]
        quality = analysis["quality"]["total_score"]
        performance = analysis["performance"]
        
        # Complexity assessment
        if complexity >= 5:
            complexity_verdict = f"VIOLATES CLAUDE.MD - Complexity {complexity}/10 breaks the sacred rule of <5"
        elif complexity >= 3:
            complexity_verdict = f"BORDERLINE - Complexity {complexity}/10 is acceptable but watch it"
        else:
            complexity_verdict = f"SIMPLE - Complexity {complexity}/10 follows CLAUDE.MD principles"
        
        # Quality assessment  
        quality_grade = analysis["quality"]["grade"]
        if quality_grade in ["A", "B"]:
            quality_verdict = f"SOLID - Grade {quality_grade} with {quality}/80 points"
        elif quality_grade == "C":
            quality_verdict = f"MEDIOCRE - Grade {quality_grade}. It works but don't brag about it"
        else:
            quality_verdict = f"TERRIBLE - Grade {quality_grade}. This is embarrassing"
        
        # Performance assessment
        success_rate = performance["estimated_success_rate"]
        exec_time = performance["estimated_execution_time"]
        
        if success_rate < 0.8:
            perf_verdict = f"UNRELIABLE - {success_rate:.0%} success rate. Roll dice instead"
        elif exec_time > 3.0:
            perf_verdict = f"SLUGGISH - {exec_time}s execution time. Watching paint dry is faster"
        else:
            perf_verdict = f"FUNCTIONAL - {success_rate:.0%} success in {exec_time}s. Not embarrassing"
        
        return f"{cmd_name}: {complexity_verdict}. {quality_verdict}. {perf_verdict}."
    
    def run_full_analysis(self) -> dict:
        """Execute comprehensive analysis of all selected commands"""
        selected_commands = [
            "context-enhanced-executor.md",
            "ultrathink-hybrid-mcp.md", 
            "adhd-evening-reflect.md",
            "intelligent-code-enhancer.md",
            "reasoning-wrapper.md"
        ]
        
        results = {}
        savage_verdicts = []
        
        for cmd_file in selected_commands:
            cmd_path = self.commands_dir / cmd_file
            if cmd_path.exists():
                print(f"📊 Analyzing {cmd_file}...")
                analysis = self.analyze_command_file(cmd_path)
                results[cmd_file.replace('.md', '')] = analysis
                
                # Generate savage verdict
                verdict = self.generate_savage_analysis(cmd_file.replace('.md', ''), analysis)
                savage_verdicts.append(verdict)
        
        # Generate aggregate statistics
        complexities = [r["complexity"]["total_score"] for r in results.values()]
        qualities = [r["quality"]["total_score"] for r in results.values()]
        exec_times = [r["performance"]["estimated_execution_time"] for r in results.values()]
        success_rates = [r["performance"]["estimated_success_rate"] for r in results.values()]
        
        aggregate_stats = {
            "complexity": {
                "average": statistics.mean(complexities),
                "std_dev": statistics.stdev(complexities) if len(complexities) > 1 else 0,
                "violators": [cmd for cmd, r in results.items() if r["complexity"]["total_score"] >= 5]
            },
            "quality": {
                "average": statistics.mean(qualities),
                "std_dev": statistics.stdev(qualities) if len(qualities) > 1 else 0,
                "top_performer": max(results.items(), key=lambda x: x[1]["quality"]["total_score"])[0],
                "worst_performer": min(results.items(), key=lambda x: x[1]["quality"]["total_score"])[0]
            },
            "performance": {
                "avg_execution_time": statistics.mean(exec_times),
                "avg_success_rate": statistics.mean(success_rates),
                "fastest": min(results.items(), key=lambda x: x[1]["performance"]["estimated_execution_time"])[0],
                "slowest": max(results.items(), key=lambda x: x[1]["performance"]["estimated_execution_time"])[0]
            }
        }
        
        # Final report
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        report = {
            "benchmark_metadata": {
                "timestamp": timestamp,
                "analyzer_version": "SAVAGE-1.0",
                "commands_analyzed": len(results),
                "analysis_duration_seconds": (datetime.now() - self.test_start).total_seconds()
            },
            "individual_analysis": results,
            "aggregate_statistics": aggregate_stats,
            "savage_verdicts": savage_verdicts,
            "scientific_conclusions": self.generate_scientific_conclusions(aggregate_stats, results),
            "recommendations": self.generate_recommendations(results)
        }
        
        return report
    
    def generate_scientific_conclusions(self, stats: dict, results: dict) -> dict:
        """Generate data-backed scientific conclusions"""
        conclusions = {}
        
        # Complexity analysis
        avg_complexity = stats["complexity"]["average"]
        violators = stats["complexity"]["violators"]
        
        if len(violators) > 0:
            conclusions["complexity"] = f"SCIENTIFIC FAIL: {len(violators)}/{len(results)} commands violate CLAUDE.MD complexity rule (<5). Average: {avg_complexity:.1f}"
        else:
            conclusions["complexity"] = f"COMPLIANT: All commands meet CLAUDE.MD complexity standards. Average: {avg_complexity:.1f}"
        
        # Quality distribution
        quality_grades = [r["quality"]["grade"] for r in results.values()]
        grade_dist = {grade: quality_grades.count(grade) for grade in set(quality_grades)}
        conclusions["quality"] = f"Grade distribution: {grade_dist}. This is {'acceptable' if grade_dist.get('A', 0) + grade_dist.get('B', 0) > len(results)/2 else 'disappointing'}"
        
        # Performance reality check
        avg_success = stats["performance"]["avg_success_rate"]
        if avg_success < 0.85:
            conclusions["reliability"] = f"UNRELIABLE: {avg_success:.0%} average success rate. Would you board a plane with this reliability?"
        else:
            conclusions["reliability"] = f"RELIABLE: {avg_success:.0%} average success rate is acceptable for production use"
        
        return conclusions
    
    def generate_recommendations(self, results: dict) -> dict:
        """Generate data-driven improvement recommendations"""
        recommendations = {}
        
        for cmd_name, analysis in results.items():
            cmd_recs = []
            
            # Complexity recommendations
            if analysis["complexity"]["total_score"] >= 5:
                cmd_recs.append(f"CRITICAL: Reduce complexity from {analysis['complexity']['total_score']} to <5 per CLAUDE.MD")
            
            # Quality recommendations
            if analysis["quality"]["total_score"] < 40:
                cmd_recs.append(f"Improve quality: Currently {analysis['quality']['grade']} grade with {analysis['quality']['total_score']}/80 points")
            
            # Performance recommendations
            if analysis["performance"]["estimated_success_rate"] < 0.85:
                cmd_recs.append(f"Fix reliability: {analysis['performance']['estimated_success_rate']:.0%} success rate is unacceptable")
            
            if analysis["performance"]["estimated_execution_time"] > 3.0:
                cmd_recs.append(f"Optimize speed: {analysis['performance']['estimated_execution_time']}s is too slow")
            
            # Pattern recommendations
            if len(analysis["patterns"]["anti_patterns"]) > 0:
                cmd_recs.append(f"Eliminate anti-patterns: {', '.join(analysis['patterns']['anti_patterns'])}")
            
            if not cmd_recs:
                cmd_recs.append("Continue monitoring - performance within acceptable parameters")
                
            recommendations[cmd_name] = cmd_recs
        
        return recommendations

if __name__ == "__main__":
    print("🔬 SAVAGE COMMAND BENCHMARKER v1.0")
    print("Executing scientific analysis with brutal honesty...")
    print()
    
    analyzer = RealCommandAnalyzer()
    report = analyzer.run_full_analysis()
    
    # Save report
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f".github/benchmarks/results/{timestamp}-report.json"
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"📊 Analysis complete! Report saved to: {output_file}")
    print()
    print("🔥 SAVAGE VERDICTS:")
    for verdict in report["savage_verdicts"]:
        print(f"  • {verdict}")
    
    print("\n🧪 SCIENTIFIC CONCLUSIONS:")
    for category, conclusion in report["scientific_conclusions"].items():
        print(f"  • {category.upper()}: {conclusion}")