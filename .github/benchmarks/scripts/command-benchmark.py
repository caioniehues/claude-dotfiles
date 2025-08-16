#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientifically measures and brutally judges commands
"""

import json
import time
import os
import sys
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class BenchmarkMetrics:
    command_name: str
    complexity_score: int
    line_count: int
    token_estimate: int
    thinking_blocks: int
    mcp_integrations: int
    xml_structure_quality: float
    reasoning_depth: int
    pattern_violations: List[str]
    maintainability_score: float
    execution_time: float
    memory_footprint: int

class SavageBenchmarker:
    def __init__(self):
        self.commands_dir = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
        self.selected_commands = [
            "adhd-context-switch.md",
            "generate-thinking-command.md", 
            "adhd-evening-reflect.md",
            "intelligent-refactor-session.md",
            "reasoning-wrapper.md"
        ]
        self.results = []
        
    def analyze_command(self, command_file: str) -> BenchmarkMetrics:
        """Brutally analyze a command file"""
        start_time = time.time()
        
        file_path = Path(self.commands_dir) / command_file
        content = file_path.read_text()
        
        # Basic metrics
        line_count = len(content.splitlines())
        token_estimate = len(content.split()) * 1.3  # Rough token estimation
        
        # Complexity analysis (CLAUDE.md compliant)
        complexity_score = self._calculate_complexity(content)
        
        # Thinking block analysis
        thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content, re.IGNORECASE))
        
        # MCP integration detection
        mcp_integrations = len(re.findall(r'mcp__', content))
        
        # XML structure quality
        xml_quality = self._analyze_xml_structure(content)
        
        # Reasoning depth
        reasoning_depth = self._calculate_reasoning_depth(content)
        
        # Pattern violations (CLAUDE.md rules)
        violations = self._find_pattern_violations(content)
        
        # Maintainability (subjective but measurable)
        maintainability = self._calculate_maintainability(content)
        
        execution_time = time.time() - start_time
        memory_footprint = sys.getsizeof(content)
        
        return BenchmarkMetrics(
            command_name=command_file,
            complexity_score=complexity_score,
            line_count=line_count,
            token_estimate=int(token_estimate),
            thinking_blocks=thinking_blocks,
            mcp_integrations=mcp_integrations,
            xml_structure_quality=xml_quality,
            reasoning_depth=reasoning_depth,
            pattern_violations=violations,
            maintainability_score=maintainability,
            execution_time=execution_time,
            memory_footprint=memory_footprint
        )
    
    def _calculate_complexity(self, content: str) -> int:
        """Calculate complexity score based on CLAUDE.md rules"""
        score = 1  # Base complexity
        
        # Each interface/abstraction adds complexity
        if re.search(r'interface|abstract|factory', content, re.IGNORECASE):
            score += 2
            
        # Nested XML structures
        nested_depth = self._max_xml_nesting(content)
        score += max(0, nested_depth - 2)
        
        # Multiple thinking blocks can indicate complexity
        thinking_count = len(re.findall(r'<[^>]*thinking[^>]*>', content, re.IGNORECASE))
        if thinking_count > 5:
            score += 1
            
        # Long parameter lists (anti-pattern)
        parameter_matches = re.findall(r'parameter>[^<]+', content)
        if len(parameter_matches) > 3:
            score += 1
            
        return min(score, 10)  # Cap at 10
    
    def _max_xml_nesting(self, content: str) -> int:
        """Calculate maximum XML nesting depth"""
        max_depth = 0
        current_depth = 0
        
        for match in re.finditer(r'</?[^>]+>', content):
            tag = match.group(0)
            if tag.startswith('</'):
                current_depth -= 1
            else:
                current_depth += 1
                max_depth = max(max_depth, current_depth)
                
        return max_depth
    
    def _analyze_xml_structure(self, content: str) -> float:
        """Analyze XML structure quality (0-1)"""
        score = 1.0
        
        # Check for proper XML structure
        open_tags = re.findall(r'<([^/>]+)>', content)
        close_tags = re.findall(r'</([^>]+)>', content)
        
        # Mismatched tags penalty
        if len(open_tags) != len(close_tags):
            score -= 0.3
            
        # Self-closing tags are good
        self_closing = len(re.findall(r'<[^>]+/>', content))
        if self_closing > 0:
            score += 0.1
            
        # Nested complexity penalty
        if self._max_xml_nesting(content) > 5:
            score -= 0.2
            
        return max(0.0, min(1.0, score))
    
    def _calculate_reasoning_depth(self, content: str) -> int:
        """Calculate reasoning depth from thinking blocks"""
        thinking_content = re.findall(r'<[^>]*thinking[^>]*>.*?</[^>]*thinking[^>]*>', 
                                    content, re.DOTALL | re.IGNORECASE)
        
        if not thinking_content:
            return 0
            
        # Analyze reasoning patterns
        depth_indicators = [
            r'reasoning:',
            r'analysis:',
            r'decision:',
            r'why\s+',
            r'because',
            r'therefore',
            r'assessment:',
            r'evaluation:'
        ]
        
        total_depth = 0
        for block in thinking_content:
            block_depth = sum(len(re.findall(pattern, block, re.IGNORECASE)) 
                            for pattern in depth_indicators)
            total_depth += block_depth
            
        return min(total_depth, 20)  # Cap at reasonable level
    
    def _find_pattern_violations(self, content: str) -> List[str]:
        """Find violations of CLAUDE.md patterns"""
        violations = []
        
        # Check for wildcard imports (Java anti-pattern)
        if re.search(r'import.*\*', content):
            violations.append("Wildcard imports detected")
            
        # Check for functions > 20 lines (rough estimation)
        functions = re.findall(r'function\s+\w+.*?\{.*?\}', content, re.DOTALL)
        for func in functions:
            if len(func.splitlines()) > 20:
                violations.append("Function exceeds 20 lines")
                
        # Check for null returns
        if re.search(r'return\s+null', content, re.IGNORECASE):
            violations.append("Null return detected")
            
        # Check for missing final parameters (Java)
        if re.search(r'public.*\([^)]*[^f][^i][^n][^a][^l]\s+\w+', content):
            violations.append("Non-final parameters detected")
            
        # Check for complexity > 5 indicator
        if self._calculate_complexity(content) >= 5:
            violations.append("Complexity score exceeds CLAUDE.md limit")
            
        return violations
    
    def _calculate_maintainability(self, content: str) -> float:
        """Calculate maintainability score (0-1)"""
        score = 1.0
        
        # Length penalty
        if len(content) > 10000:
            score -= 0.2
            
        # Complexity penalty  
        complexity = self._calculate_complexity(content)
        score -= (complexity / 10) * 0.3
        
        # Good patterns bonus
        if re.search(r'<thinking', content, re.IGNORECASE):
            score += 0.1
            
        if re.search(r'mcp__', content):
            score += 0.1
            
        # Documentation bonus
        if re.search(r'##\s+', content):
            score += 0.1
            
        return max(0.0, min(1.0, score))

    def run_benchmarks(self) -> Dict[str, Any]:
        """Execute brutal benchmarking on selected commands"""
        print("🔬 SAVAGE COMMAND BENCHMARKER ACTIVATED")
        print("=" * 50)
        
        for command in self.selected_commands:
            print(f"Analyzing {command}...")
            try:
                metrics = self.analyze_command(command)
                self.results.append(metrics)
                print(f"✅ {command} brutally analyzed")
            except Exception as e:
                print(f"❌ {command} failed analysis: {e}")
        
        return self._generate_report()
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate savage statistical report"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Calculate statistics
        complexities = [r.complexity_score for r in self.results]
        token_estimates = [r.token_estimate for r in self.results]
        reasoning_depths = [r.reasoning_depth for r in self.results]
        maintainability_scores = [r.maintainability_score for r in self.results]
        
        # Statistical analysis
        def stats(data):
            return {
                "mean": sum(data) / len(data) if data else 0,
                "min": min(data) if data else 0,
                "max": max(data) if data else 0,
                "std_dev": self._std_dev(data)
            }
        
        report = {
            "timestamp": timestamp,
            "commands_analyzed": len(self.results),
            "statistical_analysis": {
                "complexity_scores": stats(complexities),
                "token_estimates": stats(token_estimates),
                "reasoning_depths": stats(reasoning_depths),
                "maintainability_scores": stats(maintainability_scores)
            },
            "savage_rankings": self._generate_savage_rankings(),
            "pattern_violations": self._aggregate_violations(),
            "recommendations": self._generate_recommendations(),
            "raw_metrics": [
                {
                    "command": r.command_name,
                    "complexity": r.complexity_score,
                    "tokens": r.token_estimate,
                    "lines": r.line_count,
                    "thinking_blocks": r.thinking_blocks,
                    "mcp_integrations": r.mcp_integrations,
                    "xml_quality": r.xml_structure_quality,
                    "reasoning_depth": r.reasoning_depth,
                    "violations": r.pattern_violations,
                    "maintainability": r.maintainability_score,
                    "execution_time": r.execution_time,
                    "memory_footprint": r.memory_footprint
                }
                for r in self.results
            ]
        }
        
        return report
    
    def _std_dev(self, data):
        """Calculate standard deviation"""
        if len(data) < 2:
            return 0
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
        return variance ** 0.5
    
    def _generate_savage_rankings(self):
        """Generate brutal command rankings"""
        # Sort by different criteria
        by_complexity = sorted(self.results, key=lambda x: x.complexity_score, reverse=True)
        by_maintainability = sorted(self.results, key=lambda x: x.maintainability_score, reverse=True)
        by_violations = sorted(self.results, key=lambda x: len(x.pattern_violations), reverse=True)
        
        return {
            "most_complex": {
                "command": by_complexity[0].command_name,
                "score": by_complexity[0].complexity_score,
                "roast": "This command has more layers than a wedding cake in complexity hell."
            },
            "least_complex": {
                "command": by_complexity[-1].command_name,  
                "score": by_complexity[-1].complexity_score,
                "praise": "Finally, someone who understands KISS principle."
            },
            "most_maintainable": {
                "command": by_maintainability[0].command_name,
                "score": by_maintainability[0].maintainability_score,
                "praise": "This is how you write maintainable code."
            },
            "most_violations": {
                "command": by_violations[0].command_name,
                "count": len(by_violations[0].pattern_violations),
                "roast": "Violated more patterns than a rebel teenager."
            }
        }
    
    def _aggregate_violations(self):
        """Aggregate all pattern violations"""
        violations = {}
        for result in self.results:
            for violation in result.pattern_violations:
                violations[violation] = violations.get(violation, 0) + 1
        return violations
    
    def _generate_recommendations(self):
        """Generate improvement recommendations"""
        return [
            "Reduce complexity scores > 5 to meet CLAUDE.md standards",
            "Add thinking blocks to commands with reasoning_depth < 3",
            "Fix pattern violations to improve maintainability",
            "Consider MCP integration for complex commands",
            "Break down commands > 500 lines into smaller units"
        ]

if __name__ == "__main__":
    benchmarker = SavageBenchmarker()
    report = benchmarker.run_benchmarks()
    
    # Save report
    output_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{report['timestamp']}-report.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n🔬 Savage analysis complete! Report saved: {output_file}")