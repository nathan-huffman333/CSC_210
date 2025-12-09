# tests.py
# Tests of Stack and Queue
# Please exercise them enough to
# show they work under different combinations
# of operations and different orders of those operations
# Modified by: Nathan Huffman
import unittest
from stack import Stack
from que import Queue


class TestStack(unittest.TestCase):
    def test_stack_with_ints(self):
        stack = Stack()

        for i in range(6):
            # Populate stack with nums 0 to 5 and peek at the last index.
            stack.push(i)
            self.assertTrue(stack.peek() == i)
        
        # Check .__len__() and .__repr__() functions.
        self.assertTrue(stack.__len__() == 6) 
        self.assertTrue(stack.__repr__() == "[0, 1, 2, 3, 4, 5]") 
        
        for i in range(stack.__len__()-1, -1, -1):
            # Unpopulate stack using .pop() and ensure that it does so using .peek().
            self.assertTrue(stack.peek() == i)
            stack.pop()
        
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to remove num from empty stack.
            stack.pop()
        
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to peek last num in empty stack.
            stack.peek()
        
        stack._data = [7, 3, 6, 10, 43, 52, 74, 5, 39]
        self.assertTrue(stack.peek() == 39) # Test .peek() on an unordered stack.
        stack.pop()
        stack.pop()
        self.assertTrue(stack.peek() == 74) # Test .peek() again after popping multiple times.
        stack.push(45)
        stack.push(99)
        self.assertTrue(stack.peek() == 99) # Test .peek() after pushing multiple times.
        
        # Check .__len__() and .__repr__() functions.
        self.assertTrue(stack.__len__() == 9)
        self.assertTrue(stack.__repr__() == "[7, 3, 6, 10, 43, 52, 74, 45, 99]")
        

    def test_stack_with_strings(self):
        stack = Stack()
        stack._data = ["computer", "python", "coding", "documentation", "strings", "stacks"]
        
        # Check .__len__() and .__repr__() functions.
        self.assertTrue(stack.__len__() == 6) 
        self.assertTrue(stack.__repr__() == "['computer', 'python', 'coding', 'documentation', 'strings', 'stacks']")

        self.assertTrue(stack.peek() == "stacks") # Test .peek() after populating array.
        stack.pop() 
        self.assertTrue(stack.peek() == "strings") # Test .peek() after popping.
        stack.push("queues")
        self.assertTrue(stack.peek() == "queues") # Test .peek() after pushing.
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.peek() == "coding") # Test .peek() after popping multiple times.
        stack.push("stacks")
        stack.push("data")
        stack.push("algorithms")
        self.assertTrue(stack.peek() == "algorithms") # Test .peek() after pushing multiple times.

        for i in range(stack.__len__()-1, -1, -1):
            # Unpopulate stack using .pop() and ensure that it does so using .peek().
            self.assertTrue(stack.peek() == stack._data[i])
            stack.pop()

        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to remove str from empty stack.
            stack.pop()
        
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to peek at last str in empty stack.
            stack.peek()


class TestQueue(unittest.TestCase):
    def test_queue_with_ints(self):
        queue = Queue()

        for i in range(6):
            # Populate queue with nums 0 to 5 and use .peek() to ensure the first index is unchanging.
            queue.push(i)
            self.assertTrue(queue.peek() == 0)
            
        # Check .__len__() and .__repr__() functions.
        self.assertTrue(queue.__len__() == 6) 
        self.assertTrue(queue.__repr__() == "[0, 1, 2, 3, 4, 5]") 
        
        for i in range(queue.__len__()):
            # Unpopulate queue using .pop() and ensure that it does so using .peek().
            self.assertTrue(queue.peek() == queue._data[0])
            queue.pop()
        
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to remove num from empty queue.
            queue.pop()
        
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to peek first num in empty queue.
            queue.peek()
        
        queue._data = [7, 3, 6, 10, 43, 52, 74, 5, 39]
        self.assertTrue(queue.peek() == 7) # Test .peek() on an unordered queue.
        queue.pop()
        queue.pop()
        queue.pop()
        self.assertTrue(queue.peek() == 10) # Test .peek() again after popping multiple times.
        queue.push(45)
        queue.push(99)

        for i in range(queue.__len__()-2):
            # Remove older indexes from queue using .pop() to ensure nums 45 and 99 were at the end.
            queue.pop()
        self.assertTrue(queue.peek() == 45)
        queue.pop()
        self.assertTrue(queue.peek() == 99)
        queue.pop()
        
        # Repopulate queue in numeric order.
        queue.push(3)
        queue.push(6)
        queue.push(7)
        queue.push(10)
        queue.push(43)
        queue.push(45)
        queue.push(52)
        queue.push(74)
        queue.push(99)
        
        # Check .__len__() and .__repr__() functions.
        self.assertTrue(queue.__len__() == 9)
        self.assertTrue(queue.__repr__() == "[3, 6, 7, 10, 43, 45, 52, 74, 99]")
        

    def test_queue_with_strings(self):
        queue = Queue()
        queue._data = ["computer", "python", "coding", "documentation", "strings", "queues"]
        
        # Check .__len__() and .__repr__() functions.
        self.assertTrue(queue.__len__() == 6) 
        self.assertTrue(queue.__repr__() == "['computer', 'python', 'coding', 'documentation', 'strings', 'queues']")

        self.assertTrue(queue.peek() == "computer") # Test .peek() after populating array.
        queue.pop() 
        self.assertTrue(queue.peek() == "python") # Test .peek() after popping.
        queue.push("stacks")
        self.assertTrue(queue.peek() == "python") # Test .peek() after pushing.

        for i in range(queue.__len__()-1):
            # Remove older indexes from queue using .pop() to ensure "stacks" was at the end.
            queue.pop()
        self.assertTrue(queue.peek() == "stacks")

        # Remove "stacks" and repopulate queue in alphabetical order.
        queue.pop()
        queue.push("coding")
        queue.push("computer")
        queue.push("documentation")
        queue.push("python")
        queue.push("queues")
        queue.push("strings")
        self.assertTrue(queue.peek() == "coding") # Test .peek() after popping multiple times.
        
        for i in range(queue.__len__()):
            # Unpopulate queue using .pop() and ensure that it does so using .peek().
            self.assertTrue(queue.peek() == queue._data[0])
            queue.pop()
            
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to remove str from empty queue.
            queue.pop()
        
        with self.assertRaises(IndexError):
            # IndexError is raised when attempting to peek at first str in empty queue.
            queue.peek()


if __name__ == '__main__':
    unittest.main()