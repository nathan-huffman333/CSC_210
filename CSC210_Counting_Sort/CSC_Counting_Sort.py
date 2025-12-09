def counting_sort(unsorted_array):
    length = len(unsorted_array)
    
    if length == 1:
        return unsorted_array
    
    max_value = max(unsorted_array)

    # Create count_array with a length of max_value + 1.
    count_array = [0] * (max_value + 1)

    # Populate count_array with the amount that each value occurs.
    for value in unsorted_array:
        count_array[value] += 1

    # Calculate prefix sum.
    for index in range(1, max_value + 1):
        count_array[index] += count_array[index - 1]

    sorted_array = [0] * length

    # Loop from the end, find index placement, subtract value to keep stable. 
    for index in range(length - 1, -1, -1):
        value = unsorted_array[index]
        sorted_array[count_array[value] - 1] = value
        count_array[value] -= 1
    
    return sorted_array


if __name__ == "__main__":
    array = [9, 4, 7, 3, 6, 8, 0, 1, 0, 4, 5, 7, 8]
    sorted_array = counting_sort(array)
    print(sorted_array)