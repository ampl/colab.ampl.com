This notebook provides the implementation of the production problem described in the book *AMPL: A Modeling Language for Mathematical Programming*
by Robert Fourer, David M. Gay, and Brian W. Kernighan.

## Diet problem
As an intuitive example of a cost-minimizing model, we use the well-known "diet problem", which finds a mix of foods that satisfies requirements on the amounts of various vitamins. We will construct a small, explicit linear program, and then show how a general model can be formulated for all linear programs of that kind.

After formulating the diet model, we will discuss a few changes that might make it more realistic. The full power of this model, however, derives from its applicability to many situations that have nothing to do with diets. A general model derived from the diet formulation can be also applied to blending, economics, and scheduling.

### Solving a diet problem instance

Consider the problem of choosing prepared foods to meet certain nutritional requirements. Suppose that precooked dinners of the following kinds are available for the following prices per package:

|      | Name              | Price $ |
| ---- | ----------------- | ------- |
| BEEF | beef              | 3.19    |
| CHK  | chicken           | 2.59    |
| FISH | fish              | 2.29    |
| HAM  | ham               | 2.89    |
| MCH  | macaroni & cheese | 1.89    |
| MTL  | meat loaf         | 1.99    |
| SPG  | spaghetti         | 1.99    |
| TUR  | turkey            | 2.49    |

These dinners provide the following percentages, per package, of the minimum daily requirements for vitamins A, C, B1 and B2:


|      | A   | C   | B1  | B2  |
| ---- | --- | --- | --- | --- |
| BEEF | 60% | 20% | 10% | 15% |
| CHK  | 8   | 0   | 20  | 20  |
| FISH | 8   | 10  | 15  | 10  |
| HAM  | 40  | 40  | 35  | 10  |
| MCH  | 15  | 35  | 15  | 15  |
| MTL  | 70  | 30  | 15  | 15  |
| SPG  | 25  | 50  | 25  | 15  |
| TUR  | 60  | 20  | 15  | 10  |

The problem is to find the cheapest combination of packages that will meet a week's requirements - that is, at least 700% of the daily requirement for each nutrient.

Let us write $X_{beef}$ for the number of packages of beef dinner to be purchased, $X_{chk}$ for the number of packages of chicken dinner, and so forth. Then the total cost of the diet will be:
```ampl
total cost =
      3.19 Xbeef + 2.59 Xchk + 2.29 Xfish + 2.89 Xham +
      1.89 Xmch + 1.99 Xmtl + 1.99 Xspg + 2.49 Xtur
```

The total percentage of the vitamin A requirement is given by a similar formula, except that X BEEF , X CHK , and so forth are multiplied by the percentage per package instead of the cost per package:
```ampl
total percentage of vitamin A daily requirement met =
      60 Xbeef + 8 Xchk + 8 Xfish + 40 Xham +
      15 Xmch + 70 Xmtl + 25 Xspg + 60 Xtur
```

This amount needs to be greater than or equal to 700 percent. There is a similar formula for each of the other vitamins, and each of these also needs to be $\geq$ 700.

Putting these all together, we have the following linear program:

```ampl
Minimize
    3.19 Xbeef + 2.59 Xchk + 2.29 Xfish + 2.89 Xham +
    1.89 Xmch + 1.99 Xmtl + 1.99 Xspg + 2.49 Xtur

Subject to
     60 Xbeef + 8 Xchk + 8 Xfish + 40 Xham +
    15 Xmch + 70 Xmtl + 25 Xspg + 60 Xtur >= 700

      20 Xbeef + 0 Xchk + 10 Xfish + 40 Xham +
      35 Xmch + 30 Xmtl + 50 Xspg + 20 Xtur >= 700

      10 Xbeef + 20 Xchk + 15 Xfish + 35 Xham +
      15 Xmch + 15 Xmtl + 25 Xspg + 15 Xtur >= 700

      15 Xbeef + 20 Xchk + 10 Xfish + 10 Xham +
      15 Xmch + 15 Xmtl + 15 Xspg + 10 Xtur >= 700

      Xbeef >= 0, Xchk >= 0, Xfish >= 0, Xham >= 0,
      Xmch >= 0, Xmtl >= 0, Xspg >= 0, Xtur >= 0
```

