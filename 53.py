from poiler_common import *

#find the number of (n,r) pairs (n<=100) such that number of combinations nCr is > 1000000

count = 0
for n in range(1,101):
  for r in range(0,n+1):
    if nCr(n,r) > 1000000:
      count += 1

print count

