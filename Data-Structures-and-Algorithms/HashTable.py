'''
Key/Value Pair

Search: O(1)
Insert: O(1)
Space: O(n)
Delete: O(1)

An element is converted into an integer by using a hash function.
This element can be used as an index to store the original element, which falls into the hash table.

Applications:
    Associative Arrays
    Database Indexing
    Caches
    Object Representation
'''

# HashTable() can create a new hash table that is empty.
# It needs no parameters and returns an empty hash table.
class HashTable:

    def __init__(self):
        self.size = 256
        self.hashmap = [[] for _ in range(0, self.size)]

    def hash_func(self, key): # Converting range of keys into a range of Key Values.
        hashed_key = hash(key) % self.size # It needs key as a parameter and returns a hashed key.
        return hashed_key
    
    # Setting a Key Value pair in the Hash Table.
    def __setitem__(self, key, value):  # It needs key and value as parameters and returns nothing.
        hash_key =  self.hash_func(key) # Calling hash_func() to convert key into hashed key.
        key_exists = False
        for i, key_value in enumerate(self.hashmap[hash_key]):
            if len(key_value) == 2 and key_value[0] == key:
                self.hashmap[hash_key][i] = (key, value)
                key_exists = True
        if not key_exists:
            self.hashmap[hash_key].append((key, value)) # Hash Table is modified.

    # Getting a value from the Hash Table using Key.
    def __getitem__(self, key): # It needs key as a parameter and returns the value associated to that key.
        hash_key = self.hash_func(key)  # Calling hash_func() to convert key into hashed key.
        key_exists = False
        for key_value in self.hashmap[hash_key]:
            if key_value[0] == key:
                return key_value[1] # Hash Table is not modified.
        raise KeyError('Does not exist!')   # Raise Key Error if Key not found in Hash Table.
    
    # Deleting a Key Value pair from the Hash Table.
    def __delitem__(self, key): # It needs key as a parameter and returns nothing.
        hash_key = self.hash_func(key)  # Calling hash_func() to convert key into hashed key.
        key_exists = False
        for i, key_value in enumerate(self.hashmap[hash_key]):
            if key_value[0] == key:
                del self.hashmap[hash_key][i]   # Hash Table is modified.
                key_exists = True
        if not key_exists:
                raise KeyError('Does not exist!')   # Raise Key Error if key not found in Hash Table.