# Insert a new number into a sorted Linked List
# sorted in increasing order

# 1. If list is empty, new node is head node.
# 2. If head node is already larger, then just push the node before it.
# 3. If head node is smaller, walk along list until find right spot

# This doesn't work and I'm too stupid to figure out why. Seriously
# somebody should just shoot me in the face right now.
# https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    # Create a new linked list, with a head node
    def __init__(self):
        self.head = None

    def sorted_insert(self, node):

        # Case 1: we don't have a head node!
        if self.head is None:
            node.next = self.head
            self.head = node

        elif self.head.value >= node.value:
            node.next = self.head
            self.head = node

        # Case 3: we need to walk along the list until the current value
        else:

            current = self.head

            while current.next is not None and current.next.value < node.value:
                current = current.next

            # When the loop breaks, either the next is None, or our node value is greater
            node.next = current.next
            current.next = node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next


llist = LinkedList()
new_node = Node(5)
llist.sorted_insert(new_node)
new_node = Node(10)
llist.sorted_insert(new_node)
new_node = Node(7)
llist.sorted_insert(new_node)
new_node = Node(3)
llist.sorted_insert(new_node)
new_node = Node(1)
llist.sorted_insert(new_node)
new_node = Node(9)
llist.sorted_insert(new_node)
print("Create Linked List")
llist.printList()
