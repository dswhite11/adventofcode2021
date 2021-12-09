# Part 2

import pandas as pd

# Import the input data from CSV file into a pandas dataframe

text = pd.read_csv('/Users/dwhite/Downloads/advent of code - Day 2.csv')

# Initialize variables

aim = 0
depth = 0
hor = 0

# Defining the function to be used over the dataframe

def func(row):
    global aim
    global depth
    global hor
    if row['direction'] == 'forward':
        hor = hor + row['unit_num']
        depth = depth + (aim * row['unit_num'])
    elif row['direction'] == 'down':
        aim = aim + row['unit_num']
    else:
        aim = aim - row['unit_num']
    print('aim = ', aim, 'hor = ', hor, 'depth = ', depth)

# Applying the function

text.apply(func, axis=1)

# Printing the product of horizontal position and depth, which answers the prompt

print(hor * depth)
