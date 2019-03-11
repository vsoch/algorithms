#!/usr/bin/env python

# We have a container of capacity N, and some number of values with weights
values = [60, 100, 120] 
weights = [10, 20, 30] 

# We want to put items up to a maximum weight
max_weight = 50

# N is index of items we are checking
n = len(values) 

def knapsack(max_weight, weights, values, n):

    # Case 1: the max weight is zero, or items is 0
    if n == 0 or max_weight == 0:
        return 0
  
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (weights[n-1] > max_weight): 
        return knapsack(max_weight, weights, values, n-1) 
  
    # return the maximum of two cases: if nth item is included or not    
    else: 
        return max(values[n-1] + knapsack(max_weight-weights[n-1] , weights, values, n-1), 
                   knapsack(max_weight , weights , values, n-1)) 


print(knapsack(max_weight , weights, values, n))
