def d(n):
  # Express n as i^th digit (starting from left) of the j^th number of k digits
  # Each section of k-digit numbers has k*9*(10**(k-1)) digits.
  # So we loop up to figure out which section we fall in -> get k
  # Then calculate the position within the section and within the number -> j,i
  i,j,k = 0,0,1
  nn = n-1
  while True :
    if (nn < k*9*(10 ** (k-1))):
      j,i = divmod(nn,k)
      break 
    else :
      nn -= k*9*(10 ** (k-1))
      k += 1
  # Finally convert i,j,k to a single return digit.
  num = (10**(k-1)) + j
  ns  = str(num)
  dd  = int(ns[i])
  return dd

# Debug / check.
#for i in xrange(1,200):
#  print i,d(i)

prod = 1
for i in range(7):
  digit = d(10**i)
  prod *= digit
  print digit, " == d(",10**i,")"

print "======"
print prod

        

                
    
