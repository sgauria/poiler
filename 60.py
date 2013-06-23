from poiler_common import *
import itertools

def join_numbers(n1,n2):
  return int(str(n1)+str(n2))

assert (join_numbers(55,66) == 5566)

NN = [3000]
MM = 5

for N in NN:
  is_prime = seive_of_E(N)
  lprimes  = [n for (n,is_p) in enumerate(is_prime) if is_p == 1]
  is_prime = seive_of_E(join_numbers(N,N))
  for M in range(2,MM+1):
    print "*", M, len(lprimes)
    lprimes_nxt = []
    for c in itertools.combinations(lprimes, M):
      remarkable = 1
      for (n1,n2) in itertools.permutations(c,2):
        j = join_numbers(n1,n2)
        if not is_prime[j]:
          remarkable = 0
          break
      if remarkable == 1:
        lprimes_nxt.extend(c)
        if M == MM :
          print sum(c), c
    lprimes = list(set(lprimes_nxt))




# Notes 
# N = 1000
# - Just searching all 168 primes for sets of length 4 takes 105 secs.
# - Searching incrementally (first sets of l=2, then l=3, then l=4) takes 80s. even though it only reduces the search for l=4 from 168 to 156 primes.
# - Searching till l = 5 also takes only 80s
# N = 3000 , M = 5
# - even the search of all 4 pairs had not completed in 2246 seconds.
