import random
import sys
sys.path.append("..")

from helpers.Helpers import *
from lesson2.DataStructures import *

# Fun fun fun!
# Makes for some very fast searching

class SkipNode:
    def __init__(self, height = 0, value = None):
        self.value = value
        self.next = [None]*height

# A skip list uses random heights to put nodes at,
# it then moves down the heights to search and the nodes
# guaranteeing O(log n) search time
class SkipList:

    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    @timing
    def timeFind(self, value):
        return self.find(value)


    def find(self, value, update = None):
        if update == None:
            update = self.updateList(value)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.value == value:
                return candidate
        return None

    # Chooses a random height for our list
    # and where to place nodes
    def randomHeight(self):
        height = 1
        while random.randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, value):
        update = [None] * self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
            update[i] = x
        return update

    def add(self, value):

        node = SkipNode(self.randomHeight(), value)

        self.maxHeight = max(self.maxHeight, len(node.next))

        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(value)

        if self.find(value, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

def main():
    s = SkipList()
    l = LinkedList()
    values = random.sample(xrange(1000), 1000)

    for x in values:
        s.add(x)
        l.add(x)

    s.timeFind(10)
    l.timeSearch(l, 10)


if __name__ == "__main__":
    main()
