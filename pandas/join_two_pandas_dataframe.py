## Author : Rishabh Gautam
## Program to JOIN two pandas dataframes

# Import relevant libraries
import pandas as pd

df1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(df1, columns = ['subject_id', 'first_name', 'last_name'])
print(df_a)

df2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(df2, columns = ['subject_id', 'first_name', 'last_name'])
print(df_b)

df3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(df3, columns = ['subject_id','test_id'])
print(df_n)

# Join the two dataframes along rows
print(pd.concat([df_a, df_b]))

# Join the two dataframes along columns
print(pd.concat([df_a, df_b], axis=1))

# Merge two dataframes with both the left and right dataframes using the subject_id key
print(pd.merge(df_a, df_b, left_on='subject_id', right_on='subject_id', how='left'))
