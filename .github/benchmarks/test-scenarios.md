# Command Testing Scenarios

## Test Scenarios for Scientific Benchmarking

### senior-developer-analysis.md
1. **Simple File Test**: Analyze a single 50-line JavaScript file
2. **Complex System Test**: Analyze multiple interconnected files
3. **Legacy Code Test**: Analyze poorly written legacy code
4. **Empty Input Test**: Run with no arguments 
5. **Invalid Path Test**: Run with non-existent file path

### safe-code-beautifier.md  
1. **Simple Beautification**: Beautify well-written code
2. **Ugly Code Test**: Beautify poorly formatted, complex code
3. **No Changes Needed**: Run on already beautiful code
4. **Dangerous Code**: Run on code that could break with changes
5. **Empty Input Test**: Run with no arguments

### adhd-evening-reflect.md
1. **Complete Reflection**: Full evening reflection with all prompts
2. **Partial Data**: Run with some missing daily data
3. **No Memory**: Run without basic memory integration
4. **Invalid Date**: Run with malformed dates
5. **Empty Response**: Run and provide minimal responses

### ultrathink.md
1. **Simple Problem**: Basic technical question
2. **Complex Problem**: Multi-layered architectural decision
3. **Abstract Problem**: Philosophical or creative challenge
4. **No Problem**: Empty or vague input
5. **Recursive Thinking**: Problem that references itself

## Success Criteria
- **Time to Complete**: < 30 seconds for simple tasks
- **Token Efficiency**: < 2000 tokens for standard operations
- **Success Rate**: > 80% successful executions
- **User Confusion**: < 20% users need clarification
- **Behavior Change**: 0% for beautifier (safety requirement)