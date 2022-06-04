#!/usr/bin/env python

numbers = [0, 1, 5, 3, 6, 3, 2, 7]


def mergesort(numbers):

    # Only need to split if more than one element
    if len(numbers) > 1:
        midpoint = int(len(numbers) / 2)
        left = numbers[0:midpoint]
        right = numbers[midpoint:]

        # Recursively call merge sort (list will be updated)
        mergesort(left)
        mergesort(right)

        # Now left and right are sorted, we need to combine them
        # i is index into left, j is index into right, k is index into numbers
        i = j = k = 0

        while i < len(left) and j < len(right):
            # if the left side is smaller
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        # We could have leftover elements in left or right
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

    return numbers


print(mergesort(numbers))
