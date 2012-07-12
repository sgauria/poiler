# I assume all line equations to be of the form
# y - sx + k = 0
#  s is the slope
#  -k is the y intercept
#  k is the evaluation of the equation at (0,0)


def line_slope(x0,y0,x1,y1):
  s = 1.0*(y1-y0)/(x1-x0)
  return s

def line_y_intercept(x0,y0,x1,y1):
  k = 1.0*(x0*y1-x1*y0)/(x1-x0)
  return k

def eval_line_at_point(s,k,x,y):
  e = y - s*x + k
  return e

def same_sign(a,b):
  if (a < 0 and b < 0):
    return True
  if (a > 0 and b > 0):
    return True
  # 0 is always considered the opposite sign.
  return False

def triangle_contains_origin(x0,y0,x1,y1,x2,y2):
  #print x0,y0,x1,y1,x2,y2

  s0 = line_slope(x0,y0,x1,y1)
  s1 = line_slope(x1,y1,x2,y2)
  s2 = line_slope(x2,y2,x0,y0)
  #print s0,s1,s2

  k0 = line_y_intercept(x0,y0,x1,y1)
  k1 = line_y_intercept(x1,y1,x2,y2)
  k2 = line_y_intercept(x2,y2,x0,y0)
  #print k0,k1,k2

  e0 = eval_line_at_point(s0,k0,x2,y2)
  e1 = eval_line_at_point(s1,k1,x0,y0)
  e2 = eval_line_at_point(s2,k2,x1,y1)
  #print e0,e1,e2

  if same_sign(e0,k0) and same_sign(e1,k1) and same_sign(e2,k2):
    return True
  else :
    return False

assert (triangle_contains_origin(-340,495,-153,-910,835,-947) == True)
assert (triangle_contains_origin(-175, 41,-421,-714,574,-645) == False)

import sys

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'triangles.txt'

ft = open(fname,'r')
tlines = ft.readlines()
tco_count = 0
for tl in tlines:
  (x0,y0,x1,y1,x2,y2) = map(int, tl.split(','))
  if triangle_contains_origin(x0,y0,x1,y1,x2,y2):
    tco_count += 1

print tco_count
