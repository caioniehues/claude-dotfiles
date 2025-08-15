#!/bin/bash

# SAVAGE COMMAND BENCHMARKER
# PhD-level roasting with statistical precision
# Usage: ./run-savage-benchmark.sh [num_commands]

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BENCHMARKER_SCRIPT="$SCRIPT_DIR/scripts/savage-command-benchmarker.py"
RESULTS_DIR="$SCRIPT_DIR/results"
NUM_COMMANDS=${1:-3}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

echo -e "${PURPLE}🔬 SAVAGE COMMAND BENCHMARKER${NC}"
echo -e "${PURPLE}PhD in roasting bad code with statistical precision${NC}"
echo "============================================================"

# Check dependencies
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 not found! Please install Python 3.7+${NC}"
    exit 1
fi

# Check if commands directory exists
if [ ! -d "commands" ]; then
    echo -e "${RED}❌ Commands directory not found!${NC}"
    echo "Please run this script from the repository root."
    exit 1
fi

# Create necessary directories
mkdir -p "$RESULTS_DIR"
mkdir -p "$SCRIPT_DIR/data"

echo -e "${BLUE}📊 Running benchmark on $NUM_COMMANDS random commands...${NC}"

# Run the benchmarker
python3 "$BENCHMARKER_SCRIPT" "$NUM_COMMANDS"

# Find the latest report
LATEST_REPORT=$(ls -t "$RESULTS_DIR"/*.json | head -n1)

if [ -f "$LATEST_REPORT" ]; then
    echo -e "${GREEN}✅ Benchmark complete!${NC}"
    echo -e "${BLUE}📄 Report: $LATEST_REPORT${NC}"
    
    # Extract key metrics for summary
    if command -v jq &> /dev/null; then
        echo ""
        echo -e "${YELLOW}📊 QUICK SUMMARY:${NC}"
        
        OVERALL_SCORE=$(jq -r '.aggregate_statistics.overall_scores.mean' "$LATEST_REPORT" 2>/dev/null || echo "N/A")
        COMPLEXITY_VIOLATIONS=$(jq -r '.aggregate_statistics.commands_exceeding_complexity' "$LATEST_REPORT" 2>/dev/null || echo "N/A")
        TOTAL_ANALYZED=$(jq -r '.aggregate_statistics.total_commands_analyzed' "$LATEST_REPORT" 2>/dev/null || echo "N/A")
        
        printf "   Average Quality Score: %.1f/100\n" "$OVERALL_SCORE" 2>/dev/null || echo "   Average Quality Score: $OVERALL_SCORE/100"
        echo "   Complexity Violations: $COMPLEXITY_VIOLATIONS/$TOTAL_ANALYZED commands"
        
        # Extract commentary
        COMMENTARY=$(jq -r '.summary_commentary' "$LATEST_REPORT" 2>/dev/null || echo "Commentary not available")
        echo ""
        echo -e "${YELLOW}🎯 VERDICT:${NC}"
        echo "$COMMENTARY"
        
    else
        echo -e "${YELLOW}💡 Install 'jq' for detailed summary output${NC}"
    fi
    
    echo ""
    echo -e "${BLUE}🔍 To view full report:${NC}"
    echo "   cat $LATEST_REPORT | jq ."
    echo ""
    echo -e "${BLUE}📈 To run continuous benchmarking:${NC}"
    echo "   watch -n 3600 './run-savage-benchmark.sh 5'"
    
else
    echo -e "${RED}❌ Benchmark failed - no report generated${NC}"
    exit 1
fi

# Optional: Auto-commit results if in git repo
if [ -d ".git" ] && [ "$2" = "--commit" ]; then
    echo -e "${BLUE}📝 Auto-committing benchmark results...${NC}"
    git add "$LATEST_REPORT"
    
    # Extract timestamp for commit message
    TIMESTAMP=$(basename "$LATEST_REPORT" | cut -d'-' -f1-2)
    
    git commit -m "🔬 Benchmark Report $TIMESTAMP: Your commands have been scientifically roasted

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>" || echo "Nothing to commit"
fi

echo -e "${GREEN}🎉 Savage benchmarking complete!${NC}"