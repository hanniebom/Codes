#note to self:
# add a desc for each function [], write the rest of the comments [], 
# fix waiting time, (UPDATE, it was actually counting, the test data tricked me LOL) [DONE], 
# add file input choice [], add the option to esc if the user wants to finish the program early
# add visual presentation (gantt chart) (optional)

from collections import deque

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
    while True:
        choice = input("Press 1 for Default Data or 2 for Custom Input: ")
        if choice == "1":  #those are test values
            processes = [
                ["P1", 0, 5],
                ["P2", 2, 3],
                ["P3", 16, 7],
                ["P4", 6, 2]
            ]
            time_quantum = 2
            return processes, time_quantum, len(processes)
        
        elif choice == "2":
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    num_of_procs = get_number("Enter the number of processes: ", 1)
    processes = []

    for proc_count in range(1, num_of_procs + 1):
        print(f"\nEnter data for Process {proc_count}:")
        arrival_time = get_number("Arrival Time: ", 0)
        burst_time = get_number("Burst Time: ", 1)
        processes.append([f"P{proc_count}", arrival_time, burst_time])

    time_quantum = get_number("\nEnter the Time Quantum: ", 1)

    return processes, time_quantum, num_of_procs

#Algorithm: Scheduling logic and calculations
def round_robin_alg(processes, time_quantum, num_of_procs):

    arrival_order = sorted(range(num_of_procs), key= lambda i: processes[i][1])
    next_to_arrive = 0
    ready_procs_queue = deque()
    num_of_completed_procs = 0

    # Store each process's remaining burst time
    remaining_time = [proc[2] for proc in processes]

    # Store completion times
    completion_time = [0] * num_of_procs
    current_time = 0

    while num_of_completed_procs < num_of_procs:

        while next_to_arrive < num_of_procs and processes[arrival_order[next_to_arrive]][1]<= current_time:
            ready_procs_queue.append(arrival_order[next_to_arrive])
            next_to_arrive += 1

        #if the CPU is idle, skip the clock to the next process to arrive
        if not ready_procs_queue:
            current_time = processes[arrival_order[next_to_arrive]][1]
            continue

        #Take the process at the front of the queue
        next_proc_to_run = ready_procs_queue.popleft()

        #run it for one quantum time, or less if it finishes sooner
        run_time = min(time_quantum, remaining_time[next_proc_to_run])
        current_time += run_time
        remaining_time[next_proc_to_run] -= run_time

        # Processes that arrived while next_proc_to_run was running go in before next_proc_to_run is re-queued into ready_procs_queue
        while next_to_arrive < num_of_procs and processes[arrival_order[next_to_arrive]][1] <= current_time:
            ready_procs_queue.append(arrival_order[next_to_arrive])
            next_to_arrive += 1

        #if not finished, put the proceess back of the queue
        if remaining_time[next_proc_to_run] > 0:
            ready_procs_queue.append(next_proc_to_run)
        else:
            completion_time[next_proc_to_run] = current_time
            num_of_completed_procs += 1

    #Calculations: Waiting time and turnaround time
    results = []
    total_waiting_time = 0
    total_turnaround_time = 0

    for proc_num in range(num_of_procs):
        name = processes[proc_num][0]
        arrival_time = processes[proc_num][1]
        burst = processes[proc_num][2]

        turnaround_time = completion_time[proc_num] - arrival_time
        waiting_time = turnaround_time - burst

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        results.append([name, arrival_time, burst, completion_time[proc_num], turnaround_time, waiting_time])

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