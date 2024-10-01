reset;

### SETS
  set BRANCH ;                                        # Set of all branches where pharmacies are located
  set PHARM;                                          # Set of all pharmacies
  set PHARMACIES{BRANCH} within PHARM;                # Set of pharmacies within each branch
  set EMPLOYEES ;                                     # Set of employees
  set EMPL_WORKPLACE{EMPLOYEES} within PHARM;         # Set of base pharmacies for each employee, indicating their usual workplace
  set SHIFT_TYPES ;                                   # Set of shift types available for assignment

  param nYearDayData = 31 ;                           # Number of days for which sales and staff data are available
  param nYearDay = nYearDayData ;                     # Number of days under consideration in the current optimization model
  param SchedCycle = nYearDayData ;                   # The number of days in a scheduling cycle.
                                                      # Frequency at which an employee can switch between different shift modes, pharnacies.
                                                      # Here we can set up different conditions for different [shifts, pharmacies]
  param nScheduleCycle = ceil(nYearDay/SchedCycle) ;  # Number of scheduling cycles in the model period
  param nWeekDay = 7 ;                                # Number of days in a week
  param nWeek = ceil(nYearDay/nWeekDay) ;             # Total number of weeks considered in the model
  param nHour = 23 ;                                  # Number of hours in a working day (0 to 23, assuming 24-hour coverage)

  set PHARM_HOURS_DATA = {PHARM, 1..nYearDayData, 0..nHour};  # Set of valid combinations of pharmacies, days, and hours from the dataset
  set SHIFT_HOURS = {PHARM, SHIFT_TYPES, 0..nHour, 0..nHour}; # Set of possible pharmacy, shift, and hour combinations
  set PEAK_HOURS = {12..20} ;                         # Hours of the day when demand peaks (e.g., lunch and evening)
  set PEAK_DAYS = {120..180} ;                        # Peak days with high demand, often due to seasonal trends


