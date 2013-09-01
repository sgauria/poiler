import math

# Doesn't work because of precision issues.
def solve_D(D):
  """ Solve x^2 - Dy^2 = 1 """
  sdr = math.sqrt(D)
  sdi = int(sdr)
  if sdi == sdr :
    return None
  y = 1
  while True :
    xr = math.sqrt(y*y*D+1)
    xi = int(xr)
    if xr == xi :
      return xi
    y += 1

assert (solve_D(13) == 649)    

maxx = maxd = 0;

N = 1000

for d in range(1,N+1):
  x = solve_D(d)
  print d, x
  if x > maxx:
    maxx = x
    maxd = d

print "========="
print maxd
