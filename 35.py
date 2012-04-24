def seive_of_E(n):
  l = [0,0]+([1]*(n-2))		    # All numbers >=2  are prime-candidates
  p = 2				    # start from 2
  while (p*p < n):		    # Any composite number < n should have one factor < sqrt(n) 
    for m in xrange(2*p,n,p):	    # Mark all multiples of the current prime as composite.
      l[m] = 0
    p = p + 1 + l[p+1:].index(1)    # next prime
  return l

N = 1000000
is_prime = seive_of_E(N)

lprimes = [n for (n,is_p) in enumerate(is_prime) if is_p == 1]

ccount = 0
for p in lprimes:
  circular = True
  sp = str(p)
  for r in range(1,len(sp)):
    nsp = sp[r:] + sp[:r]
    if not is_prime[int(nsp)]:
      circular = False
      break
  if circular == True:
    print p
    ccount += 1

print "====="
print ccount
