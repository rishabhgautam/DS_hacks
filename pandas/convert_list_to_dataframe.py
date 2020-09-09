## Author : Rishabh Gautam
## Program to convert a list to a dataframe

# Import relevant libraries
import pandas as pd

# List of lists
students = [ ['jackie', 34, 'Sydney'] ,
             ['aditya', 30, 'New Delhi' ] ,
             ['radha', 16, 'New York'] ]

print(type(students))

# Creating a dataframe object from listoftuples
DF = pd.DataFrame(students)
DF.columns = ['col1', 'col2', 'col3']

print(DF)
print(type(DF))
