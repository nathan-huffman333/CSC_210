# bst.py
# An implementation of a binary search tree
# Modified by: Nathan Huffman
# Please try to write this yourself without using an LLM.

class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    # insert a value into the BST
    # put values that are less than the current node to the left
    # put values that are greater than or equal to the current node 
    # to the right
    # don't forget about the special case where the root is None
    def insert(self, value):
        if self.root == None:
            self.root = BSTNode(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left == None:
                        current.left = BSTNode(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = BSTNode(value)
                        break
                    else:
                        current = current.right

        self.count += 1
                 

    # return the number of nodes in the BST
    def __len__(self):
        return self.count

    # implement a contains like method that returns if a value is in the BST
    # the dunder contains metods is used with the "in" operator
    # like: value in bst
    def __contains__(self, value):
        current = self.root

        while current != None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
        
        return False
        
    # Helper for inOrderWalk() to call for entire bst
    def in_order_walk(self):
        result = []
        self.in_order_walk_helper(self.root, result)
        return result

    # Walk through the entire tree in ascending order, starting
    # from *current*, and accumulate the values in the
    # list *accumulated*
    # TIP: See page 288 of Chapter 12 of Introduction to Algorithms
    def in_order_walk_helper(self, current, accumulated):
        if current != None:
            self.in_order_walk_helper(current.left, accumulated)
            accumulated.append(current.value)
            self.in_order_walk_helper(current.right, accumulated)

    # Return the minimum value in the BST or None if the BST is empty
    def minimum(self):
        if self.root == None:
            return None
        current = self.root
        while current.left != None:
            current = current.left
        return current.value
    
    # Return the maximum value in the BST or None if the BST is empty
    def maximum(self):
        if self.root == None:
            return None
        current = self.root
        while current.right != None:
            current = current.right
        return current.value
    
    