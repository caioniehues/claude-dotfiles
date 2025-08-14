# CLAUDE.md - Global Configuration & Guidelines

## 🧠 PART 1: MEMORY-INTEGRATED AI ASSISTANT

### MANDATORY: SESSION INITIALIZATION PROTOCOL

**EVERY SESSION MUST START WITH THESE STEPS:**

#### 1. Load Context from Basic Memory
```bash
# ALWAYS run at session start - NO EXCEPTIONS
mcp__basic-memory__build_context "memory://life-os/*" --timeframe "7d"
mcp__basic-memory__recent_activity --timeframe "24h"
```

#### 2. Check Active Tasks & Patterns
```bash
mcp__basic-memory__search_notes "status:active OR priority:high" --entity-types "task"
mcp__basic-memory__search_notes "type:task-pattern" --after-date "7d ago"
```

### CONTINUOUS MEMORY CAPTURE

#### After Task Completion
```bash
mcp__basic-memory__write_note \
  --title "Task Pattern - [Task Name]" \
  --folder "life-os/task-patterns" \
  --content "[Pattern details with time, approach, blockers]"
```

#### Problem Solutions
```bash
mcp__basic-memory__write_note \
  --title "Solution - [Problem Description]" \
  --folder "technical/solutions" \
  --content "[Problem, approach, solution, reusable pattern]"
```

### LIFE-OS INTEGRATION

#### Morning Planning
```bash
# Load patterns for time estimates
mcp__basic-memory__search_notes "category:[task-category] energy:[current-energy]"
```

#### ADHD Optimizations (FROM PATTERNS)
- **Time Estimates**: Base × 1.5 minimum
- **Task Chunks**: Max 20 minutes (TASTE method)
- **Energy Matching**: High-energy tasks in morning
- **Context Switching**: Add 25% overhead

---

## 🎯 PART 2: JAVA CLEAN CODE STANDARDS

### SIMPLICITY FIRST - THE PRIME DIRECTIVE

#### The 3-Question Rule (ALWAYS ASK BEFORE CODING)
1. **Can I use what already exists?** → DO THAT
2. **Can I solve this with a simple method?** → DO THAT
3. **Do I really need this abstraction NOW?** → PROBABLY NOT

#### Complexity Score (MUST be < 5)
- Direct solution: 1 point
- Each new class: +2 points
- Each interface: +1 point
- Each design pattern: +3 points
- Each configuration file: +2 points

**If your score is ≥ 5, STOP and simplify!**

### 📊 SIMPLICITY DECISION MATRIX

| Scenario | ✅ SIMPLE Solution | ❌ OVER-ENGINEERED |
|----------|-------------------|-------------------|
| Validate email | `email.matches("^.+@.+\\..+$")` | EmailValidatorFactoryBuilder |
| Transform list | `list.stream().map(...).toList()` | TransformationStrategy pattern |
| Single if/else | Direct if statement | Strategy pattern |
| 3 similar methods | Extract common code | Abstract base + 3 subclasses |
| Simple CRUD | Spring Data Repository | Custom DAO pattern |
| Data mapping | Direct method `toDto()` | Transformer<S,T> interface |

### JAVA NAMING & FUNCTION RULES

#### Naming Rules
```java
// ❌ BAD - Unclear, abbreviated
String d; // elapsed time
List<String> l;

// ✅ GOOD - Clear, searchable, meaningful
String elapsedTimeInDays;
List<String> locations;
```

#### Function Rules
- **MUST be < 20 lines**
- **Do ONE thing only**
- **All parameters MUST be final**
- **Max 3 parameters** (use objects for more)

```java
// ✅ GOOD - Small, focused, clear
public Order processOrder(final OrderRequest request) {
    final Order order = createOrder(request);
    processPayment(order);
    notifyCustomer(order);
    return order;
}
```

#### Import Rules
```java
import com.richemont.ce.domain.*;     // ❌ NEVER!
import com.richemont.ce.domain.Order;  // ✅ ALWAYS!
```

### 🚫 ANTI-PATTERNS - NEVER DO THIS

#### 1. Factory Madness
```java
// ❌ STOP! 5 files for simple creation
OrderFactory → OrderFactoryImpl → OrderCreator → StandardOrderCreator

// ✅ YES! One simple method
public Order createOrder(final OrderType type, final OrderRequest request) {
    return switch (type) {
        case STANDARD -> new Order(request, standardShipping());
        case EXPRESS -> new Order(request, expressShipping());
    };
}
```

#### 2. Premature Abstraction
```java
// ❌ STOP! Only one implementation exists
interface PaymentProcessor { }
interface PaymentValidator { }  

// ✅ YES! Start concrete
@Service
public class PaymentService {
    public PaymentResult processCreditCard(final Payment payment) {
        validatePayment(payment);
        return gateway.charge(payment);
    }
}
```

