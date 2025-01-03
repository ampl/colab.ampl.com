reset;
### PARAMETERS
param total_Quantity >= 0;              # Total quantity of products available for sale
param unit_Cost >= 0;                   # Unit cost of the product

param nStep integer >= 1;               # Number of steps in the piecewise linear price function
param demand {1..nStep+1} >= 0;         # Demand values at each step
param price {1..nStep+1} >= 0;          # Price for each step


### VARIABLES
var Quantity_Sold {1..nStep} >= 0;      # Quantity sold at each price step
var Price_Selected {1..nStep} binary;   # Binary variable indicating whether the price step is selected


### OBJECTIVE
maximize Total_Revenue:                 # Maximize total revenue (profit from sales)
    sum {i in 1..nStep} 
    <<demand[i]; {p in i..i+1} price[p] 
    - unit_Cost>> Quantity_Sold[i];     # Here we use a piecewise linear function for a limited range i..i+1


### CONSTRAINTS
s.t. Single_Price:                      # Only one price step can be selected
    sum {i in 1..nStep} Price_Selected[i] = 1;

s.t. Quantity_Limit:                    # The total quantity sold cannot exceed available quantity
    sum {i in 1..nStep} Quantity_Sold[i] <= total_Quantity;

s.t. Price_Upper_Bound {i in 1..nStep}: # Quantity sold cannot exceed upper price step
    Quantity_Sold[i] <= demand[i] * Price_Selected[i];
