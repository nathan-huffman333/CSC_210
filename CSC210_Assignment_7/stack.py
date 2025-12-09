# stack.py
# A Last In First Out (LIFO) stack
# Modified by: Nathan Huffman
# Note: Please write this yourself, not using an LLM.
from sequential_collection import SequentialCollection

class Stack(SequentialCollection):
    def push(self, item): # Adds an item to the end of the list.
        self._data.append(item) # The item is appended.
    
    
    def pop(self): # Remove an item from and return the updated list.
        if self.is_empty: # Checks if the list is empty and if so...
            raise IndexError("list index out of range.") # ...raises the index 'out of range' error.
        else:
            return(self._data.pop()) # Otherwise, removes the last item in the list and returns the updated list.
        

    def peek(self):
        if self.is_empty: # Checks if the list is empty and if so...
            raise IndexError("list index out of range.") # ...raises the index 'out of range' error.
        else:
            return(self._data[(len(self._data) - 1)]) # Otherwise, returns the last item in the list.