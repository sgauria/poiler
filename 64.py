from math import *
import re

# From : http://mathworld.wolfram.com/ContinuedFraction.html
# Writing the remainders according to the recurrence relation
# r_0 = x 
# r_n = 1/(r_(n-1)-a_(n-1)) 
# 
# gives the concise formula
# a_n=|_ r_n _|.  

# From http://mathworld.wolfram.com/PellEquation.html
#  Amazingly, this turns out to always be possible as a result of the fact that the continued fraction of a quadratic surd always becomes periodic at some term a_(r+1), where a_(r+1)=2a_0
def real_to_continued(x):
  c = []
  r = x
  stop = 0
  while not stop :
    a = int(floor(r))
    r = 1 / (r - a)
    c.append(a) 
    if a == 2*c[0] :
      stop = 1
  return c

for n in [1.414, sqrt(2), sqrt(23)] :
  print n, real_to_continued(n)

def evalrepl(matchobj):
  expr = matchobj.group(0)
  subst = str(eval(expr))
  return subst

# Apply some common transformations to reduce this expression as much as possible.
def reduce_expr(expr, n=5):
  e = expr
  for i in xrange(n):
    e = re.sub(r"sqrt\(([^)]+)\)\*sqrt\(\1\)", r"\1", e)
    e = re.sub(r"\d+\*\d+"   , evalrepl, e)
    e = re.sub(r"\(\d+-\d+\)", evalrepl, e)
    e = re.sub(r"([^*])\*1", r"\1", e)
    e = re.sub(r"1\*([^*])", r"\1", e)

  return e

def sqrt_n_to_continued(n):
  sqn = sqrt(n) 
  if (int(sqn) == sqn) :
    return [int(sqn)]
  c = []
  sqns = "sqrt({n})".format(n=n)
  rn,rd = sqns,"1"
  while True :
    rs = "("+rn+")/("+rd+")"
    print "\n", len(rs), "\n"
    r = eval (rs)
    a = int(floor(r))
    c.append(a) 
    #r = 1 / (r - a)
    #r = 1 / (rn/rd - a)
    #r = (rn/rd + a) / (rn*rn/rd*rd - a*a)
    #r = (rn*rd + a*rd*rd) / (rn*rn - a*a*rd*rd)
    rn1 = "({rn}*{rd}+{a}*{rd}*{rd})".format(rn=rn, rd=rd, a=a)
    rd1 = "({rn}*{rn}-{a}*{a}*{rd}*{rd})".format(rn=rn, rd=rd, a=a)
    rnr = reduce_expr(rn1)
    rdr = reduce_expr(rd1)
    rn, rd = rnr, rdr
    if a == 2*c[0]:
      break
  return c

for n in [2, 3,4, 5,6,7, 43]:
  print n, sqrt_n_to_continued(n)


#N = 13
N = 10000
odd_period_count = 0
for n in range(1,N+1):
  c = sqrt_n_to_continued(n)
  print n,c
  period = len(c) - 1
  if period > 0 and period % 2 == 1:
    odd_period_count += 1

print "=========="
print odd_period_count

  

