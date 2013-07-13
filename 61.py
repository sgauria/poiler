from poiler_common import *
import itertools
from collections import Counter

def gen_figurate_list(k,mn, mx):
  n = 1
  l = []
  while True :
    x = n*((k-2)*n+(4-k))/2
    if mn <= x <= mx:
      #print n,x
      l.append(x)
    if x > mx :
      break
    n += 1
  return l


# Lists of 4 digit figurate numbers.
## f3 = [ x for x in [ (n*(  n+1)/2) for n in range(1,150) ] if (1000 <= x < 10000) ]
## f4 = [ x for x in [ (n*(2*n  )/2) for n in range(1,150) ] if (1000 <= x < 10000) ]
## f5 = [ x for x in [ (n*(3*n-1)/2) for n in range(1,150) ] if (1000 <= x < 10000) ]
## f6 = [ x for x in [ (n*(4*n-2)/2) for n in range(1,150) ] if (1000 <= x < 10000) ]
## f7 = [ x for x in [ (n*(5*n-3)/2) for n in range(1,150) ] if (1000 <= x < 10000) ]
## f8 = [ x for x in [ (n*(6*n-4)/2) for n in range(1,150) ] if (1000 <= x < 10000) ]

f3 = gen_figurate_list(3,1000,9999)
f4 = gen_figurate_list(4,1000,9999)
f5 = gen_figurate_list(5,1000,9999)
f6 = gen_figurate_list(6,1000,9999)
f7 = gen_figurate_list(7,1000,9999)
f8 = gen_figurate_list(8,1000,9999)




#print len(f3)
#print len(f4)
#print len(f5)
#print len(f6)
#print len(f7)
#print len(f8)

@memoize_fast_args_only
def cyclic_pair(n1, n2):
  if ((n1 % 100) == int(n2 / 100)):
    return True 
  else :
    return False

def cyclic_chain(l):
  for x in range(len(l)):
    if not cyclic_pair(l[x-1], l[x]) :
      return False
  return True

def potential_chain(l):
  dds = [] # pairs of digits
  for n in l :
    dds.append(n%100)
    dds.append(int(n/100))
  cnt = Counter(dds)
  for v in cnt.values():
    if v != 2 :
      return False
  return True
  


if 0 :
  for n3 in f3 :
    for n4 in f4 :
      for n5 in f5 :
        if cyclic_chain ((n3,n4,n5)):
          print n3,n4,n5
        if cyclic_chain ((n3,n5,n4)):
          print n3,n4,n5

if 0 :
  for t in itertools.product(f3, f4, f5, f6, f7, f8):
    print t
    if potential_chain(t) :
      # Keep one element fixed and permute the rest
      t0 = t[0]
      tr = t[1:]
      for p_tr in itertools.permutations(tr):
        p = (t0,)+p_tr
        if cyclic_chain(p):
          print p[-1:] + p[:-1]

if 0:
  fs = f3 + f4 + f5 
  ufs = list(set(fs))
  print len(ufs)
  for n3 in ufs :
    for n4 in ufs :
      if cyclic_pair(n3,n4) :
        for n5 in ufs :
          if cyclic_pair(n4,n5) :
                        if cyclic_pair(n5,n3) :
                          # Here we have 6 numbers that form a chain, but not necessarily from different lists
                          cl = (n3,n4,n5)
                          #if sorted(cl) == sorted(list(set(cl))): # no duplicates
                          f3c = sum ([f3.count(x) for x in cl]) 
                          f4c = sum ([f4.count(x) for x in cl]) 
                          f5c = sum ([f5.count(x) for x in cl]) 
                          if (f3c >= 1 and f4c >= 1 and f5c >= 1):
                            print sum(cl), cl, f3c, f4c, f5c

if 0:
  fs = f3 + f4 + f5 + f6 + f7 + f8
  ufs = list(set(fs))
  print len(ufs)
  for n3 in f8  :
    for n4 in ufs :
      if cyclic_pair(n3,n4) :
        for n5 in ufs :
          if cyclic_pair(n4,n5) :
            for n6 in ufs :
              if cyclic_pair(n5,n6) :
                for n7 in ufs :
                  if cyclic_pair(n6,n7) :
                    for n8 in ufs :
                      if cyclic_pair(n7,n8) :
                        if cyclic_pair(n8,n3) :
                          # Here we have 6 numbers that form a chain, but not necessarily from different lists
                          cl = [n3,n4,n5,n6,n7,n8]
                          if sorted(cl) == sorted(list(set(cl))): # no duplicates
                            f3c = sum ([f3.count(x) for x in cl]) 
                            f4c = sum ([f4.count(x) for x in cl]) 
                            f5c = sum ([f5.count(x) for x in cl]) 
                            f6c = sum ([f6.count(x) for x in cl]) 
                            f7c = sum ([f7.count(x) for x in cl]) 
                            f8c = sum ([f8.count(x) for x in cl]) 
                            if (f3c >= 1 and f4c >= 1 and f5c >= 1 and f6c >= 1 and f7c >= 1 and f8c >= 1):
                              print sum(cl), cl, f3c, f4c, f5c, f6c, f7c, f8c
                              for x in cl :
                                print x, ":", f3.count(x), f4.count(x), f5.count(x), f6.count(x), f7.count(x), f8.count(x)

                              
# Final version uses sets to make sure we have one number from each set.
if 1:
  fs = {}
  fs[3] = set([(x,3) for x in f3])
  fs[4] = set([(x,4) for x in f4])
  fs[5] = set([(x,5) for x in f5])
  fs[6] = set([(x,6) for x in f6])
  fs[7] = set([(x,7) for x in f7])
  fs[8] = set([(x,8) for x in f8])
  ufs = fs[3] | fs[4] | fs[5] | fs[6] | fs[7] | fs[8]

  for n3,s3 in fs[3]: # without loss of generality, speeds things up.

    ufs4 = ufs - fs[s3]
    for n4,s4 in ufs4 :
      if cyclic_pair(n3,n4) :

        ufs5 = ufs4 -fs[s4]
        for n5,s5 in ufs5 :
          if cyclic_pair(n4,n5) :

            ufs6 = ufs5 -fs[s5]
            for n6,s6 in ufs6 :
              if cyclic_pair(n5,n6) :

                ufs7 = ufs6 -fs[s6]
                for n7,s7 in ufs7 :
                  if cyclic_pair(n6,n7) :

                    ufs8 = ufs7 -fs[s7]
                    for n8,s8 in ufs8 :
                      if cyclic_pair(n7,n8) :
                        if cyclic_pair(n8,n3) :
                          cl = [n3,n4,n5,n6,n7,n8]
                          print sum(cl), cl
                                
