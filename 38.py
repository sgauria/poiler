def is_1to9_pandigital(n):
  bitmask = 0
  x = n
  while x > 0:
    digit = x%10
    x = int(x / 10)
    bitmask |= (1 << digit)
  return (bitmask == 0x3fe)

pds = set()

for i in xrange(1,100000):
  s = ""
  n = 1
  while len(s) < 9:
    p = i * n
    s += str(p)
    n += 1
  if (len(s) == 9):
    si = int(s)
    if (is_1to9_pandigital(si)):
      pds.add(si)
      #print i, si

print max(pds)
