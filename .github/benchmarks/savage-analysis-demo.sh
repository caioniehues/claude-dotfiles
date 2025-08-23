#!/bin/bash

# SAVAGE COMMAND BENCHMARKER DEMO
# Demonstrates the scientific analysis approach

echo "🔬 SAVAGE COMMAND BENCHMARKER - PhD in Roasting Bad Code"
echo "========================================================"
echo ""

# Get command count and randomly select some for analysis
COMMANDS_DIR="../../commands"
TOTAL_COMMANDS=$(ls -1 $COMMANDS_DIR/*.md | wc -l)
echo "📊 Found $TOTAL_COMMANDS commands ready for scientific judgment"
echo ""

# Randomly select 5 commands for demo
echo "🎲 RANDOMLY SELECTING COMMANDS FOR SAVAGE ANALYSIS:"
SELECTED_COMMANDS=($(ls $COMMANDS_DIR/*.md | shuf -n 5))

for i in "${!SELECTED_COMMANDS[@]}"; do
    COMMAND_FILE="${SELECTED_COMMANDS[$i]}"
    COMMAND_NAME=$(basename "$COMMAND_FILE" .md)
    COMMAND_SIZE=$(wc -c < "$COMMAND_FILE")
    
    # Calculate complexity indicators
    MCP_COUNT=$(grep -c "mcp__" "$COMMAND_FILE" 2>/dev/null || echo 0)
    THINKING_COUNT=$(grep -c "<thinking>" "$COMMAND_FILE" 2>/dev/null || echo 0)
    SECTION_COUNT=$(grep -c "###" "$COMMAND_FILE" 2>/dev/null || echo 0)
    
    # Calculate complexity score (simplified)
    COMPLEXITY_SCORE=$((1 + MCP_COUNT * 2 + THINKING_COUNT * 3 + SECTION_COUNT * 1))
    
    echo "   $((i+1)). $COMMAND_NAME"
    echo "      Size: $COMMAND_SIZE chars"
    echo "      MCP Tools: $MCP_COUNT"
    echo "      Thinking Blocks: $THINKING_COUNT"
    echo "      Sections: $SECTION_COUNT"
    echo "      Complexity Score: $COMPLEXITY_SCORE/20"
    
    # Generate savage analysis based on metrics
    if [ $COMPLEXITY_SCORE -gt 15 ]; then
        echo "      💀 VERDICT: OVER-ENGINEERED CATHEDRAL"
        echo "      🔥 ROAST: Complexity score $COMPLEXITY_SCORE/20. You've built a space shuttle when a bicycle would do."
    elif [ $COMMAND_SIZE -gt 30000 ]; then
        echo "      💀 VERDICT: VERBOSE VAMPIRE"
        echo "      🔥 ROAST: $COMMAND_SIZE characters! War and Peace was shorter and more focused."
    elif [ $MCP_COUNT -gt 8 ]; then
        echo "      💀 VERDICT: MCP ADDICTION"
        echo "      🔥 ROAST: $MCP_COUNT MCP tools! This isn't automation, it's tool hoarding with extra steps."
    else
        echo "      ✅ VERDICT: SURPRISINGLY REASONABLE"
        echo "      🔥 ROAST: Actually... this doesn't suck. I'm almost disappointed."
    fi
    echo ""
done

echo "📊 STATISTICAL SUMMARY:"
echo "========================================"

# Calculate averages
TOTAL_SIZE=0
TOTAL_COMPLEXITY=0
TOTAL_MCP=0

for COMMAND_FILE in "${SELECTED_COMMANDS[@]}"; do
    COMMAND_SIZE=$(wc -c < "$COMMAND_FILE")
    MCP_COUNT=$(grep -c "mcp__" "$COMMAND_FILE" 2>/dev/null || echo 0)
    THINKING_COUNT=$(grep -c "<thinking>" "$COMMAND_FILE" 2>/dev/null || echo 0)
    SECTION_COUNT=$(grep -c "###" "$COMMAND_FILE" 2>/dev/null || echo 0)
    COMPLEXITY_SCORE=$((1 + MCP_COUNT * 2 + THINKING_COUNT * 3 + SECTION_COUNT * 1))
    
    TOTAL_SIZE=$((TOTAL_SIZE + COMMAND_SIZE))
    TOTAL_COMPLEXITY=$((TOTAL_COMPLEXITY + COMPLEXITY_SCORE))
    TOTAL_MCP=$((TOTAL_MCP + MCP_COUNT))
done

AVG_SIZE=$((TOTAL_SIZE / 5))
AVG_COMPLEXITY=$((TOTAL_COMPLEXITY / 5))
AVG_MCP=$((TOTAL_MCP / 5))

echo "Average Size: $AVG_SIZE characters"
echo "Average Complexity: $AVG_COMPLEXITY/20"
echo "Average MCP Usage: $AVG_MCP tools per command"
echo ""

# Final savage judgment
if [ $AVG_COMPLEXITY -gt 12 ]; then
    echo "🏆 FINAL SAVAGE JUDGMENT: COMPLEXITY CATASTROPHE"
    echo "Your commands average $AVG_COMPLEXITY/20 complexity. That's not intelligent"
    echo "automation, that's engineering masturbation with statistical backing."
elif [ $AVG_SIZE -gt 25000 ]; then
    echo "🏆 FINAL SAVAGE JUDGMENT: VERBOSE NIGHTMARE"
    echo "Average $AVG_SIZE characters per command. I've seen doctoral theses"
    echo "with better brevity. Conciseness is a virtue, verbosity is a vice."
elif [ $AVG_MCP -gt 6 ]; then
    echo "🏆 FINAL SAVAGE JUDGMENT: TOOL ADDICTION DETECTED"
    echo "Average $AVG_MCP MCP tools per command. You're not solving problems,"
    echo "you're creating a dependency nightmare with statistical precision."
else
    echo "🏆 FINAL SAVAGE JUDGMENT: SURPRISINGLY COMPETENT"
    echo "Well, well. Average complexity $AVG_COMPLEXITY, reasonable size, decent tool usage."
    echo "I'm almost disappointed I can't roast this harder. Almost."
fi

echo ""
echo "📄 DEMO COMPLETE - Full statistical analysis available in benchmark framework"
echo "🔬 Run 'node run-savage-benchmark.js' for complete analysis with:"
echo "   - Token consumption measurements"
echo "   - Execution time profiling" 
echo "   - Success rate calculations"
echo "   - Standard deviation analysis"
echo "   - Cost-benefit ratios"
echo "   - Multi-run statistical significance"
echo ""