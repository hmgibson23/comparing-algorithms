import sys
sys.path.append("..")
from helpers.Helpers import *
from lesson1.Recursion import *

# A memoized fibonacci
# A more Pythonic method would be to use
# decorators and just have a memoize decorator but
# we're not trying to be pythonic, we're trying
# to learn about dynamic programming
@timing
def fibonacciMem(n):
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n];
        elif n == 1 or n == 2:
            cache[n] = 1
            return cache[n]
        else:
            cache[n] = fib(n-2) + fib(n-1)
            return cache[n]

    return fib(n)

def main():
    print fibonacci(30)
    print fibonacciMem(30)

if __name__ == "__main__":
    main()
