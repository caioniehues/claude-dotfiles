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

## 📚 BASIC MEMORY COMPREHENSIVE GUIDE

> Complete AI Assistant Guide: `/Users/caio.niehues/.claude/docs/basic memory guide.md`

### Core Tools Reference

#### Writing & Reading Knowledge
```bash
# Write/update notes (primary tool)
mcp__basic-memory__write_note \
  --title "Note Title" \
  --content "# Content\n..." \
  --folder "folder/path" \
  --tags ["tag1", "tag2"] \
  --project "project-name"

# Read existing content
mcp__basic-memory__read_note "Note Title"           # By title
mcp__basic-memory__read_note "folder/note-name"     # By path
mcp__basic-memory__read_note "memory://folder/note" # By memory URL

# View as formatted artifact (Claude Desktop)
mcp__basic-memory__view_note "Note Title"
```

#### Incremental Editing (v0.13.0)
```bash
# Edit notes incrementally (requires EXACT identifier)
mcp__basic-memory__edit_note \
  --identifier "Exact Note Title" \
  --operation "append" \              # append, prepend, find_replace, replace_section
  --content "\n## New Section\n..."

# Move/organize files
mcp__basic-memory__move_note \
  --identifier "Old Note" \
  --destination "archive/old-note.md"
```

#### Search & Discovery
```bash
# Search across knowledge base
mcp__basic-memory__search_notes "query" --types ["type1"] --after-date "7d ago"

# Build context from memory URLs
mcp__basic-memory__build_context "memory://folder/*" --timeframe "7d"

# Check recent activity
mcp__basic-memory__recent_activity --timeframe "24h"
```

#### Project Management
```bash
# List and switch projects
mcp__basic-memory__list_memory_projects
mcp__basic-memory__switch_project "work-notes"
mcp__basic-memory__get_current_project
```

### Semantic Markdown Format

#### Observations & Relations
```markdown
# Entity Title

## Observations
- [category] This is an observation #tag1 #tag2
- [decision] We chose X over Y #architecture
- [technique] Use pattern Z for performance #optimization

## Relations
- relates_to [[Other Entity]]
- implements [[Design Pattern]]
- requires [[Dependency]]
- part_of [[Parent System]]
```

#### Common Categories & Relations
**Categories**: `[idea]`, `[decision]`, `[question]`, `[fact]`, `[requirement]`, `[technique]`, `[preference]`
**Relations**: `relates_to`, `implements`, `requires`, `extends`, `part_of`, `pairs_with`, `inspired_by`

### Memory URL Patterns
- `memory://title` - Reference by title
- `memory://folder/title` - Reference by folder and title
- `memory://path/relation_type/*` - Follow all relations of type
- `memory://path/*/target` - Find all entities with relations to target

### Knowledge Graph Best Practices

1. **Build Rich Connections**
   - Add 3-5 categorized observations per note
   - Connect each note to 2-3 related entities
   - Use specific relation types (not generic `relates_to`)
   - Create bidirectional relations when appropriate

2. **Reference Accurately**
   - Use exact titles for `[[WikiLinks]]`
   - Search first to find existing entities
   - Create forward references (they link automatically later)
   - Verify identifiers with `search_notes()` before editing

3. **Capture Proactively**
   - Ask: "Would you like me to record this?"
   - Confirm: "I've saved this to Basic Memory"
   - Record decisions, patterns, solutions
   - Document relationships and context

### Common Workflows

#### Task Pattern Capture
```bash
mcp__basic-memory__write_note \
  --title "Task Pattern - [Task Name]" \
  --folder "life-os/task-patterns" \
  --content "Time: planned vs actual\nEnergy: required\nBlockers: encountered\nSuccess factors: identified"
```

#### Multi-Project Work
```bash
# Work content
mcp__basic-memory__write_note --title "Sprint Notes" --project "work-notes"

# Personal content  
mcp__basic-memory__write_note --title "Personal Task" --project "personal"
```

#### Incremental Note Building
```bash
# Search for exact title first
results = mcp__basic-memory__search_notes "setup guide"

# Then edit with exact title
mcp__basic-memory__edit_note \
  --identifier "Setup Guide v2" \
  --operation "append" \
  --content "\n## Troubleshooting\n..."
```

### Important v0.13.0 Notes
- **Strict Matching**: `edit_note` and `move_note` require EXACT identifiers
- **Search First**: Use `search_notes()` to find exact titles before editing
- **Tags Searchable**: Frontmatter tags are now indexed and searchable
- **Project Context**: All tools support `--project` parameter

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
- ALWAYS USE CLI TOOLS. run the bash command man -k . to have the full list
- ALWAYS USE GITHUB CLI gh