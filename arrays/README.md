# The Next Largest Element

> Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1

 - From (https://www.geeksforgeeks.org/next-greater-element/)[https://www.geeksforgeeks.org/next-greater-element/]

## Assumptions
We can make the following assumptions from the problem

 - distinct elements means that we have integers, and they are unique
 - order of appearance is important, so we can't sort at the beginning and lose that order

## Naive Implementation
Here is me trying this intuitively.

```
# Strategy 1: Loop to find!

A = [5,1,2,3,4]

for i in range(len(A)):

    # Set next greater as default to -1, in case we don't find answer
    next_greater = -1

    first_number = A[i] 

    # Iterate now from (one after) current to end
    for j in range(i+1, len(A)):
        second_number = A[j]
        if second_number > first_number:
            next_greater = second_number
            break

    print('The next greatest number for %s is %s' %(first_number, next_greater))  
```
```
The next greatest number for 5 is -1
The next greatest number for 1 is 2
The next greatest number for 2 is 3
The next greatest number for 3 is 4
The next greatest number for 4 is -1
```

We can now put this into a function and list, since I think that's what is wanted.

```python
def next_largest_element(A):

    # A list of the next largest elements, for each
    nexts = []

    for i in range(len(A)):

        # Set next greater as default to -1, in case we don't find answer
        next_greater = -1

        first_number = A[i] 

        # Iterate now from (one after) current to end
        for j in range(i+1, len(A)):
            second_number = A[j]
            if second_number > first_number:
                next_greater = second_number
                break

        nexts.append(next_greater)
    return nexts

# How to use it
A = [5,1,2,3,4]
nexts = next_largest_element(A)
#  [-1, 2, 3, 4, -1]
```

We would have a much easier time if we could sort this, but we can't because the ordering is
important. So let's just remember the ordering then!

```
A = [5,1,2,3,4]
lookup = dict()

# Create a lookup dictonary of indices where the element lives
# We know there aren't repeats
for i in range(len(A)):
    element = A[i]
    lookup[element] = i

# Sort A now and loop through it only up to itself
A.sort()

# We need 2 elements minimally
while len(A) > 0:

    # Set next greater as default to -1, in case we don't find answer
    first_number = A.pop(0)
    next_greater = -1


    if len(A) > 0:
        next_number = A[0]    

        first_index = lookup[first_number]
        next_index = lookup[next_number]
        if next_index > first_index:
            next_greater = A[0]
    print('The next greatest number for %s is %s' %(first_number, next_greater))  
```
```
The next greatest number for 1 is 2
The next greatest number for 2 is 3
The next greatest number for 3 is 4
The next greatest number for 4 is -1
The next greatest number for 5 is -1
```
