<task>
Implement the Java code task requested by the user, strictly following the Clean Code, Effective Java, and Simplicity principles defined in the documentation, while maintaining ultra-high code quality standards through thinking-first architecture.
</task>

<context>
This command is a comprehensive Java implementation assistant that rigorously applies:
- Clean Code principles (meaningful names, small functions, single responsibility)
- Effective Java patterns (static factories, builders, composition, immutability)
- Simplicity-first approach (3-question rule, complexity score < 5)
- Modern Java features (records, pattern matching, text blocks)
- TDD methodology (Red → Green → Refactor)
- Thinking-first architecture with decision reasoning
- Automatic complexity detection and MCP integration

Every line of code must pass the simplicity checklist and follow the established standards with documented reasoning.
</context>

<thinking_orchestration>
## Automatic Complexity Assessment
<complexity_detection>
Evaluate implementation request "$ARGUMENTS":
- Classes to create: _____
- Interfaces needed: _____
- Design patterns required: _____
- Framework integrations: _____
- Configuration files: _____
- Estimated complexity score: _____

Complexity Scoring:
- Direct solution: 1 point
- Each new class: +2 points
- Each interface: +1 point
- Each design pattern: +3 points
- Each configuration file: +2 points

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  INJECT: Java implementation strategy below
If complexity <= 3:
  USE: Structured thinking blocks below
</complexity_detection>

## Pre-Implementation Strategic Thinking
<strategic_thinking>
Before writing any code, I must deeply understand:

1. What's the REAL problem to solve?
   - Surface request: "$ARGUMENTS"
   - Underlying business need: [analyze deeper]
   - Future extensibility requirements: [predict]

2. What existing solutions can I leverage?
   - Spring Boot features: [identify applicable]
   - Java standard library: [check for built-ins]
   - Project existing code: [scan for reusable patterns]

3. What's the simplest approach that could work?
   - Direct implementation: [evaluate feasibility]
   - Composition over inheritance: [check opportunities]
   - Avoiding abstractions: [validate necessity]

4. What could go wrong with this implementation?
   - Performance implications: [assess]
   - Maintainability risks: [evaluate]
   - Testing challenges: [identify]
   - Integration issues: [predict]

Decision: [Selected approach] because [detailed reasoning]
</strategic_thinking>

## Simplicity Validation Thinking
<simplicity_thinking>
Applying the 3-Question Rule with reasoning:

1. **Can I use what already exists?**
   <thinking>
   Checking existing solutions:
   - Spring Boot: [applicable features found]
   - Java stdlib: [relevant utilities identified]
   - Project code: [reusable components located]
   Decision: [use existing / create new] because [justification]
   </thinking>

2. **Can I solve this with a simple method?**
   <thinking>
   Evaluating implementation complexity:
   - Direct method approach: [feasibility assessment]
   - Pattern necessity: [validation of need]
   - Abstraction value: [cost-benefit analysis]
   Decision: [simple method / complex solution] because [reasoning]
   </thinking>

3. **Do I really need this abstraction NOW?**
   <thinking>
   Abstraction necessity check:
   - Current implementations: [count actual, not theoretical]
   - Future predictability: [realistic assessment]
   - YAGNI principle: [apply strictly]
   Decision: [abstract / concrete] because [evidence-based reasoning]
   </thinking>

Complexity Score Calculation:
- Base solution: [points]
- Additional complexity: [breakdown]
- Total score: [sum] (Target: < 5)

If score ≥ 5: STOP and simplify approach!
</simplicity_thinking>
</thinking_orchestration>

<simplicity_check>
## Before Writing ANY Code, I Must Verify:

### The 3-Question Rule
1. **Can I use what already exists?** → Check Spring Boot, Java built-ins, existing project code
2. **Can I solve this with a simple method?** → Try direct implementation first
3. **Do I really need this abstraction NOW?** → Only if 3+ concrete implementations exist

### Complexity Score (MUST be < 5)
- Direct solution: 1 point
- Each new class: +2 points
- Each interface: +1 point
- Each design pattern: +3 points
- Each configuration file: +2 points

**If score ≥ 5, I must simplify!**
</simplicity_check>

