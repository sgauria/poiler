from poiler_common import memoize_fast_args_only, factorize

@memoize_fast_args_only
def piles(n,mss):
  """ n is the number of coins. mss is the max subset(pile) size"""
  count = 0
  if n <= 1:
    count = 1
  elif mss == 1:
    count = 1
  elif mss == 2:
    count = int(n/2) + 1
  else :
    for i in xrange(1,min(n,mss)+1):
      count += piles(n-i,min(n-i,i))
  #print "piles (",n,mss,") = ",count
  return count

# Check our fn before proceeding.
assert piles(5,5) == 7

i = 0
while True:
  i += 1
  p = piles(i,i)
  print i, p #, list(factorize(p))
  if p % 1000000 == 0:
    print "======"
    print i, p
    break
  if i == 500:
    break

