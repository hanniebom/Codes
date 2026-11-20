#INPUT: Default data
processes = [
    ["P1", 5],
    ["P2", 3],
    ["P3", 7]
]

# Sort processes in ascending order
processes.sort(key=lambda x: x[1])

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
avg_waiting_time = total_waiting_time / len(processes)
avg_turnaround_time = total_turnaround_time / len(processes)

#Output: Print formatted results table
def print_results_table(results, avg_waiting_time, avg_turnaround_time):
    print("SJF".center(50))
    print("*" * 50)
    print(f"{"Process":<12} {"Burst":<12} {"Waiting":<12} {"Turnaround":<12}")
    print("*" * 50)

    for ProcessName, burst, waiting, turnaround in results:
        print(f"{ProcessName:<12} {burst:<12} {waiting:<12} {turnaround:<12}")

    print("*" * 50)
    print(f"Average waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")
    print("*" * 50, "\n")

print_results_table(results, avg_waiting_time, avg_turnaround_time)