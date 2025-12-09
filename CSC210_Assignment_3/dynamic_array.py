# dynamic_array.py
# A dynamic array using Python's array module
# Modified by: Nathan Huffman

from array import array
from collections.abc import MutableSequence

class DynamicArray(MutableSequence):
    
    GROWTH_FACTOR = 2
    INITIAL_CAPACITY = 10

    def __init__(self, iterable=None):
        self._capacity = DynamicArray.INITIAL_CAPACITY
        self._length = 0
        self._array = array('i', [0] * self._capacity)
        if iterable is not None:
            for item in iterable:
                self.append(item)
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, index):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        return self._array[index]
    
    def __setitem__(self, index, value):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        self._array[index] = value

    def __delitem__(self, index): # Function to delete an item at a certain index.
        if index < 0: # Handle negative indices by converting them to positive indices.
            index += self._length
        if index < 0 or index >= self._length: # Check if the index is out of range.
            raise IndexError("Index out of range")
        
        for _ in range(index, self._length - 1): # Shift elements to the left to fill the gap created by the deletion.
            self._array[_] = self._array[_ + 1]

        self._length -= 1  # Decrease the length of the array by 1.

    def insert(self, index, value): # Function to insert a specified value at a certain index.
        if index < 0: # Handle negative indices by converting them to positive indices.
            index += self._length
        if index < 0 or index > (self._length): # Check if the index is out of range.
            raise IndexError("Index out of range")
        
        if self._length >= (self._capacity): # Check if the array has reached its capacity.
            self._resize() # Resize the array if it has.
        
        for _ in range(self._length, index, -1): # Shift elements to the right to make space for the new element.
            self._array[_] = self._array[_ - 1]
        
        self._array[index] = value # Insert the new value at the specified index.
        self._length += 1 # Increase the length of the array by 1.

    def _resize(self): # Function to resize the array when it reaches capacity.
        new_capacity = self._capacity * self.GROWTH_FACTOR # Update the capacity by multiplying it by the growth factor.
        new_array = array('i', [0] * new_capacity) # Create a new array with the updated capacity.
        
        for i in range(self._length): # Copy the elements from the old array to the new array.
            new_array[i] = self._array[i]
        
        self._array = new_array # Update the reference to the new array.
        self._capacity = new_capacity # Update the capacity to the new capacity.

    def __repr__(self):
        return "DynamicArray([" + ", ".join(repr(self._array[i]) for i in range(self._length)) + "])"
    
    def __iter__(self):
        for i in range(self._length):
            yield self._array[i]
    
    def append(self, value):
        self.insert(self._length, value)