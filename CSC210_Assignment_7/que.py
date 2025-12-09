# que.py
# A First In First Out (FIFO) queue
# Modified by: Nathan Huffman
# Note: Please write this yourself, not using an LLM.
from sequential_collection import SequentialCollection


class Queue(SequentialCollection):
    def push(self, item): # Adds an item to the end of the list.
        self._data.append(item) # The item is appended.
    
    
    def pop(self): # Remove an item from and return the updated list.
        if self.is_empty: # Checks if the list is empty and if so...
            raise IndexError("list index out of range.") # ...raises the index 'out of range' error.
        else:
            return(self._data.pop(0)) # Otherwise, removes the first item in the list and returns the updated list.
        

    def peek(self):
        if self.is_empty: # Checks if the list is empty and if so...
            raise IndexError("list index out of range.") # ...raises the index 'out of range' error.
        else:
            return(self._data[0]) # Otherwise, returns the first item in the list.
