reset;

# Model Name: # Pricing Optimization (Piecewise Price Elastisity of Demand)
# Description: This model maximizes total revenue by selecting the optimal price step and managing quantity sold under piecewise linear pricing.
# Version: 1.0
# Last Updated: Jan 2025

### PARAMETERS
# Input parameters defining total quantity, cost, price steps, and demand
param total_quantity >= 0;             # Total quantity of products available for sale
param unit_cost >= 0;                  # Unit cost of the product
param n_step integer > 0;              # Number of steps in the piecewise linear price function
param demand {1..n_step+1} >= 0;       # Demand values at each price step
param price {1..n_step+1} >= 0;        # Price values for each demand step

### VARIABLES
# Decision variables for managing quantity and selecting price steps
var Quantity_Sold {1..n_step} >= 0;    # Quantity sold at each price step
var Is_Price_Selected {1..n_step} binary; # Binary variable indicating whether a price step is selected

### OBJECTIVE
maximize Total_Revenue:                 # Maximize total revenue from sales while considering costs and constraints
    sum {i in 1..n_step} (
        demand[i] * price[i] * Is_Price_Selected[i] 
        - (Quantity_Sold[i] - demand[i] * Is_Price_Selected[i])
        - Quantity_Sold[i] * unit_cost );

### CONSTRAINTS
# Ensure logical and physical constraints are met

s.t. Single_Price:                      # Only one price step can be selected
    sum {i in 1..n_step} Is_Price_Selected[i] = 1;

s.t. Quantity_Limit:                    # Total quantity sold cannot exceed available quantity
    sum {i in 1..n_step} Quantity_Sold[i] <= total_quantity;

s.t. Price_Upper_Bound {i in 1..n_step}:# Quantity sold must align with selected price step (upper bound)
    Quantity_Sold[i] >= demand[i] * Is_Price_Selected[i];

s.t. Price_Lower_Bound {i in 1..n_step}:# Quantity sold must align with selected price step (lower bound)
    Quantity_Sold[i] <= demand[i+1] * Is_Price_Selected[i];
