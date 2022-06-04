#!/usr/bin/env python

numbers = [1, 2, 3, 4, 5, 8, 3, 2, 3, 1, 1, 1]


def bubblesort(numbers):

    # Keep a boolean to determine if we switched
    switched = True

    # One round of sorting
    while switched:
        switched = False
        indexA = 0
        indexB = 1

        while indexB < len(numbers):
            numberA = numbers[indexA]
            numberB = numbers[indexB]

            # If the two numbers are our of order, change them
            if numberA > numberB:
                holder = numbers[indexA]
                numbers[indexA] = numbers[indexB]
                numbers[indexB] = holder
                switched = True

            indexA += 1
            indexB += 1

    print("Sorted numbers are %s" % numbers)
    return numbers


bubblesort(numbers)
