import math
import re

our_sq = re.compile('1.2.3.4.5.6.7.8.9.0')

n1 = int( math.floor( math.sqrt( 1020304050607080900 )))
n2 = int( math.ceil ( math.sqrt( 1929394959697989990 )))
print n1,n2

# The square must end in 00, i.e. be a multiple of 100, so n must be a multiple of 10
n_lo = n1 - (n1 %10) 

for n in xrange(n_lo, n2, 10):
  #print n, "\r",
  nsq = n * n 
  if our_sq.match( str(nsq)) :
    print "\n******"
    print n, nsq
    break
  

