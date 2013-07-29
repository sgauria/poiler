from poiler_common import *

N = 10000000

def totient_direct(n) :
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

assert totient_direct(1) == 1
assert totient_direct(9) == 6
assert totient_direct(87109) == 79180

def totient_wikipedia(n):
  if n == 1:
    return 1
  cc = n
  for p,k in factorize(n):
    cc = cc * (p-1)/p
  return cc

assert totient_wikipedia(1) == 1
assert totient_wikipedia(9) == 6
assert totient_wikipedia(87109) == 79180

@memoize_fast_1_arg
def totient_recursive(n):
  if n == 1:
    return 1
  fs = list(factorize(n))
  if len(fs) == 1:
    p,k = fs[0]
    return (n*(p-1)/p)
  else :
    t = 1
    for p,k in fs :
      t *= totient_recursive (p**k)
    return t

assert totient_recursive(1) == 1
assert totient_recursive(9) == 6
assert totient_recursive(87109) == 79180

totient = totient_wikipedia

# This scheme eventually solves it, but it is slow. 
#  115s for N=  1 million.
# 3346s for N= 10 million.
if 1 :
  best_n, best_t, best_ratio = 0,0,100

  for n in xrange ( 2, N ) :
      t = totient(n)
      if sorted_digits(t) == sorted_digits(n):
        print n
        ratio = 1.0 * n / t
        if ratio <= best_ratio :
          best_n, best_t, best_ratio = n, t, ratio
          print "*", best_n, best_t, best_ratio

  print "**", best_n, best_t, best_ratio


