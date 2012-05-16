from poiler_common import seive_of_E
from math import sqrt

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
  meets_conjecture = 0
  for j in xrange(1,int(sqrt(oc/2))+2):
    pp = oc - 2*j*j # possible prime
    if pp > 0 and is_prime[pp]:
      meets_conjecture = 1
      break
  if (meets_conjecture == 0):
    print (oc)
    break

      
