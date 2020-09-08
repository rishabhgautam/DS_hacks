## Program to Lower Case Column Names In Pandas Dataframe

# Import relevant libraries
import pandas as pd

# Create an example dataframe
data = {'NAME': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'YEAR': [2012, 2012, 2013, 2014, 2014], 
        'REPORTS': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print(df)

# Lowercase column values
df.columns = map(str.lower, df.columns)
print(df)
