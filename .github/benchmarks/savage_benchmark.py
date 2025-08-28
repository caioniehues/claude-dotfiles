#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER - PhD Level Roasting with Statistical Precision
Because your commands need to be scientifically destroyed before they can be trusted.
"""

import json
import time
import re
import statistics
import hashlib
from typing import Dict, List, Any, Tuple
from pathlib import Path
import subprocess
import random

class SavageBenchmarker:
    """The Judge, Jury, and Executioner of Command Quality"""
    
    def __init__(self):
        self.test_cases = [
            "create a simple Java class for user management",
            "explain the Observer pattern",
            "refactor this method to use streams",
            "write unit tests for payment processing",
            "analyze code complexity"
        ]
        self.complexity_thresholds = {
            1: "Trivial (your intern could do this)",
            2: "Simple (basic competency required)", 
            3: "Moderate (actual thinking needed)",
            4: "Complex (better hope it works)",
            5: "Ultra-Complex (pray to your IDE gods)"
        }
        
    def calculate_complexity_score(self, command_content: str) -> Tuple[int, str]:
        """
        Calculate complexity using CLAUDE.md rules
        Returns (score, savage_commentary)
        """
        score = 1
        reasons = []
        
        # Count thinking blocks
        thinking_blocks = len(re.findall(r'<.*_thinking>', command_content))
        score += min(thinking_blocks // 5, 2)
        if thinking_blocks > 10:
            reasons.append(f"{thinking_blocks} thinking blocks (someone's overthinking)")
        
        # Count MCP invocations
        mcp_calls = len(re.findall(r'mcp__.*__', command_content))
        score += mcp_calls
        if mcp_calls > 2:
            reasons.append(f"{mcp_calls} MCP calls (dependency hell much?)")
        
        # Count complexity assessment blocks
        complexity_blocks = len(re.findall(r'complexity.*assessment', command_content, re.IGNORECASE))
        score += complexity_blocks
        
        # Pattern complexity
        if 'sequentialthinking' in command_content.lower():
            score += 2
            reasons.append("Sequential thinking (the nuclear option)")
        
        if len(command_content) > 10000:
            score += 1
            reasons.append(f"{len(command_content)} chars (novel-length commands)")
        
        if score > 5:
            score = 5
            reasons.append("MAXIMUM COMPLEXITY ACHIEVED")
        
        savage_commentary = f"Complexity {score}/5: {self.complexity_thresholds[score]}"
        if reasons:
            savage_commentary += f" - {', '.join(reasons)}"
            
        return score, savage_commentary
    
    def estimate_token_usage(self, command_content: str) -> Dict[str, int]:
        """Estimate token usage with brutal honesty"""
        # Rough estimation: 4 chars per token
        input_tokens = len(command_content) // 4
        
        # Output estimation based on command type
        if 'ultrathink' in command_content.lower():
            output_tokens = input_tokens * 3  # Verbose AF
        elif 'tdd' in command_content.lower():
            output_tokens = input_tokens * 2  # Lots of code examples
        elif 'refactor' in command_content.lower():
            output_tokens = input_tokens * 4  # Sessions are chatty
        else:
            output_tokens = input_tokens * 1.5
        
        return {
            'input_estimated': input_tokens,
            'output_estimated': output_tokens,
            'total_estimated': input_tokens + output_tokens
        }
    
    def assess_prompt_engineering_quality(self, command_content: str) -> Dict[str, Any]:
        """Judge the prompt engineering with academic rigor"""
        quality_score = 0
        max_score = 10
        issues = []
        good_patterns = []
        
        # Check for structured thinking
        if '<thinking>' in command_content or '_thinking>' in command_content:
            quality_score += 2
            good_patterns.append("Structured thinking blocks")
        else:
            issues.append("No structured thinking blocks")
        
        # Check for complexity detection
        if 'complexity' in command_content.lower() and 'assessment' in command_content.lower():
            quality_score += 2
            good_patterns.append("Complexity assessment")
        else:
            issues.append("No complexity detection")
        
        # Check for MCP integration
        if 'mcp__' in command_content:
            quality_score += 1
            good_patterns.append("MCP integration")
        
        # Check for error handling
        if 'error' in command_content.lower() and 'recovery' in command_content.lower():
            quality_score += 1
            good_patterns.append("Error recovery")
        else:
            issues.append("No error recovery patterns")
        
        # Check for examples
        example_count = len(re.findall(r'```.*?```', command_content, re.DOTALL))
        if example_count >= 3:
            quality_score += 2
            good_patterns.append(f"{example_count} code examples")
        elif example_count > 0:
            quality_score += 1
            good_patterns.append(f"Some examples ({example_count})")
        else:
            issues.append("No code examples")
        
        # Check for validation patterns
        if 'validation' in command_content.lower() or 'checklist' in command_content.lower():
            quality_score += 1
            good_patterns.append("Validation patterns")
        
        # Check for context awareness
        if '$ARGUMENTS' in command_content:
            quality_score += 1
            good_patterns.append("Context-aware design")
        else:
            issues.append("No argument processing")
        
        quality_percentage = (quality_score / max_score) * 100
        
        # Savage assessment
        if quality_percentage >= 80:
            assessment = "Actually decent engineering"
        elif quality_percentage >= 60:
            assessment = "Functional but room for improvement"
        elif quality_percentage >= 40:
            assessment = "Basic competency demonstrated"
        elif quality_percentage >= 20:
            assessment = "Needs significant work"
        else:
            assessment = "Did a junior write this?"
        
        return {
            'score': quality_score,
            'max_score': max_score,
            'percentage': quality_percentage,
            'assessment': assessment,
            'good_patterns': good_patterns,
            'issues': issues
        }
    
    def benchmark_command(self, command_path: Path) -> Dict[str, Any]:
        """Benchmark a single command with scientific precision"""
        command_name = command_path.stem
        
        with open(command_path, 'r') as f:
            content = f.read()
        
        # Calculate metrics
        complexity_score, complexity_commentary = self.calculate_complexity_score(content)
        token_usage = self.estimate_token_usage(content)
        quality_assessment = self.assess_prompt_engineering_quality(content)
        
        # Composition compatibility (can it work with others?)
        compatibility_score = 5  # Assume good until proven bad
        if complexity_score >= 4:
            compatibility_score -= 2
        if 'session' in content.lower() and 'state' in content.lower():
            compatibility_score -= 1  # Stateful = harder to compose
        if len(re.findall(r'mcp__.*__', content)) > 3:
            compatibility_score -= 1  # Too many dependencies
        
        compatibility_score = max(0, compatibility_score)
        
        # Risk assessment
        risk_factors = []
        if complexity_score >= 4:
            risk_factors.append("High complexity")
        if 'refactor' in command_name:
            risk_factors.append("Code modification risk")
        if 'sequential' in content.lower():
            risk_factors.append("Deep thinking dependency")
        if len(content) > 15000:
            risk_factors.append("Maintenance nightmare length")
        
        # Calculate hash for change tracking
        content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        
        return {
            'command_name': command_name,
            'file_size_bytes': len(content.encode()),
            'file_size_lines': len(content.split('\n')),
            'content_hash': content_hash,
            'complexity': {
                'score': complexity_score,
                'max_score': 5,
                'commentary': complexity_commentary
            },
            'token_usage': token_usage,
            'quality_assessment': quality_assessment,
            'compatibility_score': compatibility_score,
            'risk_factors': risk_factors,
            'estimated_execution_time_seconds': complexity_score * 30,  # Rough estimate
            'maintainability_score': 10 - complexity_score,  # Inverse relationship
            'last_analyzed': time.time()
        }
    
    def generate_savage_summary(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate a brutally honest summary"""
        
        # Calculate statistics
        complexity_scores = [r['complexity']['score'] for r in results]
        quality_scores = [r['quality_assessment']['percentage'] for r in results]
        compatibility_scores = [r['compatibility_score'] for r in results]
        token_estimates = [r['token_usage']['total_estimated'] for r in results]
        
        # Find the worst offenders
        most_complex = max(results, key=lambda x: x['complexity']['score'])
        lowest_quality = min(results, key=lambda x: x['quality_assessment']['percentage'])
        token_monster = max(results, key=lambda x: x['token_usage']['total_estimated'])
        least_compatible = min(results, key=lambda x: x['compatibility_score'])
        
        # Generate savage insights
        savage_insights = []
        
        if statistics.mean(complexity_scores) > 3.5:
            savage_insights.append(
                "Your commands are more complex than quantum physics. "
                "Einstein would weep at this overengineering."
            )
        
        if statistics.mean(quality_scores) < 60:
            savage_insights.append(
                "Quality scores suggest these were written during a coffee shortage. "
                "Time to read some prompt engineering books."
            )
        
        if max(token_estimates) > 5000:
            savage_insights.append(
                f"'{token_monster['command_name']}' uses ~{token_monster['token_usage']['total_estimated']} tokens. "
                "That's not a command, that's a novella with commitment issues."
            )
        
        if min(compatibility_scores) < 3:
            savage_insights.append(
                f"'{least_compatible['command_name']}' plays well with others like a toddler with anger issues. "
                "Composition? More like decomposition."
            )
        
        # ROI Analysis
        avg_complexity = statistics.mean(complexity_scores)
        avg_quality = statistics.mean(quality_scores)
        roi_score = (avg_quality / avg_complexity) if avg_complexity > 0 else 0
        
        if roi_score > 20:
            roi_assessment = "Actually worth the complexity"
        elif roi_score > 15:
            roi_assessment = "Questionable but acceptable"
        elif roi_score > 10:
            roi_assessment = "Complexity outweighing benefits"
        else:
            roi_assessment = "Engineering for the sake of engineering"
        
        return {
            'summary_statistics': {
                'total_commands_analyzed': len(results),
                'avg_complexity': round(statistics.mean(complexity_scores), 2),
                'complexity_std_dev': round(statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0, 2),
                'avg_quality_percentage': round(statistics.mean(quality_scores), 1),
                'avg_compatibility': round(statistics.mean(compatibility_scores), 1),
                'total_estimated_tokens': sum(token_estimates),
                'avg_tokens_per_command': round(statistics.mean(token_estimates))
            },
            'worst_offenders': {
                'most_complex': {
                    'command': most_complex['command_name'],
                    'score': most_complex['complexity']['score'],
                    'commentary': most_complex['complexity']['commentary']
                },
                'lowest_quality': {
                    'command': lowest_quality['command_name'],
                    'percentage': lowest_quality['quality_assessment']['percentage'],
                    'issues': lowest_quality['quality_assessment']['issues']
                },
                'token_monster': {
                    'command': token_monster['command_name'],
                    'estimated_tokens': token_monster['token_usage']['total_estimated']
                },
                'least_compatible': {
                    'command': least_compatible['command_name'],
                    'compatibility_score': least_compatible['compatibility_score']
                }
            },
            'roi_analysis': {
                'score': round(roi_score, 2),
                'assessment': roi_assessment
            },
            'savage_insights': savage_insights,
            'recommendations': [
                "Consider if that complexity is actually solving a real problem",
                "More examples, fewer philosophy dissertations",
                "Test your commands before declaring them 'intelligent'",
                "Remember: users want solutions, not architectural monuments"
            ]
        }

