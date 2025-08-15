# SAVAGE BENCHMARKING SUITE

## Test Scenarios

### 1. ultrathink.md
**Complexity Score**: 5 (High)
**Test Cases**:
- Simple question: "What is 2+2?" (Expected: overkill)
- Moderate complexity: "How to optimize database queries?"
- Complex problem: "Design a distributed caching system"

### 2. java-rapid-implementation.md  
**Complexity Score**: 4 (Moderate-High)
**Test Cases**:
- Simple method: "Create a sum function"
- Moderate class: "Create an Order class with validation"
- Complex pattern: "Implement observer pattern"

### 3. adhd-morning-assistant.md
**Complexity Score**: 3 (Moderate)
**Test Cases**:
- No memory patterns: "Plan my morning"
- With patterns: "Plan my morning" (after seeding data)
- Integration test: Full memory integration

### 4. git-backup-sync.md
**Complexity Score**: 4 (Moderate-High)
**Test Cases**:
- Clean repo: Simple sync
- Dirty repo: Uncommitted changes
- Conflict scenario: Simulated merge conflicts

### 5. reasoning-wrapper.md
**Complexity Score**: 3 (Moderate)
**Test Cases**:
- Simple command wrap: "ls"
- Complex command wrap: Another command
- Code snippet wrap: JavaScript function

## Measurement Framework

### Token Metrics
- Input tokens consumed
- Output tokens generated
- Total conversation cost
- Efficiency ratio (output value/token cost)

### Performance Metrics
- Execution time (start to completion)
- Response latency
- Number of tool calls
- Memory operations

### Quality Metrics
- Task completion success (binary)
- Output relevance (1-5 scale)
- Adherence to command purpose (1-5 scale)
- Complexity appropriateness (1-5 scale)

### Error Metrics
- Failure rate
- Error types
- Recovery success
- Graceful degradation

## Statistical Requirements
- 3 runs minimum per test case
- Standard deviation calculation
- Confidence intervals
- Outlier identification