<implementation_rules>
## Non-Negotiable Standards

### 1. Naming (Clean & Searchable)
```java
// ❌ NEVER
String d; // elapsed time
List<String> l;
Map<String, List<String>> grps;

// ✅ ALWAYS
String elapsedTimeInDays;
List<String> locations;
Map<String, List<String>> anagramGroups;
```

### 2. Function Rules
- **< 20 lines** (no exceptions)
- **Do ONE thing only**
- **All parameters MUST be final**
- **Max 3 parameters** (use objects for more)

### 3. Import Rules
```java
import com.richemont.ce.domain.*;     // ❌ NEVER!
import com.richemont.ce.domain.Order;  // ✅ ALWAYS!
```

### 4. Error Handling
```java
// ❌ NEVER hide failures
try {
    return repository.findById(id);
} catch (Exception e) {
    return null; // NO!
}

// ✅ Let it fail clearly
return repository.findById(id)
    .orElseThrow(() -> new NotFoundException(id));
```

### 5. Modern Java (21+) Usage
- Records for DTOs
- Pattern matching for clean switches
- Text blocks for multi-line strings
- Optional instead of null
- Stream API for collections
</implementation_rules>

<effective_java_patterns>
## Mandatory Patterns

### 1. Static Factory Methods Over Constructors
```java
// ❌ BAD
public User(String email) { }
public User(String email, String name) { }

// ✅ GOOD
public static User withEmail(String email) { }
public static User withEmailAndName(String email, String name) { }
```

### 2. Builder for Complex Objects (4+ parameters)
```java
@Builder(toBuilder = true)
public class OrderRequest {
    private final String customerId;
    private final List<OrderItem> items;
    @Builder.Default
    private final ShippingMethod shipping = ShippingMethod.STANDARD;
}
```

### 3. Favor Composition Over Inheritance
```java
// ❌ BAD - Deep hierarchy
class Manager extends Employee { }

// ✅ GOOD - Composition
@Value
public class Employee {
    Person personalInfo;
    Role role;
}
```

### 4. Enums Instead of Constants
```java
// ❌ BAD
public static final int STATUS_PENDING = 0;

// ✅ GOOD
public enum OrderStatus {
    PENDING("Awaiting approval") {
        @Override
        public boolean canTransitionTo(OrderStatus status) {
            return status == APPROVED || status == REJECTED;
        }
    }
}
```
</effective_java_patterns>

<tdd_process>
## TDD Workflow (MANDATORY with Thinking)

### 1. RED - Write Failing Test First (with Pre-Test Thinking)
<test_thinking>
Before writing the test, I need to think:
- What behavior am I testing? [specific functionality]
- What are the edge cases? [boundary conditions]
- What's the expected interface? [method signature]
- How will this fail initially? [failure mode]

Test design decision: [chosen approach] because [reasoning]
</test_thinking>

```java
@Test
void calculateTotal_emptyCart_returnsZero() {
    // Thinking: Testing the simplest case first - empty cart should return zero
    // This establishes the baseline behavior before adding complexity
    
    // Given
    Cart emptyCart = Cart.empty();
    
    // When
    BigDecimal total = calculator.calculateTotal(emptyCart);
    
    // Then
    assertThat(total).isEqualTo(BigDecimal.ZERO);
}
```

### 2. GREEN - Minimal Implementation (with Implementation Thinking)
<implementation_thinking>
For the minimal implementation:
- What's the absolute simplest code that passes? [identify minimal logic]
- Am I avoiding premature optimization? [check for over-engineering]
- Does this maintain the simplicity principle? [validate approach]

Implementation choice: [selected approach] because [justification]
</implementation_thinking>

```java
public BigDecimal calculateTotal(final Cart cart) {
    // Thinking: Most direct implementation - guard clause for empty, otherwise delegate
    // Avoids complex conditional logic while satisfying the test
    return cart.isEmpty() ? BigDecimal.ZERO : cart.getTotal();
}
```

