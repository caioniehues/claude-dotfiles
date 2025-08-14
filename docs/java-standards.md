# Java Clean Code Standards

## 🎯 CORE PRINCIPLES

### 1. Meaningful Names
```java
// ❌ BAD - Unclear abbreviations and mental mapping
String d; // elapsed time in days
List<String> l = {"Austin", "New York", "San Francisco"};
Map<String, List<String>> anagrams = new HashMap<String, List<String>>();

// ✅ GOOD - Clear, pronounceable, searchable names
String elapsedTimeInDays;
List<String> locations = {"Austin", "New York", "San Francisco"};
Map<String, List<String>> anagramGroups = new HashMap<>();
```

### 2. Functions Should Do One Thing
```java
// ❌ BAD - Multiple responsibilities
public void emailClients(List<Client> clients) {
    for (Client client : clients) {
        Client clientRecord = repository.findOne(client.getId());
        if (clientRecord.isActive()) {
            email(client);
        }
    }
}

// ✅ GOOD - Single responsibility with clear separation
public void emailActiveClients(List<Client> clients) {
    clients.stream()
        .filter(this::isActiveClient)
        .forEach(this::sendEmail);
}

private boolean isActiveClient(Client client) {
    return repository.findOne(client.getId()).isActive();
}

private void sendEmail(Client client) {
    emailService.send(client);
}
```

### 3. Small Functions (< 20 lines)
```java
// ✅ GOOD - Each method is focused and small
@Service
@RequiredArgsConstructor
public class OrderProcessor {
    private final OrderRepository repository;
    private final PaymentService paymentService;
    private final NotificationService notificationService;
    
    public Order processOrder(final OrderRequest request) {
        final Order order = createOrder(request);
        processPayment(order);
        notifyCustomer(order);
        return order;
    }
    
    private Order createOrder(final OrderRequest request) {
        final Order order = Order.from(request);
        return repository.save(order);
    }
    
    private void processPayment(final Order order) {
        paymentService.charge(order.getCustomerId(), order.getTotal());
    }
    
    private void notifyCustomer(final Order order) {
        notificationService.sendOrderConfirmation(order);
    }
}
```

## 🏗️ EFFECTIVE JAVA PATTERNS

### 1. Static Factory Methods Over Constructors
```java
// ❌ BAD - Multiple confusing constructors
public class User {
    public User(String email) { }
    public User(String email, String name) { }
    public User(String email, String name, Role role) { }
}

// ✅ GOOD - Clear static factory methods
public class User {
    private User(String email, String name, Role role) { }
    
    public static User withEmail(String email) {
        return new User(email, null, Role.USER);
    }
    
    public static User withEmailAndName(String email, String name) {
        return new User(email, name, Role.USER);
    }
    
    public static User admin(String email, String name) {
        return new User(email, name, Role.ADMIN);
    }
}
```

### 2. Builder Pattern for Complex Objects
```java
// ✅ GOOD - Builder for objects with many parameters
@Getter
@Builder(toBuilder = true)
public class OrderRequest {
    private final String customerId;
    private final List<OrderItem> items;
    @Builder.Default
    private final ShippingMethod shipping = ShippingMethod.STANDARD;
    @Builder.Default
    private final PaymentMethod payment = PaymentMethod.CREDIT_CARD;
    private final String promoCode;
    private final Address shippingAddress;
    private final Address billingAddress;
}

// Usage
OrderRequest order = OrderRequest.builder()
    .customerId("CUST-123")
    .items(List.of(item1, item2))
    .shipping(ShippingMethod.EXPRESS)
    .promoCode("SAVE20")
    .shippingAddress(address)
    .build();
```

### 3. Favor Composition Over Inheritance
```java
// ❌ BAD - Deep inheritance hierarchy
class Employee extends Person { }
class Manager extends Employee { }
class Executive extends Manager { }

// ✅ GOOD - Composition with clear responsibilities
@Value
public class Employee {
    Person personalInfo;
    Role role;
    Department department;
    
    public boolean hasPermission(Permission permission) {
        return role.hasPermission(permission);
    }
}
```

### 4. Use Enums Instead of Constants
```java
// ❌ BAD - Int constants
public static final int STATUS_PENDING = 0;
public static final int STATUS_APPROVED = 1;
public static final int STATUS_REJECTED = 2;

// ✅ GOOD - Type-safe enum with behavior
public enum OrderStatus {
    PENDING("Awaiting approval") {
        @Override
        public boolean canTransitionTo(OrderStatus status) {
            return status == APPROVED || status == REJECTED;
        }
    },
    APPROVED("Order approved") {
        @Override
        public boolean canTransitionTo(OrderStatus status) {
            return status == FULFILLED || status == CANCELLED;
        }
    },
    REJECTED("Order rejected") {
        @Override
        public boolean canTransitionTo(OrderStatus status) {
            return false;
        }
    };
    
    private final String description;
    
    OrderStatus(String description) {
        this.description = description;
    }
    
    public abstract boolean canTransitionTo(OrderStatus status);
}
```

