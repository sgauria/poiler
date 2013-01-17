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

N = 100

# cfl_e = continued fraction list for 'e'
cfl_e = [0]*N
for i in range(N):
  if i == 0:
    val = 2
  elif i%3 == 2:
    val = ((i+1)/3)*2
  else :
    val = 1
  cfl_e[i] = val

# numerator and denominator lists.
nrl_e = [0]*N
drl_e = [0]*N

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

for i in range(N):
  calculate_nth_convergent(cfl_e, nrl_e, drl_e, i)
  #print nrl_e[i] ,"/", drl_e[i] , (1.0 * nrl_e[i] / drl_e[i])

print sum_of_digits(nrl_e[N-1])

