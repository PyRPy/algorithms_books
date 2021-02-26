package ctci;

public class Permutation {
	public static String sort(String s) {
		char[] content = s.toCharArray();
		java.util.Arrays.sort(content);
		return new String(content);
	}
	
	public static boolean permutation(String s, String t) {
		if (s.length() != t.length()) {
			return false;
		}
		
		return sort(s).equals(sort(t));
	}
	
	public static void main(String[] args) {
		String a = "god";
		String b = "dog";
		System.out.println("is " + a + " permutation of " + b + " : " + permutation(a, b));

	}

}
