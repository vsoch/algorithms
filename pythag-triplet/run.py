
# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

# First way is brute force

def is_triplet(array):

    # Base case, if array is under 3 elements, not possible
    if len(array) < 3:
        return False

    # Iterate through first element options
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j, len(array)): 
                A = array[i] * array[i]
                B = array[j] * array[j]
                C = array[k] * array[k]

                # generate all combinations    
                if (A + B == C) or (A + C == B) or (B + C == A):
                    print(array[i], array[j], array[k])
                    return True

    return False

print(is_triplet([3, 1, 4, 6, 5]))

# above is N^3

# Next idea - take square of every number
# sort the array of squared numbers
# set the last element to A
# find B and C

def is_triplet(array):

    if len(array) < 3:
        return False

    # Take square of all elements
    array = [A*A for A in array]

    # Sort the squared value
    array.sort()

    # Set the last element to be A (the largest)
    # A^2 = B^2 + C^2
    for i in range(len(array) - 1, 1, -1):  
        # Fix A, this is a squared
        A = array[i]

        # Start from index 0 up to A
        j = 0
        k = len(array) - 1  # last index

        # Keep going until we cross
        while j < k:
            B = array[j]
            C = array[k]

            # Check for a triple
            if (A == C + B):
                print(A, B, C)
                return True

            # Check if we need the numbers to be bigger
            elif (A > C + B):
                j = j+ 1
            else:
                k = k -1

    return False
            
    
# Driver program to test above function */ 
array = [3, 1, 4, 6, 5] 
print(is_triplet(array))
