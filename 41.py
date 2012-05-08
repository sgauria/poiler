from poiler_common import gen_perm, is_prime

# Generate pandigitals in descending order.
# Stop at the first one that is prime.
X = "987654321"
for i in range(9):
  gpx = gen_perm(X[i:])
  for s in gpx:
    n = int(s)
    if is_prime(n):
      print n
      exit(0)

# I first tried using seive of Eratosthenes for this, it turns out that 
# using direct prime checks is more efficient since we are only testing a
# small fraction of the numbers (400k out of 10^9)
