import node
from node import Node

class Unorderedlist:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
