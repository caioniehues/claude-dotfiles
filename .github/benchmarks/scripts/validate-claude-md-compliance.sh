#!/bin/bash

# CLAUDE.md COMPLIANCE VALIDATOR
# Automatically checks commands against CLAUDE.md complexity rules
# Returns exit code 1 if any command violates the rules

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
COMMANDS_DIR="$REPO_ROOT/commands"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

violations=0
total_commands=0

echo "🔍 CLAUDE.md Compliance Validator"
echo "=================================="
echo ""

# Function to check complexity score against CLAUDE.md rules
check_command_compliance() {
    local file="$1"
    local cmd_name=$(basename "$file" .md)
    
    # Calculate complexity score based on CLAUDE.md rules:
    # - Direct solution: 1 point
    # - Each new class: +2 points
    # - Each interface: +1 point  
    # - Each design pattern: +3 points
    # - Each configuration file: +2 points
    
    local score=1  # Base score
    
    # Count classes
    local classes=$(grep -c "^class \|^public class \|new.*Class\|Class.*{" "$file" 2>/dev/null || echo 0)
    score=$((score + classes * 2))
    
    # Count interfaces  
    local interfaces=$(grep -c "^interface \|implements\|extends.*Interface" "$file" 2>/dev/null || echo 0)
    score=$((score + interfaces))
    
    # Count design patterns
    local patterns=0
    patterns=$((patterns + $(grep -c -i "factory\|builder\|strategy\|observer\|singleton\|adapter\|decorator\|facade" "$file" 2>/dev/null || echo 0)))
    score=$((score + patterns * 3))
    
    # Count configuration complexity
    local configs=$(grep -c -i "config\|\.json\|\.yml\|\.yaml\|settings\|properties" "$file" 2>/dev/null || echo 0)
    score=$((score + configs * 2))
    
    # Command-specific complexity indicators
    local orchestration=$(grep -c "orchestration\|mcp__.*mcp\|sequential.*thinking" "$file" 2>/dev/null || echo 0)
    score=$((score + orchestration))
    
    local thinking_complexity=$(grep -c "<.*thinking.*>\|thinking.*phase\|meta.*thinking" "$file" 2>/dev/null || echo 0)
    score=$((score + thinking_complexity / 3))  # Every 3 thinking blocks = +1
    
    local abstraction_layers=$(grep -c "layer\|abstract\|meta.*\|wrapper\|proxy" "$file" 2>/dev/null || echo 0)
    score=$((score + abstraction_layers / 2))  # Every 2 abstractions = +1
    
    total_commands=$((total_commands + 1))
    
    # Check against CLAUDE.md threshold (< 5)
    if [ "$score" -ge 5 ]; then
        echo -e "${RED}❌ VIOLATION: $cmd_name${NC}"
        echo "   Complexity Score: $score/5 (threshold: < 5)"
        echo "   Classes found: $classes (+$((classes * 2)) points)"
        echo "   Interfaces found: $interfaces (+$interfaces points)"
        echo "   Design patterns: $patterns (+$((patterns * 3)) points)"
        echo "   Config complexity: $configs (+$((configs * 2)) points)"
        echo "   Command complexity: +$((score - 1 - classes * 2 - interfaces - patterns * 3 - configs * 2)) points"
        echo ""
        violations=$((violations + 1))
        return 1
    else
        echo -e "${GREEN}✅ COMPLIANT: $cmd_name${NC} (score: $score/5)"
        return 0
    fi
}

# Check all .md files in commands directory
echo "Checking commands in: $COMMANDS_DIR"
echo ""

for cmd_file in "$COMMANDS_DIR"/*.md; do
    if [ -f "$cmd_file" ]; then
        check_command_compliance "$cmd_file"
    fi
done

echo ""
echo "=================================="
echo "📊 COMPLIANCE SUMMARY"
echo "=================================="
echo "Total commands checked: $total_commands"
echo "Compliant commands: $((total_commands - violations))"
echo "Violations found: $violations"

if [ "$violations" -eq 0 ]; then
    echo -e "${GREEN}🎉 ALL COMMANDS COMPLIANT with CLAUDE.md rules!${NC}"
    echo ""
    echo "Your commands respect the complexity threshold."
    echo "Keep it simple, keep it working!"
    exit 0
else
    compliance_rate=$(( (total_commands - violations) * 100 / total_commands ))
    echo -e "${RED}⚠️  COMPLIANCE RATE: ${compliance_rate}%${NC}"
    echo ""
    echo -e "${YELLOW}RECOMMENDATION:${NC}"
    echo "- Refactor violating commands to reduce complexity"
    echo "- Apply the 3-Question Rule from CLAUDE.md:"
    echo "  1. Can I use what already exists?"
    echo "  2. Can I solve this with a simple method?"
    echo "  3. Do I really need this abstraction NOW?"
    echo ""
    echo -e "${RED}Violations must be fixed before deployment!${NC}"
    exit 1
fi