# Two Sum

> Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

```python
N= [0, 1, 1, 3, 3, 4, 5]
target = 4
```
```python

# Naive, and brute force and inefficient

seen = []
pairs = []
for i in range(len(N)):
    n1 = N[i]
    for j in range(len(N)):
       n2 = N[j]
       if n1 + n2 == target:
           if i not in seen and j not in seen:
               seen = seen + [i,j]
               pair = (i,j)
               pairs.append(pair)
               print(pair)
```
```
# The print output when running the function
(0, 5)
(1, 3)
(2, 4)
```

and here is a quick way to check:
```python

for pair in pairs:
    i = pair[0]
    j = pair[1]
    print('%s + %s = %s' %(N[i], N[j], target))
```
```
0 + 4 = 4
1 + 3 = 4
1 + 3 = 4
```

We see that each pair of indices above, when indexing the array, adds up to 4.

A slightly better idea, we can create a lookup to get the index. If we do this once,
we don't need to do it again.

## Step 1: construct lookup

```python

lookup = dict()

for i in range(len(N)):
    n1 = N[i]

    # We can look up the index for the element based on the element

    # If we already have seen it:
    if n1 in lookup:
        lookup[n1].append(i)
    else:
        lookup[n1] = [i]
```
```
lookup
# {0: [0], 1: [1, 2], 3: [3, 4], 4: [5], 5: [6]}
``` 

## Step 2: Pair Elements

Choose a single target for each, find in lookup.

```
# Keep a list of paired elements
pairs = []

for i in range(len(N)):
    n1 = N[i]
    n2 = target - n1   # the other number we need

    # We know n1 is in the lookup, but did we use it?
    if len(lookup[n1]) > 0:

        # is it a number we have?
        if n2 in lookup:

            # Have we used all the elements?
            options = lookup[n2]

            # Do we have options left?
            if len(options) > 0:
                pair1 = lookup[n1].pop(0)
                pair2 = options.pop(0)
                pairs.append((pair1,pair2))
```

## Step 3: Check output

```
for pair in pairs:
    i = pair[0]
    j = pair[1]
    print('%s + %s = %s' %(N[i], N[j], target))
```
```
0 + 4 = 4
1 + 3 = 4
1 + 3 = 4
```
