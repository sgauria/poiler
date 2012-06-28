import math

N = 1000000000

def triangle_area(a,b,c):
  s = (a+b+c)/2.0
  a = math.sqrt(s*(s-a)*(s-b)*(s-c))
  return a

def is_square(n):
  return (int(math.sqrt(n))**2) == n

assert triangle_area(5,5,6) == 12
assert triangle_area(3,4,5) == 6

# Candidate triangles are a,a,b1 and a,a,b2
b1,a,b2 = 1,2,3 
p1 = 2*a+b1
p2 = 2*a+b2
q1 = 2*a-b1
q2 = 2*a-b2
sum_of_perimeters = 0
while True :
  # Dead-simple
  #t1 = triangle_area(a,a,b1)
  #t2 = triangle_area(a,a,b2)

  # Less calculations per step
  #t1 = math.sqrt(p1*b1*b1*q1)/4
  #t2 = math.sqrt(p2*b2*b2*q2)/4
  
  # Factor out more stuff
  #t1 = (math.sqrt(p1*q1)*b1)/4
  #t2 = (math.sqrt(p2*q2)*b2)/4

  # Don't actually need the area number, just whether it is integral.
  #t1 = math.sqrt(p1*q1)
  #t2 = math.sqrt(p2*q2)

  # Better check, without floating point issues, 
  # - use is_square

  #if (t1 == int(t1)):
  if (is_square(p1*q1)):
    sum_of_perimeters += p1
    print 1, p1, a, b1

  #if (t2 == int(t2)):
  if (is_square(p2*q2)):
    sum_of_perimeters += p2
    print 2, p2, a, b2
  if (p1 > N):
    break

  b1,a,b2 = a,b2,b2+1
  p1 += 3
  p2 += 3
  q1 += 1
  q2 += 1


print sum_of_perimeters

# This version takes 743 seconds.
