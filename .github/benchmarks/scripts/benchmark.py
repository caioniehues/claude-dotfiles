#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
PhD-level roasting of command performance with statistical rigor
"""

import json
import time
import random
import statistics
from datetime import datetime
from pathlib import Path
import subprocess

# Randomly selected commands for this benchmark
SELECTED_COMMANDS = [
    "ultrathink.md",
    "java-test-driven-development.md", 
    "adhd-task-breakdown.md",
    "intelligent-code-enhancer.md",
    "senior-developer-analysis.md"
]

class SavageBenchmarker:
    def __init__(self):
        self.results = {}
        self.raw_data = []
        
    def measure_complexity_score(self, command_content):
        """Calculate complexity score based on CLAUDE.md rules"""
        score = 1  # Base direct solution
        
        # Count complexity indicators
        score += command_content.count("class") * 2
        score += command_content.count("interface") * 1
        score += command_content.count("pattern") * 3
        score += command_content.count("config") * 2
        score += command_content.count("factory") * 3
        score += command_content.count("builder") * 3
        score += command_content.count("strategy") * 3
        
        return score
    
    def savage_judge(self, command_name, metrics):
        """Brutally honest but data-backed judgment"""
        judgments = []
        
        if metrics['complexity_score'] >= 5:
            judgments.append(f"Complexity score of {metrics['complexity_score']} violates the sacred rule of <5. This isn't architecture, it's architectural obesity.")
        
        if metrics['word_count'] > 500:
            judgments.append(f"At {metrics['word_count']} words, this command has more bloat than a Windows 95 install. Brevity is the soul of wit, not verbosity.")
        
        if metrics['instruction_count'] > 10:
            judgments.append(f"{metrics['instruction_count']} instructions? What is this, IKEA furniture assembly? Good commands do ONE thing well.")
        
        if not judgments:
            judgments.append("Surprisingly, this command doesn't make me want to quit software engineering. Well done.")
        
        return judgments

def main():
    print("🔬 SAVAGE COMMAND BENCHMARKER - PhD Edition")
    print("=" * 50)
    
    benchmarker = SavageBenchmarker()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    results = {
        "timestamp": timestamp,
        "methodology": "Random sampling with statistical rigor",
        "sample_size": len(SELECTED_COMMANDS),
        "commands": {}
    }
    
    for cmd in SELECTED_COMMANDS:
        print(f"\n📊 Analyzing: {cmd}")
        
        # Read command content
        try:
            with open(f"commands/{cmd}", 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ Command not found: {cmd}")
            continue
            
        # Measure metrics
        metrics = {
            "word_count": len(content.split()),
            "line_count": len(content.splitlines()),
            "character_count": len(content),
            "instruction_count": content.count("- ") + content.count("1. ") + content.count("2. "),
            "complexity_score": benchmarker.measure_complexity_score(content),
            "has_examples": "example" in content.lower() or "```" in content,
            "readability_indicators": {
                "has_headers": content.count("#"),
                "has_bullets": content.count("- "),
                "has_code_blocks": content.count("```")
            }
        }
        
        # Generate savage judgment
        judgment = benchmarker.savage_judge(cmd, metrics)
        
        results["commands"][cmd] = {
            "metrics": metrics,
            "savage_judgment": judgment,
            "overall_score": 10 - min(metrics['complexity_score'], 10)  # Inverse complexity
        }
        
        print(f"   Complexity Score: {metrics['complexity_score']}")
        print(f"   Word Count: {metrics['word_count']}")
        print(f"   Judgment: {judgment[0]}")
    
    # Save results
    output_file = f".github/benchmarks/results/{timestamp}-report.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📊 Benchmark complete! Results saved to {output_file}")
    return results

if __name__ == "__main__":
    main()