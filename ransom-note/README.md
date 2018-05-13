# Ransom Note

> Example: A ransom note can be formed by cutting words out of a magazine to form a new sentence. How would you figure out if a ransom note (represented as a string) can be formed from a given magazine (string)?


## Assumptions

 - We have to assume that the count of the words is relevant (e.g., if I use a word from the magazine and there is only one, I can't use it again)
 - Empty string is not a word
 - The note is not empty, meaning that the empty string cannot be considered a valid note
 - Since we cut out of the magazine, capitalization is important.

Let's simplify the problem by changing it to:


> How would you figure out if a string can be formed from a given string (group of letters)?

## Approach

 1. Create count
 2. Have data structure to hold counts
 3. Iterate through the string and update the data structure
 4. If we hit a 0 and we need a letter, we fail
 5. If we make it through the whole thing, success

```python

def is_cut_from_magazine(magazine, note):

    # Dictionary of counts
    counts = dict()

    for letter in magazine:
        if letter in counts:
            # Add 1 to the count
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Could the magazine have created the note?
    possible = True

    # Case 1: Letter is empty
    if len(letter) == 0:
        possible = False

    for letter in note:
        if letter in counts:
            counts[letter]-=1
            if counts[letter] < 0:
                possible = False
                break
        else:
            possible = False
            break

    print("Can the note be formed from the magazine? %s" %possible)
    return possible
```

### Example Where it Can be Cut

```python
magazine = 'tejumpedbthhappyerolazywwasuovericnkqfogxohdheand'
note = 'jumpifyoudare'

is_cut_from_magazine(magazine, note)
# Can the note be formed from the magazine? True
# True
```

### Example Where it Cannot

```python
magazine = 'tejumpedbthhappye'
note = 'jumpifyoudarezzzzzz'
is_cut_from_magazine(magazine, note)
False
```

# Extend to words
We now need to tweak the problem to be about words and not letters. This is fairly
easy, except instead of keeping a count of strings, we keep a count of words. We also
care about capitalization, since cutting "Apple" from a magazine is different than cutting
"apple." This just means we won't take the lowercase of the content. And you know what else
this means? The equation doesn't change at all! That's pretty neat :)

```python
magazine = ['I', 'wonder', 'as', 'I', 'wander']
note = ['I', 'wander']
is_cut_from_magazine(magazine, note)
# Can the note be formed from the magazine? True
# True
```

```python
magazine = ['I', 'wonder', 'as', 'I', 'wander']
note = ['I', 'wander', 'where', 'my', 'shoes', 'are']
is_cut_from_magazine(magazine, note)
# Can the note be formed from the magazine? False
# False
```
