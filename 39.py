import math
import time

c1 = time.clock()
N = 1000

maxcount = 0
maxp     = 0
for p in range(1,N+1):
    s = math.ceil(p/2)
    count = 0
    for a in range(1,s):
        for b in range(a,s):
            c = p - a - b
            if (c > b):
                if (c < s):
                    if (a*a + b*b == c*c):
                        count += 1
                        #print (p,a,b,c)
            else :
                break # c is less than b and will only get smaller as b increases.
    if (count >  maxcount):
        maxcount = count
        maxp     = p

print (maxp, maxcount)
c2 = time.clock()                
print (c2-c1)

# TODO : This runs in 17 seconds, but need to tighten all the ranges and make it run faster.
