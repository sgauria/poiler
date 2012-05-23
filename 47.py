from poiler_common import *

a,b,c,d = 1,2,3,4
na,nb,nc,nd = 1,1,1,1
while True:
  if (na == nb == nc == nd == 4):
    print a,b,c,d
    break
  e = d+1
  fe = [x for x in factorize(e)]
  ne = len(fe)
  a,b,c,d = b,c,d,e
  na,nb,nc,nd = nb,nc,nd,ne
  
