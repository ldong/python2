#!/usr/bin/env python
# http://pymotw.com/2/re/

import re

def example1():
    patterns = [ 'this', 'that' ]
    text = 'Does this text match the pattern?'

    for pattern in patterns:
        print 'Looking for "%s" in "%s" ->' % (pattern, text),

        if re.search(pattern,  text):
            print 'found a match!'
        else:
            print 'no match'

def example2():
    pattern = 'this'
    text = 'Does this text match the pattern?'

    match = re.search(pattern, text)

    s = match.start()
    e = match.end()

    print 'Found "%s" in "%s" from %d to %d ("%s")' % \
        (match.re.pattern, match.string, s, e, text[s:e])

def example3():
    regexes = [re.compile(p) for p in [ 'this', 'that', ]]
    text = 'Does this text match the pattern?'

    for regex in regexes:
        print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),

        if regex.search(text):
            print 'found a match!'
        else:
            print 'no match'

def main():
    print 'Example 1'
    example1()
    print '\nExample 2'
    example2()
    print '\nExample 3'
    example3()

if __name__ == '__main__':
    main()
