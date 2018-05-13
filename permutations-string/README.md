# Permutations of a String

> Generate all permutations of a string

We can do this recursively:

## Approach 1

 1. Start with string, chop off i'th letter
 2. For each permutation, add the i'th letter to beginning
 3. Stop at one letter


```python
def generate_permutations(S):

    perms = []

    if len(S) == 1:
        return [S]

    elif len(S) == 0:
        return []

    for i in range(len(S)):
        letter = S[i]
        remainder = S[:i] + S[i+1:]
        for perm in generate_permutations(remainder):
            perms.append(letter + perm)

    return perms
```
