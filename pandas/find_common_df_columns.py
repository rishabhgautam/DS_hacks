## Program to find Columns Shared By Two Data Frames

# Import relevant libraries
import pandas as pd

# Create a data frame
dataframe_one = pd.DataFrame()
dataframe_one['1'] = ['1', '1', '1']
dataframe_one['B'] = ['b', 'b', 'b']

# Create a second data frame
dataframe_two = pd.DataFrame()
dataframe_two['2'] = ['2', '2', '2']
dataframe_two['B'] = ['b', 'b', 'b']

# set of columns shared by both data frames.
set.intersection(set(dataframe_one), set(dataframe_two))
