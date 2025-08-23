#!/usr/bin/env python3
"""
Execute the savage benchmark analysis on selected commands
"""

import sys
import os
sys.path.append('.github/benchmarks/tools')

from benchmark_engine import SavageCommandBenchmarker
import json

def main():
    # Our randomly selected commands for scientific roasting
    selected_commands = [
        "ultrathink-hybrid-mcp.md",
        "adaptive-complexity-router.md", 
        "adhd-context-switch.md",
        "intelligent-code-enhancer.md",
        "intelligent-refactor-session.md"
    ]
    
    print("🔬 SAVAGE COMMAND BENCHMARKER")
    print("=" * 50)
    print("Scientific Analysis of Command Quality with PhD-level Brutality")
    print()
    print(f"Selected commands for roasting: {len(selected_commands)}")
    for i, cmd in enumerate(selected_commands, 1):
        print(f"  {i}. {cmd}")
    print()
    
    # Initialize the roaster
    benchmarker = SavageCommandBenchmarker()
    
    # Run comprehensive benchmarks
    print("🔥 Commencing Scientific Roasting...")
    print()
    
    results = benchmarker.run_full_benchmark(selected_commands)
    
    print()
    print("📊 BENCHMARK RESULTS")
    print("=" * 50)
    
    # Quick summary
    for command, result in results.items():
        print(f"📍 {command}: {result.savage_score:.1f}/10")
        print(f"   Complexity: {result.metrics.complexity_score:.1f}/5")
        print(f"   Success Rate: {result.metrics.success_rate:.1%}")
        print(f"   Token Usage: {result.metrics.token_consumption_total:,}")
        print()
    
    # Generate final report
    print("📝 Generating comprehensive savage report...")
    report_file = benchmarker.generate_final_report(results)
    
    print(f"✅ Complete report saved to: {report_file}")
    print()
    print("🔍 Key Findings:")
    
    # Load and show key insights
    with open(report_file, 'r') as f:
        report_data = json.load(f)
    
    print()
    print("💀 SAVAGE INSIGHTS:")
    for insight in report_data['savage_insights']:
        print(f"  • {insight}")
    
    print()
    print("🧪 SCIENTIFIC CONCLUSIONS:")
    for conclusion in report_data['scientific_conclusions']:
        print(f"  • {conclusion}")
    
    print()
    print("🏆 COMMAND RANKINGS:")
    for ranking in report_data['command_rankings'][:3]:  # Top 3
        print(f"  {ranking['rank']}. {ranking['command']}: {ranking['savage_score']:.1f}/10")
    
    print()
    print(f"📄 Full report with statistical analysis: {report_file}")
    print("💀 The roasting is complete. Your commands have been scientifically judged.")

if __name__ == "__main__":
    main()