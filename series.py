# whats panadas?
# a library used for working with data sets.
# Pandas can clean messy data sets, and make them readable and relevant.
import pandas as pd

a = [1, 7, 2]
# series is like a column on table.
series = pd.Series(a)
print(series)
# lables -  If nothing else is specified, the values are labeled with their index number
# how to create lablels?
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
# then you can access item by the new index, like:
print(myvar["x"])

# objects with series:
calories = {"day1": 420, "day2": 380, "day3": 390}
obj = pd.Series(calories)
# Note: The keys of the dictionary become the labels.
print(obj)
# To select only some of the items in the dictionary, use the index argument and specify only the items you want to
# include in the Series.
objSelect = pd.Series(calories, index=["day1", "day2"])
print(objSelect)

