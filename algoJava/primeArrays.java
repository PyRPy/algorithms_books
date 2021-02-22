package hello;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;
public class primeArrays {

	public static void main(String[] args) {
		Scanner data = null;
		Integer[] count = {0,0,0,0,0,0,0,0,0,0};
		Integer idx;
		
		try {
			data = new Scanner(new File("test.dat"));
		}
		catch (IOException e) {
			System.out.println("sorry, unable to open your data");
			e.printStackTrace();
			System.exit(0);
		}
		
		while (data.hasNextInt()) {
			idx = data.nextInt();
			count[idx] = count[idx] + 1;
		}
		
		idx = 0;
		for (Integer i : count ) {
			System.out.println(idx + " occured " + i + " times ");
			idx++;
			
		}

	}

}
