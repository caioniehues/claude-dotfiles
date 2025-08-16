import java.util.*;
import java.util.stream.*;

public class OrderProcessor {
    private Map<String, Double> prices = new HashMap<>();
    private List<Order> orders = new ArrayList<>();
    
    public void processOrders(List<OrderRequest> requests) {
        for (OrderRequest req : requests) {
            Order order = new Order();
            order.setId(UUID.randomUUID().toString());
            order.setItems(req.getItems());
            double total = req.getItems().stream()
                .mapToDouble(item -> prices.get(item.getId()) * item.getQuantity())
                .sum();
            order.setTotal(total);
            orders.add(order);
        }
    }
    
    static class Order {
        private String id;
        private List<OrderItem> items;
        private double total;
        // getters and setters...
    }
    
    static class OrderRequest {
        private List<OrderItem> items;
        // getters and setters...
    }
    
    static class OrderItem {
        private String id;
        private int quantity;
        // getters and setters...
    }
}