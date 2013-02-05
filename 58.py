# Copied from 28, and modified.
# Calculate only the diagonal entries.
from poiler_common import is_prime

prev_n = 1
step = 2
prime_count, diagonal_count = 0,1
while True:
  for j in xrange(4):
    n = prev_n + step
    if is_prime(n):
      prime_count += 1
    prev_n = n
  diagonal_count += 4
  step += 2
  if prime_count * 10 < diagonal_count:
    break

print step-1
