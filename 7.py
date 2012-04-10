import math

def is_prime(n) :
    for i in range(2,(math.ceil(math.sqrt(n)+1)+1)):
        if ((n % i) == 0) :
            return False
    return True

num_p = 6;
for p in range(15,1000000,2) :
    if (is_prime(p)) :
        num_p += 1
        print num_p, p
        if (num_p == 10002) :
            break

print "done"
