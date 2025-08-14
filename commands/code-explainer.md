# Code Explainer - Simple Code Analysis

<task>
Explain what code does in clear, practical terms: $ARGUMENTS
</task>

<context>
Reads code and explains what it actually does, how it works, and any notable patterns. Focuses on facts, not speculation about business context.
</context>

## Process

1. **Read the code** using Read tool
2. **Explain what it does** - the actual functionality
3. **Note any patterns** - design patterns, frameworks used
4. **Highlight gotchas** - edge cases, potential issues
5. **Suggest improvements** if obvious issues exist

## Analysis Focus

- **What it does**: Core functionality and behavior
- **How it works**: Key algorithms and data flow  
- **Notable patterns**: Design patterns, architectural choices
- **Potential issues**: Performance, maintainability, or security concerns
- **Dependencies**: What it relies on to function

No speculation about business requirements or elaborate architectural philosophy - just clear explanation of the code that exists.

## Example Output

```
## OrderService Analysis

**What it does**: Manages order operations with database persistence

**Key functionality**:
- Creates new orders from request data
- Validates order data before saving
- Retrieves orders by ID with Optional return
- Handles order status transitions

**Patterns used**:
- Service layer pattern for business logic
- Repository pattern for data access
- Builder pattern for order creation

**Notable aspects**:
- Uses Optional to avoid null returns
- Final parameters for immutability
- Clean separation of concerns

**Potential improvements**:
- Consider adding validation for edge cases
- Could benefit from explicit error handling
```

Simple, factual, useful.