#### 3. Exception Swallowing
```java
// ❌ NEVER hide failures
try {
    return repository.findById(id);
} catch (Exception e) {
    return null; // Hidden failure!
}

// ✅ Let it fail clearly
return repository.findById(id)
    .orElseThrow(() -> new NotFoundException(id));
```

### 🏗️ WHEN TO ADD COMPLEXITY (ONLY WHEN)

1. **You have 3+ REAL implementations** (not theoretical)
2. **The abstraction REMOVES duplication** (not adds it)
3. **Framework requires it** (Spring interfaces)
4. **External API isolation** (third-party dependencies)

### 💎 MODERN JAVA PATTERNS (USE THESE)

#### Records for DTOs
```java
public record OrderDto(
    String orderId,
    String customerId,
    BigDecimal total
) { }
```

#### Pattern Matching
```java
return switch (obj) {
    case Integer i -> "Number: " + i;
    case String s -> "Text: " + s;
    case null -> "No value";
    default -> "Unknown";
};
```

#### Optional over Null
```java
return repository.findById(id); // Returns Optional<Order>
```

### 🔴 TDD: RED → GREEN → REFACTOR

#### Test Naming
```java
methodName_condition_expectedResult

@Test
void calculateTotal_emptyCart_returnsZero() { }
```

#### Test First, Code Second
1. **RED** - Write failing test
2. **GREEN** - Minimal code to pass
3. **REFACTOR** - Improve design

---

## ✔️ THE UNIFIED CHECKLIST

### Before ANY Work
- [ ] **Loaded Basic Memory context?**
- [ ] **Searched for existing patterns/solutions?**
- [ ] **Applied ADHD time multipliers?**

### Before Committing Code
- [ ] **Can I explain this solution in ONE sentence?**
- [ ] **Would a junior developer understand this immediately?**
- [ ] **Am I solving a REAL problem or an imaginary one?**
- [ ] **Have I avoided unnecessary abstractions?**
- [ ] **Is my complexity score < 5?**
- [ ] **Are all my functions < 20 lines?**
- [ ] **Are all parameters final?**
- [ ] **No wildcard imports?**
- [ ] **No null returns?**

### After Task Completion
- [ ] **Captured pattern to Basic Memory?**
- [ ] **Documented actual vs estimated time?**
- [ ] **Noted blockers and solutions?**

---

## 📏 QUICK REFERENCE

### Memory Commands
```bash
# Start of session
mcp__basic-memory__build_context "memory://life-os/*" --timeframe "7d"

# Search for anything
mcp__basic-memory__search_notes "[query]"

# Save insight
mcp__basic-memory__write_note --title "[Title]" --folder "[folder]"
```

### Code DO's ✅
- Start simple, refactor when needed
- Use built-in Java/Spring features first
- Direct implementation over patterns
- Meaningful, searchable names
- Small functions (< 20 lines)
- Let exceptions bubble up
- Use Optional for nullables
- Modern Java features (records, pattern matching)

### Code DON'Ts ❌
- NO wildcard imports
- NO null returns
- NO defensive try-catch
- NO functions > 20 lines
- NO > 3 parameters
- NO inheritance > 1 level
- NO abstractions without 3+ implementations
- NO complexity score ≥ 5

---

## 🚨 CRITICAL RULES - NEVER VIOLATE

1. **ALWAYS start sessions with memory context** - No exceptions
2. **ALWAYS capture patterns after tasks** - Even small ones
3. **ALWAYS check memory before starting new work** - Avoid repetition
4. **ALWAYS apply ADHD time multipliers** - From learned patterns
5. **ALWAYS keep code simple** - Complexity score < 5
6. **ALWAYS use explicit imports** - No wildcards
7. **ALWAYS make parameters final** - Immutability first

---

## 💡 REMEMBER

> "Any fool can write code that a computer can understand.
> Good programmers write code that humans can understand." - Martin Fowler

**SIMPLICITY IS THE ULTIMATE SOPHISTICATION!**

*When in doubt, choose the simpler solution. You can always add complexity later, but you can rarely remove it.*

---

**Basic Memory Project**: obsidian | **Code Standards**: Active | **Last Updated**: 2025-01-14

---

## 📝 IMPORTANT NOTES

- **Commands Location**: All commands should be located at `/Users/caio.niehues/.claude/commands/`
- **Agent Selection**: Always use the appropriate agent for the action (use meta-agent to create agents)
- **File Reading**: ALWAYS read all mentioned related files before proceeding
- **Documentation**: NEVER create documentation files unless explicitly requested