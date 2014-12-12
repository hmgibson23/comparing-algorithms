import sys
sys.path.append("..")
from helpers.Helpers import *

###### RECURSIVE ALGORITHMS ######
@timing
def factorial(n):

    # the actual function
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n-1)

    return fact(n)

@timing
def fibonacci(n):

    # the actual function
    def fib(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    return fib(n)


def main():

    fact = factorial(5)
    print "factorial(" + str(5) + ") is " + str(fact) + "\n"
    fib = fibonacci(5)
    print "fibonacci(" + str(5) + ") is " + str(fib) + "\n"

if __name__ == "__main__":
    main()
