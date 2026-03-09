
set TIME ordered;                       # Set of hours in the simulation (1..8760)
set MONTHS;                             # Set of months

# ----------------------------------------------------------------------------
# PARAMETERS
# ----------------------------------------------------------------------------

# Mapping parameter to link time steps to rate periods
param time_month_map {TIME} within MONTHS;

# Load and Rates
param site_electric_load {TIME} >= 0;   # Baseline facility load (kW) [Symbol: L]
param energy_rate {MONTHS} >= 0;        # Retail energy rate ($/kWh) [Symbol: RE]
param demand_rate {MONTHS} >= 0;        # Retail demand rate ($/kW) [Symbol: RD]

# Market Prices and Signals
param tso_energy_price {TIME};          # Electricity market price ($/MWh) [Symbol: ME]
param tso_flex_up_price {TIME} >= 0;    # Freq regulation market price ($/MWh) [Symbol: MR]
param tso_flex_down_price {TIME} >= 0;  # Freq regulation market price for regulation down ($/MWh) [Symbol: MR_DN]
param reg_d_up {TIME};        # Freq reg signal for increased supply (%) [Symbol: RS_U]
param reg_d_down {TIME};      # Freq reg signal for decreased supply (%) [Symbol: RS_D]
param tso_load {TIME} >= 0;             # Aggregate demand for TSO (MW) [Symbol: TL]
param dso_load {TIME} >= 0;             # Aggregate demand for DSO (MW) [Symbol: DL]
param cp_tso_rate_kw >= 0;              # Coincident peak capacity rate ($/kW) [Symbol: RC]
param cp_dso_rate_kw >= 0;              # Coincident peak capacity rate for DSO (if applicable) ($/kW) [Symbol: RC_DSO]

# Battery Technical Specs
param battery_power >= 0;               # Inverter capacity/Max rate (kW) [Symbol: Gbattery]
param battery_energy >= 0;              # Storage capacity (kWh) [Symbol: Sbattery]
param efficiency >= 0, <= 1;            # Battery efficiency (%) [Symbol: E]
param battery_fixed_om >= 0;            # Battery O&M costs ($/kWh-year) [Symbol: OMbattery]
param initial_soc_pct >= 0, <= 1, default 0.5;  # Initial state of charge (kWh) [Symbol: Soc0]
param min_soc_pct >= 0, <= 1, default 0.1;      # Minimum state of charge as % of capacity (kWh) [Symbol: MinSoc]
param max_soc_pct >= 0, <= 1, default 0.9;

# Solar Technical Specs
param solar_capacity >= 0;              # Solar generation capacity (kW) [Symbol: Gsolar]
param solar_production_profile {TIME} >= 0; # Solar production per unit capacity (%) [Symbol: U]
param solar_fixed_om >= 0;              # Solar O&M costs ($/kW-year) [Symbol: OMsolar]

# Coincident Peak Identification
# Find the max TSO load to identify t*
param max_tso_val = max {t in TIME} tso_load[t];
param max_tso_time = max {t in TIME: tso_load[t] = max_tso_val} t;  # Only count 1 hour for the coincident peak, not every hour where max demand happens

param max_dso_val = max {t in TIME} dso_load[t];
param max_dso_time = max {t in TIME: dso_load[t] = max_dso_val} t;  # Only count 1 hour for the coincident peak, not every hour where max demand happens

# Baseline peak parameter for each month
param baseline_peak {m in MONTHS} = max {t in TIME: time_month_map[t] = m} site_electric_load[t];

# Operating and Maintenance Costs
# OM1 = Fixed costs (Battery + Solar)
param OM1 = (battery_fixed_om * battery_energy) + (solar_fixed_om * solar_capacity);

# ----------------------------------------------------------------------------
# DECISION VARIABLES
# ----------------------------------------------------------------------------

var SolarProduction {TIME} >= 0;    # Solar electricity production (kW) [Symbol: P]
var BatteryCharge {TIME} >= 0;      # BESS electric charge (kW) [Symbol: C]
var BatteryDischarge {TIME} >= 0;   # BESS electric discharge (kW) [Symbol: D]
var Soc {TIME} >= min_soc_pct * battery_energy, <= max_soc_pct * battery_energy;                     # BESS state of charge (kWh) [Symbol: Soc]
var NetLoad {TIME} >= 0;            # Net facility load after BESS/Solar (kW) [Symbol: N]
var ExportToGrid {TIME} >= 0;       # Surplus solar production exported (kW) [Symbol: X]
var FlexUpBattery {TIME} >= 0, <= battery_power;         # BESS capacity participating in Freq Reg (kW) [Symbol: FR]
var FlexDownBattery {TIME} >= 0, <= battery_power;       # BESS capacity participating in Freq Reg for regulation down (kW) [Symbol: FR_DN]

# Auxiliary variables for peak tracking (Required for Demand Charge Savings)
var PeakNetLoad {MONTHS} >= 0;      # Max net load per month

var BatteryCharging {TIME} binary;  # Binary variable to indicate if battery is charging (1) or discharging (0) at time t
var BatteryDischarging {TIME} binary;   # Binary variable to indicate if battery is discharging (1) or charging (0) at time t

