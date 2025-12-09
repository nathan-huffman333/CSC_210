# pq.py
# An implementation of binary max-heap based priority queue
# Modified by: Nathan Huffman
# Please try to write this yourself without using an LLM.

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)
    
    def __repr__(self):
        return repr(self.heap)
    
    # What is the maximum value in the priority queue?
    # In other words, what is the next value that would be popped?
    # TIP: See pseudocode for HEAP-MAXIMUM in Introduction to Algorithm Chapter 6 page 163
    # NOTE: Our heap starts at 0, not 1
    def peek(self):
        # Returns first/largest element in the heap.
        return self.heap[0]

    # Put a new element into the priority queue
    # TIP: A combination of HEAP-INCREASE-KEY() and MAX-HEAP-INSERT()
    # in Intro to Algorithms Chapter 6; they set the last element to
    # -infinity; we will set our last element to *key*, and then float it up
    # as is done in HEAP-INCREASE-KEY()
    # NOTE: function parent() is defined at the top of this file
    # NOTE: our last element is at len(self.heap) - 1 after being appended to the list
    def push(self, key):
        # Add key to the end and determine the length of heap.
        self.heap.append(key)
        length = len(self.heap) - 1
        
        # While the added key is larger than its parent, move it up the heap.
        while length > 0 and self.heap[parent(length)] < self.heap[length]:
            p = parent(length)
            self.heap[length], self.heap[p] = self.heap[p], self.heap[length]
            length = p
    
    
    # Remove the next element (max element) in the heap and return it
    # TIP: See pseudocode in Introduction to Algorithm Chapter 6 page 163
    # for HEAP-EXTRACT-MAX()
    # NOTE: Our heap starts at 0, not 1
    # NOTE: Do not worry about contracting the size of the backing vector
    # after a pop.
    def pop(self):
        # Replace first index with last, pop it off, fix order, return max. 
        max = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self._max_heapify(0)
        return max

    
    # Push down the element at *i* to maintain the max-heap property
    # TIP: See pseudocode in Introduction to Algorithm Chapter 6 page 154
    # NOTE: functions left() and right() are defined at the top of this file
    def _max_heapify(self, i):
        # Determine the left + right of i and length of heap.
        lt = left(i)
        rt = right(i)
        length = len(self.heap)

        # Check if left or right child is bigger than i. 
        if lt < length and self.heap[lt] > self.heap[i]:
            largest = lt
        else:
            largest = i
        if rt < length and self.heap[rt] > self.heap[largest]:
            largest = rt

        # If the parent i is smaller than its children, swap and check again.
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._max_heapify(largest)
    