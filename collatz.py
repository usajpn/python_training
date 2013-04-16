#! /usr/bin/python
# -*- coding: utf-8 -*-


def collatz(num):
    counter = 0

    while True:
        counter += 1

        if num == 1:
            break
        elif num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1

    return counter


def findMax(minScope, maxScope):
    maxSeqNum = 0
    maxSeqLen = 0
    tmpLen = 0

    for num in range(minScope, maxScope):
        tmpLen = collatz(num)

        if tmpLen > maxSeqLen:
            maxSeqLen = tmpLen
            maxSeqNum = num

    return maxSeqNum, maxSeqLen


def printNumbers(num, len):
    print "Maximum Sequence Number: " + str(num)
    print "Maximum Sequence Length: " + str(len)


if __name__ == "__main__":
    minScope = 2
    maxScope = 1000000

    maxSeqNum, maxSeqLen = findMax(minScope, maxScope)
    printNumbers(maxSeqNum, maxSeqLen)
