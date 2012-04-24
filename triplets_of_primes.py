def seive_of_E(n):
  l = [0,0]+([1]*(n-2))		    # All numbers >=2  are prime-candidates
  p = 2				    # start from 2
  while (p*p < n):		    # Any composite number < n should have one factor < sqrt(n) 
    for m in xrange(2*p,n,p):	    # Mark all multiples of the current prime as composite.
      l[m] = 0
    p = p + 1 + l[p+1:].index(1)    # next prime
  return l

N = [100,1000,10000,100000,1000000]
is_prime = seive_of_E(3*max(N))

lprimes = [n for (n,is_p) in enumerate(is_prime) if is_p == 1]

for nn in N:
  trip_sum_prime_count = trip_sum_not_prime_count = 0
  for i1 in xrange(1,nn):
    p1 = lprimes[i1]
    if (p1 > nn) : break
    for i2 in xrange(i1,nn):
      p2 = lprimes[i2]
      if (p2 > nn) : break
      for i3 in xrange(i2,nn):
	p3 = lprimes[i3]
	if (p3 > nn) : break
	if (is_prime[(p1+p2+p3)]):
	  trip_sum_prime_count += 1
	else :
	  trip_sum_not_prime_count += 1
  print "N =",nn," prime_triplets =",trip_sum_prime_count," non-prime-triplets =",trip_sum_not_prime_count


# Random code trying to see if the sum of 3 primes is likely to yield to be prime or not.