### 3. REFACTOR - Improve Design (with Refactoring Thinking)
<refactoring_thinking>
Refactoring decision points:
- Does current code violate any clean code principles? [assess violations]
- Can I reduce complexity without adding abstraction? [simplification opportunities]
- Are there code smells that need addressing? [identify issues]
- Will refactoring maintain or improve simplicity? [validate benefit]

Refactoring decision: [refactor / keep as-is] because [evidence-based reasoning]
</refactoring_thinking>

Only refactor if complexity can be reduced while maintaining simplicity
</tdd_process>

<implementation_workflow>
## Step-by-Step Process (Thinking-Enhanced)

### Phase 1: Analysis (Strategic Thinking)
<analysis_thinking>
1. **Understand the requirement**
   <thinking>
   Deep requirement analysis:
   - What does the user really need? [core functionality]
   - What are the implicit requirements? [unstated expectations]
   - How will this be used? [usage patterns]
   Decision: [requirement interpretation] based on [evidence]
   </thinking>

2. **Check existing solutions**
   <thinking>
   Solution landscape scan:
   - Spring Boot: [relevant features discovered]
   - Java standard library: [applicable utilities found]
   - Project code: [reusable components identified]
   Decision: [use existing / build new] because [cost-benefit analysis]
   </thinking>

3. **Calculate complexity score**
   <thinking>
   Complexity assessment:
   - Direct solution: [points]
   - Required additions: [breakdown with justification]
   - Total score: [sum]
   Decision: [proceed / simplify] based on score [value] vs threshold [5]
   </thinking>

4. **Choose simplest approach**
   <thinking>
   Approach selection:
   - Option A: [direct approach] - pros: [benefits] cons: [drawbacks]
   - Option B: [alternative approach] - pros: [benefits] cons: [drawbacks]
   Selected: [chosen approach] because [detailed reasoning]
   </thinking>
</analysis_thinking>

### Phase 2: Test First (TDD with Decision Thinking)
<tdd_thinking>
1. **Write test with descriptive name**
   <thinking>
   Test naming strategy:
   - Method under test: [method name]
   - Condition being tested: [specific scenario]
   - Expected result: [outcome]
   Name: [methodName_condition_expectedResult] captures [what it validates]
   </thinking>

2. **Ensure test fails (RED)**
   <thinking>
   Failure validation:
   - Does test fail for the right reason? [verify failure mode]
   - Is the error message clear? [check diagnostic quality]
   RED confirmed: [test fails as expected] because [reason]
   </thinking>

3. **Write minimal code to pass (GREEN)**
   <thinking>
   Minimal implementation strategy:
   - What's the simplest code that passes? [identify minimal logic]
   - Am I adding unnecessary complexity? [check for over-engineering]
   GREEN approach: [implementation strategy] chosen for [simplicity reason]
   </thinking>

4. **Refactor only if needed (REFACTOR)**
   <thinking>
   Refactoring necessity:
   - Are there code smells? [identify issues]
   - Can I reduce complexity? [improvement opportunities]
   - Will refactoring add value? [benefit assessment]
   REFACTOR decision: [yes/no] because [evidence-based reasoning]
   </thinking>
</tdd_thinking>

### Phase 3: Implementation (Pattern Decision Thinking)
<implementation_thinking>
1. **Start with direct, simple solution**
   <thinking>
   Implementation approach:
   - Direct implementation feasibility: [assessment]
   - Pattern necessity validation: [check if patterns add value]
   Chosen: [direct/pattern-based] because [simplicity justification]
   </thinking>

2. **Use modern Java features**
   <thinking>
   Modern Java feature selection:
   - Records appropriate? [for data classes]
   - Pattern matching beneficial? [for conditional logic]
   - Text blocks needed? [for multi-line strings]
   Features used: [list] for reasons: [specific benefits]
   </thinking>

3. **Apply code quality rules**
   <thinking>
   Quality enforcement reasoning:
   - Functions < 20 lines: [checking each method]
   - Parameters final: [enforcing immutability]
   - No wildcard imports: [maintaining explicit dependencies]
   - Optional for nulls: [avoiding null references]
   Each rule applied because: [specific benefit to code quality]
   </thinking>
</implementation_thinking>

