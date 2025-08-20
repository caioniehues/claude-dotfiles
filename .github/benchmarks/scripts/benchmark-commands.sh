#!/bin/bash

# SAVAGE COMMAND BENCHMARKER SCRIPT
# Scientifically measures and brutally judges command quality
# Usage: ./benchmark-commands.sh [--all | --random N | command1 command2 ...]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
COMMANDS_DIR="$REPO_ROOT/commands"
RESULTS_DIR="$REPO_ROOT/.github/benchmarks/results"
METRICS_DIR="$REPO_ROOT/.github/benchmarks/metrics"

# Ensure directories exist
mkdir -p "$RESULTS_DIR" "$METRICS_DIR"

# Colors for savage commentary
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to calculate CLAUDE.md complexity score
calculate_complexity_score() {
    local file="$1"
    local score=1  # Base score for direct solution
    
    # Count new classes (+2 each)
    local classes=$(grep -c "^class \|^public class \|^private class " "$file" 2>/dev/null || echo 0)
    score=$((score + classes * 2))
    
    # Count interfaces (+1 each)
    local interfaces=$(grep -c "^interface \|^public interface " "$file" 2>/dev/null || echo 0)
    score=$((score + interfaces))
    
    # Count design patterns (+3 each - look for common pattern indicators)
    local patterns=0
    patterns=$((patterns + $(grep -c "Factory\|Builder\|Strategy\|Observer\|Singleton" "$file" 2>/dev/null || echo 0)))
    score=$((score + patterns * 3))
    
    # Count configuration files (+2 each - look for config indicators)
    local configs=$(grep -c "config\|configuration\|settings\.json\|\.yml\|\.yaml" "$file" 2>/dev/null || echo 0)
    score=$((score + configs * 2))
    
    # Special complexity indicators for command files
    local thinking_blocks=$(grep -c "<thinking>\|<.*_thinking>" "$file" 2>/dev/null || echo 0)
    score=$((score + thinking_blocks / 3))  # Every 3 thinking blocks = +1 complexity
    
    local orchestration=$(grep -c "orchestration\|mcp__\|sequential" "$file" 2>/dev/null || echo 0)
    score=$((score + orchestration / 2))  # Every 2 orchestration refs = +1 complexity
    
    echo "$score"
}

# Function to estimate token consumption
estimate_tokens() {
    local file="$1"
    local line_count=$(wc -l < "$file")
    local char_count=$(wc -c < "$file")
    
    # Rough estimation: 1 token ≈ 4 characters, plus response multiplier
    local input_tokens=$((char_count / 4))
    local estimated_response_tokens=$((input_tokens * 13 / 10))  # 1.3x response factor
    local total_tokens=$((input_tokens + estimated_response_tokens))
    
    echo "$total_tokens"
}

# Function to assess cognitive load
assess_cognitive_load() {
    local file="$1"
    local load=1
    
    # Count nesting indicators
    local nesting=$(grep -c "^  .*<\|^    .*<\|^      .*<" "$file" 2>/dev/null || echo 0)
    load=$((load + nesting / 10))
    
    # Count decision points
    local decisions=$(grep -c "if\|else\|switch\|case\|when\|routing\|decision" "$file" 2>/dev/null || echo 0)
    load=$((load + decisions / 5))
    
    # Count abstractions
    local abstractions=$(grep -c "abstract\|interface\|pattern\|orchestrat\|meta" "$file" 2>/dev/null || echo 0)
    load=$((load + abstractions / 3))
    
    # Cap at 10
    if [ "$load" -gt 10 ]; then
        load=10
    fi
    
    echo "$load"
}