### PARAMETERS
 ## Pharmacy-specific parameters
  param ph_StartTime{PHARM} >= 0 ;                    # Start time of the workday at each pharmacy (in hours, 0..23)
  param ph_WorkDuration{PHARM} >= 0 ;                 # Duration of the working day for each pharmacy (in hours)
  param ph_Distance{p in PHARM, pp in PHARM: p != pp} >= 0 ;  # Distance between pharmacies
  param staffReserve >= 0 ;                           # Reserve staff requirement during peak times (extra staff needed during busy hours)

  param ph_ItemsSold{PHARM_HOURS_DATA} default 1 >= 0;# Number of items sold at each pharmacy at each hour on each day
  param ph_AdjustedItemsSold{(ph,d,h) in PHARM_HOURS_DATA} := # Adjusted number of items sold during peak times, with a staff reserve multiplier
   if (h in PEAK_HOURS or d in PEAK_DAYS)
   then ph_ItemsSold [ph,d,h] * staffReserve          # Multiply sales during peak hours/days by the reserve factor
   else ph_ItemsSold [ph,d,h] ;                       # Regular sales during non-peak times

  param ph_Revenue{PHARM_HOURS_DATA} default 0 >= 0 ; # Revenue generated from sales at each pharmacy for each hour on each day
  param penaltyCoeff >= 0 default 1;                  # Penalty coefficient for unmet demand

  param ph_DaySchedule {SHIFT_HOURS} >= 0 default 0 ; # Defines pharmacy work schedules per day for different shifts


  ## Shift-related parameters
  set SHIFT_PARAM = {                                 # Set of different parameters defining shift rules and limitations.
    'DailyWorkHours',                                 # Working hours per day by shift type
    'OvertimeHours',                                  # Overtime hours per day allowed for shift type.
    'maxWeeklyHours',                                 # Maximum working hours per week by shift type
    'maxWeeklyOvertimeHours',                         # Maximum overtime hours per week by shift type
    'maxYearOvertimeHours',                           # Maximum overtime hours per year by shift type
    'TotalHours'};                                    # Total hours per shift, including both regular and overtime hours

  param shiftAtr {SHIFT_TYPES, SHIFT_PARAM} >= 0 ;    # Defines parameters for each shift type (e.g., daily hours, overtime)
  param cycleSchedule{SHIFT_TYPES, 1..SchedCycle} >= 0 default 0; # Schedule defining how shifts are distributed across the days

 ## Employee-specific parameters
  set EMPL_PARAM = {                                  # Set of parameters related to employee attributes.
    'MaxItemsSoldPerHour',                            # Max number of items an employee can sell per hour (workload capacity)
    'MaxReplaceDistance',                             # Maximum distance between pharmacies for employee reassignment
    'SalaryPerHour',                                  # Hourly wage for each employee
    'VacationStartPeriod',                            # Start day for vacations for each employee
    'VacationDuration',                               # Duration of vacation for each employee
    'SalesPerformance'} ;                             # Sales performance metric for each employee (used for priority scheduling)

  param emplAtr{EMPLOYEES, EMPL_PARAM} >= 0 ;         # Table of employee-specific attributes and constraints.

  # Total salary cost for each employee per shift, including overtime.
  param empl_SalaryPerShift{e in EMPLOYEES, sh in SHIFT_TYPES} =
    emplAtr[e, 'SalaryPerHour'] * (shiftAtr[sh, 'DailyWorkHours'] + 2 * shiftAtr[sh, 'OvertimeHours']) ;

 ## Assignment Links and Shift Links Definitions
  # ASSIGNMENT_LINKS defines valid assignment scenarios of employees to branches, pharmacies, days, and hours, based on certain conditions.
  set ASSIGNMENT_LINKS within {br in BRANCH, PHARMACIES[br], EMPLOYEES, 1..nYearDay, 0..nHour} :=
    setof {br in BRANCH, ph in PHARMACIES[br], e in EMPLOYEES, d in 1..nYearDay, h in 0..nHour:
    (ph, d, h) in PHARM_HOURS_DATA and                # Only consider valid working hours
    d >= 1 and d <= nYearDay and                      # Only consider valid working days
    h >= ph_StartTime[ph] and                         # Ensure the hour is after or at the start of the working day
    h < ph_StartTime[ph] + ph_WorkDuration[ph]-1 and  # Ensure the hour is before the end of the working day
    sum {ew in EMPL_WORKPLACE[e]} (if (ph != ew) then ph_Distance[ew, ph] else 0) <= emplAtr[e, 'MaxReplaceDistance'] and # Ensure max distance constraint is respected
    ph in PHARMACIES[br] and                          # Pharmacy must be within the current branch
    exists {ew in EMPL_WORKPLACE[e]} (ew in PHARMACIES[br]) and     # Employee's base pharmacy must be in the same branch
    not (d >= emplAtr[e,'VacationStartPeriod'] and d < emplAtr[e,'VacationStartPeriod'] + emplAtr[e,'VacationDuration']) # Exclude vacation period
    } (br,ph,e,d,h);                                  # Set of valid assignments based on above conditions

  # Set of valid branch-pharmacy-employee-day-hour-shift type combinations
  set SHIFT_LINKS within {br in BRANCH, PHARMACIES[br], EMPLOYEES, 1..nYearDay, 0..nHour, SHIFT_TYPES} :=
    setof {(br,ph,e,d,h) in ASSIGNMENT_LINKS,  sh in SHIFT_TYPES: # Iterate over valid assignment links and shift types to determine valid shift start times
    h <= ph_StartTime[ph]                             # Ensure that the shift can start and finish within the pharmacy's working hours. The shift must end before the pharmacy closes
    + ph_WorkDuration[ph]
    - shiftAtr[sh,'TotalHours']}
    (br,ph,e,d,h,sh);                                 # Creates the set of valid shift links based on the conditions above.

  # Set for valid assignments considering branch, pharmacy, employee, day, and shift
  set SHIFT_LINKS_br_ph_e_d_sh  := setof{(br,ph,e,d,h,sh) in SHIFT_LINKS}   (br,ph,e,d,sh);
  set SHIFT_LINKS_br_ph_e_sh    := setof{(br,ph,e,d,h,sh) in SHIFT_LINKS}   (br,ph,e,sh);
  set SHIFT_LINKS_e_sh          := setof{(br,ph,e,d,h,sh) in SHIFT_LINKS}   (e,sh);
  set LINKS_br_ph_d_h           := setof{(br,ph,e,d,h) in ASSIGNMENT_LINKS} (br,ph,d,h) ;
  set LINKS_e_d                 := setof{(br,ph,e,d,h) in ASSIGNMENT_LINKS} (e,d) ;

