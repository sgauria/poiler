from math import sqrt, ceil

root2 = sqrt(2)

# n total discs
# b  blue discs
# Probability is b/n * b-1/n-1
# Since b/n > b-1/n-1, and both must be pretty close to 1/root2 :
# b must be ceil(n / root2)

n = 10
#n = 1000000000000 # 10^12

print "blue,\tred,\ttotal"
while True :
  b = int(ceil(n/root2))
  #print (2*b*(b-1)), (n*(n-1))
  if (2*b*(b-1)) == (n*(n-1)):
    print b, (n-b), n, (2*b*(b-1)), (n*(n-1))
    if n > 1e12:
      break 
  n += 1
