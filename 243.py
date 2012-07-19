# Compare fractions
from poiler_common import prime_factor_candidates, factorize
def resilience_simple(d):
  r = d - 1
  for i in range(2,d):
    if (d % i == 0):
      r -= 1
      continue
    for p in prime_factor_candidates(i):
      if i % p == 0 and d % p == 0:
	r -= 1
	break
  return (1.0*r/(d-1))

import itertools
def resilience_complex(d):
  fd = [x for (x,y) in factorize(d)] # Factors of d.
  r = d - 1
  for sss in range(1,len(fd)+1): # subset size
    sign = ((-1) ** sss)
    for c in itertools.combinations(fd,sss):
      prod = 1
      for f in c :
	prod *= f
      r += sign*((d-1)/prod)
  return (1.0*r/(d-1))

resilience = resilience_complex

assert (resilience(12) == (4.0/11))
assert (resilience(509) == 1)

n = 2*3*5*7*11*13*17
#assert(resilience_simple(n) == resilience_complex(n))
#print n, resilience(n)
#exit(0)

# Safe to assume that d must be a multiple of all the small primes.
d = n
minr = 1
while True:
  d += n
  r = resilience(d)
  minr = min(r,minr)
  print minr, d, r
  if (r < (15499.0/94744)):
    print "****", d, "****"
    print "****(", [x for x in factorize(d)], ")****"
    break
