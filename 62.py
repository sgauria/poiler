from poiler_common import *

def is_cube(n):
  f = list(factorize(n))
  is_cube_flag = True
  for fn, fc in f :
    if (fc % 3 != 0) :
      is_cube_flag = False
      break
  return is_cube_flag

def num_cubic_perms(n, check_cube):
  ns = str(n)
  perms = list(set(gen_perm(ns)))

  perm_cube_count = 0
  for c in perms:
    ci = int(c)
    if ci >= n and len(str(ci)) == len(ns) : # ci >= n ensures only lowest cube is printed.
      if check_cube(ci) :
        # print " ", ci
        perm_cube_count += 1

  return perm_cube_count

# i = 1 
# while True :
#   i += 1
#   n = i ** 3
#   ncp = num_cubic_perms(n)
#   if ncp >= 3 :
#     print "___", n, ncp 
#     if ncp >= 5 :
#       break

n = 1
nd = 1
maxlen = 0
while True :
  # Create list of cubes with nd digits
  list_cubes = []
  while True :
    c = n ** 3
    if len(str(c)) <= nd:
      list_cubes.append(c)
      n += 1
    else :
      break

  # Create a dict with cubes grouped by digital signature.
  cmap = {}
  for c in list_cubes:
    csd = sorted_digits(c)
    if csd not in cmap :
      cmap[csd] = []
    cmap[csd].append(c)

  # Check each list and print each one that sets a new record in length.
  for s in cmap :
    l = cmap[s]
    ll = len(l)
    if ll > maxlen  :
      print ll, l
      maxlen = max(ll, maxlen)

  if maxlen >= 5:
    break

  nd += 1

