# Simple Java - Basic Java Generation

<task>
Generate basic Java code following clean principles: $ARGUMENTS
</task>

## Quick Rules
- Keep complexity < 5
- Functions < 20 lines
- Parameters final
- No wildcard imports
- Use Optional not null

## Templates

**Service**:
```java
@Service
public class ${Name}Service {
    public ${ReturnType} ${methodName}(final ${ParamType} ${param}) {
        // Implementation
    }
}
```

**Record DTO**:
```java
public record ${Name}Dto(String id, String name) {}
```

**Controller**:
```java
@RestController
public class ${Name}Controller {
    @GetMapping("/${path}")
    public ResponseEntity<${Type}> get${Name}() {
        // Implementation
    }
}
```

That's it. No overthinking.