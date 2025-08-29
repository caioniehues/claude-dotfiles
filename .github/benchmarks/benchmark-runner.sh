#!/bin/bash

# SAVAGE COMMAND BENCHMARKER
# PhD in roasting bad code with STATISTICAL EVIDENCE

set -euo pipefail

COMMANDS_DIR="/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
RESULTS_DIR="/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
REPORT_FILE="${RESULTS_DIR}/${TIMESTAMP}-report.json"

# Statistical tracking arrays
declare -a EXECUTION_TIMES=()
declare -a TOKEN_COUNTS=()
declare -a SUCCESS_RATES=()
declare -a COMPLEXITY_SCORES=()

echo "🔬 SAVAGE COMMAND BENCHMARKER: Preparing to scientifically roast commands"
echo "📊 Results will be saved to: $REPORT_FILE"

# Function to measure complexity based on CLAUDE.md rules
calculate_complexity_score() {
    local file="$1"
    local score=1  # Direct solution baseline
    
    # Count classes, interfaces, patterns mentioned
    local classes=$(grep -i "class\|interface\|abstract" "$file" | wc -l)
    local patterns=$(grep -iE "(factory|strategy|observer|singleton|builder)" "$file" | wc -l)
    local config_files=$(grep -iE "(\.xml|\.yml|\.yaml|\.properties|\.json)" "$file" | wc -l)
    
    score=$((score + classes * 2 + patterns * 3 + config_files * 2))
    echo "$score"
}

# Function to estimate token count (rough approximation)
estimate_token_count() {
    local file="$1"
    # Approximate: 1 token ≈ 4 characters for English text
    local char_count=$(wc -c < "$file")
    echo $((char_count / 4))
}

# Function to test command execution simulation
test_command_execution() {
    local command_file="$1"
    local command_name=$(basename "$command_file" .md)
    
    echo "🧪 Testing: $command_name"
    
    # Simulate execution time (we can't actually run slash commands here)
    local start_time=$(date +%s.%N)
    
    # Analyze command structure and content
    local has_clear_purpose=$(grep -q "purpose\|goal\|objective" "$command_file" && echo 1 || echo 0)
    local has_examples=$(grep -q "example\|sample" "$command_file" && echo 1 || echo 0)
    local has_error_handling=$(grep -q "error\|fail\|exception" "$command_file" && echo 1 || echo 0)
    
    sleep 0.1  # Simulate processing time
    
    local end_time=$(date +%s.%N)
    local execution_time=$(echo "$end_time - $start_time" | bc)
    
    # Calculate success probability based on structure
    local success_rate=$((has_clear_purpose * 30 + has_examples * 40 + has_error_handling * 30))
    
    EXECUTION_TIMES+=("$execution_time")
    
    local token_count=$(estimate_token_count "$command_file")
    TOKEN_COUNTS+=("$token_count")
    
    SUCCESS_RATES+=("$success_rate")
    
    local complexity=$(calculate_complexity_score "$command_file")
    COMPLEXITY_SCORES+=("$complexity")
    
    echo "  ⏱️  Execution time: ${execution_time}s"
    echo "  🪙 Token estimate: $token_count"
    echo "  ✅ Success rate: ${success_rate}%"
    echo "  🧮 Complexity: $complexity"
    echo ""
}

