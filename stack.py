class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []


    def push(self, item):
        return self.items.append(item)

    def pop(self):

        return self.items.pop()

    def peek(self):

        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def rev_string(string):
    temp_stack = Stack()
    for s in string.items:
        temp_stack.push(s)
    rev_stack = Stack()
    while not temp_stack.is_empty():
        rev_stack.push(temp_stack.pop())
    return rev_stack


def d_by_2(d):
    s = Stack()
    while d > 0:
        rem = d % 2
        s.push(rem)
        d = d
    bin_n = " "
    while not s.is_empty():
        bin_n = bin_n + str(s.pop())
    return bin_n
    
def base_converter(dec_number, base):
   digits = "0123456789ABCDEF"
   rem_stack = Stack()
   while dec_number > 0:
      rem = dec_number % base
      rem_stack.push(rem)
      dec_number = dec_number // base
   new_string = ""
   while not rem_stack.is_empty():
      new_string = new_string + digits[rem_stack.pop()]
   return new_string
