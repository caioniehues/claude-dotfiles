// Test Scenario 2: Complex Service Class (High Complexity)
import java.util.*;
import java.util.stream.Collectors;

public class UserService {
    private Map<String, Object> userCache = new HashMap<>();
    private List<String> activeUsers = new ArrayList<>();
    
    public Object getUserData(String id, boolean cached, String type) {
        if (cached) {
            Object data = userCache.get(id);
            if (data != null) {
                return data;
            }
        }
        
        Object userData = fetchFromDatabase(id);
        
        if (type.equals("premium")) {
            userData = enhanceWithPremiumFeatures(userData);
        } else if (type.equals("admin")) {
            userData = enhanceWithAdminFeatures(userData);
        }
        
        if (cached) {
            userCache.put(id, userData);
        }
        
        return userData;
    }
    
    private Object fetchFromDatabase(String id) {
        // Simulate database call
        return new Object();
    }
    
    private Object enhanceWithPremiumFeatures(Object data) {
        return data;
    }
    
    private Object enhanceWithAdminFeatures(Object data) {
        return data;
    }
}