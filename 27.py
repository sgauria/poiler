import math

# Straight from the discussion of problem 7.
# Definition of is_prime for n<=0 is bit unclear, but false is convenient here.
def is_prime(n) :
    if (n <= 1) :  
      return False
    if (n < 4) :
      return True
    if ((n % 2) == 0) :
      return False
    if (n < 9) :
      return True
    if ((n % 3) == 0) :
      return False
    top = int(math.sqrt(n)+1)
    for f in xrange(5,top,6):
        if ((n % f) == 0) :
            return False
        if ((n % (f+2)) == 0) :
            return False
    return True

maxcount = 0
maxa = maxb = 5000

# b must be positive and prime for f(0) to be prime.
for b in xrange(1,1000,2):
  if (is_prime(b)): 
    for a in xrange(-b,1000): # We want f to always be +ve
      n = 1
      while True :
	f = n*n + a*n + b
	if (is_prime(f)):
	  n += 1
	else :
	  break
      if (n > maxcount):
	maxcount = n+1
	maxa = a
	maxb = b
        #print maxcount, maxa, maxb, (maxa*maxb)


print maxcount, maxa, maxb, (maxa*maxb)

#n = 0
#while True :
#  f = n*n + maxa*n + maxb
#  if (is_prime(f)):
#    print f
#    n += 1
#  else :
#    break
