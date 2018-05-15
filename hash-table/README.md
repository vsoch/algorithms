# Hash Table

A hash table is a dictionary. We can implement a simple one on our own!

## Assumptions
 
 - I know the size of the set of values to create table for in advance


```python
## Implementation of dictionary with a hash map

class HashEntry(object):
  
    def __init__(self):
        self.key_value_pairs = []
  
class HashTable(object):

    def __init__(self, length):
      
        self.length = length
        self.table = [HashEntry() for x in range(self.length)]


    def hash_function(self, number):
        '''hash function for a number.
        '''
        return number%self.length

      
    def add(self, key, value):
        hash_value = self.hash_function(key)
        entry = self.table[hash_value]
        
        ## First check if the key is present in the HashEntry.
        ## If it exists, replace it.
        for i, (k, v) in enumerate(entry.key_value_pairs):
            if k == key:
                entry.key_value_pairs[i] = (key, value)
        ## If the key is not present, add a new key, value pair.
        else:
            entry.key_value_pairs.append((key, value))
            
    def get(self, key):
        hash_value = self.hash_function(key)
        entry = self.table[hash_value]

        for i, (k, v) in enumerate(entry.key_value_pairs):
            if k == key:
                return entry.key_value_pairs[i][1]
        else:
            raise ValueError("Key %s not found." %key)
```

Testing

```
hashy = HashTable(100)
hashy.add(179, "hi")
hashy.get(179)
# 'hi'
```
