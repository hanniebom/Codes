#INPUT: User enters data 
def fetch_user_input(): 

    num_of_procs = int(input("Enter the number of processes: "))

    processes = []

    for proc_count in range(1, num_of_procs + 1):
        print(f"\nEnter data for Process {proc_count}:")
        burst_time = int(input('\nBurst Time: '))
        processes.append([f"P{proc_count}", burst_time])

    
    return processes, num_of_procs


def fcfs_alg(processes, num_of_procs):

    total_waiting_time = 0
    total_turnaround_time = 0

    #Algorithm: Scheduling logic and calculations
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

    #Averages: Average waiting time, average turnaround time
    avg_waiting_time = total_waiting_time / num_of_procs
    avg_turnaround_time = total_turnaround_time / num_of_procs
    return results, avg_waiting_time, avg_turnaround_time

#Output: Print formatted results table
def print_results_table(results, avg_waiting_time, avg_turnaround_time):
    print("FCFS".center(50))
    print("*" * 50)
    print(f"{"Process":<12} {"Burst":<12} {"Waiting":<12} {"Turnaround":<12}")
    print("*" * 50)

    for ProcessName, burst, waiting, turnaround in results:
        print(f"{ProcessName:<12} {burst:<12} {waiting:<12} {turnaround:<12}")

    print("*" * 50)
    print(f"Average waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")
    print("*" * 50, "\n")

processes, num_of_procs = fetch_user_input()
results, avg_waiting_time, avg_turnaround_time = fcfs_alg(processes, num_of_procs)
print_results_table(results, avg_waiting_time, avg_turnaround_time)