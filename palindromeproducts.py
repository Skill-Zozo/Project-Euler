import math

def is_palindrome(num):
	number_as_string = '%d' % num
	return  number_as_string == number_as_string[::-1]

def three_digit_factors(N):
	# if x is a factor of y, then either x or the co factor of x is <= sqrt(y)
	candidates = []
	if N%2==0:
		candidates = range(2, int(math.sqrt(N)) +1)
	else:
		candidates = range(3, int(math.sqrt(N)) +1, 2)
	for candidate in candidates:
		if(N%candidate==0 and (len('%d' % candidate)==3 and len('%d' % (N/candidate))==3)):
			return [candidate, int(N/candidate)]
	return []





largest_product = 999*999

smallest_product = 100*100

candidates = list(range(smallest_product, largest_product+1))

palindromic_candidates = list(filter(is_palindrome, candidates))[::-1]

for palindrome in palindromic_candidates:
	factors = three_digit_factors(palindrome)
	if(len(factors) > 0):
		print("largest palindrome is: %d which is a product of %d and %d" % (palindrome, factors[0], factors[1]))
		break;

print("Ain't shxt")