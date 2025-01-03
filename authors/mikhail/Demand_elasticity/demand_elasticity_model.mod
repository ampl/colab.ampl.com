reset;
### Sets and Parameters
set POINTS;                             # Set of interpolated points
param demand{POINTS};                   # Demand values for each point
param price{POINTS};                    # Price values for each point
param revenue{POINTS};                  # Revenue (Precomputed demand * price) values for each point
param cost = 2;                         # Fixed costs

### Decision Variables
var select{POINTS}, binary;             # Binary decision variable to select a point with demand & price

### Objective Function: Maximize Profit
maximize TotalProfit:
    sum {p in POINTS} (revenue[p] - demand[p] * cost) * select[p];

# Constraints
s.t. OnePointSelected:
    sum {p in POINTS} select[p] = 1;    # Exactly one point is selected