At the end we have added the common-sense requirement that no fewer than zero packages of a food can be purchased. And now, we can transcribe the model to an AMPL statement of the explicit diet LP:


```cell
%%writefile diet0.mod
# Variables
var Xbeef >= 0; var Xchk >= 0; var Xfish >= 0;
var Xham >= 0; var Xmch >= 0; var Xmtl >= 0;
var Xspg >= 0; var Xtur >= 0;

# Objective function (minimizing)
minimize cost:
	3.19*Xbeef + 2.59*Xchk + 2.29*Xfish + 2.89*Xham +
	1.89*Xmch + 1.99*Xmtl + 1.99*Xspg + 2.49*Xtur;

# Constraints
subject to A:
	60*Xbeef + 8*Xchk + 8*Xfish + 40*Xham +
	15*Xmch + 70*Xmtl + 25*Xspg + 60*Xtur >= 700;
subject to C:
	20*Xbeef + 0*Xchk + 10*Xfish + 40*Xham +
	35*Xmch + 30*Xmtl + 50*Xspg + 20*Xtur >= 700;
subject to B1:
	10*Xbeef + 20*Xchk + 15*Xfish + 35*Xham +
	15*Xmch + 15*Xmtl + 25*Xspg + 15*Xtur >= 700;
subject to B2:
	15*Xbeef + 20*Xchk + 10*Xfish + 10*Xham +
	15*Xmch + 15*Xmtl + 15*Xspg + 10*Xtur >= 700;
```


A few AMPL commands then suffice to read the file, send the LP to a solver, and retrieve the results (using CBC solver from coin). AMPL commands within a Jupyter Notebook should be executed in a cell with the `%%ampl_eval` header.


```cell
%%ampl_eval
model diet0.mod;
option solver cbc;
solve;
display Xbeef,Xchk,Xfish,Xham,Xmch,Xmtl,Xspg,Xtur;
```

The optimal solution is found quickly, but it is hardly what we might have hoped for. The cost is minimized by a monotonous diet of 46 and 2/3 packages of macaroni and cheese! You can check that this neatly provides $15\% \times 46\frac{2}{3} = 700\%$ of the requirement for vitamins A, B1 and B2, and a lot more vitamin C than necessary; the cost is only $\$1.89 × 46\frac{2}{3} = \$88.20.$

You might guess that a better solution would be generated by requiring the amount of each vitamin to equal 700% exactly. Such a requirement can easily be imposed by changing each >= to = in the AMPL constraints. If you go ahead and solve the changed LP, you will find that the diet does indeed become more varied: approximately 19.5 packages of chicken, 16.3 of macaroni and cheese, and 4.3 of meat loaf. But since equalities are more restrictive than inequalities, the cost goes up to $89.99.

## An AMPL model for the diet problem

Clearly we will have to consider more extensive modifications to our linear program in order to produce a diet that is even remotely acceptable. We will probably want to change the sets of food and nutrients, as well as the nature of the constraints and bounds. As in the production example of the previous chapter, this will be much easier to do if we rely on a general model that can be coupled with a variety of specific data files.

This model deals with two things: nutrients and foods. Thus we begin an AMPL model by declaring sets of each:
```ampl
set NUTR;
set FOOD;
```
Next we need to specify the numbers required by the model. Certainly a positive cost should be given for each food:
```ampl
param cost {FOOD} > 0;
```
We also specify that for each food there are lower and upper limits on the number of packages in the diet:
```ampl
param f_min {FOOD} >= 0;
param f_max {j in FOOD} >= f_min[j];
```
Notice that we need a dummy index `j` to run over `FOOD` in the declaration of `f_max`, in order to say that the maximum for each food must be greater than or equal to the corresponding minimum.

To make this model somewhat more general than our examples so far, we also specify similar lower and upper limits on the amount of each nutrient in the diet:

