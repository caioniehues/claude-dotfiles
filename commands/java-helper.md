# Java Helper - Simple Java Code Generation

<task>
Generate clean Java code following CLAUDE.md standards: $ARGUMENTS
</task>

<context>
Simple Java code generation that follows CLAUDE.md simplicity rules. No over-engineering, no complex patterns, just clean Java that solves real problems.
</context>

## Process

1. **Check CLAUDE.md compliance**:
   - Complexity score < 5? 
   - Can use existing solution?
   - Really need this abstraction now?

2. **Generate simple Java**:
   - Meaningful names (no abbreviations)
   - Functions < 20 lines
   - All parameters final
   - No wildcard imports
   - Return Optional not null

3. **Apply modern Java**:
   - Records for DTOs
   - Pattern matching for switches
   - Text blocks for multi-line strings

## Examples

```java
// Simple service
@Service
@RequiredArgsConstructor
public class OrderService {
    private final OrderRepository repository;
    
    public Optional<Order> findById(final String id) {
        return repository.findById(id);
    }
}

// DTO with record
public record OrderDto(String id, String customerId, BigDecimal total) {}

// Clean controller
@RestController
@RequiredArgsConstructor
public class OrderController {
    private final OrderService service;
    
    @GetMapping("/orders/{id}")
    public ResponseEntity<OrderDto> getOrder(@PathVariable final String id) {
        return service.findById(id)
            .map(this::toDto)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
}
```

**Remember**: If it's getting complex, you're probably over-engineering. Keep it simple.