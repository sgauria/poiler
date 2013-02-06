# How many n-digit positive integers exist which are also an nth power?
# ===
# How many n-th powers are n-digits long.

# 10^n is always n+1 digits.
#   So base must always be less than 10.
# math.log (10.0) / math.log(10.0/9) = 21.8
#  So we can infer than n > 22 will have too much difference in number of digits between 9^n and 10^n
#    It's the solution of 10^n / 9^n > 10


count = 0

for n in range(1,22):
  for base in range(1,10):
    x = base ** n
    lx = len(str(x))
    if lx == n :
      count += 1
      #print base, "^", n, "=", x
    elif lx > n:
      break
    
print count
