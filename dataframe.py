import pandas as pd

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

# print(series)
# DataFrame =
df = pd.DataFrame(mydataset)
print(df)
# to locate a specific row, use the index: (please notice the this expression will return a Series)
print(df.loc[0])
# or even 2 rows:
print(df.loc[[0, 1]])
# how to name the indexs?
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
# how to locate a specific column? (please notice the this expression will return a Series)
print(df.loc["day1"])
