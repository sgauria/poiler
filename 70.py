from poiler_common import factorize, sorted_digits

def totient(n) :
  if n == 1:
    return 1
  fs = [ p for p,np in factorize(n)] # factors
  cc = 0 # coprime count
  for i in xrange(1,n):
    coprime = 1
    for p in fs:
      if i % p == 0 :
        coprime = 0
        break
    if coprime == 1 :
      cc += 1
  return cc

assert totient(1) == 1
assert totient(9) == 6
assert totient(87109) == 79180

best_n, best_t, best_ratio = 0,0,100

for n in xrange ( 2, 10000000 ) :
  t = totient(n)
  if sorted_digits(t) == sorted_digits(n):
    print n
    ratio = 1.0 * n / t
    if ratio <= best_ratio :
      best_n, best_t, best_ratio = n, t, ratio
      print "*", best_n, best_t, best_ratio

print "**", best_n, best_t, best_ratio

# This should solve it, but is prohibitively slow.

