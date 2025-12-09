# main.py
# Compare search times for linked lists and dynamic arrays

from linked_list import LinkedList
from dynamic_array import DynamicArray
from random import randint
from time import perf_counter_ns

def draw_search_speed_charts(search_times, list_lengths):
    import matplotlib.pyplot as plt

    ll_search_times = []
    da_search_times = []
    for search_pair in search_times:
        ll_search_times.append(search_pair[0])
        da_search_times.append(search_pair[1])
    plt.plot(list_lengths, ll_search_times, marker='o', label='Linked List')
    plt.plot(list_lengths, da_search_times, marker='o', label='Dynamic Array')
    plt.title("Linked List vs Dynamic Array for Linear Search")
    plt.xlabel("Items")
    plt.ylabel("Nanoseconds per Search")
    plt.legend()
    plt.grid()
    plt.show()


def experiment(num_trials, list_size, min_value, max_value):
    ll = LinkedList()
    da = DynamicArray()
    for _ in range(list_size):
        value = randint(min_value, max_value)
        ll.append(value)
        da.append(value)

    ll_search_total_time = 0
    da_search_total_time = 0

    for _ in range(num_trials):
        target = randint(min_value, max_value)

        start_time = perf_counter_ns()
        if target in ll:
            pass
        end_time = perf_counter_ns()
        ll_search_total_time += (end_time - start_time)

        start_time = perf_counter_ns()
        if target in da:
            pass
        end_time = perf_counter_ns()
        da_search_total_time += (end_time - start_time)

    avg_ll_search_time = ll_search_total_time / num_trials
    avg_da_search_time = da_search_total_time / num_trials

    return (avg_ll_search_time, avg_da_search_time)



def main():
    print("Running search time trials...")
    experiment_sizes = [5000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    search_times = []
    num_trials = 10
    min_value = 1
    max_value = 1000000
    for size in experiment_sizes:
        search_pair = experiment(num_trials, size, min_value, max_value)
        search_times.append(search_pair)
    print("Search Times (ns):")
    print("Items\tLinked List\tDynamic Array")
    for i in range(len(experiment_sizes)):
        print(f"{experiment_sizes[i]}\t{search_times[i][0]:.2f}\t{search_times[i][1]:.2f}")
    draw_search_speed_charts(search_times, experiment_sizes)

if __name__ == '__main__':
    main()