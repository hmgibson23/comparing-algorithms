import random
import itertools
import sys
sys.path.append("..")
from helpers.Helpers import *
from lesson3.Sorting import *

# Remember the naive quicksort from last week that didn't do as well as the others?
# It can be improved by



@timing
def qsort2(n):
    return qsort(n)

def qsort(L):
    if len(L)<2: return L
    pivot_element = random.choice(L)
# In Python QuickSort will be much faster withlist comprehensions
    small = [i for i in L if i< pivot_element]
    medium = [i for i in L if i==pivot_element]
    large = [i for i in L if i> pivot_element]
    return qsort(small) + medium + qsort(large)
def main():

    values = random.sample(xrange(5000), 5000)

    sorted = bubbleSort(values)

    sorted = heapSort(values)

    sorted = mergeSort(values)

    sorted = qsort2(values)

if __name__ == "__main__":
    main()
