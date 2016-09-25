import java.util.*;

public class bottle1
{
	public static void main(String [] args)
	{
		int s, v1, v2;
		Scanner in = new Scanner(System.in);

		s = in.nextInt();
		v1 = in.nextInt();
		v2 = in.nextInt();
			int t1 = (s/v1)*v1;
			while (t1 >= 0 && (s-t1)%v2 != 0)
				t1 -= v1;
			if (t1 >= 0)
				System.out.println(t1/v1 + " " + (s-t1)/v2);
			else if (s%v2 == 0)
				System.out.println(0 + " " + s/v2);
			else
				System.out.println("Impossible");
	}
}
