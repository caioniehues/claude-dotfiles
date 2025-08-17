# TDD Test Scenario

Implement a simple shopping cart discount calculator with the following requirements:

1. Calculate discounts for different customer types (STANDARD, PREMIUM, VIP)
2. Handle empty carts (return zero)
3. Validate input parameters (throw exceptions for null)
4. Apply percentage discounts: STANDARD=0%, PREMIUM=10%, VIP=20%
5. Return BigDecimal for monetary calculations

Requirements for TDD implementation:
- Follow RED-GREEN-REFACTOR cycle
- Write tests first
- Keep functions under 20 lines
- Use final parameters
- No null returns