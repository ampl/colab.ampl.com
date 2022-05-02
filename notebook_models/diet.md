### Example: diet

Generated using diet.mod, diet.dat, and diet.run.

Consider the problem of choosing prepared foods to meet certain nutritional requirements.

Sets:
- `NUTR`: set of nutrients to consider
- `FOOD`: set of food to consider

Parameters:
- `cost {FOOD}`: cost of each food
- `f_min {FOOD}`: minimum amount of food to buy
- `f_max {FOOD}`: maximum amount of food to buy
- `n_min {NUTR}`: minimum amount required of each nutrient
- `n_max {NUTR}`: maximum amount allowed of each nutrient
- `amt {NUTR, FOOD}`: amount of each nutrient in each food

Variables:
- `Buy {FOOD}`: amount of food to buy

Objective:
- `Total_Cost`: total cost of the diet

Constraints:
- `Diet {NUTR}`: ensure that the nutritional requirements are satisfied by the diet. 
