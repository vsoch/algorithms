
# Compare two strings represented as linked lists
# Given two linked lists, represented as linked lists (every character is a node in linked list). Write a function compare() that works similar to strcmp(), i.e., it returns 0 if both strings are same, 1 if first linked list is lexicographically greater, and -1 if second string is lexicographically greater.

# Examples:

# Input: list1 = g->e->e->k->s->a
#       list2 = g->e->e->k->s->b
# Output: -1

# Input: list1 = g->e->e->k->s->a
#       list2 = g->e->e->k->s
# Output: 1

# Input: list1 = g->e->e->k->s
#        list2 = g->e->e->k->s
# Output: 0


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, char): 
        self.c = char
        self.next = None

def compare(str1, str2):

    # Case 1: both strings are the same, return 0
    # Case 2: first string is lexograph. greater, return 1
    # Case 3: second string is greater, return -1

    # Iterate through both until one ends, or not equal
    while (str1 and str2) and str1.c == str2.c:
        str1 = str1.next
        str2 = str2.next

    # When we get here, if both are still defined
    if (str1 and str2):
        if str1.c > str2.c:
            return 1
        return -1

    # If either ended
    if not str1:
        return -1

    if not str2:
        return 1

    return 0

# Driver program 
  
list1 = Node('g') 
list1.next = Node('e') 
list1.next.next = Node('e') 
list1.next.next.next = Node('k') 
list1.next.next.next.next = Node('s') 
list1.next.next.next.next.next = Node('b') 
  
list2 = Node('g') 
list2.next = Node('e') 
list2.next.next = Node('e') 
list2.next.next.next = Node('k') 
list2.next.next.next.next = Node('s') 
list2.next.next.next.next.next = Node('a') 
  
print(compare(list1, list2))
