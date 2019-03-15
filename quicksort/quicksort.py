#!/usr/bin/env python

# 1. Choose a pivot - all items to the left will be smaller, right will be greater
# 2. choose a number randomly (the last one) and this will be the pivot
# 3. choose an item from the left, and the right (moving inward) that is smaller and larger than the pivot, switch them
# 4. When the left index crosses over the right, just switch left and pivot. 
 
def partition(array, low, high):

    # The pivot is at the high
    pivot = array[high]
    leftMarker = low
    rightMarker = high - 1
     
    while True:
        

        # Find the first element from the left that may need to be swapped
        while array[leftMarker] < pivot and leftMarker < rightMarker:
            leftMarker +=1

        # Find the first element from the right that may need to be swapped
        while array[rightMarker] > pivot and leftMarker < rightMarker:
            rightMarker -=1
            
        # In the special case the markers meet, we know everything to the left
        # is smaller than the pivot, and everything to the right is bigger.
        # So we swap the pivot with the rightMarker, and return its location.
        if leftMarker >= rightMarker:
            array[rightMarker], array[high] = array[high], array[rightMarker]
            return rightMarker

        # If we reach here, it means the leftMarker and rightMarker both need
        # to be swapped to get the order we want.
        array[leftMarker], array[rightMarker] = array[rightMarker], array[leftMarker]
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quicksort(array, low, high):

    if low < high:
 
        # We want to partition, so partition is at right spot (splits in half)
        new_partition = partition(array, low, high)
 
        # Recursively call quicksort on the rest
        quicksort(array, low, new_partition - 1)
        quicksort(array, new_partition + 1, high)
 
# Driver code to test above
array = [10, 7, 8, 9, 1, 5]
n = len(array)  # 6
low = 0    
high = n - 1  # 5
quicksort(array, low, high)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %array[i], end = " ")
