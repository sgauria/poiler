from math import sqrt, ceil, floor

root2 = sqrt(2)

# n total discs
# b  blue discs
# Probability is b/n * b-1/n-1
# Since b/n > b-1/n-1, and both must be pretty close to 1/root2 :
# b must be ceil(n / root2)

b = 2
bp=np=1

print "blue,\tred,\ttotal"
while True :
  n = int(floor(b*root2))
  if (2*b*(b-1)) == (n*(n-1)):
    print b, n, (1.0*b/bp), (1.0*n/np)
    bp = b
    np = n
    if n > 1000000:
      break 
  b += 1
