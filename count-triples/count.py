# Given an array of distinct integers and a sum value. Find count of triplets 
# with sum smaller than given sum value. Expected Time Complexity is O(n2).

sum_value = 2
array = [-2, 0, 1, 3]

# goal is to return count


def count_triples(array, sum_value):

    count = 0

    # If no triples, return 0
    if len(array) < 3:
        return count
 
    # Here we know the array is 3 or more

    # Fix the first number
    for F in range(0, len(array) - 2):
        # Fix the second number
        for S in range(F+1, len(array) -1):
             # Fix the last number
             for L in range(S+1, len(array)):
                 # If the sum is less than sum_value, add to count
                 if (array[F] + array[S] + array[L]) < sum_value:
                     count+=1
        
    return count

print(count_triples(array, sum_value))

array = [5, 1, 3, 4, 7] 
sum_value = 12
print(count_triples(array, sum_value)) 

# Complexity above is N^3
  

def count_triples(array, sum_value):
 
    # Sort the array first
    array.sort()

    count = 0 

    # Choose the first element
    for F in range(0, len(array)-2):
        # Fix the next elements
        S = F + 1
        T = len(array) - 1      
          
        # While the element on the right doesn't cross over
        while T > S:
            # If the sum is greater than or equal to sum value, need to 
            # decrease second element
            if (array[F] + array[S] + array[T]) >= sum_value:
                T-=1
            # Otherwise, add number of elements in range to count and move left value
            else:
                count+=(T-S)
                S+=1

    return count
  
array = [5, 1, 3, 4, 7]  
print(count_triples(array, 12))
