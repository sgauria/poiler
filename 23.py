# Copied from 21.py and modified.
import math

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

def sum_of_divisors(n):
    f  = factorize(n)
    l  = [(pf,c) for (pf,c) in f] # list of factors and counts
    #print (l)
    l2 = [(pf,0) for (pf,c) in l]
    #print (l2)
    #print (len(l2))
    sum_div = 0
    while True:
        div = 1
        for (pf,c) in l2:
            div *= (pf**c)
        #print(div)
        if (l2 == l) :
            break
        sum_div += div
        for i in range (len(l2)):
            (pf,c) = l2[i]
            (pfo,co) = l[i]
            if (c < co):
                l2[i] = (pf,c+1)
                break
            else :
                l2[i] = (pf,0)
    return sum_div


#f = factorize(1001)
#for i in f:
#    print (i)

#s = sum_of_divisors(220)
#print (s)
#s = sum_of_divisors(284)
#print (s)

N=28124

sods = [sum_of_divisors(i) for i in range(N)]

abundants = []
for i in xrange(1,N):
  if (sods[i] > i):
    abundants.append(i)

#print abundants

la = len (abundants)
abundant_sums = set()
for i in (xrange(la)):
  for j in (xrange(i,la)):
    asum = abundants[i] + abundants[j]
    if asum > N:
      break
    abundant_sums.add(asum)

#print abundant_sums

total = 0
for i in xrange(1,N):
  if i not in abundant_sums :
    total += i

print total
  