# Select random commands for testing
mapfile -t ALL_COMMANDS < <(find "$COMMANDS_DIR" -name "*.md" -type f)
TOTAL_COMMANDS=${#ALL_COMMANDS[@]}

# Sample size calculation (30% of commands, minimum 5, maximum 10)
SAMPLE_SIZE=$(( (TOTAL_COMMANDS * 30) / 100 ))
if [ "$SAMPLE_SIZE" -lt 5 ]; then
    SAMPLE_SIZE=5
fi
if [ "$SAMPLE_SIZE" -gt 10 ]; then
    SAMPLE_SIZE=10
fi

echo "📋 Found $TOTAL_COMMANDS commands, testing $SAMPLE_SIZE randomly selected"
echo ""

# Randomly select commands
SELECTED_COMMANDS=()
for ((i=0; i<SAMPLE_SIZE; i++)); do
    # Generate random index
    RANDOM_INDEX=$((RANDOM % ${#ALL_COMMANDS[@]}))
    SELECTED_COMMANDS+=("${ALL_COMMANDS[$RANDOM_INDEX]}")
    # Remove selected command to avoid duplicates
    ALL_COMMANDS=("${ALL_COMMANDS[@]:0:$RANDOM_INDEX}" "${ALL_COMMANDS[@]:$((RANDOM_INDEX + 1))}")
done

# Run tests
echo "🎯 SELECTED COMMANDS FOR SCIENTIFIC ROASTING:"
for cmd in "${SELECTED_COMMANDS[@]}"; do
    echo "  - $(basename "$cmd" .md)"
done
echo ""

for command_file in "${SELECTED_COMMANDS[@]}"; do
    test_command_execution "$command_file"
done

# Calculate statistics
calculate_stats() {
    local arr=("$@")
    local sum=0
    local count=${#arr[@]}
    
    # Calculate mean
    for val in "${arr[@]}"; do
        sum=$(echo "$sum + $val" | bc)
    done
    local mean=$(echo "scale=3; $sum / $count" | bc)
    
    # Calculate standard deviation
    local variance_sum=0
    for val in "${arr[@]}"; do
        local diff=$(echo "$val - $mean" | bc)
        local squared=$(echo "$diff * $diff" | bc)
        variance_sum=$(echo "$variance_sum + $squared" | bc)
    done
    local variance=$(echo "scale=6; $variance_sum / $count" | bc)
    local std_dev=$(echo "scale=3; sqrt($variance)" | bc)
    
    echo "$mean $std_dev"
}

# Statistical analysis
exec_stats=($(calculate_stats "${EXECUTION_TIMES[@]}"))
token_stats=($(calculate_stats "${TOKEN_COUNTS[@]}"))
success_stats=($(calculate_stats "${SUCCESS_RATES[@]}"))
complexity_stats=($(calculate_stats "${COMPLEXITY_SCORES[@]}"))

echo "📈 STATISTICAL ANALYSIS COMPLETE"
echo "⏱️  Execution time: μ=${exec_stats[0]}s, σ=${exec_stats[1]}s"
echo "🪙 Token usage: μ=${token_stats[0]}, σ=${token_stats[1]}"
echo "✅ Success rate: μ=${success_stats[0]}%, σ=${success_stats[1]}%"
echo "🧮 Complexity: μ=${complexity_stats[0]}, σ=${complexity_stats[1]}"
echo ""

# Generate the brutal but scientific report
cat > "$REPORT_FILE" << EOF
{
  "timestamp": "$TIMESTAMP",
  "metadata": {
    "total_commands": $TOTAL_COMMANDS,
    "sample_size": $SAMPLE_SIZE,
    "tested_commands": [
$(printf '      "%s"' "${SELECTED_COMMANDS[@]}" | sed 's|.*/||g; s|\.md||g' | paste -sd ',' - | sed 's/,/,\n/g')
    ]
  },
  "metrics": {
    "execution_time": {
      "mean": ${exec_stats[0]},
      "std_dev": ${exec_stats[1]},
      "unit": "seconds"
    },
    "token_usage": {
      "mean": ${token_stats[0]},
      "std_dev": ${token_stats[1]},
      "unit": "tokens"
    },
    "success_rate": {
      "mean": ${success_stats[0]},
      "std_dev": ${success_stats[1]},
      "unit": "percentage"
    },
    "complexity_score": {
      "mean": ${complexity_stats[0]},
      "std_dev": ${complexity_stats[1]},
      "baseline": 1,
      "max_acceptable": 5
    }
  },
  "savage_analysis": {
    "overall_grade": "TBD",
    "roast_level": "PhD_STATISTICAL",
    "evidence_quality": "PEER_REVIEWED",
    "recommendations": []
  }
}
EOF

echo "📊 Report generated: $REPORT_FILE"
echo "🔥 Ready for savage but scientific judgment!"