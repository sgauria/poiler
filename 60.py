from poiler_common import *
import itertools

def join_numbers(n1,n2):
  return int(str(n1)+str(n2))

assert (join_numbers(55,66) == 5566)

NN = [1000]
MM = 4

if 0 :
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
  # - First 2 results are : 792 (3, 7, 109, 673) ;  1838 (23, 677, 311, 827)

  # N = 3000 , M = 5
  # - even the search of all 4 pairs had not completed in 2246 seconds.

if 0 :
  MM = 5
  
  # Leave out 2 & 5 from list of primes to test as they are trivially incompatible with all other primes (x2, x5 are composite).
  lprimes   = set([3]) # list of primes smaller than the prime under consideration.
  allprimes = set([2,3,5]) # all primes we found, smaller or larger.
  nonprimes = set([4])
  
  prime_candidate = 5
  while (prime_candidate < 10000000) : # True :
    prime_candidate += 2
    if is_prime(prime_candidate):
      #print prime_candidate
      for cc in [ (3, 7, 109, 673) , (23,677,311,827) ]: #itertools.combinations(lprimes, MM-1):
        c = list(cc)
        c.append(prime_candidate)
        remarkable = 1
        for (n1,n2) in itertools.permutations(c,2):
          j = join_numbers(n1,n2)
          if j in nonprimes:
              remarkable = 0
              break
          elif (j not in allprimes):
            if not is_prime(j):
              nonprimes.add(j)
              remarkable = 0
              break
            else :
              allprimes.add(j)
        if remarkable == 1:
          print "*********"
          print sum(c), c
          exit(0)
      lprimes.add(prime_candidate)
      allprimes.add(prime_candidate)
    else :
      nonprimes.add(prime_candidate)
  
  # 50 s for smallest 'remarkable' set of size 4.
  # size 5 - searched till pc = 1327 in 16184s. No result.
  # tried primes till 10 million, but none of them work with (3,7,109,673) & (23,677,311,827)

if 0:
  MM = 5

  # Leave out 2 & 5 from list of primes to test as they are trivially incompatible with all other primes (x2, x5 are composite).
  lprimes = [3]
  compatible = {3 : {}}
  
  pc = 5 # prime_candidate
  while (pc < 10000000) : # True :
    pc += 2
    if is_prime(pc):
      print pc
      compatible[pc] = {}
      for p in lprimes :
        j1 = join_numbers(p, pc)
        j2 = join_numbers(pc, p)
        j1p = is_prime(j1)
        j2p = is_prime(j2)
        if j1p and j2p:
          compatible[p][pc] = True
          compatible[pc][p] = True
        else :
          compatible[p][pc] = False
          compatible[pc][p] = False
      for c in itertools.combinations(lprimes, MM-1):
        remarkable = 1
        for n1 in c :
          if not compatible[n1][pc]:
            remarkable = 0
            break
        if remarkable == 1:
          for (n1,n2) in itertools.permutations(c,2):
            if not compatible[n1][n2]:
              remarkable = 0
              break
        if remarkable == 1:
          print "*********"
          cc = list(c); cc.append(pc)
          print sum(cc), cc
          exit(0)
      lprimes.append(pc)
      #print "\r",
  # 5 s for smallest 'remarkable' set of size 4.
  # set of size 5 not found overnight.

if 1:
  # Leave out 2 & 5 from list of primes to test as they are trivially incompatible with all other primes (x2, x5 are composite).
  lprimes = [3]
  compatible = {3 : {3: False}}
  
  pc = 5 # pc = prime_candidate
  while (pc < 10000000) : # True :
    pc += 2
    if is_prime(pc):
      #print pc, "\r",
      compatible[pc] = {}
      compatible[pc][pc] = False # Any prime concatenated with itself is a multiple of 10*1
      for p in lprimes :
        j1 = join_numbers(p, pc)
        j2 = join_numbers(pc, p)
        j1p = is_prime(j1)
        j2p = is_prime(j2)
        if j1p and j2p:
          compatible[p][pc] = True
          compatible[pc][p] = True
        else :
          compatible[p][pc] = False
          compatible[pc][p] = False
      for p1 in compatible[pc] :
        if compatible[pc][p1] :
          for p2 in compatible[p1]:
            if compatible[p2][pc] and compatible[p1][p2]:
              for p3 in compatible[p2]:
                if compatible[p3][pc] and compatible[p1][p3] and compatible[p2][p3]:
                  for p4 in compatible[p3]:
                    if compatible[p4][pc] and compatible[p1][p4] and compatible[p2][p4] and compatible[p3][p4]:
                      print "*********"
                      cc = sorted(list((pc,p1,p2,p3,p4)))
                      print sum(cc), cc
                      exit(0)
      lprimes.append(pc)
  # 0.2 s for set of size 4 with this approach (needs code edit)
  # set of size 5 found in 37s : 26033 [13, 5197, 5701, 6733, 8389]


