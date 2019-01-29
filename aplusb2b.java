import java.util.*;
import java.math.*;

public class aplusb2b {
	public static Scanner stdin = new Scanner(System.in);

	public static void main(String[] args) {
		int numPineapples = stdin.nextInt();
		int size, v1[], v2[], sum[], val;
	        String victim1, victim2;

		for (int i = 0; i < numPineapples; i++) {
			victim1 = stdin.next();
			victim2 = stdin.next();

			size = Math.max(victim1.length(), victim2.length()) + 10;

			sum = new int[size];
			v1 = new int[size];
			v2 = new int[size];

			for (int a = victim1.length() - 1; a > -1; a--) {
				if (victim1.charAt(a) != '-') {
					v1[size - victim1.length() + a] = Integer.parseInt("" + victim1.charAt(a)) * ((victim1.charAt(0) == '-') ? -1 : 1);
				}
			}

			for (int b = victim2.length() - 1; b > -1; b--) {
				if (victim2.charAt(b) != '-') {
					v2[size - victim2.length() + b] = Integer.parseInt("" + victim2.charAt(b)) * ((victim2.charAt(0) == '-') ? -1 : 1);
				}
			}

			for (int c = size - 1; c > -1; c--) {
				val = v1[c] + v2[c];

				if (val > 9) {
					sum[c - 1] += (int) (val - val % 10) / 10;
				}

				sum[c] += val % 10;

				System.out.println(v1[c] + " " + v2[c] + " " + sum[c]);
			}

			System.out.print("\n");
		}
	}
}
