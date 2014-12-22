import sys
sys.path.append("..")
from helpers.Helpers import *

# Disclaimer: I suck at OO programming so if the classes etc. are bad
# I apologise but I never really did OO!


# Don't arrays (lists in Python but they're the same)
# are data structures too
array = [1,2,3,4]


# this is singly linked
# the same principles apply in
# doubly linked and circular lists
# Typically queues, stacks, lists are implemented
# out of linked lists.
class LinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    # What is the complexity of traversing the list?
    def end(self):
        temp = self
        # go to the end
        while temp.next:
            temp = temp.next

        return temp


    def show(self):
        temp = self
        while temp.next:
            print temp.value
            temp = temp.next



    # We only append it this specific list. Of course, you could
    # implement it differently
    def add(self, value):
        end = self.end()
        end.next = LinkedList(value)


    # This does not need to be done recursively but I just prefer it that way
    def search(self, current, value):
        if current.value == value:
            return current
        elif current.value != value and current.next == None:
            return "Not found!"
        else:
            return self.search(current.next, value)

    # This will be used in the final week
    @timing
    def timeSearch(self, current, value):
        return self.search(current, value)






# Binary tree. A fundamental tree.
# We'll talk about self-balancing binary trees
# in the class. This is a somewhat naive one as the tree
# can become unbalanced and our structure lost
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    # What's the complexity of this traverse?
    # What order traversal is this? Pre or post?
    def traverse(self, current):

        if not current.right and not current.left:
            print current.value

        if current.left:
            current.traverse(current.left)
            print current.value

        if current.right:
            current.traverse(current.right)
            print current.value


    # How about the insert?
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    # If you're bored - try and implement a search function for
    # this tree

def main():
    # LinkedList
    print "Linked List"
    print "==========="
    l = LinkedList("A")
    l.add("link")
    l.add("ed")
    l.add("list")
    l.add("!")
    l.show()

    # Binary tree
    print "\nBinary Tree"
    print "==========="
    t = BinaryTree(6)
    t.insert(5)
    t.insert(10)
    t.insert(3)
    t.insert(2)
    t.insert(1)
    t.insert(11)
    t.insert(12)
    t.traverse(t)


if __name__ == "__main__":
    main()