```ampl
param n_min {NUTR} >= 0;
param n_max {i in NUTR} >= n_min[i];
```
Finally, for each combination of a nutrient and a food, we need a number that represents the amount of the nutrient in one package of the food. Such a "product" of two sets is written by listing them both:
```ampl
param amt {NUTR,FOOD} >= 0;
```
References to this parameter require two indices. For example, `amt[i,j]` is the amount of nutrient `i` in a package of food `j`.

The decision variables for this model are the numbers of packages to buy of the different foods:
```ampl
var Buy {j in FOOD} >= f_min[j], <= f_max[j];
```
The number of packages of some food `j` to be bought will be called `Buy[j]`; in any acceptable solution it will have to lie between `f_min[j]` and `f_max[j]`.

The total cost of buying a food `j` is the cost per package, `cost[j]`, times the number of packages, `Buy[j]`. The objective to be minimized is the sum of this product over all foods `j`:
```ampl
minimize Total_Cost: sum {j in FOOD} cost[j] * Buy[j];
```
Similarly, the amount of a nutrient `i` supplied by a food `j` is the nutrient per package, `amt[i,j]`, times the number of packages `Buy[j]`. The total amount of nutrient `i` supplied is the sum of this product over all foods `j`:
```ampl
sum {j in FOOD} amt[i,j] * Buy[j];
```
To complete the model, we need only specify that each such sum must lie between the appropriate bounds. Our constraint declaration begins
```ampl
subject to Diet {i in NUTR}:
```
to say that a constraint named `Diet[i]` must be imposed for each member `i` of `NUTR`. The rest of the declaration gives the algebraic statement of the constraint for nutrient `i`: the variables must satisfy
```ampl
n_min[i] <= sum {j in FOOD} amt[i,j] * Buy[j] <= n_max[i]
```
A "double inequality" like this is interpreted in the obvious way: the value of the sum in the middle must lie between `n_min[i]` and `n_max[i]`. We can write all together into a model file `diet.mod`:


```cell
%%writefile diet.mod
set NUTR;
set FOOD;

param cost {FOOD} > 0;
param f_min {FOOD} >= 0;
param f_max {j in FOOD} >= f_min[j];

param n_min {NUTR} >= 0;
param n_max {i in NUTR} >= n_min[i];

param amt {NUTR,FOOD} >= 0;

var Buy {j in FOOD} >= f_min[j], <= f_max[j];

minimize Total_Cost:  sum {j in FOOD} cost[j] * Buy[j];

subject to Diet {i in NUTR}:
   n_min[i] <= sum {j in FOOD} amt[i,j] * Buy[j] <= n_max[i];
```


## Data file

By specifying appropriate data, we can solve any of the linear programs that correspond to the above model. Let's begin by using the data from the previous example.

The values of `f_min` and `n_min` are as given originally, while `f_max` and `n_max` are set, for the time being, to large values that won't affect the optimal solution. In the table for `amt`, the notation (tr) indicates that we have "transposed" the table so the columns correspond to the first index (nutrients), and the rows to the second (foods). Alternatively, we could have changed the model to say
```ampl
param amt {FOOD,NUTR}
```
in which case we would have had to write amt[j,i] in the constraint.

The data file `diet.dat` is created with:


```cell
%%writefile diet.dat
data;

set NUTR := A B1 B2 C ;
set FOOD := BEEF CHK FISH HAM MCH MTL SPG TUR ;

param:   cost  f_min  f_max :=
  BEEF   3.19    0     100
  CHK    2.59    0     100
  FISH   2.29    0     100
  HAM    2.89    0     100
  MCH    1.89    0     100
  MTL    1.99    0     100
  SPG    1.99    0     100
  TUR    2.49    0     100 ;

param:   n_min  n_max :=
   A      700   10000
   C      700   10000
   B1     700   10000
   B2     700   10000 ;

param amt (tr):
           A    C   B1   B2 :=
   BEEF   60   20   10   15
   CHK     8    0   20   20
   FISH    8   10   15   10
   HAM    40   40   35   10
   MCH    15   35   15   15
   MTL    70   30   15   15
   SPG    25   50   25   15
   TUR    60   20   15   10 ;
```


