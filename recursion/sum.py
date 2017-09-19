import stack
from stack import Stack

def sum_list(num_list):
    if len(num_list) == 1:
        return num_list[0]

    else:
        return num_list[0] + sum_list(num_list[1:])

r_stack = Stack()

def to_str(n, base):
   convert_string = "0123456789ABCDEF"
   while n > 0:
      if n < base:
         r_stack.push(convert_string[n])
      else:
         r_stack.push(convert_string[n % base])
      n = n // base
   res = ""
   while not r_stack.is_empty():
      res = res + str(r_stack.pop())
   return res

def palindorm(string): #none-recursive
    size = len(string) - 1
    if ord(string[0]) - ord(string[1:len(string) - 1]) == 0:
         return palindorm(string)
    else:
        return False

def is_palindrome(s):
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            # v-- forgot this here
            return is_palindrome(s[1:-1])
        else:
            return False
