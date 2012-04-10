N = 100

nf = 1
for i in range(1,N+1):
    nf *= i

sum = 0
for c in str(nf):
    sum += int(c)

print sum
