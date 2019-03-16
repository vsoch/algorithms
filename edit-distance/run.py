# Find the minimum number of operations to convert string 1 to string 2

str1 = "sunday"
str2 = "saturday"


# If last characters of two strings are same, nothing much to do. 
# Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
# Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
# Insert: Recur for m and n-1
# Remove: Recur for m-1 and n
# Replace: Recur for m-1 and n-1

# n and m are used as indices so we don't have to keep track of cutting strings
def edit_distance(str1, str2, m, n):

    # If either string is empty, the answer is length of the other string
    # because we would have to insert that many
    if m == 0:
        return n
    if n == 0:
        return m

  
    # If last two characters are same, just compare for the rest of the string
    if str1[n-1] == str2[m-1]:
        return edit_distance(str1, str2, m-1, n-1)
  
    # If characters aren't the same, just consider all the options
    # these are relative to string 2
    return 1 + min(edit_distance(str1, str2, m, n-1),       # insert
                   edit_distance(str1, str2, m-1, n),       # remove
                   edit_distance(str1, str2, m-1, n-1))     # replace

  
# Driver program to test the above function (start at lengths)
print(edit_distance(str1, str2, len(str2), len(str1)))


def edit_distance(str1, str2, m, n):

    # n is rows
    # m is columns

    # Create a matrix of values coinciding with the prefix / letters of the words
    # We add one more to account for the empty string
    df = [[ x for x in range(0, n+1)] for y in range(0,m+1)]

    # Go through grid of prefixes
    for i in range(0, m+1):
        for j in range(0, n+1):
        
            # If n is an empty string, the edit distance is the length of m
            if i == 0:
                df[i][j] = j

            # Same with j
            elif j == 0:
                df[i][j] = i

            # If they are both the same, we don't do anything
            # We go diagonally one back
            elif str2[i-1] == str1[j-1]:
                df[i][j] = df[i-1][j-1]

            # Otherwise, we take the minimum of three options
            else:
                df[i][j] = 1+ min(df[i][j-1], df[i-1][j], df[i-1][j-1]) 
            

    return df[m][n]

print(edit_distance(str1, str2, len(str2), len(str1)))
