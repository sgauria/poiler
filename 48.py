N = 1000
sum = 0 
for i in xrange(1,N+1):
  sum += i**i

result = sum % (10**10)

print result
