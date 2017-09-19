class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_rear(self, item):
        self.items.insert(0, item)
    def add_front(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def normal(number):
    word_key_map = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
        '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
    number_scope_map = {'1' : '', '2':'tens', '3': 'hundred', '4': 'thousand', '7': 'millions', '10': 'billions'}
    tens_map = {'10': 'ten', '20': 'twenty', '30':'thirty', '40' :'fourty', '50': 'fifty', '60':'sixty', ''}
    a_list = Deque()
    for i in str(number):
        a_list.add_front(i)

    for i in a_list:
        if i in word_key_map:
             print(word_key_map.get(i))


    return a_list
