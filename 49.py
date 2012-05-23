from poiler_common import *

def sorted_digits(n):
  return int("".join(sorted(list(str(n)))))

N1 = 1000
N2 = 10000

is_prime = seive_of_E(N2)
primes = []
for i in xrange(N1,N2):
  if is_prime[i]:
    primes.append(i)

# Look for arithmetic sequences of len 3 in the primes list.
# If a sequence is found, check if the numbers are permutations.
for i in range(len(primes)):
  for j in range(i+1,len(primes)):
    pi = primes[i]
    pj = primes[j]
    pk = pj + (pj-pi)
    if pk < N2 and is_prime[pk]:
      if (sorted_digits(pi) == sorted_digits(pj) == sorted_digits(pk)):
	print pi,pj,pk
  

