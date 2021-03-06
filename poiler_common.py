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
@memoize_fast_1_arg
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

def digits(n):
  #return map(int, list(str(n)))
  r = []
  x = n
  while x > 0:
    x, digit = divmod(x, 10)
    r.append(digit)
  return r


# To test if different numbers have the same digits.
def sorted_digits(n):
  return "".join(sorted(list(str(n))))

# nCr : number of possible combinations of r things selected from a set of n things.
def nCr(n,r):
  assert (0 <= r <= n)
  lr = r if (r > (n-r)) else (n-r) # larger of r and n-r
  result = 1
  for i in range(lr+1,n+1):
    result *= i
  for i in range(1,(n-lr)+1):
    result /= i
  return result

def digital_sum(n):
  sum = 0
  for d in str(n):
    sum += int(d)
  return sum

sum_of_digits = digital_sum
digit_sum     = digital_sum

# The neat thing about this code is that I am not converting to strings anywhere to check palindrome-ness.
def reverse_num(num,base=10):
   nn = num
   rn = 0
   while (nn > 0) :
       digit = nn % base 
       nn = (nn - digit) / base
       rn = rn*base + digit
   return rn

def num_is_palindrome(num,base=10):
   rn = reverse_num(num,base)
   if (rn == num) :
       return True
   else :
       return False

def all_subsets(myset, min_size=1, max_size=float('Inf')):
  if max_size > len(myset):
    max_size = len(myset)
  for l in range(min_size, max_size+1):
    for c in itertools.combinations(myset, l):
      yield c

@memoize_fast_args_only
def hcf(n1,n2):
  """ Calculate Highest common factor of n1 and n2. n1 must be less than n2."""
  assert n1 < n2

  q,r = divmod(n2,n1)
  #print n1, n2, q, r
  if r == 0:
    return n1
  else :
    return hcf(r,n1)

assert hcf(64,72) == 8

#                      0 1 2 3  4   5   6    7     8      9
first_10_factorials = [1,1,2,6,24,120,720,5040,40320,362880]
@memoize_fast_1_arg
def sum_of_factorials(n):
  if (n < 10):
    return first_10_factorials[n]
  else :
    return (first_10_factorials[n%10] + sum_of_factorials(int(n/10)))


