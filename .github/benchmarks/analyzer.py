#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific Analysis of Claude Commands with Brutal Honesty
"""

import os
import re
import json
import time
from pathlib import Path
from datetime import datetime
import statistics

class CommandAnalyzer:
    def __init__(self):
        self.commands_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands")
        self.selected_commands = [
            "ultrathink-full-mcp.md",
            "analyze-project-architecture.md", 
            "safe-code-beautifier.md",
            "git-backup-sync.md"
        ]
        
    def analyze_command(self, filename):
        """Brutally analyze a single command file"""
        filepath = self.commands_dir / filename
        
        if not filepath.exists():
            return {"error": f"Command file {filename} not found"}
            
        content = filepath.read_text()
        lines = content.split('\n')
        
        # Basic metrics
        metrics = {
            "filename": filename,
            "line_count": len(lines),
            "char_count": len(content),
            "word_count": len(content.split()),
            
            # Complexity indicators
            "thinking_blocks": len(re.findall(r'<.*?thinking.*?>', content, re.IGNORECASE)),
            "xml_tags": len(re.findall(r'<[^>]+>', content)),
            "mcp_calls": len(re.findall(r'mcp__', content)),
            "code_blocks": len(re.findall(r'```', content)),
            "bash_commands": len(re.findall(r'```bash', content)),
            
            # Structure analysis
            "sections": len(re.findall(r'^##[^#]', content, re.MULTILINE)),
            "subsections": len(re.findall(r'^###[^#]', content, re.MULTILINE)),
            "examples": len(re.findall(r'example', content, re.IGNORECASE)),
            
            # Complexity score calculation
            "nesting_depth": self._calculate_nesting_depth(content),
            "cyclomatic_complexity": self._estimate_complexity(content),
        }
        
        # Calculate composite scores
        metrics["complexity_score"] = self._calculate_complexity_score(metrics)
        metrics["maintainability_score"] = self._calculate_maintainability_score(metrics)
        metrics["usability_score"] = self._calculate_usability_score(metrics)
        
        return metrics
    
    def _calculate_nesting_depth(self, content):
        """Calculate maximum nesting depth of XML-like tags"""
        max_depth = 0
        current_depth = 0
        
        for match in re.finditer(r'<(/?)([^>]+)>', content):
            is_closing = match.group(1) == '/'
            if is_closing:
                current_depth = max(0, current_depth - 1)
            else:
                current_depth += 1
                max_depth = max(max_depth, current_depth)
        
        return max_depth
    
    def _estimate_complexity(self, content):
        """Estimate cognitive complexity based on control structures"""
        complexity = 0
        
        # Decision points
        complexity += len(re.findall(r'if\s+', content, re.IGNORECASE))
        complexity += len(re.findall(r'switch\s*\(', content, re.IGNORECASE))
        complexity += len(re.findall(r'for\s+', content, re.IGNORECASE))
        complexity += len(re.findall(r'while\s+', content, re.IGNORECASE))
        complexity += len(re.findall(r'\?\s*:', content))
        
        # Nested structures add exponential complexity
        nesting_penalty = self._calculate_nesting_depth(content) ** 1.5
        
        return complexity + nesting_penalty
    
    def _calculate_complexity_score(self, metrics):
        """Calculate composite complexity score (1-10 scale)"""
        # Normalize different metrics
        line_factor = min(metrics["line_count"] / 100, 5)
        thinking_factor = min(metrics["thinking_blocks"] / 10, 3)
        nesting_factor = min(metrics["nesting_depth"] / 5, 2)
        
        raw_score = line_factor + thinking_factor + nesting_factor
        return min(raw_score, 10)
    
    def _calculate_maintainability_score(self, metrics):
        """Calculate maintainability score (higher is worse)"""
        # Penalties for bad practices
        penalties = 0
        
        # Too many thinking blocks = analysis paralysis
        if metrics["thinking_blocks"] > 20:
            penalties += 2
            
        # Too long = nobody will read it
        if metrics["line_count"] > 500:
            penalties += 3
            
        # Too complex nesting = cognitive overload
        if metrics["nesting_depth"] > 10:
            penalties += 2
            
        return penalties
    
    def _calculate_usability_score(self, metrics):
        """Calculate how usable this command actually is"""
        score = 10  # Start optimistic
        
        # Length penalty - nobody wants to read War and Peace
        if metrics["line_count"] > 300:
            score -= 2
        if metrics["line_count"] > 600:
            score -= 3
            
        # Complexity penalty - if it's too smart, nobody understands
        if metrics["thinking_blocks"] > 15:
            score -= 2
            
        # Boost for examples
        if metrics["examples"] > 3:
            score += 1
            
        return max(0, score)
    
    def estimate_token_consumption(self, metrics):
        """Estimate token consumption for this command"""
        # Rough estimation: 1 token per 3.5 characters
        input_tokens = metrics["char_count"] / 3.5
        
        # Output tokens scale with complexity
        complexity_multiplier = 1 + (metrics["complexity_score"] / 10)
        output_tokens = input_tokens * complexity_multiplier * 0.7
        
        return {
            "estimated_input_tokens": round(input_tokens),
            "estimated_output_tokens": round(output_tokens),
            "total_estimated_tokens": round(input_tokens + output_tokens)
        }
    
    def run_benchmarks(self):
        """Run the full benchmark suite"""
        results = {
            "timestamp": datetime.now().isoformat(),
            "benchmarker_version": "1.0-savage",
            "commands_analyzed": len(self.selected_commands),
            "analysis": {}
        }
        
        for command in self.selected_commands:
            print(f"🔬 Analyzing {command}...")
            
            start_time = time.time()
            metrics = self.analyze_command(command)
            analysis_time = time.time() - start_time
            
            # Add performance metrics
            metrics["analysis_time_ms"] = round(analysis_time * 1000, 2)
            
            # Add token estimates
            token_data = self.estimate_token_consumption(metrics)
            metrics.update(token_data)
            
            results["analysis"][command] = metrics
            
        # Calculate aggregate statistics
        results["aggregate_stats"] = self._calculate_aggregate_stats(results["analysis"])
        
        return results
    
    def _calculate_aggregate_stats(self, analysis_data):
        """Calculate brutal aggregate statistics"""
        all_metrics = list(analysis_data.values())
        
        # Extract numeric values for statistics
        complexity_scores = [m["complexity_score"] for m in all_metrics]
        line_counts = [m["line_count"] for m in all_metrics]
        token_estimates = [m["total_estimated_tokens"] for m in all_metrics]
        usability_scores = [m["usability_score"] for m in all_metrics]
        
        return {
            "total_lines_analyzed": sum(line_counts),
            "avg_complexity_score": round(statistics.mean(complexity_scores), 2),
            "complexity_std_dev": round(statistics.stdev(complexity_scores), 2),
            "avg_line_count": round(statistics.mean(line_counts), 2),
            "median_line_count": statistics.median(line_counts),
            "total_estimated_tokens": sum(token_estimates),
            "avg_usability_score": round(statistics.mean(usability_scores), 2),
            "usability_variance": round(statistics.variance(usability_scores), 2),
            
            # Quality assessments
            "commands_over_500_lines": sum(1 for lc in line_counts if lc > 500),
            "commands_high_complexity": sum(1 for cs in complexity_scores if cs > 7),
            "commands_low_usability": sum(1 for us in usability_scores if us < 5),
        }

def main():
    analyzer = CommandAnalyzer()
    results = analyzer.run_benchmarks()
    
    # Save results
    output_file = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results") / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-report.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📊 Analysis complete. Results saved to {output_file}")
    return results

if __name__ == "__main__":
    main()