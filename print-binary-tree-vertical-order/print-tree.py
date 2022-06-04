# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/

# First create a node, should hold left and right


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


"""
           1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9               
"""

# Create a tiny tree to test

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)
root.right.right.rigt = Node(9)

# The general idea is to store a dictionary of distances, and each has
# a list of nodes of that distance


def getVerticalOrder(root, horizontal_distance, lookup):

    # If no tree, no result
    if root is None:
        return

    # Whatever node we are at, add its distance
    try:
        lookup[horizontal_distance].append(root.value)
    except:
        lookup[horizontal_distance] = [root.value]

    # Store nodes in left and right
    getVerticalOrder(root.left, horizontal_distance - 1, lookup)
    getVerticalOrder(root.right, horizontal_distance + 1, lookup)


def printVerticalOrder(root):

    lookup = dict()
    horizontal_distance = 0
    getVerticalOrder(root, horizontal_distance, lookup)

    # Traverse the map and print nodes at every horizontal
    # distance (hd)
    for index, value in enumerate(sorted(lookup)):
        output = [str(x) for x in lookup[value]]
        print(" ".join(output))


printVerticalOrder(root)

"""
4
2
1 5 6
3 8
7
"""
