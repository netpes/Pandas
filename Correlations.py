# Finding Relationships:


# The corr() method calculates the relationship between each column in your data set.
import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())
# explained result:
# the closer to 1 or -1, the more correlated the data.
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
