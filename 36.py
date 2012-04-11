# The neat thing about this code is that I am not converting to strings anywhere to check palindrome-ness.
# All the arithmetic is integer, so could easily port to C, and should be pretty snappy.

def ispal(num,base):
   nn = num
   rn = 0
   while (nn > 0) :
       digit = nn % base 
       nn = (nn - digit) / base
       rn = rn*base + digit
   if (rn == num) :
       return True
   else :
       return False

total = 0
for i in xrange(1,1000000):
  if ispal(i,10):
    if ispal(i,2):
      total += i
      print i

print "========"
print total
