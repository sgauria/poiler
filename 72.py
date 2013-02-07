import sys

if len (sys.argv) >= 2:
  N = int(sys.argv[1])
else :
  N = 1000000

# Number of fractions with each denominator.
fracs_72 = [0,0] + range(1,N)
#print fracs_72

# Go up the denominator list and cancel out all the multiples of each proper fraction.
# Since we are moving up, duplicates are already taken care of.
for i in range(2,N):
  num_frac_i = fracs_72[i]
  for j in range(2*i, N+1, i):
    fracs_72[j] -= num_frac_i

#print fracs_72
print sum(fracs_72)
