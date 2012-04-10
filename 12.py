import math

#factor_cache = {}

def list_factors(n) :
    f = []
    #if (n in factor_cache):
    #    return factor_cache[n]
    if (n == 1) :
        return []
    if (n % 2 == 0):
        f.append(2)
        f.extend(list_factors(n/2))
        #factor_cache[n] = f
        return f
    top = int(math.sqrt(n)+1)
    for i in xrange(3,top,2):
        if ((n % i) == 0) :
            f.append(i)
            f.extend(list_factors(n/i))
            #factor_cache[n] = f
            return f
    f.append(n)
    return f

def count_factors(n) :
    f = list_factors(n)
    count = 1
    while (len(f) > 0):
        f0 = f[0]
        c = f.count(f0)
        count *= (c+1)
        while (c > 0):
            f.remove(f0)
            c -= 1
    return count


t = 0
for n in xrange(1,1000000):
    t += n
    c = count_factors(t)
    if (n % 1000 == 0):
        print n, t, c
    if (c > 500):
        print "Done", n, t, c, list_factors(t)
        break


