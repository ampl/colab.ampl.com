reset;

# Model Name: Pricing Optimization (AMPL Piecewise construction for Price Elasticity of Demand)
# Version: 1.0
# Last Updated: Jan 2025

### PARAMETERS
param total_quantity >= 0;                  # Total quantity of products available for sale
param unit_cost >= 0;                       # Unit cost of the product

param n_step integer >= 1;                 # Number of steps in the piecewise linear price function
param demand {1..n_step+1} >= 0;           # Demand values at each step
param price {1..n_step+1} >= 0;            # Price for each step

### VARIABLES
var Quantity_Sold {1..n_step} >= 0;        # Quantity sold at each price step
var IsPrice_Selected {1..n_step} binary;   # Binary variable indicating whether the price step is selected

### OBJECTIVE
maximize Total_Revenue:                     # Maximize total revenue from sales           
    sum {i in 1..n_step} 
    <<demand[i]; {p in i..i+1} price[p] 
    - unit_cost>> Quantity_Sold[i];   

### CONSTRAINTS

s.t. Single_Price:                    # Ensure that only one price step can be selected
    sum {i in 1..n_step} IsPrice_Selected[i] = 1;

s.t. Quantity_Limit:                  # The total quantity sold cannot exceed the available quantity
    sum {i in 1..n_step} Quantity_Sold[i] <= total_quantity;

s.t. Price_Demand_Limit {i in 1..n_step}:    # Quantity sold at each step cannot exceed demand for that step if the price is selected
    Quantity_Sold[i] <= demand[i] * IsPrice_Selected[i];