def main():
    """Execute the savage benchmark"""
    benchmarker = SavageBenchmarker()
    
    # Commands to benchmark
    commands = [
        Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands/java-test-driven-development.md"),
        Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands/ultrathink.md"),
        Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands/intelligent-code-enhancer.md"),
        Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands/intelligent-refactor-session.md")
    ]
    
    results = []
    for cmd_path in commands:
        if cmd_path.exists():
            print(f"Benchmarking {cmd_path.name}...")
            result = benchmarker.benchmark_command(cmd_path)
            results.append(result)
        else:
            print(f"Command not found: {cmd_path}")
    
    # Generate summary
    summary = benchmarker.generate_savage_summary(results)
    
    # Create final report
    report = {
        'benchmark_metadata': {
            'timestamp': time.time(),
            'date_human': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
            'benchmarker_version': '1.0.0-savage',
            'methodology': 'Scientific roasting with statistical backing',
            'commands_tested': len(results)
        },
        'individual_results': results,
        'savage_summary': summary
    }
    
    # Save report
    timestamp = time.strftime('%Y%m%d-%H%M%S', time.gmtime())
    report_path = Path(f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{timestamp}-savage-report.json")
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n🔥 SAVAGE BENCHMARK COMPLETE 🔥")
    print(f"Report saved to: {report_path}")
    print(f"Commands analyzed: {len(results)}")
    print(f"Average complexity: {summary['summary_statistics']['avg_complexity']}/5")
    print(f"Average quality: {summary['summary_statistics']['avg_quality_percentage']:.1f}%")
    print(f"ROI Assessment: {summary['roi_analysis']['assessment']}")
    
    return report_path

if __name__ == "__main__":
    main()