### Phase 4: Validation (Quality Reasoning)
<validation_thinking>
Quality checkpoint reasoning:
- [ ] **Can I explain this in ONE sentence?** 
     <thinking>Explanation: [one sentence summary] - validates: [simplicity achievement]</thinking>
- [ ] **Would a junior understand immediately?** 
     <thinking>Junior perspective: [readability assessment] - indicates: [code clarity level]</thinking>
- [ ] **Am I solving a REAL problem?** 
     <thinking>Problem validation: [actual vs imaginary problem] - confirms: [necessity]</thinking>
- [ ] **Have I avoided unnecessary abstractions?** 
     <thinking>Abstraction check: [abstractions used] - justified by: [concrete need]</thinking>
- [ ] **Is complexity score < 5?** 
     <thinking>Score calculation: [final score] - meets threshold: [yes/no]</thinking>
- [ ] **Are all functions < 20 lines?** 
     <thinking>Line count check: [method sizes] - ensures: [single responsibility]</thinking>
- [ ] **Are all parameters final?** 
     <thinking>Immutability check: [parameter review] - provides: [safety guarantee]</thinking>
- [ ] **No wildcard imports?** 
     <thinking>Import review: [import analysis] - maintains: [explicit dependencies]</thinking>
- [ ] **No null returns?** 
     <thinking>Return type review: [null safety analysis] - ensures: [robust API]</thinking>
</validation_thinking>
</implementation_workflow>

<code_templates>
## Standard Templates

### Simple Service
```java
@Service
@RequiredArgsConstructor
@Slf4j
public class OrderService {
    private final OrderRepository repository;
    
    public Order processOrder(final OrderRequest request) {
        final Order order = createOrder(request);
        saveOrder(order);
        return order;
    }
    
    private Order createOrder(final OrderRequest request) {
        return Order.builder()
            .customerId(request.customerId())
            .items(request.items())
            .build();
    }
    
    private void saveOrder(final Order order) {
        repository.save(order);
        log.info("Order saved: {}", order.getId());
    }
}
```

### DTO with Record
```java
public record OrderDto(
    String orderId,
    String customerId,
    List<OrderItemDto> items,
    BigDecimal total
) {
    public OrderDto {
        Objects.requireNonNull(orderId);
        Objects.requireNonNull(customerId);
        items = List.copyOf(items);
    }
}
```

### Clean REST Controller
```java
@RestController
@RequestMapping("/api/orders")
@RequiredArgsConstructor
@Validated
public class OrderController {
    private final OrderService orderService;
    
    @PostMapping
    public ResponseEntity<OrderDto> createOrder(
            @Valid @RequestBody final OrderRequest request) {
        final Order order = orderService.processOrder(request);
        return ResponseEntity.ok(toDto(order));
    }
    
    private OrderDto toDto(final Order order) {
        return new OrderDto(
            order.getId(),
            order.getCustomerId(),
            order.getItems(),
            order.getTotal()
        );
    }
}
```

### Pattern Matching
```java
public String processPayment(final Payment payment) {
    return switch (payment.getType()) {
        case CREDIT_CARD -> processCreditCard(payment);
        case PAYPAL -> processPayPal(payment);
        case BANK_TRANSFER -> processBankTransfer(payment);
    };
}
```
</code_templates>

<anti_patterns_to_avoid>
## NEVER Do This

### 1. Factory Obsession
```java
// ❌ STOP! Unnecessary abstraction
OrderFactory → OrderFactoryImpl → OrderCreator

// ✅ Simple method
public Order createOrder(final OrderType type) {
    return switch (type) {
        case STANDARD -> new Order(...);
        case EXPRESS -> new Order(...);
    };
}
```

### 2. Premature Interfaces
```java
// ❌ STOP! Only one implementation
interface PaymentProcessor { }
class CreditCardProcessor implements PaymentProcessor { }

// ✅ Start concrete
@Service
public class PaymentService {
    public PaymentResult processCreditCard(final Payment payment) {
        // Direct implementation
    }
}
```

### 3. Deep Inheritance
```java
// ❌ STOP! 
class Executive extends Manager extends Employee extends Person

// ✅ Use composition
class Employee {
    private final Person personalInfo;
    private final Role role;
}
```
</anti_patterns_to_avoid>

