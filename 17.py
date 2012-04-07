smap = { 
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety" }


def n_to_s(n):
  s = ""

  # thousands
  t = int (n/1000)
  n = n % 1000
  if (t > 0):
    s = smap[t] + " thousand"

  # hundreds
  h = int(n/100)
  n = n % 100
  if (h > 0) :
    s += smap[h] + " hundred"
    if (n != 0):
      s += " and "
  
  # tens and units
  t = int(n/10) * 10
  u = n % 10

  if ( 11 <= n <= 19):
    s += smap[n]
  else :
    if (t > 0):
      s += smap[t]
      if (u > 0):
	s += "-"
    if (u > 0):
      s += smap[u]

  return s

def count_letters(s):
  return sum(map(lambda x : 1 if ('a' <= x <= 'z') else 0, s)) 


total = 0
for i in xrange(1,1001):
  s = n_to_s(i)
  c = count_letters(s)
  total += c
  print i, s, c, total

print total
