from poiler_common import memoize_fast_args_only

@memoize_fast_args_only
def piles(n,mss):
  """ n is the number of coins. mss is the max subset(pile) size"""
  count = 0
  if n <= 1:
    count = 1
  elif mss == 1:
    count = 1
  else :
    for i in xrange(1,min(n,mss)+1):
      count += piles(n-i,min(n-i,i))
  #print "piles (",n,mss,") = ",count
  return count

#print piles(5,5)

#for i in range(20):
#  print i,piles(i,i)

i = 1
while True:
  p = piles(i,i)
  if p % 10 == 0:
    print i, p
    if p % 1000000 == 0:
      print "======"
      print i, p
      break
  i += 1
  #if i == 500:
  #  break

