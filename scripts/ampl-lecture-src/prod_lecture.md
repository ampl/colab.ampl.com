This notebook provides the implementation of the production problem described in the book *AMPL: A Modeling Language for Mathematical Programming*
by Robert Fourer, David M. Gay, and Brian W. Kernighan.

## Example: production model

It is usual to adopt mathematical notation as a general and concise way of expressing problems based on variables, constraints, and objectives. We can write a compact description of the general form of a production problem, which we call a *model*, using algebraic notation for the objective and the constraints.

### Algebraic formulation

Given:

* $P$, a set of products
* $a_j$ = tons per hour of product $j$, for each $j \in P$
* $b$ = hours available at the mill
* $c_j$ = profit per ton of product $j$, for each $j \in P$
* $u_j$ = maximum tons of product $j$, for each $j \in P$

Define variables:   $X_j$ = tons of product $j$ to be made, for each $j \in P$.

Maximize:
$$\sum \limits_{j \in P} c_j X_j$$

Subject to:
$$\sum \limits_{j \in P} \frac{1}{a_j} X_j \leq b$$

$$0 \leq X_j \leq u_j, \text{ for each }j \in P$$

The model describes an infinite number of related optimization problems. If we provide specific values for data, however, the model becomes a specific problem, or instance of the model, that can be solved. Each different collection of data values defines a different instance.


### Model implementation

The general formulation above can be written with AMPL as follows:


```cell
%%writefile prod.mod
# Sets and parameters
set P;

param a {j in P};
param b;
param c {j in P};
param u {j in P};

# Variables
var X {j in P};

# Objective function
maximize Total_Profit: sum {j in P} c[j] * X[j];

# Time and Limits constraints
subject to Time: sum {j in P} (1/a[j]) * X[j] <= b;

subject to Limit {j in P}: 0 <= X[j] <= u[j];
```

### Data

Due to the model and data separation, the abstract formulation works for any correct data input we provide to AMPL. A possible instance of the production problem is the following:


```cell
%%writefile prod.dat

set P := bands coils;

param:     a     c     u  :=
  bands   200   25   6000
  coils   140   30   4000 ;

param b := 40;
```


### Solve the problem

We can load the generated model and data files, and solve them by using a linear solver as CBC. Finally, the solution (values for X) is displayed.


```cell
%%ampl_eval
model prod.mod;
data prod.dat;
option solver cbc;
solve;
display X;
```


