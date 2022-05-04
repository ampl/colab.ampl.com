This notebook provides the implementation of the production problem described in the book *AMPL: A Modeling Language for Mathematical Programming*
by Robert Fourer, David M. Gay, and Brian W. Kernighan.

## Example: steel model

This is an application of a generic production formulation described in the AMPL book with the following algebraic description, given:

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

We need not feel constrained by all the conventions of algebra, and we can instead consider changes that might make the model easier to work with when writing the model in AMPL. The short "mathematical" names for the sets, parameters and variables can be replaced by longer, more meaningful ones. These changes produce the following model:



```cell
%%writefile steel.mod
set PROD;  # products

param rate {PROD} > 0;     # tons produced per hour
param avail >= 0;          # hours available in week

param profit {PROD};       # profit per ton
param market {PROD} >= 0;  # limit on tons sold in week

var Make {p in PROD} >= 0, <= market[p]; # tons produced

maximize Total_Profit: sum {p in PROD} profit[p] * Make[p];

               # Objective: total profits from all products

subject to Time: sum {p in PROD} (1/rate[p]) * Make[p] <= avail;

               # Constraint: total of hours used by all
               # products may not exceed hours available


```


The indexing expressions have become {p in PROD}, or just {PROD} in those declarations that do not use the index p. The bounds on variables have been placed within their var declaration, rather than in a separate constraint; analogous bounds have been placed on the parameters, to indicate the ones that must be positive or nonnegative in any meaningful linear program derived from the model.

Finally, comments have been added to help explain the model. Comments begin with # and end at the end of the line. As in any programming language, judicious use of meaningful names, comments and formatting helps to make AMPL models more readable and understandable.

There are always many ways to describe a particular model in AMPL. It is left to the modeler to pick the way that seems clearest or most convenient. Our earlier, mathematical approach is often preferred for working quickly with a familiar model. On the other hand, the second version is more attractive for a model that will be maintained and modified by several people over months or years.


```cell
%%writefile steel.dat
data;

set PROD := bands coils;

param:    rate  profit  market :=
  bands    200    25     6000
  coils    140    30     4000 ;

param avail := 40;


```


```cell
%%ampl_eval
model steel.mod;
data steel.dat;
option solver cbc;
solve;
display Make;
```



### Adding lower bounds to the model

Once the model and data have been set up, it is a simple matter to change them and then re-solve. Indeed, we would not expect to find an LP application in which the model and data are prepared and solved just once, or even a few times. Most commonly, numerous refinements are introduced as the model is developed, and changes to the data continue for as long as the model is used.

Let's conclude this notebook with a few examples of changes and refinements. These examples also highlight some additional features of AMPL.

Suppose first that we add another product, steel plate. The model stays the same, but in the data we have to add plate to the list of members for the set PROD, and we have to add a line of parameter values for plate:


```cell
%%writefile steel2.dat
set PROD := bands coils plate;
param:        rate    profit     market :=
 bands        200      25        6000
 coils        140      30        4000
 plate        160      29        3500 ;
param avail := 40;
```


```cell
%%ampl_eval
reset data;
data steel2.dat;
solve;
display Make;
```

    


Profits have increased compared to the two-variable version, but now it is best to produce no coils at all! On closer examination, this result is not so surprising. Plate yields a profit of \$4640 per hour, which is less than for bands but more than for coils. Thus plate is produced to absorb the capacity not taken by bands; coils would be produced only if both bands and plate reached their market limits before the available hours were exhausted.

In reality, a whole product line cannot be shut down solely to increase weekly profits. The simplest way to reflect this in the model is to add lower bounds on the production amounts. We are declaring a new collection of parameters named commit, to represent the lower bounds on production that are imposed by sales commitments, and we have changed `>= 0` to `>= commit[p]` in the declaration of the variables `Make[p]`.


```cell
%%writefile steel3.mod
set PROD;                     # products
param rate {PROD} > 0;        # produced tons per hour
param avail >= 0;             # hours available in week
param profit {PROD};          # profit per ton
param commit {PROD} >= 0;     # lower limit on tons sold in week
param market {PROD} >= 0;     # upper limit on tons sold in week
var Make {p in PROD} >= commit[p], <= market[p]; # tons produced
maximize Total_Profit: sum {p in PROD} profit[p] * Make[p];
					    # Objective: total profits from all products
subject to Time: sum {p in PROD} (1/rate[p]) * Make[p] <= avail;
					    # Constraint: total of hours used by all
					    # products may not exceed hours available
```



```cell
%%writefile steel3.dat
set PROD := bands coils plate;
param:   rate  profit   commit   market :=
bands   200    25      1000     6000
coils   140    30       500     4000
plate   160    29       750     3500 ;
param avail := 40;
```



```cell
%%ampl_eval
reset; # clear the previous model
model steel3.mod;
data steel3.dat;
option solver cbc;
solve;
display commit, Make, market;
```



### Adding resource constraints to the model

Processing of steel slabs is not a single operation, but a series of steps that may proceed at different rates. To motivate a more general model, imagine that we divide production into a reheat stage that can process the incoming slabs at 200 tons per hour, and a rolling stage that makes bands, coils or plate at the rates previously given. Further imagine that there are only 35 hours of reheat time, even though there are 40 hours of rolling time.

