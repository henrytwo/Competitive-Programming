import java.util.*;
import java.math.*;

public class aplusb2 {
	public static Scanner stdin = new Scanner(System.in);

	public static void main(String[] args) {
		int numPineapples = stdin.nextInt();
		BigInteger victim1, victim2, sum;

		for (int i = 0; i < numPineapples; i++) {
			victim1 = new BigInteger(stdin.next());
			victim2 = new BigInteger(stdin.next());
			sum = victim1.add(victim2);

			System.out.println(sum.toString());
		}
	}
}
