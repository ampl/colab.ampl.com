param predicted_demand;
param unit_cost;
param price;
param capacity;

var quantity >= 0, <= capacity;

maximize profit: (price - unit_cost) * quantity;

s.t. DemandLimit: quantity <= predicted_demand;
