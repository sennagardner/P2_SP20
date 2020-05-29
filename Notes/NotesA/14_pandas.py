# Pandas!

import pandas as pd
import random

# lists --> dicts --> dataframes (series)

# Series are pandas arrays (1d arrays)
s = [random.randrange(100) for x in range(10)]
my_series = pd.Series(s)
print(my_series)
print(type(my_series))  # pd.Series type
print(list(my_series))  # conversion to list is simple

# make a df (DataFrame) from a dictionary
d = {'coll': [1,2,3], 'col2': [4,5,6]}
df = pd.DataFrame(data=d)
print(df)

# from an array/list
d2 = [[1,2,3], [4,5,6], [7,8,9]]  # each item is a row
cols = ["A", "B", "C"]
df2 = pd.DataFrame(data=d2)
print(df2)

# read from a csv (or other data)
df3 = pd.read_csv('World firearms murders and ownership - Sheet 1.tsv', sep='\t')
print(df3)

# useful methods
print(df3.head())  # first 5 rows/items
print(df3.tail())  # last 5
print(df3.info())  # datatypes (null values)
print(df3.describe())  # basic stats
