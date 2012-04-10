def ispal(n):
   nn=n
   rn = 0
   while (nn > 0) :
       digit = nn % 10
       nn = (nn -digit) / 10
       rn = rn*10 + digit
   if (rn == n) :
       return True
   else :
       return False

N = 999
done = False
maxpal = 0;
for x in range (N,0,-1) :
    for y in range (N,x-1,-1) :
        p = x*y
        if ispal(p):
            print x,y,p
            if (p > maxpal):
                maxpal = p

print "maxpal is",maxpal 

#test = [90209, 91209,354453, 99999, 99999999]
#for t in test:
    #if (ispal(t)) :
        #print t, " is a palindrome";
    #else :
        #print t, " is not a palindrome";
