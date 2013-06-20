from poiler_common import *

def chain_length (n):
  x = n
  chain = [x]
  while True :
    x = sum_of_factorials(x)
    if x in chain :
      break
    else :
      chain.append(x)
  return len(chain)

# Manuals memoization. Need to fill in the loops manually beforehand. Runs really fast after that.
known_lengths = {
    1      : 1,
    2      : 1,
    145    : 1,
    40585  : 1,

    871    : 2,
    45361  : 2,

    872    : 2,
    45362  : 2,

    169    : 3,
    363601 : 3,
    1454   : 3,

    }

def chain_length_recursive (n):
  if n in known_lengths :
    l = known_lengths[n]
    return l
  else :
    x = sum_of_factorials(n)
    if (x == n):
      clr = 1
    else :
      clr = chain_length_recursive(x) + 1
    known_lengths[n] = clr
    return clr

assert (chain_length          (3) == 16)
assert (chain_length_recursive(3) == 16)
assert (chain_length          (4) == 8)
assert (chain_length_recursive(4) == 8)

# Search till 1 million
N = 1000000
count = 0

for i in xrange(1,N):
  l = chain_length_recursive(i)
  if l == 60 :
    count += 1
    print "*", i

print "==========="
print "count = ", count


