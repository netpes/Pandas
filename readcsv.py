# read csv files,
# A simple way to store big data sets is to use CSV files (comma separated files).
import pandas as pd

# access the csv file location
df = pd.read_csv('data.csv')

# print the entire DataFrame:
print(df.to_string())

# if i have a large csv, pandas will print only the first 5 rows and the last 5 rows:
print(df)

# You can check your system's maximum rows with the pd.options.display.max_rows statement:
print(pd.options.display.max_rows)
# to change the max rows, use the pd.options.display.max_rows statement:
pd.options.display.max_rows = 9999
# how every print statement will be printed upto 9999 rows:
print(df)
