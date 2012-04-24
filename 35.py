def seive_of_E(n):
  l = [1]*n # All numbers >=2  are prime-candidates
  l[0] = l[1] = 0
  p = 2 # start from 2
  while (p*p < n):
    #print l
    #print p
    m = 2*p
    while (m < n):
      l[m] = 0
      m += p 
    p = p + 1 + l[p+1:].index(1)
  return l


#print seive_of_E(1000)

N = 1000000
is_prime = seive_of_E(N)
#print is_prime.count(1)

lprimes = []
for i in xrange(N):
  if (is_prime[i]):
    lprimes.append(i)

ccount = 0
for p in lprimes:
  circular = True
  sp = str(p)
  for r in range(1,len(sp)):
    nsp = sp[r:] + sp[:r]
    if not is_prime[int(nsp)]:
      circular = False
      break
  if circular == True:
    print p
    ccount += 1

print "====="
print ccount
