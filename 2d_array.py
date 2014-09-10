#!/usr/bin/env python

from pprint import pprint as pp

def two_d_array(x):
    return [[0 for i in xrange(x)] for i in xrange(x)]

def main():
    x = input('Input size: ')
    pp(two_d_array(x))

if __name__ == '__main__':
    main()
