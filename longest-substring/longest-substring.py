#!/usr/bin/env python3

# Given a string, find longest substring without repeating characters


def longest_substring_simple(string):
    """This function is based on the idea that substrings exist in substrings,s
       so we can find the longest substring for each index i, store
       the longest in a set, and then find the very longest (for all the i's)
       in the set
    """
    # We'll eventually take longest substring of all i's
    substrings = set()

    # First idea, loop through i and j,
    for i, chari in enumerate(string):

        longest = chari

        # We only need to start at the next character
        for j in range(i + 1, len(string)):

            charj = string[j]

            # Case 1, j is already in the longest, stop
            if charj in longest:
                substrings.add(longest)
                longest = ""
                break

            # Otherwise we add to longest
            else:
                longest = "%s%s" % (longest, charj)

        # Add the longest to the list for i
        substrings.add(longest)

    # At the end we find the longest
    for substring in substrings:
        if len(substring) > len(longest):
            longest = substring

    print("The longest is %s" % longest)


def longest_substring(string):
    """We can reduce complexity to O(n) if we keep an index where the last
       value of any particular character was seen. That way we only need to loop
       through the i's once
    """
    if string == "":
        return string

    # where each character was last seen
    seen = {}
    longest = ""
    start = 0
    end = 0

    while True:

        # Check if the new ending character has been seen
        if string[end] in seen:

            # The new start is one after the previous seen
            start = seen[string[end]] + 1

        # Update seen to be the current index
        seen[string[end]] = end

        # The index doesn't include the last one, so add it
        if len(string[start : end + 1]) > len(longest):
            longest = string[start : end + 1]

        # If end goes over list length, we're done
        if end == len(string) - 1:
            break

        end += 1

    print("Longest is %s" % longest)
