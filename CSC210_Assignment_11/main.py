# main.py
# Compare search times for BST and Python list

from bst import BST
from random import randint
from time import perf_counter_ns
import matplotlib.pyplot as plt


def draw_search_speed_charts(search_times, list_lengths):
    bst_search_times = []
    list_search_times = []

    for bst_time_per_search, list_time_per_search in search_times:
        bst_search_times.append(bst_time_per_search)
        list_search_times.append(list_time_per_search)

    plt.plot(list_lengths, bst_search_times, marker='o', label='BST')
    plt.plot(list_lengths, list_search_times, marker='o', label='Python List')
    plt.title("BST vs Python List for Search")
    plt.xlabel("Items")
    plt.ylabel("Nanoseconds per Search")
    plt.legend()
    plt.grid()
    plt.show()


def search_speed(length):
    # Generate random data structures
    test_array1 = [randint(0, length) for _ in range(length)]
    test_array2 = [randint(0, length) for _ in range(length)]

    # Build BST from test_array1
    bst = BST()
    for num in test_array1:
        bst.insert(num)

    # Time BST search: value in bst  (uses __contains__)
    start = perf_counter_ns()
    for num in test_array2:
        _ = (num in bst)
    end = perf_counter_ns()
    bst_total_ns = end - start

    # Time list search: value in list
    start = perf_counter_ns()
    for num in test_array2:
        _ = (num in test_array1)
    end = perf_counter_ns()
    list_total_ns = end - start

    # Average time per search
    bst_time_per_search = bst_total_ns / length
    list_time_per_search = list_total_ns / length

    return (bst_time_per_search, list_time_per_search)


def main():
    print("Running search time trials (BST vs Python list)...")
    experiment_sizes = [1000, 5000, 15000, 20000, 25000, 30000]
    search_times = []

    for size in experiment_sizes:
        result = search_speed(size)
        search_times.append(result)

    print("Average Search Time (ns per search):")
    print("Items\tBST\t\tList")
    for n_items, (bst_t, list_t) in zip(experiment_sizes, search_times):
        print(f"{n_items}\t{bst_t:.2f}\t{list_t:.2f}")

    draw_search_speed_charts(search_times, experiment_sizes)


if __name__ == '__main__':
    main()