#### Problem: Given a string, find the longest substring without repeating characters

All of the possible substrings of the string s have some starting index i and and ending index j. The brute force solution would just be to check all of them, s[i:j]. The complexity of the brute force solution is O(n^3) because the total number of pairs is O(n^2), and each check requires iterating over the length of an entire substring (on average it has length n/2).

The main insight is: Some substrings contain other substrings, and specifically if we have one substring without repeating characters we do not need to check any of its substrings because they are all shorter and we only care about the longest substring without repeating characters.

With this insight alone we can come up with a better algorithm (improvement #1): For each possible starting index i, find the longest substring s[i:j] for some j. Then take the maximum for all possible starting indices i. Specifically, for each i we can start at j = i + 1 and add new characters one at a time (incrementing j) and keep track of seen characters with a set. When a new character is already in the set, record the length of the substring for the index i and move on to the next index. This solution has O(n^2) complexity (there are two nested loops without early stopping conditions).

Improvement #2 (more tricky, but important!): In the previous solution, we restarted the j index for each to i, once a repeated value was found. The idea here is a way to avoid this, so we can increment i without having to reset j= i + 1 (later I explain why this is strategy is correct). However, there is now an issue: If we just increment i by 1, it is not guaranteed we got rid of the repeat. For example, consider “abcbd”. When i=0, we start with j=1, and increment it, and our set of seen values starting at i is {a}, {a,b}, {a,b,c}, and finally we get the repeated value b. At this point, the problem is that we didn’t record where the first value of b is, so we can’t just increment i by 1. One way out is to increment i by 1 and remove the corresponding element from the set (a when i=0) until we reach the repeated value (in this case b). Another way is to store a map from each element to the index where it was last seen, so we can just jump to the right place (in this case i=2, since we want to skip ‘a’ and the first ‘b’). The complexity of both of these methods is O(n), since we have two iterators but each one moves over the data at most once.

This is an example of the ‘two iterators’ trick, and variations of it are common. Here are some examples:
 - https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
 - https://www.geeksforgeeks.org/count-pairs-array-whose-sum-less-x/

The idea is to have two indices moving at the same time, in such a way as to efficiently not consider all cases that can be ruled out. In the solution above, this is needed to justify the correctness of the problem. Specifically, how could we be sure that once we found a repeat, it is enough to leave j as-is, and increment i instead until we found a valid solution? The reason is that before we found the repeat (call its index j*) we knew that none of the values from i to j*-1 had any repeats. So once we found the new valid starting index i*, we knew there was no need to consider any value of j before j*. Any of these values would have just resulted in a shorter (although still valid) substring.

Variations (don’t code these, just think about how they would be different, and what the complexity is):
 - What if we want each number to be repeated no more than 3 times?
 - What if there is a 2-dimensional grid of letters, and we want the largest rectangle with unique values?
