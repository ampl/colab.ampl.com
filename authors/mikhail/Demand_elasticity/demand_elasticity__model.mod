reset;
# Model Name: Pricing Optimization (Price Elasticity of Demand)
# Purpose: Select one point from a set of price level and demand to maximize total profit
# Version: 1.0
# Last Updated: Jan 2025


### SETS & PARAMETERS
# Input parameters defining total quantity, cost, price steps, and demand
param unit_cost >= 0;                   # Unit cost of the product
param n_step integer > 0;               # Number of steps in the piecewise linear price function
param demand {1..n_step} >= 0;          # Demand values at each price step
param price {1..n_step} >= 0;           # Price values for each demand step

### VARIABLES
# Define decision variables for point selection
var IsSelect {1..n_step} binary;        # Binary decision variable: 1 if point is selected, 0 otherwise

### OBJECTIVE
# Maximize total profit based on selected point
maximize TotalProfit:
    sum {p in 1..n_step} demand[p] * (price[p] - unit_cost) * IsSelect[p];

### CONSTRAINTS
# Ensure exactly one point is selected
subject to OnePriceSelected:
    sum {p in 1..n_step} IsSelect[p] = 1;   # Exactly one point is selected
