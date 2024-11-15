reset;

### SETS ###
set DIAMETERS ;                           # Set of pipeline diameters, mm
set YEARS ;                               # Set representing each year of the 5-year diagnostic plan
set KTD ;                                 # List of diagnostic equipment types
set ATTR ;                                # Set of attributes for each diagnostic equipment type

### PARAMETERS ###
param budget {DIAMETERS, YEARS} >= 0;     # Annual budget allocation for diagnostics per pipeline diameter and year
param min_length {DIAMETERS, YEARS} >= 0; # Planned diagnostic length (km) each year by pipeline diameter

param KTD_attributes {KTD, ATTR} >= 0;    # Attributes for each equipment type (cost, min/max diameter)
param KTD_amount {KTD, YEARS} >= 0;       # Amout of each diagnostic equipment type available each year
param KTD_perfomance {KTD, DIAMETERS} >= 0;# Diagnostic performance of each equipment type by pipeline diameter

set LINKS within {KTD, DIAMETERS} :=      # Define compatibility between equipment types and pipeline diameters
    {i in KTD, d in DIAMETERS: KTD_attributes [i,'d_min'] <= d <= KTD_attributes [i,'d_max']} ;  

### VARIABLES ###
var KTD_Usage {LINKS, YEARS} binary;      # Indicating whether a diagnostic equipment type (i) is used for a pipeline diameter (d) in a given year (t).
var KTD_Required {LINKS, YEARS} integer >= 0 ; # Integer amount of diagnostic equipment required for each compatible equipment-diameter pair (LINKS) each year (YEARS)

 # Auxiliary variables
var Budget_Diameters_Years {d in DIAMETERS, t in YEARS} = 
  sum{(i,d) in LINKS} KTD_Required[i,d,t] * KTD_perfomance[i,d] * KTD_attributes[i,'cost'] ;
var Length_Diameters_Years {d in DIAMETERS, t in YEARS} = 
  sum{(i,d) in LINKS} KTD_Required[i,d,t] * KTD_perfomance[i,d] ;
var KTD_Perfomance_Years {i in KTD, t in YEARS} = 
  sum{(i,d) in LINKS} KTD_Required[i,d,t] * KTD_perfomance[i,d] ;

### OBJECTIVE FUNCTION ###
# Minimize the total cost of diagnostic operations over the 5-year period
maximize Total_Length: sum {i in KTD, t in YEARS} 
     sum{(i,d) in LINKS} KTD_Required [i,d,t] * KTD_perfomance[i,d] ;

minimize Total_Cost: sum {i in KTD, t in YEARS} 
  sum{(i,d) in LINKS} KTD_Required [i,d,t] * KTD_perfomance[i,d] * 10e3 * KTD_attributes[i,'cost'] ;


### CONSTRAINTS ###
# 1. Limit each diagnostic equipment type `i` to be used only once per pipeline diameter `d` per year `t`.
s.t. KTD_Usage_Limit {i in KTD, t in YEARS}: 
   sum{(i,d) in LINKS} KTD_Usage[i,d,t] <= 1 ;

 # 2. Ensure total diagnostic cost across all years and diameters does not exceed the overall budget
   s.t. Annual_Budget_Limit {d in DIAMETERS, t in YEARS}: 
      sum {(i,d) in LINKS} KTD_Required[i,d,t] * KTD_perfomance[i,d] * 10e3 * KTD_attributes[i,'cost'] <= budget[d,t] * 10e3 ;

 # 3. Match the planned diagnostic length for each pipeline diameter each year
   s.t. Planned_Diagnostics {d in DIAMETERS, t in YEARS}:
      sum {(i,d) in LINKS} KTD_Required[i,d,t] * KTD_perfomance[i,d] >= min_length[d,t];

 # 4. Ensure that the equipment used does not exceed the available amount
   s.t. Equipment_Availability {(i,d) in LINKS, t in YEARS}: 
      KTD_Required[i,d,t] <= KTD_Usage[i,d,t] * KTD_amount[i,t];
