# Longest K Unique Characters Substring

Given a string you need to print the size of the longest possible substring that has exactly k unique characters.
If there is no possible substring print -1.

## Example

For the string `aabacbebebe` and k = 3 the substring will be cbebebe with length 7.
Specifically, there are three unique characters (c, b, and e) and they create a substring of length 7.
We assume that we aren't reordering the string. I first started out with this approach:

```python
S='aabacbebebe'

k=3
longest=-1    # keep record of the longest
start=0       # start of the current substring being evaluated
chars=set()   # keep a record of characters that we've seen

def update_longest(start, end, S, longest):
    contender = S[start:end]
    if longest == -1:
        return contender
    if len(contender) > len(longest):
        longest=contender
    print('New longest is %s' %longest)
    return longest


for idx in range(len(S)):
    s = S[idx]

    # The character is in the current substring
    if s in chars:
        print('%s is in %s, continuing' %(s, chars))
        longest = update_longest(start, idx, S, longest)
    else:
        # S isn't one of the characters, and we are at stopping point
        if len(chars) == k:
            print('final evaluation of %s,%s' %(s, chars))
            end = 0
            if idx > 0:
                end = idx-1
            longest = update_longest(start, end, S, longest)
            start=idx
            chars=set(s)
        else:
            chars.add(s)
            longest = update_longest(start, idx, S, longest)
            print('added %s,%s' %(s, chars))
```

And I continually would get an answer that didn't seem to move along the string (e.g., 

```bash
added a,{'a'}
a is in {'a'}, continuing
New longest is a
New longest is aa
added b,{'b', 'a'}
a is in {'b', 'a'}, continuing
New longest is aab
New longest is aaba
added c,{'c', 'b', 'a'}
b is in {'c', 'b', 'a'}, continuing
New longest is aabac
final evaluation of e,{'c', 'b', 'a'}
New longest is aabac
New longest is aabac
added b,{'b', 'e'}
e is in {'b', 'e'}, continuing
New longest is aabac
b is in {'b', 'e'}, continuing
New longest is aabac
e is in {'b', 'e'}, continuing
New longest is aabac
```

Crap, the reason is because when we hit the case that the number of unique characters is equal to k, and the new one isn't in k, I am setting the
start to be that current index. The problem with this is that it could be the case that we could step back along the string and grab some k-N characters that, along with our new k, would be the solution! I decided to rethink the problem at this point. You see, I'm very block headed
it comes to algorithms. If the solution isn't something simple that I can think of today and then remember tomorrow, 
it's not a good solution for me. Instead of trying to shove all this logic into one complicated loop, I decided to step
back and think of the problem much more simply.  Gogo Dinosaur Strategy Session!

### Strategy:
Hello my name is strategy! I don't remember complicated things, but I like simple ALOT. Today we are going to:

1. generate all substrings
2. count unique characters
3. The longest one with k wins!

```
def generate_substrings(S, k=3):
    substrings = []

    # Case 1: fewer characters in S than k, impossible
    if len(S) < k:
        return substrings
    # Case 2: if the substring is == k, then it's the only option
    elif len(S) == k:
        return [S]

    # Case 3: we can generate substrings!
    for s1 in range(len(S)):
        substrings.append(S[s1:])
    return substrings

```

This would produce this output:

```python
$ generate_substrings(S)

['aabacbebebe',
 'abacbebebe',
 'bacbebebe',
 'acbebebe',
 'cbebebe',
 'bebebe',
 'ebebe',
 'bebe',
 'ebe',
 'be',
 'e']
```

Note that we aren't considering the number of unique characters, actually if 
the length of the above is less than our k, it's impossible to have three unique,
so let's filter those out.

```python
def generate_substrings(S, k=3):
    substrings = []

    # Case 1: fewer characters in S than k, impossible
    if len(S) < k:
        return substrings
    # Case 2: if the substring is == k, then it's the only option
    elif len(S) == k:
        return [S]

    # Case 3: we can generate substrings!
    for s1 in range(len(S)):
        if len(S[s1:]) >= k:
            substrings.append(S[s1:])
    return substrings
```

Now we get a slightly smaller list:

```python
$ generate_substrings(S)

['aabacbebebe',
 'abacbebebe',
 'bacbebebe',
 'acbebebe',
 'cbebebe',
 'bebebe',
 'ebebe',
 'bebe',
 'ebe']
```

Okay, so now we want to just find the longest with k unique. Let's do that.

```
substrings = generate_substrings(S, k=3)
longest = -1

for contender in substrings:
    unique_chars = len(set(contender))
    # Condition 1: the number of characters must be less than = k
    if unique_chars == k:
        # Case 1: we don't have a longest. Now we do
        if longest == -1:
            longest = contender
        # Case 2: the new string is longer
        elif len(contender) > len(longest):
            longest = contender
```

We can then run the above and get the longest, 'cbebebe'. I realize that it's 
probably not super efficient to do this in two steps - generating
all the substrings and then testing, but it's so much more clean and logical, and
so is a solution I'm happy with.
