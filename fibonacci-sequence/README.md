# Fibonacci's Sequence

I think this would best be done recursively! As a reminder, Fibonacci's Sequence:

```bash
0 1 1 2 3 5 8 13...
```

Let's write a function to return the sequence for N characters.


```python


def fibonacci(N):
    first = 0
    second = 1
    count = 0
    sequence = [first, second]

    while count < N:
        sequence.append(first+second)

        # Second number becomes the new first
        holder = first
        first = second
        second = holder+second
        count+=1

    return sequence

```

Now let's write a function to return the number of the Nth character.


```python


def fibonacci(N):

    # Base cases
    if N in [0,1]:
        return N

    # Otherwise, return previous two fibonacci numbers
    return fibonacci(N-1) + fibonacci(N-2)


```
