# Thomas Roux
# Analysis of iris data set
# 13/04/2019

# Import necessary modules
import numpy as np
import pandas as pd

# Increases output display
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# Imports data set, headings automatically ascribed from .csv file
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
# Headings: sepal_length; sepal_width; petal_length; petal_width; species
data = pd.read_csv('data/irisdataset.csv', delimiter = ',')

# Prints descriptive stats of each variable, ungrouped
print("\nDescriptive stats, ungrouped")
print(data.describe())

# Prints descriptive stats of each variable, grouped by species
print("\nDescriptive stats, grouped by species")
print(data.groupby('species').describe())
