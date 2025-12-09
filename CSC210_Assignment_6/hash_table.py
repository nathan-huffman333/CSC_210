# hash_table.py
# implementation of simple hash table
# we'll use separate chaining with Python's built-in 
# list type acting as the chains
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a data structure yourself is the best
# way to learn how it works.
# Modified by: Nathan Huffman
from random import randint

class HashTable:
    MAX_LOAD_FACTOR = 0.7
    GROWTH_FACTOR = 2

    def __init__(self, slots = 10):
        self.slots = slots
        self.num_items = 0
        self.backing_store = [[] for _ in range(slots)]

    def _hash(self, key):
        return hash(key) % self.slots


    def insert(self, key, value): # Allows for a new key-value pair to be inserted into the hash table.
        index = self._hash(key) # The hash function is called to determine what index the appropriate key should be inserted to.
        
        for i, (k, v) in enumerate(self.backing_store[index]): # Loops through the key value pairs looking for a duplicate key.
            if k == key: # If the key is found... 
                self.backing_store[index][i] = (key, value) # ...replace the value assigned to it with the new value.
                return 
        
        self.backing_store[index].append((key, value)) # Otherwise, if the key is not found, simply append it to the end of the list.
        self.num_items += 1 # Update to the correct number of items.

        if (self.num_items / self.slots) > self.MAX_LOAD_FACTOR: # If the ratio of the number of items vs. the number of total slots exceeds the max load factor...
            self._resize() # ...call the resize function to enlarge the hash table.
    

    def get(self, key): # Used to return the value associated with the key
        index = self._hash(key) # Determine what index the key should be assigned to.
        
        for key_value_pair in self.backing_store[index]: # Loop through the key-value pairs in the index that the value should be located in within the hash table.  
            k, v = key_value_pair # Assign the key and value of each key-value pair.
            if k == key: # If the key of the observed key-value pair matches the wanted key...
                return v # ...return the value.
        return None


    def remove(self, key): # Used to eliminate the key-value pair associated with key
        index = self._hash(key) # Determine what index the key-value pair should go to using the hash function.

        for key_value_pair in self.backing_store[index]: # Loop through the key-value pairs in the index that the value should be located in within the hash table.
            k, v = key_value_pair # Assign the key and value of each key-value pair.
            if k == key: # If the key of the observed key-value pair matches the wanted key...
                self.backing_store[index].remove(key_value_pair) # ...remove the key-value pair from the index of the hash table and...
                self.num_items -= 1 # ...decrease the number of items by 1.
                return True
        return False
    

    def _resize(self): # Used for resizing the hash table when it has exceeded its max load factor.
        new_size = self.slots * self.GROWTH_FACTOR # The new size fo the hash table is created by multiplying the number of slots by the growth factor.
        new_backing_store = [[] for _ in range(new_size)] # The new empty hash table is created with the new, larger number of slots. 

        for index in self.backing_store: # For every index in the old hash table...
            for key, value in index: # ...find every key and value in the index and then...
                new_hash = hash(key) % new_size # ...use the hash function to assign it to a new key and append the key and value to the right index.
                new_backing_store[new_hash].append((key, value)) 

        self.slots = new_size # Make the count of the number of slots the new size.             
        self.backing_store = new_backing_store # Make the old hash table the new hash table.
    

    def __str__(self):
        return str(self.backing_store)