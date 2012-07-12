# I assume all line equations to be of the form
# ax + by + c = 0


def line_params(x0,y0,x1,y1):
  if (x0 != x1):
    a = 1.0*(y0-y1)/(x1-x0)
    b = 1.0 
    c = 1.0*(x0*y1-x1*y0)/(x1-x0)
  else :
    a = 1.0
    b = 0.0
    c = x0
  return (a,b,c)


def eval_line_at_point(a,b,c,x,y):
  e = a*x + b*y + c
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

  (a0,b0,c0) = line_params(x0,y0,x1,y1)
  (a1,b1,c1) = line_params(x1,y1,x2,y2)
  (a2,b2,c2) = line_params(x2,y2,x0,y0)

  e0 = eval_line_at_point(a0,b0,c0,x2,y2)
  e1 = eval_line_at_point(a1,b1,c1,x0,y0)
  e2 = eval_line_at_point(a2,b2,c2,x1,y1)
  #print e0,e1,e2

  if same_sign(e0,c0) and same_sign(e1,c1) and same_sign(e2,c2):
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
