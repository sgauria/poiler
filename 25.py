f1 = 1
f2 = 1
fn = f1 + f2
n  = 3

while (len(str(fn)) < 1000):
  #if (n%100 == 0):
  #  print n,fn
  f1 = f2
  f2 = fn
  fn = f1+f2 
  n  = n + 1

print n,fn
