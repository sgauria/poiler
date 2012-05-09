from poiler_common import sieve_of_N

N = 1000000
is_prime = seive_of_E(N)

odd_primes = []
odd_composites = []

for i in xrange(3,N,2):
  if is_prime[i]:
    odd_primes.append(i)
  else:
    odd_composites.append(i)

for oc in odd_composites:
  for j in xrange(1,oc-1):
    pp = oc - 2*j*j # possible prime
    if is_prime[pp]:
      break
  if (j == oc-2):
    print (oc)
    break

      
