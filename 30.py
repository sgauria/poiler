def sum_for_powers_of_digits(num,power):
  sum = 0
  n = num
  while (n > 0):
    d = n % 10
    sum += d**power
    n = int(n/10)
  return sum

# The max possible sum of powers for a 6 digit number is 9^5*6 = 354294, so all larger numbers can't be equal to the sum of their powers.
result = 0
for i in xrange(10,354300):
  if (sum_for_powers_of_digits(i,5) == i):
    print "==", i
    result += i

print "====", result

