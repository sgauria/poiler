# Copied from 28. Calculate only the diagonal entries.
from poiler_common import is_prime

d = [1]
step = 2
i = 0
prime_count, diagonal_count = 0,1
while True:
  for j in xrange(4):
    n = d[4*i+j] + step
    d.append(n)
    if is_prime(n):
      prime_count += 1
  diagonal_count += 4
  i += 1
  step += 2
  if prime_count * 10 < diagonal_count:
    break

#print d
#print sum(d)

print 2*i+1

