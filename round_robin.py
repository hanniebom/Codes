#INPUT: Default data
processes = [
    ["P1", 0, 5],
    ["P2", 0, 3],
    ["P3", 0, 7],
    ["P4", 0, 2]
]

time_quantum = 2

# Store each process's remaining burst time
remaining_time = [5, 3, 7, 2]

# Store completion times
completion_time = [0, 0, 0, 0]

total_waiting_time = 0
total_turnaround_time = 0

#Algorithm: Scheduling logic and calculations
current_time = 0

while any(remaining_time):

    # Go through each process
    for p in range(len(processes)):

        # Only run processes that still have time remaining
        if remaining_time[p] > 0:

            if remaining_time[p] > time_quantum:
                current_time += time_quantum
                remaining_time[p] -= time_quantum

            else:
                current_time += remaining_time[p]
                remaining_time[p] = 0
                completion_time[p] = current_time

#Calculations: Waiting time and turnaround time
results = []

for p in range(len(processes)):
    name = processes[p][0]
    arrival_time = processes[p][1]
    burst = processes[p][2]

    turnaround_time = completion_time[p] - arrival_time
    waiting_time = turnaround_time - burst

    total_waiting_time += waiting_time
    total_turnaround_time += turnaround_time
    results.append([name, arrival_time, burst, completion_time[p], turnaround_time, waiting_time])

#Averages: Average waiting time, average turnaround time
avg_waiting_time = total_waiting_time / len(processes)
avg_turnaround_time = total_turnaround_time / len(processes)

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

print_results_table(results, avg_waiting_time, avg_turnaround_time)