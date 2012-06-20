N = 10000000000
p = 1
for i in xrange (7830457):
  p = (p*2) % N
p = (28433*p) % N
p = (p+1) % N

print p
