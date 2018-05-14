candidates = [i for i in range(19, 19*20000000, 19) if i > 2520]

def divides_all(num, divisors):
	for divisor in divisors:
		if num%divisor!=0:
			return False
	return True
ans = 0
ans = next((i for i in candidates if divides_all(i, range(1,21))), None)

print(ans)