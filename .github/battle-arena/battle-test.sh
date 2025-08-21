#!/bin/bash

# ⚔️ BATTLE ARENA TEST HARNESS
# Testing: ultrathink vs ultrathink-pure-xml

echo "⚔️ INITIALIZING BATTLE ARENA ⚔️"
echo "================================"
echo "Red Corner: ultrathink (MCP-integrated deep thinking)"
echo "Blue Corner: ultrathink-pure-xml (Pure XML, zero dependencies)"
echo ""

# Test Case: Complex database query optimization
TEST_CASE="analyze and optimize a complex database query for high-concurrency writes with multiple JOIN operations"

echo "📊 TEST CASE: $TEST_CASE"
echo ""

# Create results directory
mkdir -p .github/battle-arena/results

# Round 1: Speed Test
echo "🏃 ROUND 1: SPEED TEST"
echo "----------------------"

# Warm-up run
echo "Warming up..."
claude --no-style "test warmup" > /dev/null 2>&1

# Test ultrathink speed (5 runs)
echo "Testing ultrathink..."
ULTRA_TIMES=()
for i in {1..5}; do
    START=$(date +%s%N)
    timeout 30 claude --no-style "/user:ultrathink \"$TEST_CASE\"" > /tmp/ultra_output_$i.txt 2>&1
    END=$(date +%s%N)
    ELAPSED=$((($END - $START) / 1000000))
    ULTRA_TIMES+=($ELAPSED)
    echo "  Run $i: ${ELAPSED}ms"
    sleep 2
done

echo ""
echo "Testing ultrathink-pure-xml..."
XML_TIMES=()
for i in {1..5}; do
    START=$(date +%s%N)
    timeout 30 claude --no-style "/user:ultrathink-pure-xml \"$TEST_CASE\"" > /tmp/xml_output_$i.txt 2>&1
    END=$(date +%s%N)
    ELAPSED=$((($END - $START) / 1000000))
    XML_TIMES+=($ELAPSED)
    echo "  Run $i: ${ELAPSED}ms"
    sleep 2
done

