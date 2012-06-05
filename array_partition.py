# Hao-Ju's problem.
# Given an array : find the optimal partition of the array into 2 arrays such that the sums of the arrays are as close as possible.
# Extra-credit : how do you do an approximate but fast solution to the problem.

def array_partition(x):
  a = x
  a.sort()
  a.reverse()
  b = []
  c = []
  rsb = rsc = 0 # running sums
  for i in a:
    if (rsb < rsc):
      b.append(i)
      rsb += i
    else :
      c.append(i)
      rsc += i
  return (b,c)
# Seems to do a good job, but results are not optimal.


import random
N = 10
x = []
for i in range(N):
  x.append(random.randint(0,5000))

y,z = array_partition(x)

for i in x,y,z:
  print len(i), sum(i), i
  print "\n"

