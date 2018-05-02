def is_prime(x):
  return len(list(filter(lambda y: x%y==0, range(2,int(x/2)+1)))) == 0 

def find_first_prime_factor(N):
  candidates = []
  if N%2==0:
    candidates = range(2, int(N/2 +1))
  else:
    candidates = range(3, int(N/2 +1), 2)

  for candidate in candidates:
    if((N%candidate == 0) and (is_prime(candidate))):
      return (N/candidate, candidate)
  # failed to find factor, return arg
  return (N, N)

def primitization(x, factors=[]):
  divident, first_prime = find_first_prime_factor(x)

  if divident == first_prime:
    factors.append(first_prime)
    return factors
  else:
    factors.append(first_prime)
    return primitization(divident, factors)

if __name__ == '__main__':
  print(primitization(7100202642887))