# Calculate statistics
calculate_stats() {
    local -n arr=$1
    local sum=0
    local n=${#arr[@]}
    
    for val in "${arr[@]}"; do
        sum=$((sum + val))
    done
    
    local mean=$((sum / n))
    
    # Sort for median
    IFS=$'\n' sorted=($(sort -n <<<"${arr[*]}"))
    unset IFS
    local median=${sorted[2]}
    
    # Calculate std dev
    local variance=0
    for val in "${arr[@]}"; do
        local diff=$((val - mean))
        variance=$((variance + diff * diff))
    done
    variance=$((variance / n))
    local std_dev=$(echo "scale=2; sqrt($variance)" | bc 2>/dev/null || echo "N/A")
    
    echo "$mean $median $std_dev"
}

echo ""
echo "📊 Speed Statistics:"
read ultra_mean ultra_median ultra_std <<< $(calculate_stats ULTRA_TIMES)
read xml_mean xml_median xml_std <<< $(calculate_stats XML_TIMES)

echo "ultrathink: Mean=${ultra_mean}ms, Median=${ultra_median}ms, StdDev=${ultra_std}"
echo "ultrathink-pure-xml: Mean=${xml_mean}ms, Median=${xml_median}ms, StdDev=${xml_std}"

# Determine speed winner
if [ $xml_mean -lt $ultra_mean ]; then
    SPEED_WINNER="ultrathink-pure-xml"
    SPEED_LOSER="ultrathink"
    SPEED_DIFF=$(( (ultra_mean - xml_mean) * 100 / ultra_mean ))
    echo "🏆 WINNER: ultrathink-pure-xml (${SPEED_DIFF}% faster)"
else
    SPEED_WINNER="ultrathink"
    SPEED_LOSER="ultrathink-pure-xml"
    SPEED_DIFF=$(( (xml_mean - ultra_mean) * 100 / xml_mean ))
    echo "🏆 WINNER: ultrathink (${SPEED_DIFF}% faster)"
fi

echo ""
echo "🎯 ROUND 2: ACCURACY TEST"
echo "-------------------------"

# Check output quality
echo "Analyzing output quality..."

# Count key analysis elements
check_accuracy() {
    local file=$1
    local score=0
    
    # Check for key database optimization concepts
    grep -qi "index" "$file" && score=$((score + 10))
    grep -qi "partition" "$file" && score=$((score + 10))
    grep -qi "denormali" "$file" && score=$((score + 10))
    grep -qi "cache" "$file" && score=$((score + 10))
    grep -qi "lock" "$file" && score=$((score + 10))
    grep -qi "concurrency" "$file" && score=$((score + 10))
    grep -qi "write.*amplification\|amplification.*write" "$file" && score=$((score + 10))
    grep -qi "batch" "$file" && score=$((score + 10))
    grep -qi "async\|queue" "$file" && score=$((score + 10))
    grep -qi "monitor\|metric\|observ" "$file" && score=$((score + 10))
    
    echo $score
}

ULTRA_ACCURACY=$(check_accuracy /tmp/ultra_output_1.txt)
XML_ACCURACY=$(check_accuracy /tmp/xml_output_1.txt)

echo "ultrathink accuracy score: $ULTRA_ACCURACY/100"
echo "ultrathink-pure-xml accuracy score: $XML_ACCURACY/100"

if [ $ULTRA_ACCURACY -gt $XML_ACCURACY ]; then
    ACC_WINNER="ultrathink"
    ACC_LOSER="ultrathink-pure-xml"
    echo "🏆 WINNER: ultrathink (more comprehensive)"
elif [ $XML_ACCURACY -gt $ULTRA_ACCURACY ]; then
    ACC_WINNER="ultrathink-pure-xml"
    ACC_LOSER="ultrathink"
    echo "🏆 WINNER: ultrathink-pure-xml (more comprehensive)"
else
    ACC_WINNER="TIE"
    ACC_LOSER="TIE"
    echo "⚖️ TIE: Both equally accurate"
fi

echo ""
echo "💰 ROUND 3: EFFICIENCY TEST"
echo "---------------------------"

# Count tokens (approximate by character count)
ULTRA_CHARS=$(wc -c < /tmp/ultra_output_1.txt)
XML_CHARS=$(wc -c < /tmp/xml_output_1.txt)

# Approximate tokens (1 token ≈ 4 chars)
ULTRA_TOKENS=$((ULTRA_CHARS / 4))
XML_TOKENS=$((XML_CHARS / 4))

# Calculate efficiency (accuracy per token)
if [ $ULTRA_TOKENS -gt 0 ]; then
    ULTRA_EFFICIENCY=$((ULTRA_ACCURACY * 1000 / ULTRA_TOKENS))
else
    ULTRA_EFFICIENCY=0
fi

if [ $XML_TOKENS -gt 0 ]; then
    XML_EFFICIENCY=$((XML_ACCURACY * 1000 / XML_TOKENS))
else
    XML_EFFICIENCY=0
fi

echo "ultrathink: ~${ULTRA_TOKENS} tokens, efficiency=${ULTRA_EFFICIENCY}"
echo "ultrathink-pure-xml: ~${XML_TOKENS} tokens, efficiency=${XML_EFFICIENCY}"

if [ $ULTRA_EFFICIENCY -gt $XML_EFFICIENCY ]; then
    EFF_WINNER="ultrathink"
    EFF_LOSER="ultrathink-pure-xml"
    echo "🏆 WINNER: ultrathink (better value per token)"
else
    EFF_WINNER="ultrathink-pure-xml"
    EFF_LOSER="ultrathink"
    echo "🏆 WINNER: ultrathink-pure-xml (better value per token)"
fi

echo ""
echo "⚔️ FINAL DEATH MATCH"
echo "--------------------"

# Composite scoring
ULTRA_SCORE=0
XML_SCORE=0

# Speed (30%)
if [ "$SPEED_WINNER" = "ultrathink" ]; then
    ULTRA_SCORE=$((ULTRA_SCORE + 30))
else
    XML_SCORE=$((XML_SCORE + 30))
fi

# Accuracy (30%)
if [ "$ACC_WINNER" = "ultrathink" ]; then
    ULTRA_SCORE=$((ULTRA_SCORE + 30))
elif [ "$ACC_WINNER" = "ultrathink-pure-xml" ]; then
    XML_SCORE=$((XML_SCORE + 30))
else
    ULTRA_SCORE=$((ULTRA_SCORE + 15))
    XML_SCORE=$((XML_SCORE + 15))
fi

# Efficiency (30%)
if [ "$EFF_WINNER" = "ultrathink" ]; then
    ULTRA_SCORE=$((ULTRA_SCORE + 30))
else
    XML_SCORE=$((XML_SCORE + 30))
fi

# Complexity penalty (10%) - XML wins for being simpler
XML_SCORE=$((XML_SCORE + 10))

echo "ultrathink composite score: $ULTRA_SCORE/100"
echo "ultrathink-pure-xml composite score: $XML_SCORE/100"
echo ""

if [ $ULTRA_SCORE -gt $XML_SCORE ]; then
    echo "💀 FINAL WINNER: ultrathink"
    echo "☠️ EXECUTED: ultrathink-pure-xml"
    FINAL_WINNER="ultrathink"
    FINAL_LOSER="ultrathink-pure-xml"
else
    echo "💀 FINAL WINNER: ultrathink-pure-xml"
    echo "☠️ EXECUTED: ultrathink"
    FINAL_WINNER="ultrathink-pure-xml"
    FINAL_LOSER="ultrathink"
fi

echo ""
echo "Creating battle report..."

# Clean up temp files
rm -f /tmp/ultra_output_*.txt /tmp/xml_output_*.txt