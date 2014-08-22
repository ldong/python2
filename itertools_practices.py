#!/usr/bin/env python
# http://pymotw.com/2/itertools/
# https://docs.python.org/2/library/itertools.html

import itertools
import random

def itertools_combinations(lst, r):
    return itertools.combinations(lst, r)

def print_iters(it):
    for i in it:
        print i
    print

def itertools_islice(start=0, stop=100, step=1):
    return itertools.islice(itertools.count(), start, stop, step)

def itertools_tee(lst, r=2):
    return itertools.tee(lst, r)

def itertools_imap(irange):
    print "Double"
    for i in itertools.imap(lambda x: x*2,  irange):
        print i

    print 'Multiples'
    for i in itertools.imap(lambda x, y: x*y,  irange, irange):
        print i

def itertools_starmap():
    print '\nstarmap'
    values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    for i in itertools.starmap(lambda x, y: (x, y, x*y), values):
        print i

def itertools_izip():
    print "\nizip"
    for i in itertools.izip(itertools.count(1), ['a', 'b', 'c']):
        print i

def itertools_cycle():
    print '\nCycle'
    i = 0
    for item in itertools.cycle(['a','b','c']):
        i += 1
        if i == 10:
            break
        print (i, item)

def itertools_repeat():
    print '\nrepeat'
    for i in itertools.repeat(['a','b','c'], 3):
        print i

def combine_izip_and_repeat():
    print '\ncombine_izip_and_repeat'
    from itertools import *
    for i, s in izip(count(), repeat('over-and-over', 5)):
        print i, s

def combine_imap_and_repeat():
    print '\ncombine_imap_and_repeat'
    from itertools import *
    for i in imap(lambda x,y:(x, y, x*y), repeat(2), xrange(5)):
        print '{} * {} = {}'.format(*i)

def itertools_filter():
    from itertools import *
    print '\nitertools_filter:'
    def check_item(x):
        print 'Testing:', x
        return (x<1)
    for i in ifilter(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
        print 'Yielding:', i

    print '\nitertools_filterfalse:'
    def check_item(x):
        print 'Testing:', x
        return (x<1)

    for i in ifilterfalse(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
        print 'Yielding:', i

    print '\ndrop while'
    def should_drop(x):
        print 'Testing:', x
        return (x<1)

    for i in dropwhile(should_drop, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
        print 'Yielding:', i

    print '\ntake while'
    def should_take(x):
        print 'Testing:', x
        return (x<2)

    for i in takewhile(should_take, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
        print 'Yielding:', i

def itertools_groupdata():
    from itertools import *
    from operator import itemgetter
    print '\nitertools_groupdata'
    d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
    di = sorted(d.iteritems(), key=itemgetter(1))
    for k, g in groupby(di, key=itemgetter(1)):
        print k, map(itemgetter(0), g)

def complex_():
    pass

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) \
            for r in range(len(s)+1))


def main():
    lst = []
    lst2 = []
    for i in xrange(10):
        lst.append(random.randint(1, 100))
        lst2.append(random.randint(1, 100))
    lst3 = itertools.chain(lst, lst2)

    print_iters(lst3)
    print_iters(itertools.izip(lst,lst2))
    print_iters(itertools_combinations(lst, 3))
    print_iters(itertools_islice(stop=5))
    print_iters(itertools_islice(start=1, stop=5))
    print_iters(itertools_islice(start=3, stop=6, step=2))

    a, b, c = itertools_tee(lst, 3)
    print_iters(a)
    print_iters(b)
    print_iters(c)

    itertools_imap(xrange(5))
    itertools_starmap()

    itertools_izip()
    itertools_cycle()
    itertools_repeat()

    combine_izip_and_repeat()
    combine_imap_and_repeat()
    itertools_filter()
    itertools_groupdata()
    complex_()

    print_iters(powerset(lst))

if __name__ == '__main__':
    main()
