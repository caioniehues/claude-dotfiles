# Test Scenarios for Command Benchmarking

## Baseline Tests (All Commands)
1. **Simple Task**: "What is 2+2?"
2. **Medium Task**: "Explain how to optimize a database query"
3. **Complex Task**: "Design a microservices architecture for an e-commerce platform"
4. **Edge Case**: "Handle this broken JSON: {invalid: syntax}"
5. **Composition Test**: Chain with other commands

## Expected Baselines
- Simple Task: 50-100 tokens, 2-5 seconds, 100% success
- Medium Task: 200-500 tokens, 5-15 seconds, 90%+ success
- Complex Task: 500-2000 tokens, 15-60 seconds, 80%+ success

## Metrics Tracked
- Input tokens
- Output tokens
- Execution time
- Success rate (5 runs each)
- Error types and frequency
- Complexity score delivered vs promised
- User satisfaction proxy (clarity, usefulness)