To cover this kind of situation, we can add a set `STAGE` of production stages to our model. The parameter and constraint declarations are modified accordingly. Since there is a potentially different number of hours available in each stage, the parameter `avail` is now indexed over `STAGE`. Since there is a potentially different production rate for each product in each stage, the parameter `rate` is indexed over both `PROD` and `STAGE`. In the `Time` constraint, the production rate for product `p` in stage `s` is referred to as `rate[p,s]`; this is AMPL's version of a doubly subscripted entity like $a_{ps}$ in algebraic notation.


```cell
%%writefile steel4.mod
set PROD;                    # products
set STAGE;                   # stages
param rate {PROD,STAGE} > 0; # tons per hour in each stage
param avail {STAGE} >= 0;    # hours available/week in each stage
param profit {PROD};         # profit per ton
param commit {PROD} >= 0;    # lower limit on tons sold in week
param market {PROD} >= 0;    # upper limit on tons sold in week
var Make {p in PROD} >= commit[p], <= market[p]; # tons produced
maximize Total_Profit: sum {p in PROD} profit[p] * Make[p];
					    # Objective: total profits from all products
subject to Time {s in STAGE}:
      sum {p in PROD} (1/rate[p,s]) * Make[p] <= avail[s];
					    # In each stage: total of hours used by all
					    # products may not exceed hours available
```

The only other change is to the constraint declaration, where we no longer have a single constraint, but a constraint for each stage, imposed by limited time available at that stage. In algebraic notation, this might have been written as

*Subject to:*
$$\sum \limits_{p \in P} \frac{1}{a_{ps}} X_p \leq b_s, \text{ for each } s \in S.$$
Compare the AMPL version:
```
subject to Time {s in STAGE}:
  sum {p in PROD} (1/rate[p,s]) * Make[p] <= avail[s];
```

Since rate is now indexed over combinations of two indices, it requires a data table all to itself. The data file must also include the membership for the new set STAGE, and values of avail for both reheat and roll.


```cell
%%writefile steel4.dat
set PROD := bands coils plate;
set STAGE := reheat roll;
param rate:	reheat	roll :=
	bands	200	200
	coils	200	140
	plate	200	160 ;
param:	profit	commit	market :=
	bands	25	1000	6000
	coils	30	500	4000
	plate	29	750	3500 ;
param avail := reheat 35	roll 40 ;
```


After these changes are made, we use AMPL to get another revised solution:


```cell
%%ampl_eval
reset; # clear the previous model
model steel4.mod;
data steel4.dat;
option solver cbc;
solve;
display Make.lb, Make, Make.ub, Make.rc;
display Time;
```



At the end of the example above we have displayed the "marginal values" (also called "dual values" or "shadow prices") associated with the Time constraints. The marginal value of a constraint measures how much the value of the objective would improve if the constraint were relaxed by a small amount. For example, here we would expect that up to some point, additional reheat time would produce another \$1800 of extra profit per hour, and additional rolling time would produce \$3200 per hour; decreasing these times would decrease the profit correspondingly. In output commands like display, AMPL interprets a constraint's name alone as referring to the associated marginal values.

We also display several quantities associated with the variables Make. First there are lower bounds Make.lb and upper bounds Make.ub, which in this case are the same as commit and market. We also show the "reduced cost" Make.rc, which has the same meaning with respect to the bounds that the marginal values have with respect to the constraints. Thus we see that, again up to some point, each increase of a ton in the lower bound (or commitment) for coil production should reduce profits by about \$1.86; each one-ton decrease in the lower bound should improve profits by about \$1.86. The production levels for bands and plates are between their bounds, so their reduced costs are essentially zero, and changing their levels will have no effect.

Comparing this session with our previous one, we see that the additional reheat time restriction reduces profits by about \$4750, and forces a substantial change in the optimal solution: much higher production of plate and lower production of bands. Moreover, the logic underlying the optimum is no longer so obvious. It is the difficulty of solving LPs by logical reasoning alone that necessitates computer-based systems such as AMPL.

### Bibliography

* Julius S. Aronofsky, John M. Dutton and Michael T. Tayyabkhan, Managerial Planning with Linear Programming: In Process Industry Operations. John Wiley & Sons (New York, NY, 1978). A detailed account of a variety of profit-maximizing applications, with emphasis on the petroleum and petrochemical industries.

* Vasek Chvatal, Linear Programming, W. H. Freeman (New York, NY, 1983). A concise and economical introduction to theoretical and algorithmic topics in linear programming.

* Tibor Fabian, "A Linear Programming Model of Integrated Iron and Steel Production." Management Science 4 (1958) pp. 415-449. An application to all stages of steelmaking — from coal and ore through finished products — from the early days of linear programming.

* Robert Fourer and Goutam Dutta, "A Survey of Mathematical Programming Applications in Integrated Steel Plants." Manufacturing & Service Operations Management 4 (2001) pp. 387-400.

* David A. Kendrick, Alexander Meeraus and Jaime Alatorre, The Planning of Investment Programs in the Steel Industry. The Johns Hopkins University Press (Baltimore, MD, 1984). Several detailed mathematical programming models, using the Mexican steel industry as an example.

* Robert J. Vanderbei, Linear Programming: Foundations and Extensions (2nd edition). Kluwer Academic Publishers (Dordrecht, The Netherlands, 2001). An updated survey of linear programming theory and methods.
