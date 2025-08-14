<task>
Implement Java code using strict TDD methodology: RED → GREEN → REFACTOR, with all Clean Code and Effective Java principles, enhanced with thinking-first architecture.
</task>

<context>
This command focuses on Test-Driven Development for Java, ensuring tests are written BEFORE implementation.
Follows the complete TDD cycle while maintaining simplicity and clean code standards.

Key thinking layers:
- Pre-TDD understanding and design planning
- Test design reasoning before coding
- Implementation strategy thinking during GREEN phase
- Refactoring decision-making with complexity assessment
- Pattern learning from TDD outcomes
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate TDD task for:
- Number of classes/methods to implement: _____
- Business logic complexity: _____
- Integration points needed: _____
- Test scenario coverage required: _____
- Estimated complexity score: _____

If complexity > 3: 
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Advanced TDD strategy with sequential thinking
If complexity <= 3: 
  USE: Structured TDD thinking blocks below
</complexity_detection>

## Pre-TDD Thinking
<pre_tdd_thinking>
Before starting TDD cycle, I need to understand:
1. What is the REAL problem being solved?
   - Surface request: [requirement]
   - Underlying business need: [infer from context]
   - Edge cases that might emerge: [anticipate]

2. What design approach will be most maintainable?
   - Simple direct implementation?
   - Strategy pattern needed?
   - Composition vs inheritance considerations?
   
3. What are my TDD assumptions?
   - About the expected behavior
   - About the integration points
   - About performance requirements
   
4. What could make this TDD session fail?
   - Unclear requirements
   - Missing test scenarios
   - Over-engineering temptation
</pre_tdd_thinking>

## Test Design Thinking
<test_design_thinking>
Before writing each test:
1. What behavior am I validating?
   - Happy path scenarios
   - Edge cases and boundaries  
   - Error conditions
   
2. What test structure makes this clearest?
   - Given/When/Then appropriateness
   - Parameterized test opportunities
   - Mock vs real object decisions

3. How does this test fit the bigger picture?
   - Does it document the expected behavior clearly?
   - Will it catch regressions effectively?
   - Is it testing the right abstraction level?
</test_design_thinking>
</thinking_orchestration>

<tdd_workflow>
## TDD Process (MANDATORY) - Enhanced with Thinking

### Step 1: RED - Write Failing Test First (Thinking-Driven)
<red_phase_thinking>
Before writing the test, reasoning through:
- What specific behavior needs validation?
- What's the minimal test that proves the concept?
- What edge cases am I anticipating?
- What would make this test most valuable?
</red_phase_thinking>
```java
// Test naming: methodName_condition_expectedResult
@Test
void calculateDiscount_premiumCustomer_appliesTwentyPercent() {
    // Given - Setup test data
    Customer premiumCustomer = Customer.builder()
        .type(CustomerType.PREMIUM)
        .build();
    BigDecimal originalPrice = new BigDecimal("100.00");
    
    // When - Execute the method
    BigDecimal discounted = discountService.calculate(premiumCustomer, originalPrice);
    
    // Then - Assert expectations
    assertThat(discounted).isEqualTo(new BigDecimal("80.00"));
}
```

### Step 2: GREEN - Minimal Code to Pass (Thinking-Guided)
<green_phase_thinking>
Implementation decision-making:
- What's the SIMPLEST code that makes this pass?
- Am I adding unnecessary complexity?
- Does this implementation align with clean code principles?
- What's my complexity score so far?
</green_phase_thinking>
```java
// Write ONLY enough code to make the test pass
public BigDecimal calculate(final Customer customer, final BigDecimal price) {
    if (customer.getType() == CustomerType.PREMIUM) {
        return price.multiply(new BigDecimal("0.80"));
    }
    return price;
}
```

### Step 3: REFACTOR - Improve Design (Thinking-Informed)
<refactor_thinking>
Refactoring decision points:
- Is the current design simple enough?
- Would refactoring actually reduce complexity?
- What's the risk/benefit of this refactoring?
- Does this maintain the green test state?
- Am I solving a real problem or imaginary one?
</refactor_thinking>
```java
// Only if it reduces complexity and maintains simplicity
public BigDecimal calculate(final Customer customer, final BigDecimal price) {
    return price.multiply(customer.getType().getDiscountMultiplier());
}
```
</tdd_workflow>

<test_patterns>
## Test Structure Patterns

