This notebook provides the implementation of the transportation problem described in the book *AMPL: A Modeling Language for Mathematical Programming*
by Robert Fourer, David M. Gay, and Brian W. Kernighan.

## Example: Transportation problem
Two fundamental sets of objects underlie the transportation problem: the sources or origins (mills, in our example) and the destinations (factories). Thus we begin the AMPL model with a declaration of these two sets:
```ampl
set ORIG;
set DEST;
```
There is a supply of something at each origin (tons of steel coils produced, in our case), and a demand for the same thing at each destination (tons of coils ordered). AMPL defines nonnegative quantities like these with param statements indexed over a set; in this case we add one extra refinement, a check statement to test the data for validity:
```ampl
param supply {ORIG} >= 0;
param demand {DEST} >= 0;
check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];
```
The check statement says that the sum of the supplies has to equal the sum of the demands. The way that our model is to be set up, there can't possibly be any solutions unless this condition is satisfied. By putting it in a check statement, we tell AMPL to test this condition after reading the data, and to issue an error message if it is violated.

For each combination of an origin and a destination, there is a transportation cost and a variable representing the amount transported. Again, the ideas from previous chapters are easily adapted to produce the appropriate AMPL statements:
```ampl
param cost {ORIG,DEST} >= 0;
var Trans {ORIG,DEST} >= 0;
```
For a particular origin `i` and destination `j`, we ship `Trans[i,j]` units from `i` to `j`, at a cost of `cost[i,j]` per unit; the total cost for this pair is
```ampl
cost[i,j] * Trans[i,j]
```
Adding over all pairs, we have the objective function:
```ampl
minimize Total_Cost:
   sum {i in ORIG, j in DEST} cost[i,j] * Trans[i,j];
```
which could also be written as
```ampl
sum {j in DEST, i in ORIG} cost[i,j] * Trans[i,j];
```
or as
```ampl
sum {i in ORIG} sum {j in DEST} cost[i,j] * Trans[i,j];
```
As long as you express the objective in some mathematically correct way, AMPL will sort out the terms.

It remains to specify the two collections of constraints, those at the origins and those at the destinations. If we name these collections Supply and Demand, their declarations will start as follows:
```ampl
subject to Supply {i in ORIG}: ...
subject to Demand {j in DEST}: ...
```
To complete the `Supply` constraint for origin `i`, we need to say that the sum of all shipments out of `i` is equal to the supply available. Since the amount shipped out of `i` to a particular destination `j` is `Trans[i,j]`, the amount shipped to all destinations must be
```ampl
sum {j in DEST} Trans[i,j]
```
Since we have already defined a parameter supply indexed over origins, the amount available at i is supply[i]. Thus the constraint is
```ampl
subject to Supply {i in ORIG}:
    sum {j in DEST} Trans[i,j] = supply[i];
```
(Note that the names supply and Supply are unrelated; AMPL distinguishes upper and lower case.) The other collection of constraints is much the same, except that the roles of `i` in `ORIG`, and `j` in `DEST`, are exchanged, and the sum equals `demand[j]`.

We have been consistent in using the index i to run over the set ORIG, and the index j to run over DEST. This is not an AMPL requirement, but such a convention makes it easier to read a model. You may name your own indices whatever you like, but keep in mind that the scope of an index - the part of the model where it has the same meaning - is to the end of the expression that defines it. Thus in the `Demand` constraint
```ampl
subject to Demand {j in DEST}:
	sum {i in ORIG} Trans[i,j] = demand[j];
```
The following files describe the model and a particular data file for this problem.


```cell
%%writefile transp.mod
set ORIG;   # origins
set DEST;   # destinations

param supply {ORIG} >= 0;   # amounts available at origins
param demand {DEST} >= 0;   # amounts required at destinations

   check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];

param cost {ORIG,DEST} >= 0;   # shipment costs per unit
var Trans {ORIG,DEST} >= 0;    # units to be shipped

minimize Total_Cost:
   sum {i in ORIG, j in DEST} cost[i,j] * Trans[i,j];

subject to Supply {i in ORIG}:
   sum {j in DEST} Trans[i,j] = supply[i];

subject to Demand {j in DEST}:
   sum {i in ORIG} Trans[i,j] = demand[j];
```


```cell
%%writefile transp.dat
data;

param: ORIG:  supply :=  # defines set "ORIG" and param "supply"
        GARY   1400
        CLEV   2600
        PITT   2900 ;

param: DEST:  demand :=  # defines "DEST" and "demand"
        FRA     900
        DET    1200
        LAN     600
        WIN     400
        STL    1700
        FRE    1100
        LAF    1000 ;

param cost:
         FRA  DET  LAN  WIN  STL  FRE  LAF :=
   GARY   39   14   11   14   16   82    8
   CLEV   27    9   12    9   26   95   17
   PITT   24   14   17   13   28   99   20 ;
```



```cell
%%ampl_eval
model transp.mod;
data transp.dat;
option solver cbc;
solve;
display Trans;
```



The minimum cost is still 196200, but it is achieved in a different way. Alternative optimal solutions such as these are often exhibited by transportation problems, particularly when the coefficients in the objective function are round numbers.

