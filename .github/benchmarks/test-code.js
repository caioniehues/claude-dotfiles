// Test JavaScript file for senior-developer-analysis
function calculateTotal(items) {
    var total = 0;
    for (var i = 0; i < items.length; i++) {
        if (items[i].price) {
            total += items[i].price * (items[i].quantity || 1);
        }
    }
    return total;
}

const processOrder = async (order) => {
    const validation = validateOrder(order);
    if (!validation.valid) {
        throw new Error('Invalid order');
    }
    
    const total = calculateTotal(order.items);
    const tax = total * 0.08;
    
    return {
        id: generateOrderId(),
        total: total + tax,
        status: 'processed',
        timestamp: new Date()
    };
};

function generateOrderId() {
    return Math.random().toString(36).substring(2, 9);
}

function validateOrder(order) {
    if (!order || !order.items || order.items.length === 0) {
        return { valid: false, error: 'No items' };
    }
    return { valid: true };
}