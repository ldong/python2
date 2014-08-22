#!/usr/bin/env python
# http://goo.gl/En5qwq
from pprint import pprint
digitLetters =  {
    "2": 'abc',
    "3": 'def',
    "4": 'ghi',
    "5": 'jkl',
    "6": 'mno',
    "7": 'prs',
    "8": 'tuv',
    "9": 'wxy'
    }

def getLetters(number):
    result = []
    for digit in number:
        if digit in digitLetters:
            result.append(digitLetters[digit])
        else:
            result.append(digit)
    return result

def getCombinations(letterList):
    if len(letterList) == 1:
        return list(letterList[0])
    else:
        result = []
        for letter in letterList[0]:
            result = result + (map(lambda x: letter + x, getCombinations(letterList[1:])))
        return result

def run(number):
    pprint(getCombinations(getLetters(number)))

def main():
    number = raw_input('Enter a number i.e. 123 : ')
    run(number)

if __name__ == '__main__':
    main()
