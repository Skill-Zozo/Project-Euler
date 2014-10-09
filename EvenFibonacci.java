public class EvenFibonacci
{
	public static int getSum(int x) {
		int m = 0;
		int res = 0;
		for(int i = 1; m < x; i++) {
			m = fibonacci(i);
			if(m <= 4000000 && m % 2 == 0) res += m;
		}
		return res;		
	}

	public static int fibonacci(int i) {
		if(i == 1) return 1;
		if(i == 2) return 2;
		return fibonacci(i-1) + fibonacci(i-2);
	}

	public static void main(String[] args) 
	{
		System.out.println(getSum(4000000));
	}
}
