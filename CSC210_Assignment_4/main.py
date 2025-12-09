# main.py
# Compare search times for linked lists and dynamic arrays

from simple_sorts import bubble_sort, selection_sort, insertion_sort
from random import randint
from time import perf_counter_ns

def draw_sort_speed_charts(sort_times, list_lengths):
    import matplotlib.pyplot as plt

    bs_sort_times = []
    ss_sort_times = []
    is_sort_times = []
    py_sort_times = []
    for sort_triplet in sort_times:
        bs_sort_times.append(sort_triplet[0] / 1_000_000_000)
        ss_sort_times.append(sort_triplet[1] / 1_000_000_000)
        is_sort_times.append(sort_triplet[2] / 1_000_000_000)
        py_sort_times.append(sort_triplet[3] / 1_000_000_000)
    plt.plot(list_lengths, bs_sort_times, marker='o', label='Bubble Sort')
    plt.plot(list_lengths, ss_sort_times, marker='o', label='Selection Sort')
    plt.plot(list_lengths, is_sort_times, marker='o', label='Insertion Sort')
    plt.plot(list_lengths, py_sort_times, marker='o', label='Python Sort')
    plt.title("Bubble Sort vs Selection Sort vs Insertion Sort vs Python Sort")
    plt.xlabel("Items")
    plt.ylabel("Seconds per Sort")
    plt.legend()
    plt.grid()
    plt.show()


def experiment(num_trials, list_size, min_value, max_value):
    bs_total_time = 0
    ss_total_time = 0
    is_total_time = 0
    py_total_time = 0

    for _ in range(num_trials):
        lst1 = [randint(min_value, max_value) for _ in range(list_size)]
        lst2 = lst1.copy()
        lst3 = lst1.copy()
        lst4 = lst1.copy()

        start_time = perf_counter_ns()
        bubble_sort(lst1)
        end_time = perf_counter_ns()
        bs_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        selection_sort(lst2)
        end_time = perf_counter_ns()
        ss_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        insertion_sort(lst3)
        end_time = perf_counter_ns()
        is_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        lst4.sort()
        end_time = perf_counter_ns()
        py_total_time += (end_time - start_time)

    avg_bs_time = bs_total_time / num_trials
    avg_ss_time = ss_total_time / num_trials
    avg_is_time = is_total_time / num_trials
    avg_py_time = py_total_time / num_trials
    return (avg_bs_time, avg_ss_time, avg_is_time, avg_py_time)

def main():
    print("Running sort time trials...")
    experiment_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    sort_times = []
    num_trials = 5
    min_value = 1
    max_value = 1000000
    for size in experiment_sizes:
        sort_pair = experiment(num_trials, size, min_value, max_value)
        sort_times.append(sort_pair)
    print("Sort Times (ns):")
    print("Items\tBubble Sort\tSelection Sort\tInsertion Sort\tPython Sort")
    for i in range(len(experiment_sizes)):
        print(f"{experiment_sizes[i]}\t{sort_times[i][0]:.2f}\t{sort_times[i][1]:.2f}\t{sort_times[i][2]:.2f}")
    draw_sort_speed_charts(sort_times, experiment_sizes)

if __name__ == '__main__':
    main()