# -----
# Other variables (savings and revenues) for objective function
# -----

# Energy Charge Savings
# E1 = Sum((Lt - Nt) * RE)
var EnergyChargesSavings = sum {t in TIME} (site_electric_load[t] - NetLoad[t]) * (tso_energy_price[t]/1000 + energy_rate[time_month_map[t]]);

# Demand Charge Savings
# D1 = Sum((Max(L) - Max(N)) * RD)
var DemandChargesSavings = sum {m in MONTHS} (baseline_peak[m] - PeakNetLoad[m]) * demand_rate[m];

# Coincident Peak Charge Savings
# CP1 = RC * (Lt* - Nt*)
var CP_TSO_DemandChargesSavings =
    sum {t in TIME: t = max_tso_time} 12*(cp_tso_rate_kw * (site_electric_load[t] - NetLoad[t]));

# Coincident Peak Charge Savings for DSO
# CP2 = RC_DSO * (Dt* - Nt*)
var CP_DSO_DemandChargesSavings =
    sum {t in TIME: t = max_dso_time} 12*(cp_dso_rate_kw * (site_electric_load[t] - NetLoad[t]));

# Wholesale Energy Market Revenues
# M1 = Sum(Xt * MEt)
var ExportPowerValue = sum {t in TIME} (ExportToGrid[t] * tso_energy_price[t])/1000;

# Frequency Regulation Market Revenues
# FR1 = Sum(FRt * MRt)
var FlexUpRevenue = sum {t in TIME} (FlexUpBattery[t] * tso_flex_up_price[t])/1000;
# FR2 = Sum(FR_DNt * MR_DNt)
var FlexDownRevenue = sum {t in TIME} (FlexDownBattery[t] * tso_flex_down_price[t])/1000;


# ----------------------------------------------------------------------------
# OBJECTIVE FUNCTION
# ----------------------------------------------------------------------------

# V1 = E1 + D1 + CP1 + M1 + FR1 - OM1
maximize NetValue:
    EnergyChargesSavings +
    DemandChargesSavings +
    CP_TSO_DemandChargesSavings +
    CP_DSO_DemandChargesSavings +
    ExportPowerValue +
    FlexUpRevenue +
    FlexDownRevenue -
    OM1;

# ----------------------------------------------------------------------------
# OPERATING CONSTRAINTS
# ----------------------------------------------------------------------------

subject to Exclusive_State {t in TIME}:
    BatteryCharging[t] + BatteryDischarging[t] <= 1;

# Solar Production
subject to SolarGenDef {t in TIME}:
    SolarProduction[t] = solar_production_profile[t] * solar_capacity;

# Battery Power Capacity
subject to ChargeLimit {t in TIME}:
    BatteryCharge[t] <= battery_power * BatteryCharging[t];

subject to DischargeLimit {t in TIME}:
    BatteryDischarge[t] <= battery_power * BatteryDischarging[t];

subject to FlexUpLimit {t in TIME}:
    FlexUpBattery[t] <= ((if ord(t) > 1 then Soc[t-1] else initial_soc_pct * battery_energy) - min_soc_pct * battery_energy) / (efficiency^0.5);

subject to FlexDownLimit {t in TIME}:
    FlexDownBattery[t] <= (max_soc_pct * battery_energy - (if ord(t) > 1 then Soc[t-1] else initial_soc_pct * battery_energy)) * (efficiency^0.5);

# Battery State of Charge limits
subject to SocCapacity {t in TIME}:
    Soc[t] <= battery_energy;

# Battery Continuity Balance
subject to SocBalance {t in TIME}:
    Soc[t] = (if ord(t) > 1 then Soc[t-1] else initial_soc_pct * battery_energy)
             + ((efficiency^0.5)* BatteryCharge[t])
             - (BatteryDischarge[t] / (efficiency^0.5));

# Net Electric Load
# Nt = Lt - Pt - Dt + Ct + Xt
subject to NetLoadDef {t in TIME}:
    NetLoad[t] = site_electric_load[t]
                  - SolarProduction[t]
                  - BatteryDischarge[t]
                  + BatteryCharge[t]
                  + ExportToGrid[t];

# Frequency Regulation Participation
# Discharge must meet Up signal * Committed Capacity
subject to RegUpConstraint {t in TIME}:
    BatteryDischarge[t] >= reg_d_up[t] * FlexUpBattery[t];

# Charge must meet Down signal * Committed Capacity
subject to RegDownConstraint {t in TIME}:
    BatteryCharge[t] >= -reg_d_down[t] * FlexDownBattery[t];

# Define Peak Tracking for Demand Charges
# PeakNetLoad must be at least the NetLoad in that month
subject to PeakTracking {m in MONTHS, t in TIME: time_month_map[t] = m}:
    PeakNetLoad[m] >= NetLoad[t];

# Limit exports to onsite generation (Solar + Battery Discharge)
subject to ExportLimit {t in TIME}:
    ExportToGrid[t] <= SolarProduction[t];#+ BatteryDischarge[t];
