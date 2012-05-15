# lpns = list of pentagonal numbers
# spns = set  of pentagonal numbers
# We store the same info 2 ways : list and set
# List allows us to compute the numbers only once.
# Set  allows us to test membership quickly.
#
# We search in order of increasing sum of indices.

s = 1 # sum
lpns = [0]
spns = set()
while True :
  for x in [2*s-1, 2*s]:
    y = x*(3*x-1)/2
    lpns.append(y)
    spns.add(y)
  for a in xrange(1,s/2):
    b = s - a 
    pa = lpns[a]
    pb = lpns[b]
    if (pb - pa) in spns and (pb + pa) in spns:
      print "P(",a,") =", pa
      print "P(",b,") =", pb
      print " P(",a,") + P(",b,")  =", pb+pa, " = P(",lpns.index(pb+pa),")"
      print "|P(",a,") - P(",b,")| =", pb-pa, " = P(",lpns.index(pb-pa),")"
      exit(0)
  s += 1

