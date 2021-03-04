package DataStructure;
// https://www.geeksforgeeks.org/java-util-hashmap-in-java-with-examples/
import java.util.HashMap;

public class HashMapBasics {

	public static void main(String[] args) {
		// create a hashmap
		HashMap<String, Integer> map = new HashMap<>();
		
		// add elements
		map.put("mark", 10);
		map.put("mike", 20);
		map.put("frank", 20);
		
		// output info
		System.out.println("size of map is: " + map.size());
		System.out.println(map);
		
		// search for a key
		if (map.containsKey("mike")) {
			Integer a = map.get("mike");
			System.out.println("value for key" + " \"mike\" is : " + a);
		}
		
	}

}
