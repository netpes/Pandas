import pandas as pd

df = pd.read_csv('data.csv')
# The head() method returns the headers and a specified number of rows, starting from the top.
print(df.head(10))
# Note: if the number of rows is not specified, the head() method will return the top 5 rows.

# There is also a tail() method for viewing the last rows of the DataFrame.
print(df.tail())

# The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())
# The result tells us there are 169 rows and 4 columns:
# And the name of each column, with the data type


# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
