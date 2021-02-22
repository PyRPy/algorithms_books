package hello;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;
// https://runestone.academy/runestone/books/published/java4python/Java4Python/javadatatypes.html
public class histogram {

	public static void main(String[] args) {
		Scanner data = null;
		ArrayList<Integer> count;
		Integer idx;
		
		try {
			data = new Scanner(new File("test.dat"));
		}
		catch (IOException e) {
			System.out.println("sorry, unable to open your data");
			e.printStackTrace();
			System.exit(0);
		}
		
		count = new ArrayList<Integer>(10);
		for (Integer i = 0; i < 10; i++ ) {
			count.add(i, 0);
		}
		
		while (data.hasNextInt()) {
			idx = data.nextInt();
			count.set(idx, count.get(idx) + 1);
			
		}
		idx = 0;
		for (Integer i : count ) {
			System.out.println(idx + " occured " + i + " times ");
			idx++;
			
		}
	}

}
