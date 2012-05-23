import sys
from poiler_common import *

if len (sys.argv) >= 2:
  N = int(sys.argv[1])
else :
  N = 1000000

is_prime = seive_of_E(N)
#print "is_prime ready"

primes = []
for i in xrange(N):
  if is_prime[i]:
    primes.append(i)
lp = len(primes)
#print "primes ready"

pmax = imax = szmax = 0
for sz in xrange(2,lp):
  for i in xrange(0,lp+1-sz):
    pc = sum(primes[i:i+sz])
    if pc >= N :
	break # Larger i's will only exceed N by more.
    elif is_prime[pc]:
      pmax = pc
      imax = i
      szmax = sz
  if (i == 0) :
    break # When sum(primes[0:sz] > N), any larger sz,i combination will also be too big. So, stop.

print pmax
print szmax, ":", primes[imax:imax+szmax]