<when_to_add_complexity>
## Only Add Abstraction When:

1. **3+ REAL implementations exist** (not theoretical)
2. **Abstraction REMOVES duplication** (not adds it)
3. **Framework requires it** (Spring interfaces)
4. **External API isolation** (third-party libs)

Example of justified complexity:
```java
// ✅ JUSTIFIED - Multiple payment providers actually exist
public interface PaymentGateway {
    PaymentResult charge(Payment payment);
}

@Component("stripe")
public class StripeGateway implements PaymentGateway { }

@Component("paypal")
public class PayPalGateway implements PaymentGateway { }

@Component("square")
public class SquareGateway implements PaymentGateway { }
```
</when_to_add_complexity>

<spring_boot_best_practices>
## Spring Boot Simplicity

### 1. Use What Spring Provides
```java
// ❌ Custom validation framework
public class CustomValidator { }

// ✅ Use Bean Validation
public record OrderRequest(
    @NotNull @Size(min = 1) List<OrderItem> items,
    @NotNull @Valid Address shippingAddress
) { }
```

### 2. Spring Data Repositories
```java
// ❌ Custom DAO pattern
public class OrderDao { }

// ✅ Simple Spring Data
public interface OrderRepository extends JpaRepository<Order, String> {
    Optional<Order> findByCustomerId(String customerId);
}
```

### 3. Configuration
```java
// ❌ Complex XML configuration

// ✅ Simple annotations
@Configuration
@EnableJpaRepositories
public class DatabaseConfig { }
```
</spring_boot_best_practices>

<execution_checklist>
## Final Implementation Checklist

Before delivering ANY code:

### Simplicity
- [ ] Used existing solutions first?
- [ ] Direct implementation, no unnecessary patterns?
- [ ] Complexity score < 5?
- [ ] Can explain in one sentence?

### Clean Code
- [ ] Meaningful, searchable names?
- [ ] Functions < 20 lines?
- [ ] Functions do ONE thing?
- [ ] All parameters final?
- [ ] Max 3 parameters?

### Java Standards
- [ ] No wildcard imports?
- [ ] No null returns (use Optional)?
- [ ] Proper exception handling?
- [ ] Used modern Java features?

### Testing
- [ ] Test written first (TDD)?
- [ ] Test name: methodName_condition_result?
- [ ] Test covers edge cases?
- [ ] Code passes all tests?

### Documentation
- [ ] Code self-documents (no comments needed)?
- [ ] Public API has Javadoc?
- [ ] Complex business logic explained?
</execution_checklist>

<output_format>
When implementing code, I will:

1. **First analyze** the requirement and check complexity
2. **Write the test** following TDD (show the failing test)
3. **Implement the simplest solution** that works
4. **Refactor only if** it reduces complexity
5. **Validate against** all checklists

The code will be:
- **Simple** - Understandable by juniors
- **Clean** - Following all standards
- **Tested** - TDD approach
- **Modern** - Using Java 21+ features
- **Pragmatic** - Solving real problems, not imaginary ones
</output_format>

<adaptive_error_handling>
## Error Recovery with Reasoning
<error_recovery_thinking>
When implementation challenges arise, intelligent recovery:

### Complexity Score Exceeded
<thinking>
If complexity score ≥ 5:
- Root cause analysis: [what drove complexity up]
- Simplification options: [identified alternatives]
- Trade-off assessment: [feature reduction vs complexity]
Recovery strategy: [selected approach] because [maintains quality while reducing complexity]
</thinking>

