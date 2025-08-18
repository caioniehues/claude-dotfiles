// Moderate complexity: Service with dependency injection and error handling
interface PaymentGateway {
    processPayment(amount: number, currency: string): Promise<PaymentResult>;
}

interface PaymentResult {
    success: boolean;
    transactionId?: string;
    errorCode?: string;
    errorMessage?: string;
}

class PaymentService {
    constructor(
        private gateway: PaymentGateway,
        private logger: Logger,
        private config: PaymentConfig
    ) {}

    async processOrder(order: Order): Promise<PaymentResult> {
        try {
            this.validateOrder(order);
            
            const amount = this.calculateTotal(order);
            const currency = order.currency || this.config.defaultCurrency;
            
            this.logger.info(`Processing payment for order ${order.id}`, {
                amount,
                currency,
                customer: order.customerId
            });

            const result = await this.gateway.processPayment(amount, currency);
            
            if (result.success) {
                await this.recordSuccessfulPayment(order, result);
            } else {
                await this.handlePaymentFailure(order, result);
            }
            
            return result;
        } catch (error) {
            this.logger.error('Payment processing failed', { orderId: order.id, error });
            return {
                success: false,
                errorCode: 'PROCESSING_ERROR',
                errorMessage: error.message
            };
        }
    }

    private validateOrder(order: Order): void {
        if (!order.id || !order.customerId || !order.items?.length) {
            throw new Error('Invalid order data');
        }
    }

    private calculateTotal(order: Order): number {
        return order.items.reduce((total, item) => {
            return total + (item.price * item.quantity);
        }, 0);
    }

    private async recordSuccessfulPayment(order: Order, result: PaymentResult): Promise<void> {
        // Implementation would record to database
        this.logger.info(`Payment recorded successfully`, {
            orderId: order.id,
            transactionId: result.transactionId
        });
    }

    private async handlePaymentFailure(order: Order, result: PaymentResult): Promise<void> {
        // Implementation would handle failure scenarios
        this.logger.warn(`Payment failed for order ${order.id}`, {
            errorCode: result.errorCode,
            errorMessage: result.errorMessage
        });
    }
}