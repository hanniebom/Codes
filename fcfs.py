#INPUT: Default data
processes = [
    ["P1", 5],
    ["P2", 8],
    ["P3", 12]
]

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