from math import sqrt, ceil, floor

root2 = sqrt(2)

# n total discs
# b  blue discs
# Probability is b/n * b-1/n-1
# Since b/n > b-1/n-1, and both must be pretty close to 1/root2 :
# b must be ceil(n / root2)

b = 2
bp=np=1

print "%15s %15s %15s %15s"%("blue", "total", "blue ratio", "total ratio")
while True :
  n = int(floor(b*root2))
  if (2*b*(b-1)) == (n*(n-1)):
    print "%15d %15d %15.10f %15.10f"%(b, n, (1.0*b/bp), (1.0*n/np))
    if n > 1000000000000:
      break 
    # The solution seem to form a geometric-ish series. No idea why.
    # While converging, the ratio does increase with every step, so we can be sure we are not overshooting.
    bjump = b*b/bp 
    bp = b
    np = n
    b  = bjump
  b += 1
