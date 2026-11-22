# Helper function to validate whole number inputs
def get_number(question, minimum):
    while True:
        try:
            num = int(input(question))
            if num >= minimum:
                return num
            print(f"Please enter a number of at least {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# INPUT: Default test data or validated custom user input
def fetch_user_input():
    choice = input("Press 1 for Default Data (5, 8, 12) or 2 for Custom Input: ")
    if choice == "1":
        processes = [
            ["P1", 5],
            ["P2", 8],
            ["P3", 12]
        ]
        return processes, len(processes)

    num_of_procs = get_number("Enter the number of processes: ", 1)
    processes = []

    for proc_count in range(1, num_of_procs + 1):
        print(f"\nEnter data for Process {proc_count}:")
        burst_time = get_number("Burst Time: ", 1)
        processes.append([f"P{proc_count}", burst_time])

    return processes, num_of_procs


# ALGORITHM: Scheduling logic and calculations
def fcfs_alg(processes, num_of_procs):
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    results = []

    for p in processes:
        name = p[0]
        burst = p[1]
        waiting_time = current_time
        current_time += burst
        turnaround_time = current_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        results.append([name, burst, waiting_time, turnaround_time])

    # AVERAGES: Average waiting time, average turnaround time
    avg_waiting_time = total_waiting_time / num_of_procs
    avg_turnaround_time = total_turnaround_time / num_of_procs

    return results, avg_waiting_time, avg_turnaround_time


# OUTPUT: Print formatted results table
def print_results_table(results, avg_waiting_time, avg_turnaround_time):
    print("\n" + "FCFS".center(50))
    print("*" * 50)
    print(f"{'Process':<12} {'Burst':<12} {'Waiting':<12} {'Turnaround':<12}")
    print("*" * 50)

    for ProcessName, burst, waiting, turnaround in results:
        print(f"{ProcessName:<12} {burst:<12} {waiting:<12} {turnaround:<12}")

    print("*" * 50)
    print(f"Average waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")
    print("*" * 50, "\n")


# MAIN EXECUTION
processes, num_of_procs = fetch_user_input()
results, avg_waiting_time, avg_turnaround_time = fcfs_alg(processes, num_of_procs)
print_results_table(results, avg_waiting_time, avg_turnaround_time)