### Test Failure Patterns
<thinking>
When tests don't pass as expected:
- Failure analysis: [what's actually failing]
- Expectation validation: [are expectations realistic]
- Implementation review: [minimal implementation check]
Resolution: [fix approach] based on [failure mode understanding]
</thinking>

### Pattern Mismatch
<thinking>
When chosen patterns don't fit:
- Pattern appropriateness: [why pattern isn't working]
- Context mismatch: [what was missed in analysis]
- Alternative approaches: [simpler solutions]
Pivot decision: [new approach] because [better fits actual requirements]
</thinking>

### Integration Challenges
<thinking>
When code doesn't integrate well:
- Interface analysis: [compatibility issues]
- Dependency conflicts: [integration problems]
- Design adjustments: [minimal changes needed]
Integration strategy: [solution] preserving [simplicity principles]
</thinking>
</error_recovery_thinking>
</adaptive_error_handling>

<pattern_learning>
## Continuous Pattern Learning System
<learning_mechanisms>
From each implementation, capture:

### Successful Patterns
<success_pattern_thinking>
When implementation succeeds:
- What approach worked? [successful strategy]
- Why was it effective? [success factors]
- When is it applicable? [usage conditions]
- How can it be reused? [generalization potential]

Pattern captured: [pattern name] for [scenario type] because [effectiveness reason]
</success_pattern_thinking>

### Failed Approaches
<failure_pattern_thinking>
When implementation fails or becomes too complex:
- What went wrong? [failure analysis]
- Where did complexity creep in? [complexity sources]
- What signals were missed? [warning indicators]
- How to avoid next time? [prevention strategy]

Anti-pattern identified: [pattern to avoid] in [scenario] because [causes problems]
</failure_pattern_thinking>

### Code Quality Insights
<quality_learning_thinking>
From code reviews and validation:
- Which rules caught issues? [effective quality checks]
- What was missed by checklists? [gaps identified]
- Where do developers struggle? [common mistakes]
- How can guidance improve? [enhancement opportunities]

Quality improvement: [insight] leads to [better practice] for [developer benefit]
</quality_learning_thinking>

### Simplicity Lessons
<simplicity_learning_thinking>
From simplicity enforcement:
- When did simple approaches work best? [success scenarios]
- What complexity was actually necessary? [justified complexity]
- Where was abstraction premature? [over-engineering cases]
- How to detect complexity earlier? [early warning signs]

Simplicity principle: [learned principle] applies when [conditions] for [benefit]
</simplicity_learning_thinking>
</pattern_learning>

<critical_reminders>
## REMEMBER (With Reasoning Foundation)

1. **SIMPLICITY FIRST** - If complexity score ≥ 5, STOP and simplify!
   <thinking>Every point of complexity must justify itself with concrete value</thinking>

2. **NO PREMATURE ABSTRACTION** - Wait for 3+ real implementations
   <thinking>Abstract when duplication hurts, not when it might hurt someday</thinking>

3. **USE WHAT EXISTS** - Spring Boot, Java libs, project code
   <thinking>Standing on shoulders of giants reduces our complexity debt</thinking>

4. **TEST FIRST** - Always TDD, no exceptions
   <thinking>Tests define behavior clearly before implementation bias sets in</thinking>

5. **SMALL FUNCTIONS** - < 20 lines, do ONE thing
   <thinking>Human cognitive limits make small functions easier to reason about</thinking>

6. **FINAL PARAMETERS** - Every single parameter must be final
   <thinking>Immutability removes whole categories of bugs and mental overhead</thinking>

7. **NO WILDCARDS** - Never use wildcard imports
   <thinking>Explicit imports document dependencies and prevent naming conflicts</thinking>

8. **NO NULL** - Return Optional, not null
   <thinking>Optional makes nullability explicit and forces handling decisions</thinking>

9. **LET IT FAIL** - Don't hide exceptions
   <thinking>Fast failure with clear errors beats silent corruption</thinking>

10. **MODERN JAVA** - Records, pattern matching, text blocks
    <thinking>Language evolution provides simpler ways to express intent</thinking>

> "Any fool can write code that a computer can understand.
> Good programmers write code that humans can understand." - Martin Fowler

**SIMPLICITY IS THE ULTIMATE SOPHISTICATION!**

<thinking_foundation>
Every decision in this command is backed by reasoning that:
- Validates simplicity first
- Checks complexity thresholds
- Considers maintainability impact
- Balances current needs with future flexibility
- Prioritizes human understanding over machine efficiency

When complexity > 3: Engage mcp__mcp-sequentialthinking-tools__sequentialthinking_tools for systematic decision support
</thinking_foundation>
</critical_reminders>