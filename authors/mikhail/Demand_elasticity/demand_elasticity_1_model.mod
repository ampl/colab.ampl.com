reset;

# Model Name: # Pricing Optimization
# Description: This model maximizes total revenue by selecting the optimal price step and managing quantity sold under piecewise linear pricing.
# Version: 1.0
# Last Updated: Jan 2025

### PARAMETERS
# Input parameters defining total quantity, cost, price steps, and demand
param unit_cost >= 0;                   # Unit cost of the product
param n_step integer > 0;               # Number of steps in the piecewise linear price function
param demand {1..n_step+1} >= 0;        # Demand values at each price step
param price {1..n_step+1} >= 0;         # Price values for each demand step

### VARIABLES
# Decision variables for managing quantity and selecting price steps
var IsSelect {1..n_step} binary;        # Binary decision variable: 1 if point is selected, 0 otherwise
var Quantity_Sold {1..n_step} >= 0, integer; # Quantity sold at each price step

### OBJECTIVE
maximize Total_Profit:                  # Maximize total revenue from sales while considering costs and constraints
    sum{i in 1..n_step} Quantity_Sold[i] * (price[i] - unit_cost); 

### CONSTRAINTS
# Ensure logical and physical constraints are met
s.t. OnePriceSelected:                  # Only one price step can be selected
    sum {i in 1..n_step} IsSelect[i] = 1;

s.t. Demand_Upper_Bound {i in 1..n_step-1}:# Quantity sold must align with selected price step
    Quantity_Sold[i] <= (demand[i+1] - 0.0001)  * IsSelect[i] ;
