#!/usr/bin/env python

def lcs(A, B, n, m):
    # X is a sequence A
    # Y is a sequence, B
    # n is the starting index into A 
    # m is the starting index into B

    # Case 1, one of them doesn't have length
    if n == 0 or m == 0:
        return 0

    # Case 2: the last two characters are the same
    elif A[n-1] == B[m-1]:
        return 1 + lcs(A, B, n-1, m-1)

    # Otherwise, return the max of taking either of the last
    else:
        return max(lcs(A[:-1], B, n-1, m), lcs(A, B[:-1], n, m-1))


X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)))
