# Code that is reused across multiple scripts

################
# MEMOIZATION  #
################
# 14.py is a good testcase for comparing memoization versions.
# works, but really slow compared to hand-done memoization because of pickling.
# http://pko.ch/2008/08/22/memoization-in-python-easier-than-what-it-should-be/
import functools
try:
  import cPickle
  def memoize(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(*args,**kwargs):
                haxh = cPickle.dumps((args, sorted(kwargs.iteritems())))
                if haxh not in memory:
                        memory[haxh] = fctn(*args,**kwargs)
                return memory[haxh]
        if memo.__doc__:
            memo.__doc__ = "\n".join([memo.__doc__,"This function is memoized."])
        return memo
except ImportError:
  pass

def memoize_fast_args_only(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(*args):
                haxh = args
                if haxh not in memory:
                        memory[haxh] = fctn(*args)
                return memory[haxh]
        return memo
 
# Still not exactly as fast as hand-done implementation, probably because of the function wrapping overhead, but much closer than above.
def memoize_fast_1_arg(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(a):
            haxh = a
            if haxh in memory:
              return memory[haxh]
            else :
              result       = fctn(a)
              memory[haxh] = result
              return result
        return memo
 

################
# PERMUTATIONS #
################

# This is a generator for permutations. Works with a list or a string.
# assumes l is already sorted : easy to do once before the top gen_prem call.
# So, going left to right is equivalent to lex order, and no sorting is needed.
def gen_perm(l):
  ls = l
  ll = len(ls)
  if ll == 1:
    yield l
    return
  for i in xrange(ll): 
    a = l[i:i+1]
    b = l[0:i] + l[i+1:ll]
    g = gen_perm(b)
    for p in g:
      yield a + p
  return

################
# PRIMES       #
################

# Using lists
# Should rewrite using BitArray if I can find it installed.
# from bitstring import BitArray
def seive_of_E(n):
  l = [0,0]+([1]*(n-2))		    # All numbers >=2  are prime-candidates
  p = 2				    # start from 2
  while (p*p < n):		    # Any composite number < n should have one factor < sqrt(n) 
    for m in xrange(2*p,n,p):	    # Mark all multiples of the current prime as composite.
      l[m] = 0
    p = p + 1 + l[p+1:].index(1)    # next prime
  return l

#N = 1000000
#is_prime = seive_of_E(N)

# Straight from the discussion of problem 7.
# Definition of is_prime for n<=0 is bit unclear, but false is convenient here.
import math
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

def prime_factor_candidates(n) :
    if (n <= 1):
        return
    yield 2
    if (n <= 2):
        return
    for i in range(3,n+1,2):
        yield i
    return
              
def factorize(n):
    if (n > 3):
        top = int(min(n, int(math.sqrt(n))) + 1)
        p = prime_factor_candidates(top)
        for i in p:
            count = 0
            while (n % i == 0):
                count += 1
                n = int(n/i)
            if (count > 0) :
                yield (i,count)
        if (n != 1):    
            yield (n,1)
    else :
        yield (n,1)

########
# MISC #
########

# To test if different numbers have the same digits.
def sorted_digits(n):
  return int("".join(sorted(list(str(n)))))

