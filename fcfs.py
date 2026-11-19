#INPUT: Default data
processes = [
    ["P1", 5],
    ["P2", 8],
    ["P3", 12]
]

waiting_time = 0
turnaround_time = 0

#Algorithm: Scheduling logic and calculations
current_time = 0
results = []
for p in processes:
    name = p[0]
    burst = p[1]

#Averages: Average waiting time, average turnaround time
avg_waiting_time = sum(waiting_time)/len(processes)
avg_turnaround_time = sum(turnaround_time)/len(processes)

#Output: Print formatted results table