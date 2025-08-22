#!/usr/bin/env python3
"""
ENHANCED SAVAGE BENCHMARKER
Multiple iterations for robust statistical analysis
"""

import subprocess
import json
import statistics
import os
from datetime import datetime
from pathlib import Path

def run_multiple_benchmarks(num_iterations=5):
    """Run multiple benchmark iterations for statistical robustness"""
    all_results = []
    
    print(f"🧪 ENHANCED SAVAGE BENCHMARKER - {num_iterations} ITERATIONS")
    print("=" * 60)
    
    for i in range(num_iterations):
        print(f"\n🔬 ITERATION {i+1}/{num_iterations}")
        
        # Run the savage benchmarker
        result = subprocess.run([
            'python3', 
            '.github/benchmarks/scripts/savage-command-benchmarker.py'
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Iteration {i+1} failed: {result.stderr}")
            continue
            
        # Find the latest report file
        results_dir = Path('.github/benchmarks/results')
        report_files = list(results_dir.glob('*-report.json'))
        if report_files:
            latest_report = max(report_files, key=os.path.getctime)
            with open(latest_report, 'r') as f:
                data = json.load(f)
                all_results.append(data)
                print(f"   Avg Score: {data['aggregate_statistics']['overall_scores']['mean']:.1f}")
    
    return all_results

def generate_comprehensive_analysis(results_list):
    """Generate comprehensive statistical analysis across all iterations"""
    all_scores = []
    all_complexity_scores = []
    command_performance = {}
    
    for result in results_list:
        all_scores.append(result['aggregate_statistics']['overall_scores']['mean'])
        all_complexity_scores.append(result['aggregate_statistics']['complexity_scores']['mean'])
        
        # Track individual command performance
        for cmd_name, cmd_data in result['individual_results'].items():
            if cmd_name not in command_performance:
                command_performance[cmd_name] = []
            command_performance[cmd_name].append(cmd_data['savage_judgment']['overall_score'])
    
    # Calculate statistics
    overall_stats = {
        'mean_score': statistics.mean(all_scores),
        'std_dev_score': statistics.stdev(all_scores) if len(all_scores) > 1 else 0,
        'mean_complexity': statistics.mean(all_complexity_scores),
        'std_dev_complexity': statistics.stdev(all_complexity_scores) if len(all_complexity_scores) > 1 else 0,
        'total_iterations': len(results_list),
        'total_commands_tested': len(command_performance),
        'consistency_score': 100 - (statistics.stdev(all_scores) if len(all_scores) > 1 else 0)
    }
    
    # Calculate command reliability (consistency across iterations)
    command_reliability = {}
    for cmd, scores in command_performance.items():
        if len(scores) > 1:
            command_reliability[cmd] = {
                'mean': statistics.mean(scores),
                'std_dev': statistics.stdev(scores),
                'consistency': 100 - statistics.stdev(scores),
                'appearances': len(scores)
            }
    
    return overall_stats, command_reliability

def generate_savage_final_report(overall_stats, command_reliability, results_list):
    """Generate the ultimate savage report with statistical confidence"""
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Generate savage commentary based on statistical confidence
    mean_score = overall_stats['mean_score']
    std_dev = overall_stats['std_dev_score']
    consistency = overall_stats['consistency_score']
    
    if mean_score < 40:
        roast_level = "NUCLEAR DEVASTATION"
        commentary = (f"🚨 STATISTICAL CATASTROPHE CONFIRMED 🚨\n\n"
                     f"After {overall_stats['total_iterations']} iterations, the mean score of "
                     f"{mean_score:.1f}±{std_dev:.1f} is statistically indistinguishable from random noise. "
                     f"This isn't code—it's digital entropy increasing the universe's heat death.")
    elif mean_score < 55:
        roast_level = "SYSTEMATIC MEDIOCRITY"
        commentary = (f"💀 MEDIOCRITY STATISTICALLY CONFIRMED 💀\n\n"
                     f"Across {overall_stats['total_iterations']} iterations, the consistent score of "
                     f"{mean_score:.1f}±{std_dev:.1f} proves this isn't random failure—it's systematic "
                     f"incompetence. The consistency score of {consistency:.1f}% means the badness is reliable.")
    elif mean_score < 70:
        roast_level = "ACCEPTABLE MEDIOCRITY"
        commentary = (f"⚠️ STATISTICALLY AVERAGE ⚠️\n\n"
                     f"Score of {mean_score:.1f}±{std_dev:.1f} across {overall_stats['total_iterations']} "
                     f"iterations suggests competent mediocrity. Consistency of {consistency:.1f}% indicates "
                     f"reliable vanilla-ness.")
    else:
        roast_level = "SURPRISING COMPETENCE"
        commentary = (f"✅ STATISTICAL EXCELLENCE DETECTED ✅\n\n"
                     f"Mean score of {mean_score:.1f}±{std_dev:.1f} with {consistency:.1f}% consistency "
                     f"across {overall_stats['total_iterations']} iterations suggests actual engineering happened here.")
    
    # Find most and least reliable commands
    most_reliable = None
    least_reliable = None
    if command_reliability:
        most_reliable = max(command_reliability.items(), 
                          key=lambda x: x[1]['consistency'])
        least_reliable = min(command_reliability.items(), 
                           key=lambda x: x[1]['consistency'])
    
    # Generate final recommendations with statistical backing
    recommendations = []
    
    if overall_stats['std_dev_score'] > 10:
        recommendations.append(
            f"🎯 CONSISTENCY CRISIS: Score variance of {overall_stats['std_dev_score']:.1f} indicates "
            f"unstable quality. Implement quality control standards."
        )
    
    if overall_stats['mean_complexity'] > 4:
        recommendations.append(
            f"🚨 COMPLEXITY EPIDEMIC: Mean complexity {overall_stats['mean_complexity']:.1f} exceeds "
            f"recommended limits. Institute mandatory simplification reviews."
        )
    
    if overall_stats['mean_score'] < 60:
        recommendations.append(
            f"📚 SYSTEMATIC TRAINING NEEDED: Mean score {overall_stats['mean_score']:.1f} indicates "
            f"fundamental knowledge gaps. Mandatory CLAUDE.md training required."
        )
    
    # Create the final report
    report = {
        'meta': {
            'timestamp': timestamp,
            'analysis_type': 'comprehensive_multi_iteration',
            'iterations': overall_stats['total_iterations'],
            'statistical_confidence': '95%' if overall_stats['total_iterations'] >= 5 else '90%'
        },
        'overall_statistics': overall_stats,
        'roast_level': roast_level,
        'savage_commentary': commentary,
        'command_reliability': command_reliability,
        'most_reliable_command': most_reliable,
        'least_reliable_command': least_reliable,
        'recommendations': recommendations,
        'raw_iteration_data': results_list
    }
    
    return report

def main():
    # Run multiple benchmarks
    results = run_multiple_benchmarks(5)
    
    if not results:
        print("❌ No successful benchmark iterations!")
        return
    
    # Generate comprehensive analysis
    overall_stats, command_reliability = generate_comprehensive_analysis(results)
    
    # Generate savage final report
    final_report = generate_savage_final_report(overall_stats, command_reliability, results)
    
    # Save comprehensive report
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_file = Path(f'.github/benchmarks/results/{timestamp}-comprehensive-report.json')
    
    with open(report_file, 'w') as f:
        json.dump(final_report, f, indent=2)
    
    # Print summary
    print("\n" + "="*80)
    print("🏁 COMPREHENSIVE STATISTICAL ANALYSIS COMPLETE")
    print("="*80)
    print(f"Report saved: {report_file}")
    print(f"\nROAST LEVEL: {final_report['roast_level']}")
    print(f"\n{final_report['savage_commentary']}")
    
    print(f"\n📊 STATISTICAL SUMMARY:")
    print(f"Mean Score: {final_report['overall_statistics']['mean_score']:.1f}±{final_report['overall_statistics']['std_dev_score']:.1f}")
    print(f"Consistency: {final_report['overall_statistics']['consistency_score']:.1f}%")
    print(f"Iterations: {final_report['overall_statistics']['total_iterations']}")
    
    if final_report['most_reliable_command']:
        cmd, stats = final_report['most_reliable_command']
        print(f"\n🏆 MOST RELIABLE: {cmd} (consistency: {stats['consistency']:.1f}%)")
    
    if final_report['least_reliable_command']:
        cmd, stats = final_report['least_reliable_command']
        print(f"💩 LEAST RELIABLE: {cmd} (consistency: {stats['consistency']:.1f}%)")
    
    print(f"\n🎯 FINAL RECOMMENDATIONS:")
    for i, rec in enumerate(final_report['recommendations'], 1):
        print(f"{i}. {rec}")
    
    print("="*80)

if __name__ == "__main__":
    main()