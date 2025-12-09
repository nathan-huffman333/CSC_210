# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: Nathan Huffman (And used pseudocode from the CSC210_SimpleSortingAlgorithms notes as guidance) 

def bubble_sort(lst):
    length = len(lst) # The length of the list is stored in a variable to prevent having to recount each time.

    for i in range(length - 1): # Repeat the process of 'bubbling up' values for every value in the list.
        for j in range(length - i - 1): # Continuously compare the current index to the next index all the way through the list.
            if lst[j] > lst[j + 1]: # Check if the current value in the index being observed is greater than the next value.  
                lst[j + 1], lst[j] = lst[j], lst[j + 1] # If true, swap their indexes.

def selection_sort(lst):
    length = len(lst) # The length of the list is stored in a variable to prevent having to recount each time.

    for i in range(length - 1):
        smallest = i # The current value observed is assigned to the smallest value for comparisons.
        
        for j in range(i + 1, length): # Search through the remaining unsorted numbers.
            if lst[j] < lst[smallest]: # Check if any of the remaining values in the unsorted list are smaller than our current observed smallest.  
                smallest = j # If so, reassign smallest to this lesser value.
        
        lst[smallest], lst[i] = lst[i], lst[smallest] # After finding the smallest value in the unsorted list, swap it for the index after the unsorted section of the list.

def insertion_sort(lst):
    for i in range(1, len(lst)): # Loops through the list starting at the second element.
        unsorted_num = lst[i] # Stores the current element that needs to be reordered.
        j = i - 1 # Stores 'j' the previous index as a value.
        while j >= 0 and unsorted_num < lst[j]: # Look through the sorted part of the array until the number finds the appropriate index.
            lst[j + 1] = lst[j] # Shifts the larger element to the next index.
            j -= 1 # Decreases j to look at the next index to the left.
        lst[j + 1] = unsorted_num # Assign the unsorted number to the correct index of the sorted part of the list.