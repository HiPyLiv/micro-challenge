'''
This script will split a series of bacterial growth measurements into
distinct phases, it will then analyse these phases to determine a 
series of metrics of bacterial growth. In this example I made use of
a state table to make the analysis more adaptive, but there are other
methods of doing this.
'''
import math

states = [("lag",lambda x,y: x == y),
          ("log",lambda x,y: x > y),
          ("max",lambda x,y: x == y),
          ("death",lambda x,y: x < y)]

def state_split (series, state_table):
    '''
    Splits a numerical series into a dictionary of different state
    series according to boundary conditions within a state table,
    look at the solutions branch to better understand this component.
    '''
    index = 1
    output = {}
    for state in states:
        output[state[0]] = []
        while state[1](series[index], series[index-1]) and index<len(series)-1:
            index += 1
            output[state[0]].append(series[index-1])
    return output

def exponent_rate (log_series):
    '''
    Bacteria grow and die exponentially, by log transforming the series and
    measuring the average difference between each transform point,
    you can get a unique measure of bacterial growth and death rate.
    '''
    trans_series = [math.log2(i) for i in log_series]
    sum_of_diffs = 0
    for i in range(len(trans_series)-1):
        sum_of_diffs += trans_series[i+1]- trans_series[i]
    return round(100*sum_of_diffs/(len(trans_series)-1))

def bacterial_metrics (inputfile):
    '''
    Reads series and bacteria names from input file, and converts into
    discrete series.
    Uses series in table to determine the following metrics:-
    Time spent in lag phase,
    Growth rate constant,
    Maximum bacterial number,
    Death rate constant
    Outputs these metrics as a list of dicts
    '''
    output = []
    with open(inputfile) as source_data:
        for line in source_data:
            if line[0] == "B":
                bacteria = line.strip(" \n")
            else:
                series = [float(i) for i in line.strip(" \n").split(",")]
                state_dict = state_split(series, states)
                metrics = {"name": bacteria,
                           "lag_length": len(state_dict["lag"]),
                           "growth_rate": exponent_rate(state_dict["log"]),
                           "max_number": max(state_dict["max"]),
                           "death_rate": -1*exponent_rate(state_dict["death"])}
                output.append(metrics)
    return output

for met in bacterial_metrics("bacseries.txt"):
    print(met)