Suppose that model and data are stored in the files `diet.mod` and `diet.dat`, respectively. Then AMPL is used as follows to read these files and to solve the resulting linear program:


```cell
%%ampl_eval
reset; # to clean the previous model
model diet.mod;
data diet.dat;
option solver cbc;
solve;
display Buy;
```

Naturally, the result is the same as before.

Now suppose that we want to make the following enhancements. To promote variety, the weekly diet must contain between 2 and 10 packages of each food. The amount of sodium and calories in each package is also given; total sodium must not exceed 40,000 mg, and total calories must be between 16,000 and 24,000. All of these changes can be made through a few modifications to the data. Putting this new data in file `diet2.dat`, we can run AMPL again:




```cell
%%writefile diet2.dat
set NUTR := A B1 B2 C NA CAL ;
set FOOD := BEEF CHK FISH HAM MCH MTL SPG TUR ;
param:         cost   f_min f_max :=
	BEEF    3.19     2    10
	CHK     2.59     2    10
	FISH    2.29     2    10
	HAM     2.89     2    10
	MCH     1.89     2    10
	MTL     1.99     2    10
	SPG     1.99     2    10
	TUR     2.49     2    10 ;
param:   n_min      n_max :=
	 A      700       20000
	 C      700       20000
	 B1     700       20000
	 B2     700       20000
	 NA       0       40000
	 CAL  16000       24000 ;
param amt (tr):
		  A    C  B1  B2    NA  CAL :=
	 BEEF   60   20  10  15   938  295
	 CHK     8    0  20  20  2180  770
	 FISH    8   10  15  10   945  440
	 HAM    40   40  35  10   278  430
	 MCH    15   35  15  15  1182  315
	 MTL    70   30  15  15   896  400
	 SPG    25   50  25  15  1329  370
	 TUR    60   20  15  10  1397  450 ;
```


```cell
%%ampl_eval
reset data; # to reset the data not the model
data diet2.dat;
solve;
display Buy;
```

The message infeasible problem tells us that we have constrained the diet too tightly; there is no way that all of the restrictions can be satisfied.

AMPL lets us examine a variety of values produced by a solver as it attempts to find a solution. We can use marginal (or dual) values to investigate the sensitivity of an optimum solution to changes in the constraints. Here there is no optimum, but the solver does return the last solution that it found while attempting to satisfy the constraints. We can look for the source of the infeasibility by displaying some values associated with this solution:


```cell
%%ampl_eval
display      Diet.lb, Diet.body, Diet.ub;
```

For each nutrient, `Diet.body` is the sum of the terms `amt[i,j] * Buy[j]` in the constraint `Diet[i]`. The `Diet.lb` and `Diet.ub` values are the "lower bounds" and "upper bounds" on the sum in `Diet[i] - in this case, just the values `n_min[i]` and `n_max[i]`. We can see that the diet returned by the solver does not supply enough vitamin B2, while the amount of sodium (NA) has reached its upper bound.

At this point, there are two obvious choices: we could require less B2 or we could allow more sodium. If we try the latter, and relax the sodium limit to 50,000 mg, a feasible solution becomes possible (let statement permits modifications of data):


```cell
%%ampl_eval
let n_max["NA"] := 50000;
solve;
display Buy;
```

This is at least a start toward a palatable diet, although we have to spend \$118.06, compared to \$88.20 for the original, less restricted case. Clearly it would be easy, now that the model is set up, to try many other possibilities. Section 11.3 of the AMPL book describes ways to quickly change the data and re-solve.

One still disappointing aspect of the solution is the need to buy 5.36061 packages of beef, and 9.30605 of spaghetti. How can we find the best possible solution in terms of whole packages? You might think that we could simply round the optimal values to whole numbers - or integers, as they're often called in the context of optimization - but it is not so easy to do so in a feasible way. Using AMPL to modify the reported solution , we can observe that rounding up to 6 packages of beef and 10 of spaghetti, for example, will violate the sodium limit:


```cell
%%ampl_eval
let Buy["BEEF"] := 6;
let Buy["SPG"] := 10;

