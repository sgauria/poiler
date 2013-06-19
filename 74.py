from poiler_common import *

#            0 1 2 3  4   5   6    7     8      9
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

@memoize_fast_1_arg
def sum_of_factorials(n):
  if (n < 10):
    return factorial[n]
  else :
    return (factorial[n%10] + sum_of_factorials(int(n/10)))


def chain_length (n):
  x = n
  chain = [x]
  while True :
    x = sum_of_factorials(x)
    if x in chain :
      break
    else :
      chain.append(x)
  #print chain
  return len(chain)

# @memoize_fast_1_arg
def chain_length_recursive (n, chain):
  if n in chain :
    l = len(chain)
    return l
  else :
    chain.append(n)
    x = sum_of_factorials(n)
    clr = chain_length_recursive(x, chain)
    return clr

assert (chain_length(3) == 16)
assert (chain_length_recursive(3, []) == 16)
#exit(0)

# Search till 1 million
N = 1000000
count = 0

for i in xrange(1,N):
  l = chain_length(i)
  if l == 60 :
    count += 1
    print i

print "==========="
print count


