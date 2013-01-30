from poiler_common import reverse_num, num_is_palindrome

def is_lychrel(num, iteration=0):
  if iteration >= 50 :
    return True
  else :
    new_num = num + reverse_num(num)
    if num_is_palindrome(new_num) :
      return False
    else :
      return is_lychrel(new_num, iteration+1)

assert is_lychrel(4994) == True
    
N = 10000
count_lychrel = 0
for i in range(N):
  if is_lychrel(i):
    count_lychrel += 1

print count_lychrel

