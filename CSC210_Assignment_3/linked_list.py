# linked_list.py
# A singlely linked list with a tracked head
# Modified by: Nathan Huffman (And bugfixed by ChatGPT)

from collections.abc import MutableSequence

class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(MutableSequence):
    def __init__(self, iterable=None):
        self.head = None
        self._length = 0
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
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __delitem__(self, index): # Deletes the node at the specified index.
        if index < 0: # If the index is less than 0, adjust it to be relative to the end of the list.
            index += self._length
        if index < 0 or index >= self._length: # If the index is still out of bounds, raise an IndexError.
            raise IndexError("Index out of range")
    
        if index == 0: # If deleting the first index, update the head pointer to the node after the specified index.
            self.head = self.head.next
        else:
            current = self.head # Start at the head.
            for _ in range(index - 1): # Search through the list until the index just before the one to be deleted.
                current = current.next # Assign the current node to a placeholder variable.
            current.next = current.next.next # Bypass the node at the specified index by linking the previous node to the node after the specified index.
        self._length -= 1 # Update the length of the list.
        

    def insert(self, index, value): # Inserts a new node with the specified value at the given index.
        if index < 0: # If the index is less than 0, adjust it to be relative to the end of the list.
            index += self._length
        if index < 0 or index > self._length: # If the index is still out of bounds, raise an IndexError.
            raise IndexError("Index out of range")
        
        new_node = LLNode(value) # Create a new node with the given value.

        if index == 0: # If inserting at the head (index 0), update the head pointer.
            new_node.next = self.head # Point the new node's next to the current head.
            self.head = new_node # Update the head to be the new node.
        else: # Otherwise, traverse the list to find the node just before the insertion point.
            current = self.head # Start at the head.
            for _ in range(index - 1): # Move to the node just before the insertion point.
                current = current.next # Traverse the list.
            new_node.next = current.next # Point the new node's next to the current node's next.
            current.next = new_node # Link the previous node to the new node.
        
        self._length += 1 # Increment the length of the list.
        

    def append(self, value):
        self.insert(self._length, value)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"