reset;
# Model Name: Point Selection for Profit Maximization
# Purpose: Select one point from a set of options to maximize total profit
# Version: 1.0
# Last Updated: Jan 2025


### SETS & PARAMETERS
# Define the set of points and their associated data
set POINTS;                             # Set of interpolated points
param demand {POINTS} >= 0;             # Demand values for each point
param price {POINTS} >= 0;              # Price values for each point
param revenue {POINTS} >= 0;            # Revenue (precomputed as demand * price) for each point
param cost >= 0 := 2;                   # Fixed cost per unit of demand

### VARIABLES
# Define decision variables for point selection
var IsSelect {POINTS} binary;           # Binary decision variable: 1 if point is selected, 0 otherwise

### OBJECTIVE
# Maximize total profit based on selected point
maximize TotalProfit:
    sum {p in POINTS} (revenue[p] - demand[p] * cost) * IsSelect[p];

### CONSTRAINTS
# Ensure exactly one point is selected
subject to OnePointSelected:
    sum {p in POINTS} IsSelect[p] = 1;    # Exactly one point is selected
