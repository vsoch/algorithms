# Returns the maximum value that can be put in a knapsack of max_weight
def knapsack(max_weight, weights, values, n): 
  
    # base case - max weight is 0 or number of items is 0
    if max_weight == 0 or n == 0:
        return 0

    # Check if the last item in the list is greater than capacity
    # We do this assuming the list is sorted
    if weights[n-1] > max_weight:
        return knapsack(max_weight, weights, values, n-1)
    
    # In the other case, we want to return the maximum value for two cases 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(values[n-1] + knapsack(max_weight - weights[n-1], weights, values, n-1), # included
                   knapsack(max_weight, weights, values, n-1))
    
values = [60, 100, 120] 
weights = [10, 20, 30] 
max_weight = 50
n = len(values)
print(knapsack(max_weight , weights , values, n)) 