display Diet.lb, Diet.body, Diet.ub;
```
    

You can similarly check that rounding the solution down to 5 of beef and 9 of spaghetti will provide insufficient vitamin B2. Rounding one up and the other down doesn't work either. With enough experimenting you can find a nearby all-integer solution that does satisfy the constraints, but still you will have no guarantee that it is the least-cost allinteger solution.

AMPL does provide for putting the integrality restriction directly into the declaration of the variables:
```ampl
var Buy {j in FOOD} integer >= f_min[j], <= f_max[j];
```
This will only help, however, if you use a solver that can deal with problems whose variables must be integers. CBC solver can handle these so called integer programs. If we add integer to the declaration of variable `Buy` as above, save the resulting model in the file `dieti.mod`, and add the higher sodium limit to `diet2a.dat`, then we can re-solve as follows:


```cell
%%writefile dieti.mod
set NUTR;
set FOOD;

param cost {FOOD} > 0;
param f_min {FOOD} >= 0;
param f_max {j in FOOD} >= f_min[j];

param n_min {NUTR} >= 0;
param n_max {i in NUTR} >= n_min[i];

param amt {NUTR,FOOD} >= 0;

var Buy {j in FOOD} integer >= f_min[j], <= f_max[j];

minimize Total_Cost:  sum {j in FOOD} cost[j] * Buy[j];

subject to Diet {i in NUTR}:
   n_min[i] <= sum {j in FOOD} amt[i,j] * Buy[j] <= n_max[i];
```


```cell
%%writefile diet2a.dat
set NUTR := A B1 B2 C NA CAL ;
set FOOD := BEEF CHK FISH HAM MCH MTL SPG TUR ;
param:         cost   f_min f_max :=
	BEEF    3.19     2    10
	CHK     2.59     2    10
	FISH    2.29     2    10
	HAM     2.89     2    10
	MCH     1.89     2    10
	MTL     1.99     2    10
	SPG     1.99     2    10
	TUR     2.49     2    10 ;
param:   n_min      n_max :=
	 A      700       20000
	 C      700       20000
	 B1     700       20000
	 B2     700       20000
	 NA       0       50000
	 CAL  16000       24000 ;
param amt (tr):
		  A    C  B1  B2    NA  CAL :=
	 BEEF   60   20  10  15   938  295
	 CHK     8    0  20  20  2180  770
	 FISH    8   10  15  10   945  440
	 HAM    40   40  35  10   278  430
	 MCH    15   35  15  15  1182  315
	 MTL    70   30  15  15   896  400
	 SPG    25   50  25  15  1329  370
	 TUR    60   20  15  10  1397  450 ;
```


```cell
%%ampl_eval
model dieti.mod;
data diet2a.dat;
option solver cbc;
solve;
display Buy;
```

Since integrality is an added constraint, it is no surprise that the best integer solution costs about \$1.24 more than the best "continuous" one. But the difference between the diets is unexpected; the amounts of 3 foods change, each by two or more packages. In general, integrality and other "discrete" restrictions make solutions for a model much harder to find.

## Generalizations to blending, economics and scheduling

Your personal experience probably suggests that diet models are not widely used by people to choose their dinners. These models would be much better suited to situations in which packaging and personal preferences don't play such a prominent role — for example , the blending of animal feed or perhaps food for college dining halls.

The diet model is a convenient, intuitive example of a linear programming formulation that appears in many contexts. Suppose that we rewrite the model in a more general way:

```ampl
set INPUT;            # inputs
set OUTPUT;           # outputs
param cost {INPUT} > 0;
param in_min {INPUT} >= 0;
param in_max {j in INPUT} >= in_min[j];
param out_min {OUTPUT} >= 0;
param out_max {i in OUTPUT} >= out_min[i];
param io {OUTPUT,INPUT} >= 0;
var X {j in INPUT} >= in_min[j], <= in_max[j];
minimize Total_Cost: sum {j in INPUT} cost[j] * X[j];
subject to Outputs {i in OUTPUT}:
	out_min[i] <= sum {j in INPUT} io[i,j] * X[j] <= out_max[i];