Unfortunately, there is no easy way to characterize all the optimal solutions. You may be able to get a better choice of optimal solution by working with several objectives.

## Other interpretations of the transportation model

As the name suggests, a transportation model is applicable whenever some material is being shipped from a set of origins to a set of destinations. Given certain amounts available at the origins, and required at the destinations, the problem is to meet the requirements at a minimum shipping cost.

Viewed more broadly, transportation models do not have to be concerned with the shipping of "materials". They can be applied to the transportation of anything, provided that the quantities available and required can be measured in some units, and that the transportation cost per unit can be determined. They might be used to model the shipments of automobiles to dealers, for example, or the movement of military personnel to new assignments.

In an even broader view, transportation models need not deal with "shipping" at all. The quantities at the origins may be merely associated with various destinations, while the objective measures some value of the association that has nothing to do with actually moving anything. Often the result is referred to as an ***assignment*** model.

As one particularly well-known example, consider a department that needs to assign some number of people to an equal number of offices. The origins now represent individual people, and the destinations represent individual offices. Since each person is assigned one office, and each office is occupied by one person, all of the parameter values `supply[i]` and `demand[j]` are 1. We interpret `Trans[i,j]` as the "amount" of person `i` that is assigned to office `j`; that is, if `Trans[i,j]` is 1 then person i will occupy office j, while if `Trans[i,j]` is 0 then person i will not occupy office j.

What of the objective? One possibility is to ask people to rank the offices, giving their first choice, second choice, and so forth. Then we can let `cost[i,j]` be the rank that person i gives to office `j`. This convention lets each objective function term `cost[i,j]*Trans[i,j]` represent the preference of person i for office j, if person i is assigned to office j (`Trans[i,j]` equals 1), or zero if person i is not assigned to office j (`Trans[i,j]` equals 0). Since the objective is the sum of all these terms, it must equal the sum of all the nonzero terms, which is the sum of everyone's rankings for the offices to which they were assigned. By minimizing this sum, we can hope to find an assignment that will please a lot of people.

To use the transportation model for this purpose, we need only supply the appropriate data. We are presenting an example with 11 people to be assigned to 11 offices. The default option has been used to set all the supply and demand values to 1 without typing all the 1's. If we store this data set in `assign.dat`, we can use it with the transportation model that we already have:




```cell
%%writefile assign.dat

set ORIG := Coullard Daskin Hazen Hopp Iravani Linetsky
	    Mehrotra Nelson Smilowitz Tamhane White ;
set DEST := C118 C138 C140 C246 C250 C251 D237 D239 D241 M233 M239;
param supply default 1 ;
param demand default 1 ;
param cost:
	  C118 C138 C140 C246 C250 C251 D237 D239 D241 M233 M239 :=
Coullard    6   9    8    7   11   10    4    5    3    2    1
Daskin     11   8    7    6    9   10    1    5    4    2    3
Hazen       9  10   11    1    5    6    2    7    8    3    4
Hopp       11   9    8   10    6    5    1    7    4    2    3
Iravani     3   2    8    9   10   11    1    5    4    6    7
Linetsky 11     9   10    5    3    4    6    7    8    1    2
Mehrotra    6  11   10    9    8    7    1    2    5    4    3
Nelson     11   5    4    6    7    8    1    9   10    2    3
Smilowitz 11    9   10    8    6    5    7    3    4    1    2
Tamhane     5   6    9    8    4    3    7   10   11    2    1
White      11   9    8    4    6    5    3   10    7    2    1 ;
```


```cell
%%ampl_eval
reset data;
data assign.dat;
solve;
```


By setting the option `omit_zero_rows` to 1, we can print just the nonzero terms in the objective. This listing tells us each person's assigned room and his or her preference for it:


```cell
%%ampl_eval
option omit_zero_rows 1;
display {i in ORIG, j in DEST} cost[i,j] * Trans[i,j];
```
    


It is not hard to see that when all the `supply[i]` and `demand[j]` values are 1, any `Trans[i,j]` satisfying all the constraints must be between 0 and 1. But how did we know that every `Trans[i,j]` would equal either 0 or 1 in the optimal solution, rather than, say, 1/2 ? We were able to rely on a special property of transportation models, which guarantees that as long as all supply and demand values are integers, and all lower and upper bounds on the variables are integers, there will be an optimal solution that is entirely integral. Moreover, we used a solver that always finds one of these integral solutions. But don't let this favorable result mislead you into assuming that integrality can be assured in all other circumstances; even in examples that seem to be much like the transportation model, finding integral solutions can require a special solver, and a lot more work.

A problem of assigning 100 people to 100 rooms has ten thousand variables; assigning 1000 people to 1000 rooms yields a million variables. In applications on this scale, however, most of the assignments can be ruled out in advance, so that the number of actual decision variables is not too large. After looking at an initial solution, you may want to rule out some more assignments - in our example, perhaps no assignment to lower than fifth choice should be allowed - or you may want to force some assignments to be made a certain way, in order to see how the rest could be done optimally. These situations require models that can deal with subsets of pairs (of people and offices, or origins and destinations) in a direct way.
