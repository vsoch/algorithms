################################################################################
# 1. Design an algorithm to print all permutations of a string.
# For simplicity, assume all characters are unique.


def get_perms(letters):

    if not letters:
        letters = []

    if len(letters) == 0:
        return []

    if len(letters) == 1:
        return letters

    current = []

    for i in range(len(letters)):
        letter = letters[i]
        start = letters[:i]
        remaining = start + letters[i + 1 :]
        for perm in get_perms(remaining):
            current.append(letter + perm)

    return current


# This is how I'd actually do it, lol :)
from itertools import permutations

l = list(permutations("hello"))
print l


################################################################################
# 2. Given a smaller string S and a bigger string b, design an algorithm
# to find all permutations of the shorter string within the longer one.
# Print the location of each permutation.

import sys

big = "ABCDEFG"
small = "DEF"

# We know that all characters from small must be in big for at least one permutation
unique_small = set(small)
unique_big = set(big)

# If there are not enough overlaps to have a permutation, we don't have any
if len(unique_small.intersection(unique_big)) < len(unique_small):
    print ("No permutations of %s are possible to have in %s" % (big, small))
    sys.exit(0)


# Keep a list of found permutations
found = []
idxes = []

# Iterate through the length of the smaller string
perm = ""
for idx in range(len(big)):
    b = big[idx]
    next = idx + 1
    while b in small and next < len(big):

        # Stopping case, we found a permutation
        if len(perm) == len(small):
            found.append(perm)
            idxes.append(idx)
            perm = ""

        # if different lengths, still looking
        if big[next] in small:
            print ("%s in %s" % (big[next], small))
            perm += big[next]

        # Update character (b) and next index (next)
        b = big[next]
        next = next + 1


## Sorting

A = "AAACCDEGEFDGBBBAAACCCDDD"


def insertion_sort(A):

    if not isinstance(A, list):
        A = list(A)

    # Grab first set of two in pair
    for a in range(len(A) - 1):

        # Grab second in pair
        for b in range(a + 1, len(A)):

            # If the second is less than the first, swap
            if A[b] < A[a]:
                A[b], A[a] = A[a], A[b]

    return A


# Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class LinkedList(object):
    def __init__(self):
        self.start_node

    def add(self, value):

        if self.start_node is None:
            node = Node(value)
            self.start_node = node
        else:

            end_node = None
            contender = self.start_node

            # Traverse to end of linked list
            while end_node is None:
                if contender.right is None:
                    end_node = contender

            # Create a new node
            node = Node(value, left=contender)
            print ("Added node %s" % node)

    def remove_by_value():
        pass
