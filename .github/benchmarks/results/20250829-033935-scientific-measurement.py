#!/usr/bin/env python3
"""
SCIENTIFIC MEASUREMENT OF SELECTED COMMANDS
"""

import sys
import json
import time
import re
import statistics
from pathlib import Path
from datetime import datetime

# Import our framework
sys.path.append('/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results')
from savage_scientific_framework import SavageAnalyzer, CommandMetrics

def main():
    analyzer = SavageAnalyzer()
    
    # Our random victims
    commands = [
        '/home/runner/work/claude-dotfiles/claude-dotfiles/commands/reasoning-wrapper.md',
        '/home/runner/work/claude-dotfiles/claude-dotfiles/commands/ultrathink-pure-xml.md', 
        '/home/runner/work/claude-dotfiles/claude-dotfiles/commands/analyze-project-architecture.md',
        '/home/runner/work/claude-dotfiles/claude-dotfiles/commands/context-enhanced-executor.md'
    ]
    
    print("🔬 COMMENCING SCIENTIFIC COMMAND ANALYSIS")
    print("=" * 60)
    
    all_metrics = []
    
    for cmd_path in commands:
        print(f"\n🎯 ANALYZING: {Path(cmd_path).stem}")
        
        # Read command content
        with open(cmd_path, 'r') as f:
            content = f.read()
        
        # Run 5 measurements for statistical significance
        measurements = []
        for i in range(5):
            print(f"  📊 Measurement {i+1}/5...")
            metrics = analyzer.analyze_command(cmd_path, content)
            measurements.append(metrics)
            # Simulate variance in execution time
            time.sleep(0.1)
        
        # Calculate statistics for this command
        avg_metrics = analyzer.calculate_aggregate_metrics(measurements)
        all_metrics.append(avg_metrics)
        
        print(f"    ⚡ Avg Execution: {avg_metrics.execution_time:.2f}s")
        print(f"    🔢 Token Cost: {avg_metrics.token_count_input + avg_metrics.token_count_output}")
        print(f"    🎯 Complexity: {avg_metrics.complexity_score}/5")
    
    # Generate comprehensive savage report
    print("\n🔬 GENERATING SAVAGE SCIENTIFIC REPORT...")
    report = analyzer.generate_savage_report(all_metrics)
    
    # Save to JSON for scientific posterity
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{timestamp}-report.json"
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📁 Report saved: {output_file}")
    print("\n💀 PREPARE FOR THE STATISTICAL ROASTING...")
    return report

if __name__ == "__main__":
    main()