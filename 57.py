# Copied from 65.py
from poiler_common import *

#Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

# From wikipedia :
#  For a continued fraction [a0; a1, a2, ]
#  If successive convergents are found, with numerators h1, h2, ... and denominators k1, k2, ... then the relevant recursive relation is:
#    h_n = a_n*h_(n-1) + h_(n-2)
#    k_n = a_n*k_(n-1) + k_(n-2)
#  with
#    h_(-1) = 1 ; k_(-1) = 0
#    h_(-2) = 0 ; k_(-2) = 1

N = 1000

# cfl_r2 = continued fraction list for 'root 2'
cfl_r2 = [2]*N
cfl_r2.insert(0,1)

# numerator and denominator lists.
nrl_r2 = [0]*N
drl_r2 = [0]*N

def calculate_nth_convergent(cfl, nrl, drl, n):
  h_extra = [0,1]
  k_extra = [1,0]
  h_nm1 = nrl[n-1] if (n>=1) else h_extra[n-1]
  h_nm2 = nrl[n-2] if (n>=2) else h_extra[n-2]
  k_nm1 = drl[n-1] if (n>=1) else k_extra[n-1]
  k_nm2 = drl[n-2] if (n>=2) else k_extra[n-2]

  a_n = cfl[n]
  #print a_n, ":", h_nm1, "/", k_nm1, ":", h_nm2, "/", k_nm2
  h_n = a_n*h_nm1 + h_nm2
  k_n = a_n*k_nm1 + k_nm2
  nrl[n] = h_n
  drl[n] = k_n

count_more_digits = 0
for i in range(N):
  calculate_nth_convergent(cfl_r2, nrl_r2, drl_r2, i)
  #print nrl_r2[i] ,"/", drl_r2[i] , (1.0 * nrl_r2[i] / drl_r2[i])
  if len(str(nrl_r2[i])) > len(str(drl_r2[i])):
    count_more_digits += 1

#print sum_of_digits(nrl_r2[N-1])
print count_more_digits

