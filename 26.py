# Calculates a/b. 
# assumes a < b
def count_recurrence (a,b):
  dividend = a
  divisor = b
  dividend_list = []
  quotient_list = []
  while True:
    quotient  = int(dividend/divisor)
    remainder = dividend % divisor
    for i in xrange(len(dividend_list)):
      if (dividend_list[i] == dividend):
	# found recurrence
	return (len(dividend_list) - i)
    dividend_list.append(dividend)
    quotient_list.append(quotient)
    dividend = 10*remainder
    if (dividend == 0):
      break
  return 0

    
#print count_recurrence(1,2)
#print count_recurrence(1,3)
#print count_recurrence(1,4)
#print count_recurrence(1,5)
#print count_recurrence(1,6)
#print count_recurrence(1,7)
#print count_recurrence(1,8)
#print count_recurrence(1,9)
#print count_recurrence(1,10)

maxl = 0
maxd = 0
for d in xrange(1,1000):
  l = count_recurrence(1,d)
  if l > maxl:
    maxl = l
    maxd = d

print maxd, maxl