## 🔴 TDD: RED → GREEN → REFACTOR

### Test Naming Convention
```java
// Pattern: methodName_condition_expectedResult
@Test
void calculateTotal_emptyCart_returnsZero() { }

@Test
void processPayment_insufficientFunds_throwsPaymentException() { }

@Test
void findUser_existingEmail_returnsUser() { }
```

### TDD Example
```java
// 1. RED - Write failing test first
@Test
void calculateDiscount_premiumCustomer_appliesTwentyPercent() {
    // Given
    Customer premiumCustomer = Customer.builder()
        .type(CustomerType.PREMIUM)
        .build();
    BigDecimal originalPrice = new BigDecimal("100.00");
    
    // When
    BigDecimal discounted = discountService.calculate(premiumCustomer, originalPrice);
    
    // Then
    assertThat(discounted).isEqualTo(new BigDecimal("80.00"));
}

// 2. GREEN - Minimal implementation
public BigDecimal calculate(Customer customer, BigDecimal price) {
    if (customer.getType() == CustomerType.PREMIUM) {
        return price.multiply(new BigDecimal("0.80"));
    }
    return price;
}

// 3. REFACTOR - Improve design
public BigDecimal calculate(Customer customer, BigDecimal price) {
    return price.multiply(getDiscountMultiplier(customer));
}

private BigDecimal getDiscountMultiplier(Customer customer) {
    return customer.getType().getDiscountMultiplier();
}
```

## 🚫 ERROR HANDLING

### Let Exceptions Bubble Up
```java
// ❌ BAD - Swallowing exceptions
public Order findOrder(String id) {
    try {
        return orderRepository.findById(id);
    } catch (Exception e) {
        log.error("Error finding order", e);
        return null; // Hidden failure!
    }
}

// ✅ GOOD - Let it fail clearly
public Order findOrder(final String id) {
    return orderRepository.findById(id)
        .orElseThrow(() -> new OrderNotFoundException(id));
}
```

### Only Catch When You Can Recover
```java
// ✅ GOOD - Meaningful recovery
@Retryable(maxAttempts = 3)
public void sendNotification(final Order order) {
    try {
        emailService.send(order);
    } catch (EmailServiceException e) {
        // Fallback to SMS
        smsService.send(order);
    }
}
```

## 📏 FORMATTING STANDARDS

### Import Order (NO wildcards!)
```java
import com.richemont.ce.adapter.domain.*;     // ❌ NO!
import com.richemont.ce.adapter.domain.Order; // ✅ YES!

// Correct order:
import com.richemont.ce.adapter.domain.Order;
import com.richemont.ce.adapter.service.OrderService;

import java.time.LocalDateTime;
import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;

import static org.assertj.core.api.Assertions.assertThat;
```

### Method Parameters
```java
// All parameters MUST be final
public OrderResponse createOrder(
        final String customerId,     // ✅ final
        final OrderRequest request,  // ✅ final
        final PaymentInfo payment) { // ✅ final
    // implementation
}
```

## 🏃 QUICK REFERENCE

### Do's ✅
- Use meaningful, searchable names
- Keep functions small (< 20 lines)
- One responsibility per function/class
- Use static factory methods
- Favor composition over inheritance
- Let exceptions bubble up
- Use enums for constants
- Apply TDD: Red → Green → Refactor
- All parameters must be final

### Don'ts ❌
- No wildcard imports
- No null returns (use Optional)
- No defensive try-catch
- No commented-out code
- No magic numbers
- No abbreviations in names
- No functions with > 3 parameters
- No inheritance > 1 level deep

## 💎 Modern Java Features (Java 21)

### Pattern Matching
```java
// Use pattern matching for cleaner code
public String formatMessage(Object obj) {
    return switch (obj) {
        case Integer i -> "Number: " + i;
        case String s -> "Text: " + s;
        case List<?> list -> "List of " + list.size() + " items";
        case null -> "No value";
        default -> "Unknown: " + obj.getClass().getSimpleName();
    };
}
```

### Records for DTOs
```java
// Immutable, concise, with automatic equals/hashCode
public record OrderDto(
    String orderId,
    String customerId,
    List<OrderItemDto> items,
    BigDecimal total) {
    
    // Compact constructor for validation
    public OrderDto {
        Objects.requireNonNull(orderId);
        Objects.requireNonNull(customerId);
        items = List.copyOf(items); // Defensive copy
    }
}
```

### Text Blocks for Queries
```java
// Clean multi-line strings
String query = """
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = :status
      AND o.created_at > :startDate
    ORDER BY o.created_at DESC
    """;
```

Remember: **Clean code is simple, readable, and testable!**