// Simple utility function for testing
function calculateDiscount(price, discountPercent) {
    if (price <= 0 || discountPercent < 0 || discountPercent > 100) {
        throw new Error('Invalid input parameters');
    }
    
    const discountAmount = (price * discountPercent) / 100;
    return price - discountAmount;
}

module.exports = { calculateDiscount };