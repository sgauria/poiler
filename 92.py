from poiler_common import digits, memoize_fast_1_arg
from collections   import Counter

def sq_dig_sum(n):
  x = n
  sum = 0
  while x > 0:
    x, digit = divmod(x, 10)
    sum += digit*digit
  return sum

@memoize_fast_1_arg
def sq_d_ch_terminator(num):
  if num == 1 or num == 89:
    return num
  else :
    return sq_d_ch_terminator ( sq_dig_sum(num) )

N = 10000000
c = Counter()
for i in xrange(1,N):
  t = sq_d_ch_terminator(i)
  c.update([t])

print c
print c[89]
