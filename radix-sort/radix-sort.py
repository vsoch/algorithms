#!/usr/bin/env python

numbers = [1,2,3,4,6,8,4,3,2,2,6,2,3]

def radixsort(numbers):

    counts = dict()

    for number in numbers:
        if number not in counts:
            counts[number]=0
        counts[number]+=1

    # Python sorts by key automatically
    sortedN=[]
    for key in counts:
        sortedN = sortedN + [key]*counts[key]

    return sortedN
