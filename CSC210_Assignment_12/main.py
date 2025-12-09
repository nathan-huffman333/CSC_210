# main.py
# Compare sort times for Heap Sort vs Insertion Sort vs Python's built-in sort

from pq import PriorityQueue
from random import randint
from time import perf_counter_ns
import matplotlib.pyplot as plt

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def draw_sort_speed_charts(search_times, list_lengths):
    heap_sort_times = []
    is_sort_times = []
    builtin_sort_times = []

    for heap, is_, builtin in search_times:
        heap_sort_times.append(heap)
        is_sort_times.append(is_)
        builtin_sort_times.append(builtin)

    plt.plot(list_lengths, heap_sort_times, marker='o', label='Heap Sort')
    plt.plot(list_lengths, is_sort_times, marker='o', label='Insertion Sort')
    plt.plot(list_lengths, builtin_sort_times, marker='o', label='Built-in Sort')
    plt.title("Heap Sort vs Insertion Sort vs Built-in Sort Speed")
    plt.xlabel("Items")
    plt.ylabel("Nanoseconds per Sort")
    plt.legend()
    plt.grid()
    plt.show()

# Measure sort speed for heap sort with pq versus insertion sort and Python's built-in sort
def sort_speed(length):
    # Generate random data structures
    test_array1 = [randint(0, length) for _ in range(length)]
    test_array2 = test_array1.copy()
    test_array3 = test_array1.copy()

    # Measure priority queue sort time
    pq = PriorityQueue()
    
    for item in test_array1:
        pq.push(item)
    start_time = perf_counter_ns()
    sorted_pq = [0] * len(test_array1)
    for i in range(len(test_array1)):
        sorted_pq[i] = pq.pop()
    end_time = perf_counter_ns()
    pq_time = end_time - start_time

    # Measure insertion sort time
    start_time = perf_counter_ns()
    sorted_array2 = insertion_sort(test_array2)
    end_time = perf_counter_ns()
    is_time = end_time - start_time

    # Measure Python built-in sort time
    start_time = perf_counter_ns()
    throwaway = sorted(test_array3)
    end_time = perf_counter_ns()
    builtin_time = end_time - start_time

    return (pq_time, is_time, builtin_time)


def main():
    print("Running sort time trials (Heap Sort vs Insertion Sort vs Standard Library Sort)...")
    experiment_sizes = [500, 1000, 1500, 2000, 2500, 3000]
    search_times = []

    for size in experiment_sizes:
        result = sort_speed(size)
        search_times.append(result)

    print("Average Sort Time (ns per sort):")
    print("Items\tHeap Sort\t\tInsertion Sort\t\tBuilt-in")
    for n_items, (pq_t, is_t, builtin_t) in zip(experiment_sizes, search_times):
        print(f"{n_items}\t{pq_t:.2f}\t{is_t:.2f}\t{builtin_t:.2f}")

    draw_sort_speed_charts(search_times, experiment_sizes)


if __name__ == '__main__':
    main()