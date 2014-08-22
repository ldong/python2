#!/usr/bin/env python
from math import sqrt

def fib(n):
    a, b = 0, 1
    for i in xrange(n-1):
        a, b = b, a+b
    return b

def fib_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_formula(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def main():
    n = input('Please enter an number: ')
    print 'Correct Answer:', fib_formula(n)
    print 'Iterative: ', fib(int(n))
    print 'Recursion: ', fib_rec(int(n))

if __name__ == '__main__':
    main()
