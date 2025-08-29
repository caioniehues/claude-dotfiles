#!/bin/bash
# SAVAGE COMMAND BENCHMARKER Framework
# PhD in roasting bad code with SCIENTIFIC PRECISION

set -e

COMMANDS_DIR="/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
RESULTS_DIR="/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# Command complexity scoring based on CLAUDE.md rules
calculate_complexity_score() {
    local file="$1"
    local score=1  # Base solution
    
    # Count classes, interfaces, patterns, config files
    local classes=$(grep -c "class\|interface\|enum" "$file" 2>/dev/null || echo 0)
    local patterns=$(grep -c -i "factory\|builder\|strategy\|observer\|singleton" "$file" 2>/dev/null || echo 0)
    local configs=$(grep -c -i "configuration\|config\|@Bean" "$file" 2>/dev/null || echo 0)
    local mcp_calls=$(grep -c "mcp__" "$file" 2>/dev/null || echo 0)
    
    # Apply CLAUDE.md scoring rules
    score=$((score + classes * 2))
    score=$((score + patterns * 3))  
    score=$((score + configs * 2))
    score=$((score + mcp_calls * 1))  # MCP complexity
    
    echo $score
}

# Token estimation (rough)
estimate_tokens() {
    local file="$1"
    local words=$(wc -w < "$file")
    echo $((words / 3))  # Rough token estimation
}

# Get file metrics
get_file_metrics() {
    local file="$1"
    echo "{"
    echo "  \"filename\": \"$(basename "$file")\","
    echo "  \"size_bytes\": $(stat -f%z "$file" 2>/dev/null || stat -c%s "$file"),"
    echo "  \"lines\": $(wc -l < "$file"),"
    echo "  \"words\": $(wc -w < "$file"),"
    echo "  \"estimated_tokens\": $(estimate_tokens "$file"),"
    echo "  \"complexity_score\": $(calculate_complexity_score "$file")"
    echo "}"
}

echo "🔬 SAVAGE COMMAND BENCHMARKER Framework Initialized"
echo "📊 Found $(ls "$COMMANDS_DIR"/*.md | wc -l) commands to scientifically roast"
echo "📂 Results will be stored in: $RESULTS_DIR"