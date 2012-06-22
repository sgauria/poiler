import random

def one_i() :
  """Run one instance of the expt and return the value of i"""
  T = C = O = D = I = 0 
  T = random.randint(1,4)
  for ii in xrange(T):
    C += random.randint(1,6)
  for ii in xrange(C):
    O += random.randint(1,8)
  for ii in xrange(O):
    D += random.randint(1,12)
  for ii in xrange(D):
    I += random.randint(1,20)
  return I


N = 1000
list_i = [one_i() for ii in xrange(N)]

mean = (1.0*sum(list_i)/N)
variance = 0
for ii in list_i:
  variance += (ii - mean)**2
variance /= N

print mean, variance

# A hacky script that so far just verifies that running a few samples is not sufficient to solve this problem.