# Function to generate savage commentary
generate_savage_verdict() {
    local complexity="$1"
    local tokens="$2"
    local cognitive_load="$3"
    local lines="$4"
    local filename="$5"
    
    local verdict=""
    local probability=50
    
    if [ "$complexity" -ge 5 ]; then
        verdict="ARCHITECTURAL ABOMINATION"
        probability=15
    elif [ "$complexity" -ge 4 ]; then
        verdict="OVER-ENGINEERED NIGHTMARE"
        probability=25
    elif [ "$complexity" -ge 3 ]; then
        verdict="ACCEPTABLE CHAOS"
        probability=45
    else
        verdict="SURPRISINGLY COMPETENT"
        probability=75
    fi
    
    # Adjust probability based on other factors
    if [ "$tokens" -gt 10000 ]; then
        probability=$((probability - 20))
    fi
    
    if [ "$cognitive_load" -gt 7 ]; then
        probability=$((probability - 15))
    fi
    
    if [ "$lines" -gt 400 ]; then
        probability=$((probability - 10))
    fi
    
    # Ensure probability is within bounds
    if [ "$probability" -lt 5 ]; then
        probability=5
    elif [ "$probability" -gt 95 ]; then
        probability=95
    fi
    
    echo "$verdict|$probability"
}

# Function to benchmark a single command
benchmark_command() {
    local cmd_file="$1"
    local cmd_name=$(basename "$cmd_file" .md)
    
    echo -e "${BLUE}🔬 Analyzing $cmd_name...${NC}"
    
    # Basic metrics
    local lines=$(wc -l < "$cmd_file")
    local complexity=$(calculate_complexity_score "$cmd_file")
    local tokens=$(estimate_tokens "$cmd_file")
    local cognitive_load=$(assess_cognitive_load "$cmd_file")
    
    # Generate verdict
    local verdict_data=$(generate_savage_verdict "$complexity" "$tokens" "$cognitive_load" "$lines" "$cmd_name")
    local verdict=$(echo "$verdict_data" | cut -d'|' -f1)
    local probability=$(echo "$verdict_data" | cut -d'|' -f2)
    
    # Cost calculation (assuming $3/1M tokens)
    local cost_low=$(echo "scale=2; $tokens * 0.000003" | bc)
    local cost_high=$(echo "scale=3; $tokens * 0.000003 * 1.5" | bc)
    
    # Color-coded output based on complexity
    local color=$GREEN
    if [ "$complexity" -ge 5 ]; then
        color=$RED
    elif [ "$complexity" -ge 4 ]; then
        color=$YELLOW
    fi
    
    echo -e "${color}📊 Results for $cmd_name:${NC}"
    echo "   Lines of Code: $lines"
    echo "   Complexity Score: $complexity/5 $([ "$complexity" -ge 5 ] && echo "⚠️ EXCEEDS THRESHOLD" || echo "✅")"
    echo "   Estimated Tokens: $tokens"
    echo "   Cognitive Load: $cognitive_load/10"
    echo "   Estimated Cost: \$${cost_low} - \$${cost_high}"
    echo "   Savage Verdict: $verdict"
    echo "   Probability of Use: ${probability}%"
    echo ""
    
    # Save detailed metrics to JSON
    cat > "$METRICS_DIR/${cmd_name}_metrics.json" << EOF
{
  "command": "$cmd_name",
  "metrics": {
    "lines_of_code": $lines,
    "complexity_score": $complexity,
    "estimated_tokens": $tokens,
    "cognitive_load": $cognitive_load,
    "estimated_cost_range": "\\$${cost_low} - \\$${cost_high}",
    "savage_verdict": "$verdict",
    "probability_of_use": $probability
  },
  "analysis_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "claude_md_compliance": $([ "$complexity" -lt 5 ] && echo "true" || echo "false")
}
EOF
    
    # Return data for aggregation
    echo "$cmd_name,$lines,$complexity,$tokens,$cognitive_load,$probability,$verdict"
}

