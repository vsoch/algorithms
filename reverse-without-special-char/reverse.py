
# Given a string, that contains special character together with alphabets 
# (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that 
# special characters are not affected.


def reverse_string(string):

    # Idea: iterate through string from both sides
    
    # First turn string into a list
    lst = [x for x in string]

    # Start on both sides, these are indices
    left = 0
    right = len(lst) - 1

    # While we haven't crossed over
    while left < right:

        # Check if left is alphanumeric, if so, do nothing
        if not lst[left].isalpha():
            left = left + 1
  
        elif not lst[right].isalpha():
            right = right - 1
 
        # Otherwise, they both are alpha numeric, and we can switch
        else:
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
            left += 1

    return ''.join(lst)
  
print(reverse_string("a,b$c"))
print(reverse_string("Ab,c,de!$"))
assert(reverse_string("a,b$c") == "c,b$a")
assert(reverse_string("Ab,c,de!$") == "ed,c,bA!$")
