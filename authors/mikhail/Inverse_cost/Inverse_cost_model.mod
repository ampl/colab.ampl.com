reset;

# Model Name: Worker-Task Assignment
### Optimize task assignments to workers, minimizing costs with an inverse relationship scaling.
# Version: 1.0
# Last Updated: Jan 2025

### SETS
# Define the set of workers and tasks
set WORKERS;                             # All workers
set TASKS;                               # All tasks

### PARAMETERS
# Define cost and constraints for assignments
param cost {WORKERS, TASKS} >= 0;        # Cost of assigning a worker to a task
param max_tasks integer >= 1;            # Maximum number of tasks per worker

### VARIABLES
# Decision variable: assignment of tasks to workers
var IsAssigned {WORKERS, TASKS} binary;  # 1 if a worker is assigned to a task, 0 otherwise

### OBJECTIVE
# Minimize the total cost with an inverse relationship scaling
# The cost of assigning a worker to a task decreases with the number of tasks already assigned to that worker.
minimize TotalCost:
    sum {w in WORKERS, t in TASKS} 
        (cost[w, t] / (1 + sum{t2 in TASKS} IsAssigned[w,t2])) * IsAssigned[w,t];

### CONSTRAINTS
subject to TaskAssignment{t in TASKS}:      # Each task must be assigned to exactly one worker
    sum{w in WORKERS} IsAssigned[w,t] = 1;

subject to WorkerTaskLimit{w in WORKERS}:   # Each worker is assigned at most max_tasks tasks
    sum{t in TASKS} IsAssigned[w,t] <= max_tasks;
