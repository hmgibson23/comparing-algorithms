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
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # What is the complexity of traversing the list?
    def traverse():
        temp

        # go to the end
        while self.next:
            temp = self.next

        return temp


    # We only append it this specific list. Of course, you could
    # implement it differently
    def add():
        end = self.traverse()

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
    def traverse(current):

        if not current.right and not current.left:
            return current.value
        elif current.right:
            traverse()


    def add():
