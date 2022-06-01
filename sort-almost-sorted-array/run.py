import heapq

# These numbers are almost sorted
numbers = [3, -1, 2, 6, 4, 5, 8]

# Within 2 of the correct position
k = 2

# We want to loop through the numbers, create a heap of size k,
# and then pop out the next lowest
# this will be O(n) to go through list, O(n log k) to sort
idx = 0
h = [numbers[idx]]

# We will put our answer here
answer = []

while True:

    if not h and idx > len(numbers):
        break   
    idx += 1

    # If we don't have k yet, keep adding.
    if len(h) < k and numbers and idx < len(numbers):
        print(f'pushing {numbers[idx]} to {h}')
        heapq.heappush(h, numbers[idx])     

    # Else if it's == (and shouldn't be greater) and we have numbers left, we pop and add
    elif numbers and idx < len(numbers):
        answer.append(heapq.heappushpop(h, numbers[idx]))
        print(f'adding {numbers[idx]} to {h} and updating answer to {answer}')

    # If we don't have numbers left, and we have entries in h, just pop
    elif h:
        answer.append(heapq.heappop(h))    
        print(f'updating answer to {answer}')

print(answer)