```

The objects that were called *foods* and *nutrients* in the diet model are now referred to more generically as *inputs* and *outputs*. For each input `j`, we must decide to use a quantity `X[j]` that lies between `in_min[j]` and `in_max[j]`; as a result we incur a cost equal to `cost[j]·X[j]`, and we create `io[i,j]·X[j]` units of each output `i`. Our goal is to find the least-cost combination of inputs that yields, for each output `i`, an amount between `out_min[i]` and `out_max[i]`.

In one common class of applications for this model, the inputs are raw materials to be mixed together. The outputs are qualities of the resulting **blend**. The raw materials could be the components of an animal feed, but they could equally well be the crude oil derivatives that are blended to make gasoline, or the different kinds of coal that are mixed as input to a coke oven. The qualities can be amounts of something (sodium or calories for animal feed), or more complex measures (vapor pressure or octane rating for gasoline), or even physical properties such as weight and volume.

In another well-known application, the inputs are production activities of some sector of an **economy**, and the outputs are various products. The `in_min` and `in_max` parameters are limits on the levels of the activities, while `out_min` and `out_max` are regulated by demands. Thus the goal is to find levels of the activities that meet demand at the lowest cost. This interpretation is related to the concept of an economic equilibrium.

In still another, quite different application, the inputs are **work schedules**, and the outputs correspond to hours worked on certain days of a month. For a particular work schedule `j`, `io[i,j]` is the number of hours that a person following schedule `j` will work on day `i` (zero if none), `cost[j]` is the monthly salary for a person following schedule `j`, and `X[j]` is the number of workers assigned that schedule. Under this interpretation, the objective becomes the total cost of the monthly payroll, while the constraints say that for each day `i`, the total number of workers assigned to work that day must lie between the limits `out_min[i]` and `out_max[i]`. The same approach can be used in a variety of other scheduling contexts, where the hours, days or months are replaced by other periods of time.

Although linear programming can be very useful in applications like these, we need to keep in mind the assumptions that underlie the LP model. We have already mentioned the "continuity" assumption whereby `X[j]` is allowed to take on any value between `in_min[j]` and `in_max[j]`. This may be a lot more reasonable for blending than for scheduling.

As another example, in writing the objective as
```ampl
sum {j in INPUT} cost[j] * X[j]
```
we are assuming "linearity of costs", that is, that the cost of an input is proportional to the amount of the input used, and that the total cost is the sum of the inputs' individual costs.

In writing the constraints as
```ampl
out_min[i] <= sum {j in INPUT} io[i,j] * X[j] <= out_max[i]
```
we are also assuming that the yield of an output `i` from a particular input is proportional to the amount of the input used, and that the total yield of an output `i` is the sum of the yields from the individual inputs. This "linearity of yield" assumption poses no problem when the inputs are schedules, and the outputs are hours worked. But in the blending example, linearity is a physical assumption about the nature of the raw materials and the qualities, which may or may not hold. In early applications to refineries, for example, it was recognized that the addition of lead as an input had a nonlinear effect on the quality known as octane rating in the resulting blend.

AMPL makes it easy to express discrete or nonlinear models, but any departure from continuity or linearity is likely to make an optimal solution much harder to obtain. At the least, it takes a more powerful solver to optimize the resulting mathematical programs.

## Bibliography

* George B. Dantzig, "The Diet Problem." Interfaces 20, 4 (1990) pp. 43-47. An entertaining account of the origins of the diet problem.

* Robert Fourer, David M. Gay, and Brian W. Kernighan, "AMPL: A Modeling Language for Mathematical Programming (2nd edition)." Cengage Learning (2002).





* Susan Garner Garille and Saul I. Gass, "Stigler's Diet Problem Revisited." Operations Research 49, 1 (2001) pp. 1-13. A review of the diet problem's origins and its influence over the years on linear programming and on nutritionists.

* Said S. Hilal and Warren Erikson, "Matching Supplies to Save Lives: Linear Programming the Production of Heart Valves." Interfaces 11, 6 (1981) pp. 48-56. A less appetizing equivalent of the diet problem, involving the choice of pig heart suppliers.
