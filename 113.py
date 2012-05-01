from poiler_common import memoize_fast_args_only
N = 100

@memoize_fast_args_only
def count_decreasing(num_digits, left_digit, leftmost_digit):
   count = 0
   if (num_digits <= 1):
     if (leftmost_digit) :
       count = 9
     else :
       count = (left_digit+1)
   else :
     count += count_decreasing(num_digits-1, 0, leftmost_digit)
     if (leftmost_digit) :
       digit_limit = 10
     else :
       digit_limit = left_digit + 1
     for digit in range(1,digit_limit):
       count += count_decreasing(num_digits-1, digit, 0)
   #if (num_digits > N - 2):
   #  print "cd:",num_digits, left_digit, leftmost_digit, count
   return count

@memoize_fast_args_only
def count_increasing(num_digits, left_digit, leftmost_digit):
   count = 0
   if (num_digits <= 1):
     if (leftmost_digit) :
       count = 9
     else :
       count = (10-left_digit)
   else :
     if (leftmost_digit):
       count += count_increasing(num_digits-1, 0, leftmost_digit)
       start_digit = 1
     else :
       start_digit = left_digit
     for digit in range(start_digit,10):
       count += count_increasing(num_digits-1, digit, 0)
   #if (num_digits > N - 2):
   #  print "ci:",num_digits, left_digit, leftmost_digit, count
   return count

def count_non_bouncy(num_digits):
  count= 0
  count += count_increasing(num_digits,0,1) 
  count += count_decreasing(num_digits,9,1) 
  count -= (9 * num_digits)                # numbers that are both increasing and decreasing (i.e. same digit repeated)
  return count

print count_non_bouncy(N)
#print count_decreasing(2,1,0)
