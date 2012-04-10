# Simple implementations to get a feel for the problem.

lcm_cache = {}

def lcm(a,b):
  global lcm_cache
  if (a,b) in lcm_cache:
    return lcm_cache[(a,b)]
  m = max(a,b)
  while (m % a != 0 or m % b != 0)):
    m += 1
  lcm_cache[(a,b)] = m
  return m
#print lcm(2,3)
#print lcm(12,18)



def fn_f(n):
  count = 0
  for x in xrange(1,n+1):
    for y in xrange(x,n+1):
      if (lcm(x,y) == n):
	count += 1
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
    print i, sum
  return sum
print fn_g(100) # 647
#print fn_g(1000)

