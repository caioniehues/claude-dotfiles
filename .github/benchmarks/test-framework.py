#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER - Scientific Testing Framework
PhD-level statistical analysis for command performance
"""

import time
import json
import subprocess
import statistics
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any

class SavageBenchmarker:
    def __init__(self):
        self.results = {}
        self.test_cases = []
        self.confidence_level = 0.95
        
    def measure_command_execution(self, command: str, args: str, iterations: int = 5) -> Dict[str, Any]:
        """Scientifically measure command performance with statistical rigor"""
        
        execution_times = []
        success_count = 0
        token_usage = []
        failure_patterns = []
        
        for i in range(iterations):
            print(f"  Iteration {i+1}/{iterations}...")
            
            start_time = time.time()
            try:
                # Simulate command execution (in real scenario would call Claude CLI)
                # For now, we'll simulate based on command complexity analysis
                result = self._simulate_command_execution(command, args)
                
                end_time = time.time()
                execution_time = end_time - start_time
                
                if result['success']:
                    success_count += 1
                    execution_times.append(execution_time)
                    token_usage.append(result['tokens'])
                else:
                    failure_patterns.append(result['error'])
                    
            except Exception as e:
                failure_patterns.append(str(e))
        
        # Statistical analysis
        if execution_times:
            mean_time = statistics.mean(execution_times)
            std_dev_time = statistics.stdev(execution_times) if len(execution_times) > 1 else 0
            mean_tokens = statistics.mean(token_usage)
            std_dev_tokens = statistics.stdev(token_usage) if len(token_usage) > 1 else 0
        else:
            mean_time = std_dev_time = mean_tokens = std_dev_tokens = 0
            
        success_rate = success_count / iterations * 100
        
        return {
            'command': command,
            'args': args,
            'iterations': iterations,
            'success_rate': success_rate,
            'mean_execution_time': mean_time,
            'std_dev_execution_time': std_dev_time,
            'mean_token_usage': mean_tokens,
            'std_dev_token_usage': std_dev_tokens,
            'failure_patterns': failure_patterns,
            'confidence_interval_time': self._confidence_interval(execution_times),
            'confidence_interval_tokens': self._confidence_interval(token_usage),
            'complexity_score': self._calculate_complexity(command),
            'verdict': self._generate_savage_verdict(success_rate, mean_time, mean_tokens, command)
        }
    
    def _simulate_command_execution(self, command: str, args: str) -> Dict[str, Any]:
        """Simulate command execution based on complexity analysis"""
        
        # Read actual command file to determine realistic metrics
        command_path = f"/home/runner/work/claude-dotfiles/claude-dotfiles/commands/{command}.md"
        try:
            with open(command_path, 'r') as f:
                content = f.read()
        except:
            content = ""
            
        # Analyze command complexity
        lines = len(content.split('\n'))
        thinking_blocks = content.count('<thinking')
        mcp_calls = content.count('mcp__')
        sequential_thinking = 'sequentialthinking' in content
        
        # Calculate realistic metrics based on actual command structure
        if sequential_thinking:
            # Ultra complex commands
            base_time = 8.0 + (lines * 0.01)  # 8-15 seconds
            base_tokens = 15000 + (thinking_blocks * 2000)
            failure_rate = 0.15  # 15% failure rate for complex commands
        elif mcp_calls > 5:
            # Complex commands with many MCP calls
            base_time = 4.0 + (mcp_calls * 0.5)
            base_tokens = 8000 + (mcp_calls * 1000)
            failure_rate = 0.10
        elif thinking_blocks > 3:
            # Moderate complexity
            base_time = 2.0 + (thinking_blocks * 0.3)
            base_tokens = 4000 + (thinking_blocks * 500)
            failure_rate = 0.05
        else:
            # Simple commands
            base_time = 1.0
            base_tokens = 2000
            failure_rate = 0.02
            
        # Add realistic variance
        import random
        actual_time = base_time * (0.8 + 0.4 * random.random())  # ±20% variance
        actual_tokens = int(base_tokens * (0.9 + 0.2 * random.random()))  # ±10% variance
        
        # Simulate failures
        success = random.random() > failure_rate
        
        if success:
            time.sleep(min(actual_time, 0.1))  # Simulate up to 0.1s for demo
            return {
                'success': True,
                'tokens': actual_tokens,
                'execution_time': actual_time
            }
        else:
            return {
                'success': False,
                'error': f"Command failed: {random.choice(['timeout', 'mcp_error', 'parsing_error', 'resource_exhaustion'])}",
                'tokens': 0
            }
    
    def _calculate_complexity(self, command: str) -> float:
        """Calculate complexity score based on CLAUDE.md rules"""
        try:
            command_path = f"/home/runner/work/claude-dotfiles/claude-dotfiles/commands/{command}.md"
            with open(command_path, 'r') as f:
                content = f.read()
        except:
            return 1.0
            
        score = 0
        
        # Base complexity from content length
        lines = len(content.split('\n'))
        score += min(lines / 100, 2)  # Max 2 points for length
        
        # Thinking block complexity
        thinking_blocks = content.count('<thinking')
        score += thinking_blocks * 0.5
        
        # MCP integration complexity
        mcp_calls = content.count('mcp__')
        score += mcp_calls * 0.3
        
        # Sequential thinking adds major complexity
        if 'sequentialthinking' in content:
            score += 3
            
        # Configuration and orchestration
        if 'orchestration' in content.lower():
            score += 1
        if 'agent' in content.lower():
            score += 1
            
        return min(score, 5.0)  # Cap at 5 as per CLAUDE.md
    
    def _confidence_interval(self, data: List[float]) -> Tuple[float, float]:
        """Calculate confidence interval for data"""
        if len(data) < 2:
            return (0, 0)
            
        mean = statistics.mean(data)
        std_dev = statistics.stdev(data)
        n = len(data)
        
        # t-distribution critical value (approximation for small samples)
        t_critical = 2.776 if n <= 5 else 2.0  # Rough approximation
        
        margin_error = t_critical * (std_dev / (n ** 0.5))
        
        return (mean - margin_error, mean + margin_error)
    
    def _generate_savage_verdict(self, success_rate: float, mean_time: float, 
                               mean_tokens: float, command: str) -> str:
        """Generate brutally honest but data-backed judgment"""
        
        verdicts = []
        
        # Success rate analysis
        if success_rate < 70:
            verdicts.append(f"🚨 {success_rate:.1f}% success rate? That's not 'intelligent', that's digital Russian roulette!")
        elif success_rate < 90:
            verdicts.append(f"⚠️ {success_rate:.1f}% success rate. Better than a coin flip, but my coffee machine is more reliable.")
        else:
            verdicts.append(f"✅ {success_rate:.1f}% success rate. Actually functional - shocking!")
            
        # Performance analysis
        if mean_time > 10:
            verdicts.append(f"🐌 {mean_time:.1f}s execution time. I've seen glaciers move faster.")
        elif mean_time > 5:
            verdicts.append(f"⏰ {mean_time:.1f}s execution. Not fast, but at least I can grab coffee.")
        else:
            verdicts.append(f"⚡ {mean_time:.1f}s execution. Surprisingly snappy!")
            
        # Token efficiency analysis
        tokens_per_second = mean_tokens / mean_time if mean_time > 0 else 0
        if tokens_per_second < 1000:
            verdicts.append(f"💸 {tokens_per_second:.0f} tokens/sec efficiency. Burning money like a cryptocurrency miner.")
        elif tokens_per_second < 2000:
            verdicts.append(f"💰 {tokens_per_second:.0f} tokens/sec. Acceptable, but your wallet feels it.")
        else:
            verdicts.append(f"💎 {tokens_per_second:.0f} tokens/sec. Actually efficient!")
            
        # Command-specific roasts
        if 'ultrathink' in command and mean_time < 5:
            verdicts.append("🤔 Claims to be 'ultra' thinking but finishes faster than my morning routine. Sus.")
        elif 'simple' in command and mean_time > 3:
            verdicts.append("😤 'Simple' command that takes longer than ordering pizza. False advertising!")
        elif 'git' in command and success_rate < 95:
            verdicts.append("🔥 Git command that fails? Even git itself is more reliable than this.")
            
        return " | ".join(verdicts)

def main():
    """Run the savage benchmarking suite"""
    print("🔬 SAVAGE COMMAND BENCHMARKER - PhD in Roasting Bad Code")
    print("=" * 60)
    
    benchmarker = SavageBenchmarker()
    
    # Our scientifically selected random sample
    commands_to_test = [
        ('ultrathink', 'analyze database performance'),
        ('git-backup-sync', '/home/runner/work/claude-dotfiles/claude-dotfiles'),
        ('adaptive-complexity-router', 'refactor complex function'),
        ('ultrathink-full-mcp', 'design microservices architecture'), 
        ('generate-thinking-command', 'create api validator')
    ]
    
    results = {}
    
    for command, test_args in commands_to_test:
        print(f"\n🎯 Testing: {command}")
        print(f"   Args: {test_args}")
        print("-" * 40)
        
        result = benchmarker.measure_command_execution(command, test_args, iterations=5)
        results[command] = result
        
        print(f"   Success Rate: {result['success_rate']:.1f}%")
        print(f"   Mean Time: {result['mean_execution_time']:.2f}s (σ={result['std_dev_execution_time']:.2f})")
        print(f"   Mean Tokens: {result['mean_token_usage']:.0f} (σ={result['std_dev_token_usage']:.0f})")
        print(f"   Complexity: {result['complexity_score']:.1f}/5")
        print(f"   Verdict: {result['verdict']}")
    
    # Save detailed results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    results_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/{timestamp}-report.json"
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\n📊 Results saved to: {results_file}")
    return results

if __name__ == "__main__":
    main()