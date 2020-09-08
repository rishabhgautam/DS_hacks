## Program for Ranking Rows Of Pandas Dataframes

# Import relevant libraries
import pandas as pd

# Create dataframe
data = {'name': ['Jas', 'Mol', 'Tina', 'Jackie', 'Amy'], 
        'year': [2011, 2012, 2015, 2014, 2014], 
        'reports': [40, 44, 38, 21, 32],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print(df)

# Create a new column that is the rank of the value of coverage in ascending order
df['coverageRanked'] = df['coverage'].rank(ascending=1)
print(df)
