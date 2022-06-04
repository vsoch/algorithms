def maximum_subarray(array):
    # Walk through array and keep track of max seen, and max that ends at each location
    max_seen, max_end = 0, 0
    B = []
    for number in array:
        max_end = max(number, number + max_end)
        max_seen = max(max_seen, max_end)
        B.append(max_end)
    return max_seen, B


array = [904, 40, 523, 12, -335, -385, -124, 481, -31]
print(maximum_subarray(array))

array = [-2, 3, 1, -7, 3, 2, -1]
print(maximum_subarray(array))
