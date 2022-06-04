# Check if is full binary tree

# 1. If root node is None, return False
# 2. If root node left and right are None, return True
# 3. if both left and right are not None, check the rest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_full_tree(root):

    # No tree!
    if root == None:
        return False

    # This is a stump
    if root.left is None and root.right is None:
        return True

    # Otherwise, both child trees need to be full
    if root.left is not None or root.right is not None:
        return is_full_tree(root.left) and is_full_tree(root.right)

    return False


# Driver Program
root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.right = Node(40)
root.left.left = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

root.left.left.left = Node(80)
root.left.left.right = Node(90)
root.left.right.left = Node(80)
root.left.right.right = Node(90)
root.right.left.left = Node(80)
root.right.left.right = Node(90)
root.right.right.left = Node(80)
root.right.right.right = Node(90)

print(is_full_tree(root))
