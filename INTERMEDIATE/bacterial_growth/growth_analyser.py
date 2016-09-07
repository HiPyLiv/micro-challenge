'''
This script will split a series of bacterial growth measurements into
distinct phases, it will then analyse these phases to determine a 
series of metrics of bacterial growth. In this example I made use of
a state table to make the analysis more adaptive, but there are other
methods of doing this.
'''

states = []

def state_split (series, state_table):
    '''
    Splits a numerical series into a dictionary of different state
    series according to boundary conditions within a state table,
    look at the solutions branch to better understand this component.
    '''
    return

def exponent_rate (log_series):
    '''
    Bacteria grow and die exponentially, by log transforming the series and
    measuring the average difference between each transform point,
    you can get a unique measure of bacterial growth and death rate.
    '''
    return

def bacterial_metrics (inputfile):
    '''
    Reads series and bacteria names from input file, and converts into
    discrete series.
    Uses series in table to determine the following metrics:-
    Time spent in lag phase,
    Growth rate constant,
    Maximum bactrial number,
    Death rate constant
    Outputs these metrics as a list of dicts.
    '''
    return

for met in bacterial_metrics("bacseries.txt"):
    print(met)