### VARIABLES
  # Binary variable for the start of an assignment of employees to pharmacies and shift
  var StartPeriodSched{(br,ph,e,sh) in SHIFT_LINKS_br_ph_e_sh, 1..nScheduleCycle} binary ;

  # Binary variable indicating if an employee is assigned to work during a specific hour
  var StartDaySchedule{(br,ph,e,d,h,sh) in SHIFT_LINKS} binary;

  # Binary variable indicating the scope & conditions of assign shift by days
  var AssignDaySchedule{(br,ph,e,d,h) in ASSIGNMENT_LINKS} =
    sum{(br,ph,e,d,t,sh) in SHIFT_LINKS: t >= h - shiftAtr[sh,'TotalHours'] and t <= h}
    StartDaySchedule[br,ph,e,d,t,sh] * ph_DaySchedule[ph,sh,t,h] ;

  var StaffShortageSlack{LINKS_br_ph_d_h} >= 0 ;      # Variable representing a slack variable used when there's a staff shortage

### OBJECTIVE FUNCTION  # Objective function to maximize total profit by balancing pharmacy revenue, employee costs, and penalties for unmet demand
maximize TotalProfit:                                 # Objective function aiming to maximize total profit by balancing pharmacy revenue, employee costs, and penalties for unmet demand.
    sum{(br,ph,d,h) in LINKS_br_ph_d_h}
    (ph_Revenue[ph,d,h] * (1 - StaffShortageSlack[br,ph,d,h] / ph_ItemsSold[ph,d,h])  # Revenue from sales adjusted by the minimum demand.
    - penaltyCoeff * StaffShortageSlack[br,ph,d,h])               # Penalties for staff shortages.
    - sum{(br,ph,e,d,t,sh) in SHIFT_LINKS}
    StartDaySchedule[br,ph,e,d,t,sh] * empl_SalaryPerShift[e,sh] ;# Employee salary costs


### CONSTRAINTS
  # 1. Ensure that employees only start one shift per scheduling cycle (SchedCycle)
  s.t. PeriodCycle {e in EMPLOYEES, sch in 1..nScheduleCycle}:
    sum {(br,ph,e,sh) in SHIFT_LINKS_br_ph_e_sh}
    StartPeriodSched[br,ph,e,sh,sch] <= 1;

  # 2. Ensure valid shift assignments are respected
  s.t. ShiftAssignValidity {(br,ph,e,d,sh) in SHIFT_LINKS_br_ph_e_d_sh}:
    sum{(br,ph,e,d,h,sh) in SHIFT_LINKS} StartDaySchedule[br,ph,e,d,h,sh] <=
    sum{sch in 1..nScheduleCycle: sch = ceil(d/SchedCycle)}
      StartPeriodSched[br,ph,e,sh,sch] * cycleSchedule[sh,d] ;

  # 3. Ensure enough staff is available to handle the expected sales and Reserve of staff at each pharmacy
  s.t. StaffNumber{(br,ph,d,h) in LINKS_br_ph_d_h}:
    sum{(br,ph,e,d,h) in ASSIGNMENT_LINKS}
      AssignDaySchedule[br,ph,e,d,h] * emplAtr[e,'MaxItemsSoldPerHour'] #
      >= ph_AdjustedItemsSold[ph,d,h] - StaffShortageSlack[br,ph,d,h] ;

 ## Hours Constraints:
  # 4. Ensure employees do not exceed weekly working hours
  s.t. WeekHourLimit {(e,sh) in SHIFT_LINKS_e_sh, w in 1..nWeek}:
    sum{(br,ph,e,d,h,sh) in SHIFT_LINKS: d >= (w-1) * nWeekDay + 1 and d <= w * nWeekDay}
    StartDaySchedule[br,ph,e,d,h,sh] * shiftAtr[sh,'TotalHours']
    <= shiftAtr[sh,'maxWeeklyHours'] ;

  # 5. Ensure that weekly overtime hours do not exceed the maximum allowed
  s.t. WeekOvertimeLimit {e in EMPLOYEES, w in 1..nWeek, sh in SHIFT_TYPES}:
    sum{(br,ph,e,d,h,sh) in SHIFT_LINKS: d >= (w-1) * nWeekDay + 1 and d <= w * nWeekDay}
    StartDaySchedule[br,ph,e,d,h,sh] * shiftAtr[sh,'OvertimeHours']
    <= shiftAtr[sh,'maxWeeklyOvertimeHours'] ;

  # 6. Ensure that yearly overtime hours do not exceed the maximum allowed
  s.t. YearOvertimeLimit {e in EMPLOYEES, sh in SHIFT_TYPES}:
    sum{(br,ph,e,d,h,sh) in SHIFT_LINKS}
    StartDaySchedule[br,ph,e,d,h,sh] * shiftAtr[sh,'OvertimeHours']
    <= shiftAtr[sh,'maxYearOvertimeHours'] ;
