reset;
set R;

param cost_waste;
param cost_transport {R};
param price_min;
param price_max;
param quantity_min {R};
param quantity_max {R};
param total_amount_of_supply;
param coefficients_intercept;
param coefficients_region {R};
param coefficients_price;
param coefficients_year_index;
param coefficients_peak;
param data_year;
param data_peak;

var price {r in R} >= price_min, <= price_max;
var quantity {r in R} >= quantity_min[r], <= quantity_max[r];

var demand_expr {r in R} =
    coefficients_intercept +
    coefficients_region[r] +
    coefficients_price * price[r] +
    coefficients_year_index * (data_year - 2015) +
    coefficients_peak * data_peak;

var sales {r in R} = min(demand_expr[r], quantity[r]);
var revenue {r in R} = sales[r] * price[r];
var waste {r in R} = quantity[r] - demand_expr[r];
var costs {r in R} = cost_waste * waste[r] + cost_transport[r] * quantity[r];

maximize obj: sum {r in R} (revenue[r] - costs[r]);

subject to supply: sum {r in R} quantity[r] = total_amount_of_supply;
