reset;

### SETS
set WORKERS;                        # Set of workers
set TASKS;                          # Set of tasks

### PARAMETERS
param cost {WORKERS, TASKS} >= 0;   # Cost of assigning a worker to a task
param max_tasks integer >= 1;       # Maximum number of tasks per worker

### VARIABLES
var x {WORKERS, TASKS} binary;      # 1 if worker is assigned to task, 0 otherwise

### OBJECTIVE: Minimize the total cost with inverse relationship scaling
minimize TotalCost:
    sum {w in WORKERS, t in TASKS} (cost[w, t] / (1 + sum {t2 in TASKS} x[w, t2])) * x[w, t];

### CONSTRAINTS
subject to TaskAssignment {t in TASKS}:
    sum {w in WORKERS} x[w, t] = 1; # Each task must be assigned to exactly one worker

subject to WorkerLimit {w in WORKERS}:
    sum {t in TASKS} x[w, t] <= max_tasks; # Each worker is assigned at most max_tasks tasks
