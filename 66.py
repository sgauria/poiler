import math

def solve_D(D):
  """ Solve x^2 - Dy^2 = 1 """
  sdr = math.sqrt(d)
  sdi = int(sdr)
  if sdi == sdr :
    return -1
  print d
  y = 1
  while True :
    xr = math.sqrt(y*y*D+1)
    #print y, xr
    xi = int(xr)
    if xr == xi :
      return xi
    y += 1

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
