reset;
#############################################
problem Pattern_Opt;                       ### Master Problem for Molding Optimization
#############################################

### SETS ###
   set ITEMS ordered ;                       # Different products that need molding from the sheets (e.g., parts, components)
                 
   param nPAT >= 0, integer;                 # Total number of patterns to be considered
   set PATTERNS = 1..nPAT;                   # Represents different configurations of patterns used for molding


### PARAMETERS ###
   param nDemandWeek >= 0 ;                  # Number of scheduling periods (weeks)          
   param items{ITEMS, PATTERNS} >= 0;        # Number of items of each product within each pattern
   
   param demand {ITEMS, 1..nDemandWeek} >= 0;# Weekly demand for each item i in ITEMS over the weeks (1 to nDemandWeek)
   param sumDemand{i in ITEMS, t in 1..nDemandWeek} = sum {tt in 1..t} demand[i,tt] ;  # Cumulative demand up to week t
   param binItemLimit integer > 0;           # Max number of items per bin to avoid overloading

### VARIABLES ###
   var Mold {PATTERNS, 1..nDemandWeek} integer >= 0;  # Number of patterns molded for each week


### OBJECTIVE FUNCTION ###
   minimize TotalPallets: sum {p in PATTERNS, t in 1..nDemandWeek} Mold[p,t];  # Minimize total patterns molded over all weeks


### CONSTRAINTS ###
   s.t. OrderLimits {i in ITEMS, t in 1..nDemandWeek}: # Ensure molding meets demand for each item up to week t
      sum {p in PATTERNS, tt in 1..t} Mold[p,tt] * items[i,p] >= sumDemand[i,t] ;

#############################################
problem Pattern_Gen;                       ### Subproblem for Pattern Generation
#############################################

### SETS ###
   set ATR = { 'width', 'height','quantity'};# Attributes for each product (width, height, quantity)
   set DIFF = {'quantity'};                  # Attributes that vary by item (quantity in this case)


### PARAMETERS ###
   param prod {ITEMS, ATR} >= 0 ;            # Product dimensions and quantity for each item
   param price {ITEMS} default 0;            # Price or value of each item for objective function
 ## Bins
   param binDim {ATR diff DIFF} >= 0 ;       # Dimensions of each bin (width, height); excludes quantity
 

### VARIABLES ###
   var Use {ITEMS} integer >= 0 ;            # Number of each item used in the pattern


### OBJECTIVE FUNCTION ###
   minimize Reduced_Cost: 1- sum {i in ITEMS} price[i] * Use[i];  # Minimize total value of items used in the pattern


### CONSTRAINTS ###
   s.t. Width_Limit:                         # Ensure items fit within bin width
      sum {i in ITEMS} Use[i] * prod [i,'width'] <= binDim['width'] ; 

   s.t. Items_limit:                            # Ensure number of items does not exceed binItemLimit
      sum {i in ITEMS} Use[i] <= binItemLimit ; 
