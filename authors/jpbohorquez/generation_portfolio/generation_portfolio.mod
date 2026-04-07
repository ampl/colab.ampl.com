# Model Name: Energy Portfolio Optimization

### SETS
set PERIODS ordered;  # hours
set THERMAL_GENERATORS default {};
set RESERVOIR_HYDRO_GENERATORS default {};
set CONVENTIONAL_GENERATORS = THERMAL_GENERATORS union RESERVOIR_HYDRO_GENERATORS;
set ROR_HYDRO_GENERATORS default {};
set HYDRO_GENERATORS = RESERVOIR_HYDRO_GENERATORS union ROR_HYDRO_GENERATORS;
set UPSTREAM_GENERATORS {HYDRO_GENERATORS} within HYDRO_GENERATORS default {};
set SOLAR_GENERATORS default {};
set WIND_GENERATORS default {};
set RENEWABLE_GENERATORS = SOLAR_GENERATORS union WIND_GENERATORS;
set GENERATORS = THERMAL_GENERATORS union HYDRO_GENERATORS union RENEWABLE_GENERATORS;


### PARAMETERS
# Forecasted Params
param market_price {PERIODS} >= 0;                # Forecasted market energy price ($/MWh)
param marginal_cost {THERMAL_GENERATORS, PERIODS} >= 0;    # Marginal fuel cost ($/MWh)
param inflows {HYDRO_GENERATORS, PERIODS} >= 0 default 0;  # Water contributions/inflows (m3/s)
param renewable_resource {RENEWABLE_GENERATORS, PERIODS} >= 0; # Renewable resource availability (MW)

# Thermal Units Params
param ramp_up_rate {THERMAL_GENERATORS} >= 0;     # Ramp up limit (MW/hour)
param ramp_down_rate {THERMAL_GENERATORS} >= 0;   # Ramp down limit (MW/hour)

# Hydro Params
param efficiency {HYDRO_GENERATORS} > 0;               # Conversion Factor (MW/m3/s)
param reservoir_max_capacity {RESERVOIR_HYDRO_GENERATORS} >= 0; # Reservoir max capacity (Hm3)
param initial_storage {r in RESERVOIR_HYDRO_GENERATORS} >= 0 default 0.7*reservoir_max_capacity[r];         # Initial reservoir energy (Hm3)
param final_storage {r in RESERVOIR_HYDRO_GENERATORS} >= 0 default initial_storage[r];  # Required energy at end of horizon (Hm3)

# Operational Params/Limits
param max_generation {CONVENTIONAL_GENERATORS, PERIODS} >= 0;  # Maximum generation (MW)
param min_generation {GENERATORS, PERIODS} >= 0 default 0;  # Minimum generation (MW)

# Penalty Params
param penalty_spillage {HYDRO_GENERATORS} >= 0 default 2.5* max{t in PERIODS}(market_price[t]); # Penalty for water spillage ($/MWh)

# Computed/Scalar Params
param period_duration >=0 default 3600; # Duration of each period in seconds (default: 1 hour)
param delta_t = period_duration / 1000000;  # Constant to convert m3/s to Hm3 per period


### VARIABLES
var Generation {GENERATORS, PERIODS} >= 0;  # MW
var ReservoirStorage {RESERVOIR_HYDRO_GENERATORS, PERIODS} >= 0;  # Hm3
var TurbiningFlow {HYDRO_GENERATORS, PERIODS} >= 0;  # m3/s
var Spillage {HYDRO_GENERATORS, PERIODS} >= 0;  # MWh
var SpillageFlow {HYDRO_GENERATORS, PERIODS} >= 0;  # m3/s


### OBJECTIVE FUNCTION
maximize TotalProfit:
    sum {g in GENERATORS, t in PERIODS} (market_price[t] * Generation[g, t])
    - sum {g in THERMAL_GENERATORS, t in PERIODS} (marginal_cost[g, t] * Generation[g, t])
    - sum {g in HYDRO_GENERATORS, t in PERIODS} (penalty_spillage[g] * Spillage[g, t]);


### CONSTRAINTS
subject to ReservoirHydroBalance {g in RESERVOIR_HYDRO_GENERATORS, t in PERIODS}:
    ReservoirStorage[g, t] = (if t = first(PERIODS) then initial_storage[g] else ReservoirStorage[g, prev(t)])
                                + delta_t * (inflows[g, t]
                                            + sum {ug in UPSTREAM_GENERATORS[g]} (TurbiningFlow[ug, t] + SpillageFlow[ug, t])
                                            - TurbiningFlow[g, t]
                                            - SpillageFlow[g, t]);

subject to RunOfRiverBalance {g in ROR_HYDRO_GENERATORS, t in PERIODS}:
    TurbiningFlow[g, t] + SpillageFlow[g, t] <= inflows[g, t];

subject to ReservoirStorageLimit {g in RESERVOIR_HYDRO_GENERATORS, t in PERIODS}:
    ReservoirStorage[g, t] <= reservoir_max_capacity[g];

subject to ReservoirFinalStorage {g in RESERVOIR_HYDRO_GENERATORS}:
    ReservoirStorage[g, last(PERIODS)] = final_storage[g];

subject to HydroGenerationFromFlow {g in HYDRO_GENERATORS, t in PERIODS}:
    Generation[g, t] = efficiency[g] * TurbiningFlow[g, t];

subject to HydroSpillageFromFlow {g in HYDRO_GENERATORS, t in PERIODS}:
    Spillage[g, t] = efficiency[g] * SpillageFlow[g, t];

subject to RenewableGenerationLimit {g in RENEWABLE_GENERATORS, t in PERIODS}:
    Generation[g, t] <= renewable_resource[g, t];

subject to ThermalRampUp {g in THERMAL_GENERATORS, t in PERIODS: ord(t) > 1}:
    Generation[g, t] - Generation[g, prev(t)] <= ramp_up_rate[g];

subject to ThermalRampDown {g in THERMAL_GENERATORS, t in PERIODS: ord(t) > 1}:
    Generation[g, prev(t)] - Generation[g, t] <= ramp_down_rate[g];

subject to GenerationMaxLimit {g in CONVENTIONAL_GENERATORS, t in PERIODS}:
    Generation[g, t] <= max_generation[g, t];

subject to GenerationMinLimit {g in GENERATORS, t in PERIODS}:
    Generation[g, t] >= min_generation[g, t];

