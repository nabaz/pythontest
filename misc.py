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

    def palindorme(a_string):
        ch_dequeu = Deque()
        str_strip = a_string.strip()
        for ch in str_strip:
            ch_dequeu.add_rear(ch)

        print(ch_dequeu.items)
        still_ok = True

        while ch_dequeu.size() > 1 and still_ok:

            print(ch_dequeu.size())
            first = ch_dequeu.remove_front()
            last = ch_dequeu.remove_rear()

            if first != last:
                still_ok = False

        return still_ok
