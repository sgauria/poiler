from poiler_common import *

#@memoize_fast_1_arg
#def factorial(n):
#  if n <= 1:
#    return 1
#  else:
#    return n * factorial(n-1)

#            0 1 2 3  4   5   6    7     8      9
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

# Wow, coding up the memoized factorial function was way faster than populating this factorial array, and using the array is only 2 times faster than the function (15s vs 9s)

#def sum_of_factorials(n):
#  x = n
#  sum = 0
#  while x > 0:
#    d = x % 10
#    sum += factorial[d]
#    x = int (x/10)
#  return sum


@memoize_fast_1_arg
def sum_of_factorials(n):
  if (n < 10):
    return factorial[n]
  else :
    return factorial[n%10] + sum_of_factorials(int(n/10))

# Max possible number is < 3 million, because number of digits (N) needs to satisfy 10^(N-1) < N*9!
N = 3000000

total = 0
for i in xrange(3,N):
  if (i == sum_of_factorials(i)):
    print i
    total += i

print "====="
print total
