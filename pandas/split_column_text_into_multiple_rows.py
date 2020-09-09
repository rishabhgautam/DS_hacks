## Author : Rishabh Gautam
## Program to split column value into multiple rows based on delimiter.

# Import relevant libraries
import pandas as pd
import numpy as np

# Create a data frame
df = pd.DataFrame({'var1': ['d,e,f', '', np.nan], 'var2': [1, 2, 3]})

df1 = df.assign(var1=df['var1'].str.split(',')).explode('var1')
print(df1)
