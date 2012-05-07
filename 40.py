def d(n):
  # Express n as i^th digit (starting from left) of the j^th number of k digits
  i,j,k = 0,0,1
  nn = n-1
  while True :
    if (nn < k*9*(10 ** (k-1))):
      j,i = divmod(nn,k)
      break 
    else :
      nn -= k*9*(10 ** (k-1))
      k += 1
  num = (10**(k-1)) + j
  ns  = str(num)
  dd  = int(ns[i])
  return dd

#for i in xrange(1,200):
#  print i,d(i)

prod = 1
for i in range(7):
  digit = d(10**i)
  prod *= digit
  #print digit

#print "======"
print prod

        

                
    
