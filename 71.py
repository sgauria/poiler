# This code should solve problems 71 and 73
from __future__ import division
from poiler_common import memoize_fast_args_only, hcf, seive_of_E
import math

def tuple_to_fraction (x) :
  return x[0] / x[1]

# tried many variations, but this seems to be one of the fastest.
def generate_reduced_proper_fractions(max_denonimator, min_frac=0, max_frac=1):
  fracs = []
  for d in xrange(2,max_denonimator+1):
    min_n = max(1, int(min_frac*d))
    max_n = min(d, int(math.ceil(max_frac*d+1)))
    for n in xrange(min_n, max_n):
      value = n/d
      if min_frac <= value <= max_frac:
	if hcf(n,d) == 1:
	  fracs.append( (n,d) )
      if value > max_frac :
	break
  fracs.sort(key=tuple_to_fraction)
  return fracs

assert generate_reduced_proper_fractions(8) == [(1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (2, 7), (1, 3), (3, 8), (2, 5), (3, 7), (1, 2), (4, 7), (3, 5), (5, 8), (2, 3), (5, 7), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
assert generate_reduced_proper_fractions(8, 2/7, 3/8) == [(2, 7), (1, 3), (3, 8)]

# 71
# To keep runtime in check, generate fractions in a smaller range for values for larger N.
# Get the range from the previous run of generate_reduced_proper_fractions
# Increase N by factors of 10
N = 1000000
N2, minf, maxf = 10, 0, 3/7
while N2 <= N:
  #print N2, ":", minf, " -", maxf
  fracs_71 = generate_reduced_proper_fractions(N2, minf, maxf)
  minf = tuple_to_fraction(fracs_71[-2])
  N2 = N2 * 10

#print fracs_71[-2]
print "Solution to Problem 71 = ", fracs_71[-2][0]



#73
N = 12000
fracs_73 = generate_reduced_proper_fractions(N, 1/3, 1/2)
print "Solution to Problem 73 = ", len(fracs_73) - 2
