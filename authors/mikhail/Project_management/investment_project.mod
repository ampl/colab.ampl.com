reset;

### SETS ###
param nTASK >= 0 ;                              # Number of project work tasks
set DEP within                                  # Dependencies between tasks
    {i in 1..nTASK, j in 1..nTASK: i>j};
set DEP_TYPE =                                  # Types of task dependencies
    {'End-End', 'End-Begin', 'Begin-Begin', 'Begin-End'};
set LINKS within{DEP,DEP_TYPE} ;                # Task dependencies with sequence types

### PARAMETERS ###
param T;                                        # Total project duration in days (36 months * 30 days)
param penalty_rate;                             # Penalty rate per day of delay (0.1% per day)

param cost {1..nTASK} >= 0 ;                    # Cost of each task
param base_duration {1..nTASK} >= 0 ;           # Scheduled duration (in days) for each task
param lag {LINKS} integer;                      # Lag time between tasks (in days, can be negative)

param accel_cost {1..nTASK}  >= 0 ;             # Additional cost per day to reduce duration of each task
param max_reduction {1..nTASK} >= 0 ;           # Max days each task can be expedited
param risk_base {1..nTASK} >= 0 ;               # Base risk factor (0-1 scale) for each task
param max_risk;                                 # Maximum allowable risk increase

param permanent_cost;                           # Permanent cost per month (150K per month)

### VARIABLES ###
var Reduction {i in 1..nTASK} integer >= 0, <= max_reduction[i];  # Days by which each task duration is reduced
var Duration {i in 1..nTASK} >= 0 ;             # Actual duration of each stage after reduction
var RiskReduction {i in 1..nTASK} <= 1 + max_risk; # Increased risk for each task due to reduced duration
var Start {1..nTASK} >= 0;                      # Start time of each task
var CompletionTime {1..nTASK} >= 0;             # Actual completion time for each task
var Delay {1..nTASK} >= 0;                      # Delay in task completion (in days)
var Penalty {1..nTASK} >= 0;                    # Penalty for each task due to delay
var TotalCompletionTime >= 0, <= T;             # Maximum completion time across all tasks

### OBJECTIVE FUNCTION ###
# Maximize project profit by minimizing penalty and acceleration costs
minimize Project_Cost:
    sum {i in 1..nTASK} (cost[i] + Penalty[i] + accel_cost[i] * Reduction[i])
    + permanent_cost * (TotalCompletionTime / 30)
    + sum {i in 1..nTASK} RiskReduction[i] ;

### CONSTRAINTS ###
# 1. Start time of the first task is set to 1 (project begins with task 1)
s.t. Start_N1_At_Zero:
    Start[1] = 1;

# 2. Calculate duration of each task after considering reductions
s.t. Duration_count {i in 1..nTASK}:
    Duration[i] = base_duration[i] - Reduction[i];

# 3. Calculate risk increase based on the reduction in task duration
s.t. RiskReduction_count {i in 1..nTASK}:
    RiskReduction[i] = (1 + risk_base[i]) * (1 + Reduction[i] / base_duration[i]) ;

# 4a. Calculate each task's completion time based on start time, duration, and reductions
s.t. Completion_Calc {i in 1..nTASK}:
    CompletionTime[i] = Start[i] + Duration[i] - 1;

# 4b. Ensure TotalCompletionTime is at least the CompletionTime of each task
s.t. Max_Completion {i in 1..nTASK}:
    CompletionTime[i] <= TotalCompletionTime;

# 5. Enforce dependencies between tasks based on type and specified lag times
s.t. End_End_Dependencies {(i,j,k) in LINKS: k="End-End"}:
    CompletionTime[j] + lag[i,j,k] <= CompletionTime[i] ;

s.t. End_Begin_Dependencies {(i,j,k) in LINKS: k="End-Begin"}:    # New task (i) start, old task (j) finish
    CompletionTime[j] + lag[i,j,k] + 1 <= Start[i] ;

s.t. Begin_Begin_Dependencies {(i,j,k) in LINKS: k="Begin-Begin"}:
    Start[j] + lag[i,j,k] <= Start[i] ;

# 6. Calculate delays in task completion based on the total project duration
s.t. Delay_Calc {i in 1..nTASK}:
    Delay[i] >= CompletionTime[i] - T;

# 7. Calculate penalties based on delay duration and penalty rate
s.t. Penalty_Calc {i in 1..nTASK}:
    Penalty[i] = Delay[i] * penalty_rate * cost[i];
