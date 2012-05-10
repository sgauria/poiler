from poiler_common import gen_perm, is_prime

total = 0
primes = [2,3,5,7,11,13,17]

# Generate pandigitals in descending order.
X = "9876543210"
gpx = gen_perm(X)

for d in gpx:
  has_prop = True
  for i in range(7):
    if (int(d[i+1:i+4]) % primes[i]) != 0:
      has_prop = False
      break
  if has_prop:
    total += int(d)
    print d

print "======="
print total

