#!/usr/bin/env python


numbers = [2, 4, 3, 9, 5, 2, 7, 1, 1, 9, 5, 3]


def insertionsort(numbers):

    # Walk through list of numbers (skip over first),
    for idx in range(1, len(numbers)):
        number = numbers[idx]

        previous_index = idx - 1

        # Keep going until we reach 0 index, and our number is smaller (and should be to the left)
        while previous_index >= 0 and number < numbers[previous_index]:
            # Move backtrack forward one

            numbers[previous_index + 1] = numbers[previous_index]
            previous_index -= 1
        numbers[previous_index + 1] = number

    return numbers


print(insertionsort(numbers))
