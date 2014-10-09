public class MultiplesOf3And5
{
	public static void main (String[] args) 
	{
		int a = 5;
		int b = 3;
		int res = 0;
		for (int i = 1; i < 1000; i++) {
			if(i % 3 == 0) 	res += i;
			else if(i % 5 == 0) res += i;
		}		
		System.out.println(res);
	}
}
