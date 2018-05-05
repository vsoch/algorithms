# Example: Design an algorithm to print all permutations of a string. For simplicity, assume all char-
# acters are un ique.

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
        remaining = start + letters[i+1:]
        for perm in get_perms(remaining):
            current.append(letter + perm)

    return current
 

# This is how I'd actually do it, lol :)
from itertools import permutations
l = list(permutations('hello'))
print l
