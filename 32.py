import math

# We can work through all combinations to figure out that the product must be 4 digits.
# 1 * 1 = 7 : not possible
# 1 * 2 = 6 : not possible
# 1 * 3 = 5 : not possible
# 2 * 2 = 5 : not possible
# 1 * 4 = 4 :     possible
# 3 * 2 = 4 :     possible
# 1 * 5 = 3 : not possible
# 2 * 4 = 3 : not possible
# 3 * 3 = 3 : not possible

def is_1to9_pandigital(a,b,c):
  bitmask = 0
  for w in [a,b,c]:
    x = w
    while x > 0:
      digit = x%10
      x = int(x / 10)
      bitmask |= (1 << digit)
  return (bitmask == 0x3fe)

def digits_are_distinct(a):
  bitmask = 0
  x = a
  while x > 0:
    digit = x%10
    x = int(x / 10)
    if ((bitmask >> digit) & 0x1):
      return False
    bitmask |= (1 << digit)
  return True

pdps = set()
for i in xrange(1000,10000):
  if (digits_are_distinct(i)):
    top = int(min(i, int(math.sqrt(i))) + 1)
    for j in xrange(2,top):
      if (i % j == 0):
	k = i/j
	if (is_1to9_pandigital(j,k,i)):
	  print j,k,i
	  pdps.add(i)

#print pdps
print sum(pdps)
