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

#for n in [1.414, sqrt(2), sqrt(23)] :
#  print n, real_to_continued(n)

def evalrepl(matchobj):
  expr = matchobj.group(0)
  subst = str(eval(expr))
  return subst

import string
def switchsigns(matchobj):
  expr = matchobj.group(0)
  e2 = expr[1:]
  subst = e2.translate(string.maketrans("+-", "-+"), "()")
  return expr[0]+subst

# Apply some common transformations to reduce this expression as much as possible.
def simplify_expression(expr, sub_map = {}):
  esave = e = expr

  while True :
    e = re.sub(r"\d+[*/]\d+",                  evalrepl, e)  # eval multiplication / division
    e = re.sub(r"\(\d+[+-]\d+\)",              evalrepl, e)  # eval subtraction / addition
    e = re.sub(r"\(\(([^()]+)\)\)",             r"(\1)", e)  # Remove duplicate brackets
    e = re.sub(r"([^*])\*1\b",                    r"\1", e)  # Trivial multiplication by 1.
    e = re.sub(r"\b1\*([^*])",                    r"\1", e)  # Trivial multiplication by 1.
    e = re.sub(r"\((\d+|[a-zA-Z])\)",             r"\1", e)  # Remove redundant brackets (around a single term).
    e = re.sub(r"sqrt\(([^)]+)\)\*sqrt\(\1\)",    r"\1", e)  # sqrt(x)*sqrt(x) = x
    e = re.sub(r"(\d+|[a-zA-Z])([*/])\((\d+|[a-zA-Z])([+-])(\d+|[a-zA-Z])\)",  r"\1\2\3\4\1\2\5", e)  # a*(b+c) = a*b+a*c
    e = re.sub(r"(\d+|[a-zA-Z])([*/])\((\d+|[a-zA-Z])([+-])(\d+|[a-zA-Z])([+-])(\d+|[a-zA-Z])\)",  r"\1\2\3\4\1\2\5\6\1\2\7", e)  # a*(b+c+d) = a*b+a*c+a*d
    print e
    e = re.sub(r"-\([^()]+[+-][^()]+\)",    switchsigns, e)  # -(a-b) = -a+b
    print e
    e = re.sub(r"(^|\+)\(([^()]+)\)",           r"\1\2", e)  # +(a+-b) = +a+-b
    print e

    for k in sub_map :
      e = re.sub(k, sub_map[k], e)

    if esave == e : # Stop when no change from all the simplifying
      break
    else :
      esave = e

  return e

def sqrt_n_to_continued(n):
  sqn = sqrt(n) 
  if (int(sqn) == sqn) : # Handle square numbers trivially
    return [int(sqn)]

  c = []
  s = sqrt(n) # s stands for sqrt(n)
  rn,rd = "s","1"
  sub_map = { r"s\*s" : str(n) }
  while True :
    rs = "("+rn+")/("+rd+")"
    #print "\n", len(rs), "\n"
    print "\n", rs, "\n"
    r = eval (rs)
    print s,r
    a = int(floor(r))
    c.append(a) 
    print a

    #r = 1 / (r - a)
    #r = 1 / (rn/rd - a)
    #r = (rn/rd + a) / (rn*rn/rd*rd - a*a)
    #r = (rn*rd + a*rd*rd) / (rn*rn - a*a*rd*rd)
    #rn1 = "({rn}*{rd}+{a}*{rd}*{rd})".format(rn=rn, rd=rd, a=a)
    #rd1 = "({rn}*{rn}-{a}*{a}*{rd}*{rd})".format(rn=rn, rd=rd, a=a)

    #r = 1 / (r - a)
    #r = 1 / (rn/rd - a)
    #r = rd/ (rn - a*rd)
    rn1 = "{rd}".format(rn=rn, rd=rd, a=a)
    rd1 = "({rn})-({a}*({rd}))".format(rn=rn, rd=rd, a=a)

    rnr = simplify_expression(rn1, sub_map)
    rdr = simplify_expression(rd1, sub_map)
    rn, rd = rnr, rdr
    if a == 2*c[0]:
      break
    if len(c) >= 20:
      exit(1)
  return c

for n in [23, 139, 2, 3,4, 5,6,7, 43]:
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

  

