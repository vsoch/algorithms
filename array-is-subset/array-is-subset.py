array1 = [1,2,3]
array2 = [7,8,9,1,2,3]

# Todo: we have to determine if array 1 is a subset of array2

# Solution 1: Brute force

def is_subset(array1, array2):
    # iterate through both, continue if we have matches

    # Inidices into each array
    a1 = 0
    a2 = 0

    while a1 < len(array1) and a2 < len(array2):

        # If they don't match, continue to next in array 2
        if array1[a1] != array2[a2]:
            a2+=1

        # If they do match, take one step in both
        elif array1[a1] == array2[a2]:

            # if we are at the last index
            if a1 == len(array1) -1:
                return True

            a2+=1
            a1+=1

    return False


print(is_subset(array1, array2))


