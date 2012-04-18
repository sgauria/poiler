from poiler_common import *
#cache = {}

@memoize_fast_1_arg
def count_steps(n):
  #global cache
  #print "cs", n
  #if (n in cache):
  #  s = cache[n]
  if n == 1:
    s = 1
  elif (n % 2 == 0):
    s = (1 + count_steps(n/2))
  else :
    s = (1 + count_steps((3*n) + 1))
  #cache[n] = s
  return s

N = 1000000

maxlen = 0
maxnum = 0
for i in xrange(1,N) :
  #print "start", i
  len = count_steps(i)
  #print "end", i, len
  if (len > maxlen) :
    maxlen = len
    maxnum = i

print maxnum, maxlen
