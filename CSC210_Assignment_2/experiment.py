# experiment.py
# Run time trials of searching algorithms
# Starter Code from CSC 210
# Modified by: Nathan Huffman (and bug fixed using chatgpt but not copied directly)

from random import randint
from search import linear_search, binary_search
from time import perf_counter_ns

def random_int_list(length, min_value, max_value): # Function to populate a list with random integers.
    list = [] # Initialize an empty list.
    for index in range(length): # Loop 'length' times to add the desired number of random integers.
        list.append(randint(min_value, max_value)) # Append a random integer between 'min_value' and 'max_value' to the list.
    return list # Return the populated list.
    pass

def time_trial(num_trials, data_size, min_value, max_value): # Function used to time linear and binary search algorithms.
    data = random_int_list(data_size, min_value, max_value) # Generate a list of random integers of specified size and range.
    
    data_copy = data[:] # Creates a copy of the original list.
    start_sort_time = perf_counter_ns() # Start timing the sorting process.
    data_copy.sort() # Sorts the copied list in order for binary search.
    end_sort_time = perf_counter_ns() # End timing the sorting process.
    sort_time = (end_sort_time - start_sort_time) # Calculate the time taken to sort the list and assign it to 'sort_time'.

    lin_time_elapsed = 0 # Initialize total time for linear search as "lin_time_elapsed".
    bin_time_elapsed = 0 # Initialize total time for binary search as "bin_time_elapsed".

    for num in range(int(num_trials)): # Loop to perform the specified number of trials for both search algorithms.
        lin_key = randint(min_value, max_value) # Generate a random key for linear search.
        start_lin_time = perf_counter_ns() # Start timing the linear search.
        linear_search(data, lin_key) # Perform linear search on the original list by calling the linear_search function.
        end_lin_time = perf_counter_ns() # End timing the linear search.
        lin_time_elapsed += (end_lin_time - start_lin_time) # Accumulate the time taken for this trial to the total linear search time.
    
        bin_key = randint(min_value, max_value) # Generate a random key for binary search.
        start_bin_time = perf_counter_ns() # Start timing the binary search.
        binary_search(data_copy, bin_key) # Perform binary search on the sorted list by calling the binary_search function.
        end_bin_time = perf_counter_ns() # End timing the binary search.
        bin_time_elapsed += (end_bin_time - start_bin_time) # Accumulate the time taken for this trial to the total binary search time.

    average_linear_time = lin_time_elapsed / num_trials # Calculate the average time for linear search over all trials.
    average_binary_time = float(((bin_time_elapsed + sort_time) / num_trials)) # Calculate the average time for binary search over all trials, including the sorting time.
    
    return (average_linear_time, average_binary_time) # Returns the average times of the differing search algorithms as a tuple. 
    pass