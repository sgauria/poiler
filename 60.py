from poiler_common import *
import itertools

def join_numbers(n1,n2):
  return int(str(n1)+str(n2))

assert (join_numbers(55,66) == 5566)

NN = [1000]
M = 4

for N in NN:
  is_prime = seive_of_E(N)
  lprimes  = [n for (n,is_p) in enumerate(is_prime) if is_p == 1]
  is_prime = seive_of_E(N*N)
  for c in itertools.combinations(lprimes, M):
    remarkable = 1
    for (n1,n2) in itertools.permutations(c,2):
      j = join_numbers(n1,n2)
      if not is_prime[j]:
        remarkable = 0
        break
    if remarkable == 1:
      print sum(c), c




