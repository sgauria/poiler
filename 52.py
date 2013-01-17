from poiler_common import *

N = 0
done = False
while not done:
  N += 1
  N_digits = sorted_digits(N)
  for i in [2,3,4,5,6]:
    Ni = N*i
    Ni_digits = sorted_digits(Ni)
    if Ni_digits != N_digits:
      break
    elif i == 6:
      done = True

print N
