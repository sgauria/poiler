N = 2000
pns = [n*(3*n-1)/2 for n in xrange(1,2*N+1)] 
print "pns calculated."
#print pns

s = 1 # sum
while True :
  for x in [2*(s-1), 2*(s-1)+1]:
    pns.append(x*(3*x-1)/2)
  print "sum=",s
  for a in xrange(1,s/2):
    b = s - a 
    pa = pns[a]
    pb = pns[b]
    if (pb - pa) in pns and (pb + pa) in pns:
      print pa, pb
      exit(0)
  s += 1

# Unfinished code.
