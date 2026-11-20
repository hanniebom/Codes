#INPUT: Default data 
from collections import deque
processes[
    ["P1", 0, 5],
    ["P2", 0, 3],
    ["P3", 0, 7],
    ["P4", 0, 2]
]
time_quantum = 2
processes.sort(key=lambda p: p[1])
all_procs = []
for pid, arrival, burst in processes:
    all_procs.append([pid, arrival, burst, burst]) 
#Algorithm: Scheduling logic and calculations
queue = deque()
current_time = 0
index = 0          
completed = []
#Averages: Average waiting time, average turnaround time
#Output: Print formatted results table