

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
  
# Make dummy tree
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


def find_min_depth(root):

    # Case 1: There is no root.
    if root == None:
        return 0

    # Case 2: There is a root with no children
    if root.left == None and root.right == None:
        return 1

    # Case 3 and 4, either left or right is None
    if root.left == None:
        return 1 + find_min_depth(root.right)
  
    if root.right == None:
        return 1 + find_min_depth(root.left)

    # Last case - both aren't None
    return 1+ min(find_min_depth(root.left),find_min_depth(root.right))
    
print(find_min_depth(root))
