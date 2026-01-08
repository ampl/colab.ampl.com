from amplpy import AMPL
import pandas as pd
import numpy as np

# Unit Commitment data
generators = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']

# Generators data
generators_data = pd.DataFrame({
    'min_output':      [20, 30, 25, 15, 10, 40, 0],
    'max_output':      [100, 120, 90, 60, 50, 150, 30],
    'ramp_up_limit':   [40, 50, 30, 25, 20, 60, 10],
    'ramp_down_limit': [40, 50, 30, 25, 20, 60, 10],
    'linear_cost':     [20, 16, 18, 22, 24, 14, 12],
    'quadratic_cost':  [0.04, 0.05, 0.06, 0.03, 0.04, 0.036, 0.1],
    'startup_cost':    [400, 300, 360, 200, 160, 600, 160],
    'emission_rate':   [0.7, 0.5, 0.6, 0.4, 0.3, 0.8, 0.0]
}, index=generators)

# Generate random demand
num_time_periods = 24*2
time_periods = list(range(1, num_time_periods+1))

np.random.seed(None)
base_demand = 150 + 40 * np.sin(np.linspace(0, 3*np.pi, num_time_periods))
noise = np.random.normal(0, 10, num_time_periods)
demand = (base_demand + noise).clip(min=100).round().astype(int)

# Optimization model and data
ampl = AMPL()
ampl.read('unit_commitment.mod')  # This model should reflect renamed sets/vars/params

ampl.set['TIME'] = time_periods
ampl.set['GENERATORS'] = generators
ampl.param['demand'] = demand
ampl.set_data(generators_data, 'GENERATORS')

# Hierarchical Multi-objective configuration
# Higher priority first
ampl.eval('let Total_Cost.objpriority := 2;')
# Set 5% degradation tolerance for total cost
ampl.eval('let Total_Cost.objreltol := 0.05;')
# Second objective (less priority)
ampl.eval('let Total_Emissions.objpriority := 1;')

SOLVER='knitro'
#SOLVER='gurobi'
#SOLVER='xpress'

max_seconds = 10

if SOLVER == 'knitro':
	ampl.solve(solver='mp2nl',
		       knitro_options='maxtime='+str(max_seconds),
		       verbose=True,
		       mp2nl_options='solver=knitro obj:multi=2')
else:
	ampl.solve(solver=SOLVER,
		       mp_options='obj:multi=2 outlev=1 timelim='+str(max_seconds),
		       verbose=True)

is_committed = ampl.get_data('is_committed')
produce = ampl.get_data('power_generated')
startup = ampl.get_data('is_startup')

# Flatten the dataframe values and count 1s and 0s
values = is_committed.to_pandas().values.flatten()
num_ones = (values == 1).sum()
num_zeros = (values == 0).sum()

print(f"Total ON periods (1s): {num_ones}")
print(f"Total OFF periods (0s): {num_zeros}")

print("=== Objective Values ===")
total_cost = ampl.obj['Total_Cost'].value()
total_emissions = ampl.obj['Total_Emissions'].value()

print(f'Total cost: {total_cost:.2f}$')
print(f'Total emissions: {total_emissions:.2f} tons CO₂')