# Main benchmarking function
run_benchmark() {
    local commands_to_analyze=("$@")
    
    echo -e "${RED}🔬 SAVAGE COMMAND BENCHMARKER v2.0${NC}"
    echo -e "${RED}Where brutal honesty meets statistical rigor${NC}"
    echo ""
    
    # Track aggregate statistics
    local total_commands=0
    local total_complexity=0
    local threshold_violations=0
    local total_tokens=0
    local results=()
    
    # Process each command
    for cmd_file in "${commands_to_analyze[@]}"; do
        if [ -f "$cmd_file" ]; then
            local result=$(benchmark_command "$cmd_file")
            results+=("$result")
            
            # Extract metrics for aggregation
            local complexity=$(echo "$result" | cut -d',' -f3)
            local tokens=$(echo "$result" | cut -d',' -f4)
            
            total_commands=$((total_commands + 1))
            total_complexity=$((total_complexity + complexity))
            total_tokens=$((total_tokens + tokens))
            
            if [ "$complexity" -ge 5 ]; then
                threshold_violations=$((threshold_violations + 1))
            fi
        else
            echo -e "${RED}⚠️  Command file not found: $cmd_file${NC}"
        fi
    done
    
    # Generate summary report
    if [ "$total_commands" -gt 0 ]; then
        echo -e "${RED}📈 SAVAGE SUMMARY STATISTICS${NC}"
        echo "=================================="
        
        local avg_complexity=$(echo "scale=1; $total_complexity / $total_commands" | bc)
        local compliance_rate=$(echo "scale=0; ($total_commands - $threshold_violations) * 100 / $total_commands" | bc)
        local avg_tokens=$(echo "scale=0; $total_tokens / $total_commands" | bc)
        
        echo "Commands Analyzed: $total_commands"
        echo "Average Complexity Score: $avg_complexity/5"
        echo "CLAUDE.md Compliance Rate: ${compliance_rate}%"
        echo "Threshold Violations: $threshold_violations"
        echo "Average Token Consumption: $avg_tokens"
        echo ""
        
        # Savage verdict based on aggregate data
        if [ "$threshold_violations" -gt $((total_commands / 2)) ]; then
            echo -e "${RED}🔥 AGGREGATE VERDICT: CATASTROPHIC COMPLEXITY INFLATION${NC}"
            echo "Your commands have violated CLAUDE.md principles with the enthusiasm of"
            echo "a toddler violating physics. Consider intervention."
        elif [ "$threshold_violations" -gt 0 ]; then
            echo -e "${YELLOW}⚠️  AGGREGATE VERDICT: CONCERNING COMPLEXITY CREEP${NC}"
            echo "Some commands are showing symptoms of over-engineering. Monitor closely."
        else
            echo -e "${GREEN}✅ AGGREGATE VERDICT: ACCEPTABLE ENGINEERING DISCIPLINE${NC}"
            echo "Congratulations! You've managed to write commands without going insane."
        fi
        
        echo ""
        echo "Detailed analysis saved to: $RESULTS_DIR/"
        echo "Individual metrics saved to: $METRICS_DIR/"
    fi
}

# Command line argument parsing
if [ $# -eq 0 ]; then
    # Default: analyze all commands
    echo "No arguments provided. Analyzing all commands..."
    commands=("$COMMANDS_DIR"/*.md)
elif [ "$1" = "--all" ]; then
    commands=("$COMMANDS_DIR"/*.md)
elif [ "$1" = "--random" ] && [ $# -ge 2 ]; then
    n="$2"
    echo "Randomly selecting $n commands for analysis..."
    # Get random sample
    commands=($(find "$COMMANDS_DIR" -name "*.md" | shuf -n "$n"))
else
    # Specific commands provided
    commands=()
    for arg in "$@"; do
        if [[ "$arg" == *.md ]]; then
            commands+=("$arg")
        else
            commands+=("$COMMANDS_DIR/${arg}.md")
        fi
    done
fi

# Run the benchmark
run_benchmark "${commands[@]}"

echo ""
echo -e "${BLUE}💡 Pro tip: Try './benchmark-commands.sh --random 3' for a quick sample${NC}"
echo -e "${BLUE}📊 Or use './benchmark-commands.sh command1 command2' for specific analysis${NC}"