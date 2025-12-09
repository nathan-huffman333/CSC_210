from experiment import time_trial

def draw_search_speed_charts(search_times, list_lengths):
    import matplotlib.pyplot as plt

    linear_search_times = []
    binary_search_times = []
    for search_pair in search_times:
        linear_search_times.append(search_pair[0])
        binary_search_times.append(search_pair[1])
    plt.plot(list_lengths, linear_search_times, marker='o', label='Linear Search')
    plt.plot(list_lengths, binary_search_times, marker='o', label='Binary Search')
    plt.title("Linear Search vs Binary Search (1000 Trials Each)")
    plt.xlabel("Items")
    plt.ylabel("Nanoseconds per Search")
    plt.legend()
    plt.grid()
    plt.show()
    

def main():
    print("Running search time trials...")
    experiment_sizes = [10, 20, 40, 80, 160, 320, 640, 1280]
    search_times = []
    num_trials = 1000
    min_value = 1
    max_value = 1000000
    for size in experiment_sizes:
        search_pair = time_trial(num_trials, size, min_value, max_value)
        search_times.append(search_pair)
    print("Search Times (ns):")
    print("Items\tLinear\tBinary")
    for i in range(len(experiment_sizes)):
        print(f"{experiment_sizes[i]}\t{search_times[i][0]:.2f}\t{search_times[i][1]:.2f}")
    draw_search_speed_charts(search_times, experiment_sizes)

if __name__ == '__main__':
    main()