### 1. Unit Test Template
```java
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
    
    @Mock
    private OrderRepository repository;
    
    @InjectMocks
    private OrderService orderService;
    
    @Test
    void processOrder_validRequest_returnsOrder() {
        // Given
        OrderRequest request = createValidRequest();
        Order expectedOrder = createExpectedOrder();
        when(repository.save(any())).thenReturn(expectedOrder);
        
        // When
        Order result = orderService.processOrder(request);
        
        // Then
        assertThat(result).isNotNull();
        assertThat(result.getCustomerId()).isEqualTo(request.customerId());
        verify(repository).save(any(Order.class));
    }
}
```

### 2. Edge Cases Testing
```java
@Test
void processPayment_nullPayment_throwsException() {
    assertThatThrownBy(() -> paymentService.process(null))
        .isInstanceOf(IllegalArgumentException.class)
        .hasMessage("Payment cannot be null");
}

@Test
void calculateTotal_emptyCart_returnsZero() {
    assertThat(calculator.calculateTotal(Cart.empty()))
        .isEqualTo(BigDecimal.ZERO);
}
```

### 3. Parameterized Tests
```java
@ParameterizedTest
@ValueSource(strings = {"", " ", "invalid-email", "@example.com"})
void validateEmail_invalidFormats_returnsFalse(String email) {
    assertThat(validator.isValid(email)).isFalse();
}

@ParameterizedTest
@CsvSource({
    "STANDARD, 100.00, 100.00",
    "PREMIUM, 100.00, 80.00",
    "VIP, 100.00, 70.00"
})
void calculateDiscount_differentCustomerTypes_appliesCorrectDiscount(
        CustomerType type, BigDecimal original, BigDecimal expected) {
    Customer customer = Customer.builder().type(type).build();
    assertThat(calculator.calculate(customer, original))
        .isEqualByComparingTo(expected);
}
```
</test_patterns>

<implementation_rules>
## Clean Implementation After Test

### 1. Keep It Simple
```java
// ❌ Over-engineered after test passes
public class ComplexDiscountCalculator implements DiscountStrategy {
    private final Map<CustomerType, DiscountRule> rules;
    // 50 lines of unnecessary abstraction
}

// ✅ Simple and clean
public BigDecimal calculateDiscount(final Customer customer, final BigDecimal price) {
    return price.multiply(customer.getType().getDiscountRate());
}
```

### 2. All Parameters Final
```java
public Order createOrder(
        final String customerId,      // ✅ final
        final List<OrderItem> items,  // ✅ final
        final Address shipping) {     // ✅ final
    // implementation
}
```

### 3. No Null Returns
```java
// ❌ BAD
public Customer findCustomer(String id) {
    return repository.findById(id).orElse(null);
}

// ✅ GOOD
public Optional<Customer> findCustomer(final String id) {
    return repository.findById(id);
}
```
</implementation_rules>

<tdd_checklist>
## TDD Execution Checklist (Thinking-Enhanced)

### Before Writing Code (Pre-Analysis Thinking)
<pre_code_thinking>
- [ ] What's the core behavior I'm testing?
- [ ] Why is this test valuable?
- [ ] What could make this test fail inappropriately?
</pre_code_thinking>
- [ ] Test written first?
- [ ] Test has clear Given/When/Then structure?
- [ ] Test name follows: methodName_condition_expectedResult?
- [ ] Test fails when run (RED)?

### During Implementation (Decision Point Thinking)
<implementation_thinking>
- [ ] Am I writing the MINIMUM code to pass?
- [ ] Is this solution elegant or just working?
- [ ] What assumptions am I making?
</implementation_thinking>
- [ ] Writing minimal code to pass test?
- [ ] Not adding unnecessary features?
- [ ] All parameters are final?
- [ ] Functions < 20 lines?

### After Test Passes (Evaluation Thinking)
<evaluation_thinking>
- [ ] Does this design feel sustainable?
- [ ] What would happen if requirements change?
- [ ] Is the abstraction level appropriate?
</evaluation_thinking>
- [ ] All tests green?
- [ ] Can the code be simplified?
- [ ] Is complexity score < 5?
- [ ] Need to refactor?

### Test Coverage (Completeness Thinking)
<coverage_thinking>
- [ ] What scenarios am I NOT testing?
- [ ] Where could this break in production?
- [ ] What edge cases am I overlooking?
</coverage_thinking>
- [ ] Happy path tested?
- [ ] Edge cases tested?
- [ ] Error conditions tested?
- [ ] Boundary conditions tested?
</tdd_checklist>

