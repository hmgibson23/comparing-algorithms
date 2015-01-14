import sys
sys.path.append("..")
from helpers.Helpers import *

# A linear search algorithm
@timing
def linearSearch(val, values):
    position = 0


    while position < len(values):
        if values[position] == val:
            break;
        else:
            position = position + 1

    return position

# A binary search algorithm
@timingx
def binarySearch(val, values):
    min = 0
    max = len(values) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if values[m] < val:
            min = m + 1
        elif values[m] > val:
            max = m - 1
        else:
            return m


def main():
    values = range(1, 1000000)
    val = 340100
    pos = linearSearch(val, values)
    print "Linear search found: " + str(val) + " at index: " + str(pos) + "\n"

    pos = binarySearch(val, values)
    print "Binary search found: " + str(val) + " at index: " + str(pos) + "\n"

    # fact = fnHelper(factorial, 5)
    # print "factorial(" + str(5) + ") is " + str(fact) + "\n"
    # fib = fnHelper(fibonacci, 5)
    # print "fibonacci(" + str(5) + ") is " + str(fib) + "\n"

if __name__ == "__main__":
    main()
