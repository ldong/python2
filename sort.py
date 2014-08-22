#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Quick Sort Algorithms
From
1. http://rosettacode.org/wiki/Sorting_algorithms/Quicksort
2. http://www.pythonschool.net/algorithms_quickSort/
3. http://en.literateprograms.org/Quicksort_(Python)
4. http://stackoverflow.com/questions/17773516/in-place-quicksort-in-python
"""
from random import *
from time import *

def quicksort_simple(lst):
    ''' Simple Quick Sort version
    It uses recursions and extra space, will exceed the memory if list is large
    '''
    if not lst or len(lst) <= 1:
        return lst
    else:
        val = choice(lst)
        left = []
        right = []
        equal = []
        for v in lst:
            if v < val:
                left.append(v)
            elif v > val:
                right.append(v)
            else:
                equal.append(v)
        return quicksort_simple(left) + equal + quicksort_simple(right)

def quicksort_in_place(lst):
    if len(lst) > 1:
        pivot = choice(lst)
        left = 0
        right = len(lst) - 1
        while left < right:
            while lst[left] < pivot:
                left += 1
            while lst[right] > pivot:
                right -= 1
            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        quicksort_in_place(lst[0:right])
        quicksort_in_place(lst[left:len(lst)])

def qsort(x, l, r):
    i = l
    j = r
    # p = x[l + (r - l) / 2] # pivot element in the middle
    p = choice(x)
    while i <= j:
        while x[i] < p: i += 1
        while x[j] > p: j -= 1
        if i <= j: # swap
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
    if l < j: # sort left list
        qsort(x, l, j)
    if i < r: # sort right list
        qsort(x, i, r)
    return x

def test_qsort():
    seed()
    x = []
    for i in range(0, 100):
        x.append(randint(0, 100))

    start = time()
    print "Before: ", x
    x = qsort(x, 0, len(x) - 1)
    print "After: ", x
    print "%.2f seconds" % (time() - start)



def quick_sort_list_comprehension(a):
    '''
    More correctly in some tests:
    '''
    if not a or len(a) <= 1:
        return a
    else:
        q = choice(a)
        return quick_sort_list_comprehension([elem for elem in a if elem < q])\
             + [q] * a.count(q)\
             + quick_sort_list_comprehension([elem for elem in a if elem > q])



def bubble_sort(lst, descending=False):
    # compare = (lambda a, b: a >= b) if descending else (lambda a, b: a <= b)
    compare = lambda a, b: a >= b if descending else lambda a, b: a <= b
    thing = [compare(lst[i], lst[i+1]) for i in xrange(len(lst)-1)]
    sorted = all(thing)
    print 'Yeah, run', thing, sorted
    if not sorted:
        for i in xrange(len(lst)):
            for j in xrange(i):
                if compare(lst[i], lst[j]):
                    print lst
                    lst[i], lst[j] = lst[j], lst[i]


def insertion_sort(lst):
    pass


def test(quicksort):
    assert quicksort([7,1,3,5,6]) == [1,3,5,6,7]
    assert quicksort([-1,0,-20,-100,7,1,3,5,6]) == [-100,-20,-1,0,1,3,5,6,7]
    assert quicksort([7,1,6]) == [1,6,7]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort(None) == None

def main():
    test(quick_sort_list_comprehension)
    test(quicksort_simple)
    # test(quicksort_in_place)
    test_qsort()

if __name__ == '__main__':
    main()

## QuickSort One liner
# q_sort= lambda l: l if len(l)<=1 else q_sort([x for x in l[1:] if x<l[0]])+[l[0]]+q_sort([x for x in l[1:] if x >= l[0]])
# print q_sort([2,3,5,6,3,1,8,5])
