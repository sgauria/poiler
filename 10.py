import math

def is_prime(n) :
    if ((n % 2) == 0) :
        return False
    top = int(math.sqrt(n)+1)
    for i in xrange(3,top,2):
        if ((n % i) == 0) :
            return False
    return True

sum_p = 2
for p in xrange(3,2000000,2) :
    if (is_prime(p)) :
        sum_p += p;

print sum_p
