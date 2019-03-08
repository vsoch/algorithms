#!/usr/bin/env python


numbers = [1,2,3,4,6,8,4,3,2,2,6,2,3]

def selectionsort(numbers):

    # Keep a separate list of sorted numbers
    sortedN = []

    # Say the smallest is the first
    smallest = numbers[0]

    # Keep going through the numbers until we haven't changed
    while len(numbers) > 0:

        # Keep an index to the smallest
        smallest = 0
    
        # Start with index at 0, and move smallest element to the end
        for idx in range(0, len(numbers)):
            if numbers[idx] < numbers[smallest]:
                smallest = idx
                print('Smallest is %s' % numbers[smallest])

        # Add the smallest to the end of the sorted list
        sortedN.append(numbers.pop(smallest))

    print(sortedN)
    return sortedN


selectionsort(numbers)
