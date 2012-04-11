# Simple implementations to get a feel for the problem.

#lcm_cache = {}

def lcm(a,b):
  #global lcm_cache
  #if (a,b) in lcm_cache:
    #return lcm_cache[(a,b)]
  m = max(a,b)
  while (m % a != 0 or m % b != 0):
    m += 1
  #lcm_cache[(a,b)] = m
  return m
#print lcm(2,3)
#print lcm(12,18)



def fn_f(n):
  count = 0
  for x in xrange(1,n+1):
    for y in xrange(x,n+1):
      if (lcm(x,y) == n):
	count += 1
	#print x,y
  return count
#print fn_f(1)
#print fn_f(2)
#print fn_f(3)
#print fn_f(6)
#print fn_f(16)



def fn_g(n):
  sum = 0
  for i in xrange(1,n+1):
    sum += fn_f(i)
    #print i, sum
  return sum

#print fn_g(100) # 647
#print fn_g(1000)
#print "====" 



def fn_g_direct(n):
  count  = n # all the (a,a) points are included
  for x in xrange(1,int((n/2)+1)):
    #s = " "*x
    for y in xrange(x+1,n+1):
      if (x*y <= n) :
	count += 1
	#print x,y
	#s += "#"
      elif lcm(x,y) <= n:
	count += 1
	#print x,y
	#s += "#"
      #else :
	#s += " "
    #print s
  return count

#print fn_g_direct(50)
#print fn_g_direct(100) # 647
#print fn_g_direct(1000)
#print "====" 

for i in xrange(50):
  print i, fn_g_direct(i)

# NOTES :
#  Could calculate f directly based on factorizing the input to f and then :
#    - assuming factorization is p1^a1 ... pk^ak
#    - total number of x,y pairs is (a1+1)*...*(ak+2)*2^(k-1)
#  But I think even that's going to be insufficient.
# 
#  Looking at the diagram of g based on the printouts in fn_g_direct, it's probably possible
#  to come up with some kind of closed form formula for g (or at least each row or col of g directly.
#  Still need to figure it out exactly.
