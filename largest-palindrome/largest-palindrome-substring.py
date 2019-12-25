
# Problem: Given a string, find the longest palindrome substring

def is_palidrome(string):
    """A helper function to go from ends to middle to check if palindrome.
    """
    start = 0
    end = len(string) - 1

    while start <= end:
        if string[start] != string[end]:
            return False
        start+=1
        end-=1
    return True


def longest_palidrome_brute_force(string):
    """The brute force solution takes two indices, i and j, and checks
       all possible substrings to see if we have a palidrome.
       Since we need to loop through the string length twice, and then
       check all characters between i and j (on average N/2) this is
       complexity N^3
    """
    longest = 0
    winner = ""

    for i in range(len(string)):
        for j in range(len(string)):
            substring = string[i:j+1]
            if is_palidrome(substring):
                if len(substring) > longest:
                    winner = substring
                    longest = len(substring)

    print("The longest palindrome substring is %s" % winner)


def longest_palindrome_substructure(string):
    """The insight is that there is substructure. For example, if I know that
       abcba is a palidrome, I also know that bcb is a palindrome (i+1 and j-1)
       and don't need to check it again. I think this turns the problem
       into one where we can use dynamic programming (with a matrix) to figure
       out if an inner string is a palindrome.
    """
    lookup = dict()

    # We'll use a dictionary to store lookups of coords.
    # First index i is length, indexes list of tuples with (i,j) coords of palindromes
    for i in range(len(string)):
        lookup[i] = []

    # Length 1
    for i in range(len(string)-1):
        lookup[1].append((i, i+1))

    # Length 2
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            lookup[2].append((i, i+2))

    # Now length 3 through N
    for length in range(3, len(string) + 1):
        # Look at lengths that are two sizes smaller (and check edges)
        coords = lookup[length-2]
        # For each set of coords, check the outer characters
        for coord in coords:
            i = coord[0] - 1
            j = coord[1] + 1

            # Must be in bounds to check
            if i > 0 and j < len(string):
                if string[i] == string[j]:
                    lookup[length].append((i,j))

    # Find the longest (could be more than one)
    for i in range(len(string) -1, 0, -1):
        if len(lookup[i]) > 0:
            print("Found longest palidrome for length %s" % i)
            [print("%s\n" % string[e[0]:e[1]+1]) for e in lookup[i]]
            break
