set GENERATORS;
set TIME ordered;

param demand {TIME} >= 0;                   # Power demand at each time
param min_output {GENERATORS} >= 0;         # Minimum power output
param max_output {g in GENERATORS} >= min_output[g];  # Maximum power output
param ramp_up_limit {GENERATORS} >= 0;
param ramp_down_limit {GENERATORS} >= 0;

param linear_cost {GENERATORS};             # Linear cost coefficient
param quadratic_cost {GENERATORS} >= 0;     # Quadratic cost coefficient
param startup_cost {GENERATORS} >= 0;       # Startup cost

param emission_rate {GENERATORS} >= 0;      # Tons CO2 per MW produced

var is_committed {GENERATORS, TIME} binary;       # 1 if generator is ON
var power_generated {gen in GENERATORS, TIME} >= 0 <= max_output[gen];      # MW produced
var is_startup {GENERATORS, TIME} binary;         # 1 if generator starts up

# Generation only if committed
subject to Generation_Commitment {gen in GENERATORS, t in TIME}:
    power_generated[gen,t] > 0 <==> is_committed[gen,t] = 1;

# Meet demand in each period
subject to Demand_Satisfaction {t in TIME}:
    sum {gen in GENERATORS} power_generated[gen,t] >= demand[t];

# Startup in first period
subject to Startup_First {gen in GENERATORS}:
    is_startup[gen, first(TIME)] == is_committed[gen, first(TIME)];

# Startup logic in subsequent periods
subject to Startup_Transition {gen in GENERATORS, t in TIME: ord(t) > 1}:
    is_startup[gen,t] <==> (is_committed[gen,t] and !is_committed[gen,prev(t)]);

subject to Min_Gen_If_On {gen in GENERATORS, t in TIME}:
    power_generated[gen,t] == 0 or power_generated[gen,t] >= min_output[gen];

# Ramp-up limits
subject to Ramp_Up {gen in GENERATORS, t in TIME: ord(t) > 1}:
    power_generated[gen,t] - power_generated[gen,prev(t)] <= ramp_up_limit[gen];

# Ramp-down limits
subject to Ramp_Down {gen in GENERATORS, t in TIME: ord(t) > 1}:
    power_generated[gen,prev(t)] - power_generated[gen,t] <= ramp_down_limit[gen];

# Objective 1: Minimize total operating + startup cost
minimize Total_Cost:
    sum {gen in GENERATORS, t in TIME}
        (linear_cost[gen] * power_generated[gen,t] +
         quadratic_cost[gen] * power_generated[gen,t]^2)
  + sum {gen in GENERATORS, t in TIME} startup_cost[gen] * is_startup[gen,t];

# Objective 2: Minimize total emissions
minimize Total_Emissions:
    sum {gen in GENERATORS, t in TIME} emission_rate[gen] * power_generated[gen,t];

# Multi-objective support
suffix objpriority;
suffix objabstol;
suffix objreltol;
