# Data Cleaning:
# fixing bad data in the data set

# like:
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates
import pandas as pd

df = pd.read_csv('damgeddata.csv')
# One way to deal with empty cells is to remove rows that contain empty cells.
new_df = df.dropna()
# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
print(new_df.to_string())
# If you want to change the original DataFrame, use the inplace = True argument:
# df.dropna(inplace=True)
# print(df.to_string())

# Another way of dealing with empty cells is to insert a new value instead.
# df.fillna(130, inplace = True)

# Replace Only For Specified Columns:
# df["Calories"].fillna(130, inplace = True)

# also you can use the Mean/Median or Mode to replace missing values.

# Mean - the avg value.
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)

# Median - the middle value after you have sorted the array ascending
# x = df["Calories"].median()
# df["Calories"].fillna(x, inplace = True)

# Mode - the value that appears most frequently
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)


# Wrong Format:
# df['Date'] = pd.to_datetime(df['Date'])
# or just remove the wrong valued row:
# df.dropna(subset=['Date'], inplace = True)


# Wrong Data:
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
# if i know where i got the wrong data:
# df.loc[7, 'Duration'] = 45

# if i dont know where i got the wrong data, I can define range:
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
# or just remove the wrong data:
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)


# Remove duplicate rows:
# to discover duplicated rows:
# print(df.duplicated())
# if none so it returns false

# to remove duplicate rows:
# df.drop_duplicates(inplace = True)
