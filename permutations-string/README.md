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


## Approach 2

I have a lot of trouble getting my head around recursion, so I want to do a second
(simpler) way as well. One that fits nicely into a for loop :)

 1. Take the first letter off the string
 2. Iterate through the remaining letters, insert the first letter in all spots, add to list

```python
def generate_permutations(S):
    if len(S) == 0:
        return []
    elif len(S) == 1:
        return [S]

    # List to store permutations, will be updated
    perms = [S[0]]

    # Iterate through current letters
    for i in range(1, len(S)):
    
        # The current letter
        letter = S[i]

        # Let's keep a new list of permutations
        permutations = []

        # iterate through known permutations
        for perm in perms:

            # Put the letter in all known spots
            for loc in range(len(perm)+1):
                new_permutation = perm[:loc] + letter + perm[loc:]
                permutations.append(new_permutation)

        # Update permutations
        perms = permutations
    return perms
```
