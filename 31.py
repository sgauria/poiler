#from poiler_common import *

#@memoize_fast_args_only
def construct_sums(l_coins, total):
  my_coin = l_coins[0]
  if (len(l_coins) == 1):
    return [[(my_coin, int(total/my_coin))]]
  else :
    i = 0
    sums = []
    while (my_coin * i <= total):
      subsums = construct_sums (l_coins[1:], (total - (my_coin * i)))
      for x in subsums:
	x.insert(0, (my_coin, i))
	sums.append(x)
      i += 1
    return sums

    

english_coins = [200,100,50,20,10,5,2,1]
english_total = 200
english_sums = construct_sums(english_coins, english_total)

#print english_sums
print len(english_sums)
