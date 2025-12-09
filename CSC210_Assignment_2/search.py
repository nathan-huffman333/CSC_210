# search.py
# Implementations of simple searching algorithms
# Starter Code from CSC 210
# Modified by: Nathan Huffman (and bug fixed using chatgpt but not copied directly)

def linear_search(data, key): # This function does a linear search through the data list for the key.
    for i in range(len(data) - 1): # Loop through each index in the data list.
        if data[i] == key: # If the value at the current index is equal to the key it returns True.
            return True
    return False # If the key is not found in the list it returns False.
    pass

def binary_search(data, key): # This function does a binary search through the data list for the key.
    start = 0 # Initialize the start index to 0.
    end = int(len(data) - 1) # Initialize the end index of the list.

    while start <= end: # While the start index is less than or equal to the end index, continue searching for the key.
        middle = int((start + end) // 2) # Calculate and assigns the middle index between the current start and end indexes to a variable.
        if data[middle] < key: # Checks if the middle index between the assigned start and end is less than the key.
            start = (middle + 1) # If it is, assign a new value to "start," being one more than the middle index.
        elif data[middle] > key: # Checks if the middle index between the assigned start and end is greater than the key.
            end = (middle - 1) # If it is, assign a new value to "end," being one less than the middle index.
        else: # If the middle index is neither less than nor greater than the key, it must be equal to the key, so it returns True.
            return True 
    return False # If the entire list is searched and the key is not found, it returns False.
    pass