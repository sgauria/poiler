# Python bignum support makes this easy.
# To do it without bignum, I would calculate prime factors for each a, and store tuple lists of (prime factor, power) for each number into a set.
s = set([])
for a in xrange(2,101):
  for b in xrange(2,101):
    s.add(a**b)

print len(s)
#print s