<common_test_scenarios>
## Common Test Scenarios

### 1. Service Layer
```java
@Test
void saveOrder_validOrder_persistsAndReturnsWithId() {
    // Given
    Order order = Order.builder()
        .customerId("CUST-123")
        .items(List.of(new OrderItem("PROD-1", 2)))
        .build();
    
    // When
    Order saved = orderService.save(order);
    
    // Then
    assertThat(saved.getId()).isNotNull();
    assertThat(saved.getStatus()).isEqualTo(OrderStatus.PENDING);
}
```

### 2. REST Controller
```java
@Test
void createOrder_validRequest_returns201() throws Exception {
    // Given
    String requestJson = """
        {
            "customerId": "CUST-123",
            "items": [{"productId": "PROD-1", "quantity": 2}]
        }
        """;
    
    // When & Then
    mockMvc.perform(post("/api/orders")
            .contentType(MediaType.APPLICATION_JSON)
            .content(requestJson))
        .andExpect(status().isCreated())
        .andExpect(jsonPath("$.orderId").exists());
}
```

### 3. Repository Layer
```java
@DataJpaTest
class OrderRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private OrderRepository repository;
    
    @Test
    void findByCustomerId_existingCustomer_returnsOrders() {
        // Given
        Order order = createTestOrder("CUST-123");
        entityManager.persistAndFlush(order);
        
        // When
        List<Order> orders = repository.findByCustomerId("CUST-123");
        
        // Then
        assertThat(orders).hasSize(1);
        assertThat(orders.get(0).getCustomerId()).isEqualTo("CUST-123");
    }
}
```
</common_test_scenarios>

<output_format>
When implementing with TDD, I will:

1. **RED Phase**
   - Write failing test with clear name
   - Show test failure message
   - Explain what the test validates

2. **GREEN Phase**
   - Write minimal code to pass
   - Run test to show it passes
   - No extra features

3. **REFACTOR Phase**
   - Only if complexity can be reduced
   - Maintain all tests passing
   - Keep simplicity score < 5

4. **Final Validation**
   - All tests green
   - Code is clean and simple
   - Coverage includes edge cases
</output_format>

<error_recovery>
## TDD Error Recovery Thinking
<error_thinking>
When TDD gets stuck or fails:
1. Test won't fail initially:
   - Thinking: Why isn't this failing? Am I testing the right thing?
   - Recovery: Verify test is actually running, check assertions

2. Implementation gets complex:
   - Thinking: Am I solving the right problem? Can I simplify?
   - Recovery: Step back, write simpler test, minimal implementation

3. Refactoring breaks tests:
   - Thinking: What assumption did I violate? Is this refactoring necessary?
   - Recovery: Revert, analyze test failures, refactor in smaller steps

4. Tests become hard to maintain:
   - Thinking: Are my tests too coupled to implementation details?
   - Recovery: Focus on behavior testing, reduce mock usage
</error_thinking>
</error_recovery>

<pattern_learning>
## TDD Pattern Learning Mechanisms
<learning_thinking>
After each TDD session, reflect on:
1. What design patterns emerged naturally?
2. Which test structures were most effective?
3. What refactoring opportunities were missed?
4. How can I improve the next TDD cycle?
</learning_thinking>

### Successful Pattern Recognition
- Test structures that led to clean design
- Implementation approaches that stayed simple
- Refactoring decisions that improved maintainability

### Anti-Pattern Detection
- Tests that became brittle
- Implementations that grew complex
- Refactorings that added unnecessary abstraction

### Next Session Improvements
- Test design strategies to try
- Implementation patterns to avoid
- Refactoring checkpoints to establish
</pattern_learning>

<reminder>
## CRITICAL: Never Skip TDD Steps! (Thinking-Reinforced)

<tdd_discipline_thinking>
Why these rules exist:
1. **ALWAYS write test first** - Forces thinking about behavior before implementation
2. **Test MUST fail initially** - Proves test is actually validating something
3. **Minimal code to pass** - Prevents over-engineering and gold plating
4. **Refactor with green tests** - Provides safety net for design improvements
5. **Keep tests simple** - Tests document expected behavior clearly
</tdd_discipline_thinking>

**"TDD is not about testing, it's about design and confidence"**
</reminder>