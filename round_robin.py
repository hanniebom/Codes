#INPUT: User enters data 

def fetch_user_input(): 

    num_of_procs = int(input("Enter the number of processes: "))

    processes = []

    for proc_count in range(1, num_of_procs + 1):
        print(f"\nEnter data for Process {proc_count}:")
        arrival_time = int(input('\nArrival Time: '))
        burst_time = int(input('\nBurst Time: '))
        processes.append([f"P{proc_count}", arrival_time, burst_time])

    time_quantum = int(input('\nEnter the Time Quantum: '))
    
    return processes, time_quantum, num_of_procs
    
def round_robin_alg(processes, time_quantum, num_of_procs):
    
    processes.sort(key=lambda proc: proc[1])

    # Store each process's remaining burst time
    remaining_time = [proc[2] for proc in processes]

    # Store completion times
    completion_time = [0] * num_of_procs

    total_waiting_time = 0
    total_turnaround_time = 0



    #Algorithm: Scheduling logic and calculations
    current_time = 0

    while any(remaining_time):
        is_cpu_idle = True
        # Go through each process
        for p in range(num_of_procs):

            # Only run processes that still have time remaining and the arrival time is lessthan or equal current time
            if remaining_time[p] > 0 and processes[p][1] <= current_time:
                is_cpu_idle = False
                
                if remaining_time[p] > time_quantum:
                    current_time += time_quantum
                    remaining_time[p] -= time_quantum

                else:
                    current_time += remaining_time[p]
                    remaining_time[p] = 0
                    completion_time[p] = current_time

        if is_cpu_idle:
            current_time += 1

    #Calculations: Waiting time and turnaround time
    results = []

    for p in range(num_of_procs):
        name = processes[p][0]
        arrival_time = processes[p][1]
        burst = processes[p][2]

        turnaround_time = completion_time[p] - arrival_time
        waiting_time = turnaround_time - burst

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        results.append([name, arrival_time, burst, completion_time[p], turnaround_time, waiting_time])

    #Averages: Average waiting time, average turnaround time
    avg_waiting_time = total_waiting_time / num_of_procs
    avg_turnaround_time = total_turnaround_time / num_of_procs
    return results, avg_waiting_time, avg_turnaround_time


    #Output: Print formatted results table
def print_results_table(results, avg_waiting_time, avg_turnaround_time):
    print("RR".center(84))
    print("*" * 84)
    print(f"{'Process':<12} {'Arrival':<12} {'Burst':<12} {'Completion':<12} {'Turnaround':<12} {'Waiting':<12}")
    print("*" * 84)

    for ProcessName, arrival_time, burst, completion_time, turnaround_time, waiting_time in results:
        print(f"{ProcessName:<12} {arrival_time:<12} {burst:<12} {completion_time:<12} {turnaround_time:<12} {waiting_time:<12}")

    print("*" * 84)
    print(f"Average waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")
    print("*" * 84, "\n")

processes, time_quantum, num_of_procs = fetch_user_input()
results, avg_waiting_time, avg_turnaround_time = round_robin_alg(processes, time_quantum, num_of_procs)
print_results_table(results, avg_waiting_time, avg_turnaround_time)