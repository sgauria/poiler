N = 2000
pns = [n*(3*n-1)/2 for n in xrange(1,N+1)]
print "pns calculated."

for step in xrange(1,N/2):
  print "step=",step
  for i in xrange(N/2):
    j = i + step
    if j < N:
      #if (pns[i]+pns[j]) in pns and (pns[j]-pns[i]) in pns:
      if (pns[i]+pns[j]) in pns:
	print pns[i], pns[j]
	exit(0)

# Unfinished code.
