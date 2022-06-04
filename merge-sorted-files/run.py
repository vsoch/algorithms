import heapq

# Assume the files have already been read
# We are also giving them names, index by the name
files = {"A": [3, 5, 7], "B": [0, 6], "C": [0, 6, 28]}

# Let's create an initial state
idx = {}
entries = []
for filename, values in files.items():

    # Don't add files with no values
    if not values:
        continue

    # All indices start at 0
    idx[filename] = 0

    # Each is a tuple, so tuple comparison will use the first value
    # And the filename is cached
    entries.append((values[0], filename),)

# Create the initial heap with 0 indices
heapq.heapify(entries)
answer = []

# Keep going until we've added all values from entries
while True:

    # Stopping condition
    if not entries:
        break

    # Append the smallest value
    value = heapq.heappop(entries)
    filename = value[1]
    answer.append(value[0])

    # Increment the index of the filename
    idx[filename] += 1

    # Add the new value to the heap (if it exists)
    if idx[filename] < len(files[filename]):
        new_value = files[filename][idx[filename]]
        print(f"Pushing {new_value} to {entries}")
        heapq.heappush(
            entries, (new_value, filename),
        )

print(answer)
