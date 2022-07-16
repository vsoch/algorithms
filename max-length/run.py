mat = [[1, 2, 9], [5, 3, 8], [4, 6, 7]]
cache = {}


def get_neighbors(i, j):
    neighbors = []
    for neighbor in [[i + i, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
        check_i, check_j = neighbor
        if check_i < 0 or check_i >= len(mat):
            continue
        if check_j < 0 or check_j >= len(mat[i]):
            continue
        neighbors.append(neighbor)
    return neighbors


def find_list_at_index(i, j):
    if (i, j) in cache:
        return cache[(i, j)]
    listing = [(i, j)]
    for neighbor in get_neighbors(i, j):
        ni, nj = neighbor
        # We've found a value that increments by 1
        if mat[ni][nj] == mat[i][j] + 1:
            if (ni, nj) in cache:
                cached = cache[(ni, nj)]
            else:
                cached = find_list_at_index(ni, nj)
            listing += cached
    cache[(i, j)] = listing
    return listing


def find_maximum_length():
    max_length = -1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            length = len(find_list_at_index(i, j))
            if length > max_length:
                max_length = length
    return max_length


print(find_maximum_length())
