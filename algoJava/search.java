package search;
import java.util.Scanner;
/* https://www.youtube.com/watch?v=5KRGH2IoF7Q */
public class search {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int[] data = {2, 3, 5, 7, 4, 9, 11, 34, 12};
		int x = in.nextInt();
		int loc = -1;
		for ( int i = 0; i < data.length; i++ )
		{
			if ( x == data[i] )
			{
				loc = i;
				break;
			}
		}
		if ( loc > -1 ) 
		{
			System.out.println( x + " is " + (loc + 1) + "th element");
			
		}
		else
		{
			System.out.println( x + " is not in this array ");
		}

	}
}


