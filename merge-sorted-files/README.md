# Merge Sorted Files

We have two files with numbers in sorted order, and we want to assemble them 
into one final sorted file.

*Thinking* 

The brute force approach would assemble all of the files into one list, and
then sort. This would be complexity Nlog(N). But can we do better?

I think so - the trick is to think of a way to walk through all of the separate
lists (sort of) at the same time, and always be able to add the smallest one.
I just learned about heaps, and I think we could try:

1. Starting at an index of 0 for all files
2. Adding all the values here to a min heap, and making sure to capture the list the value is from
3. Popping out the smallest, adding to out final list, and incrementing the index for that file
4. Keeping going until each file has no more values (so it's removed from being a contender) and the final list is done (min heap is empty)

If it takes O(N) to go through the longest list, where N is the longest list,
and it takes O(K) to build the heap, where K is the number of files, then the complexity
is around O(N) + O(K). 
