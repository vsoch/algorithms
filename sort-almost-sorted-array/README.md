# Sort Almost Sorted Array

We have a really long sequence of N numbers, they are _almost sorted_ and we want
to print them in sorted order. We are confident that each number is within k positions
of its correct location.

```
pushing -1 to [3]
adding 2 to [2, 3] and updating answer to [-1]
adding 6 to [3, 6] and updating answer to [-1, 2]
adding 4 to [4, 6] and updating answer to [-1, 2, 3]
adding 5 to [5, 6] and updating answer to [-1, 2, 3, 4]
adding 8 to [6, 8] and updating answer to [-1, 2, 3, 4, 5]
updating answer to [-1, 2, 3, 4, 5, 6]
updating answer to [-1, 2, 3, 4, 5, 6, 8]
[-1, 2, 3, 4, 5, 6, 8]
```
