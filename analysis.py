# Thomas Roux
# Analysis of iris data set
# 13/04/2019

# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Increases output display to show all columns and rows
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# Imports data set, headings automatically ascribed from .csv file
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
# Headings: sepal_length; sepal_width; petal_length; petal_width; species
data = pd.read_csv('data/irisdataset.csv', delimiter = ',')

# Assesses whether pandas has detected any standard missing values 
# by showing sum of all missing values
# https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
print("\nMissing values in data set per variable:")
print(data.isnull().sum())

# Prints descriptive stats of each variable, ungrouped
print("\nDescriptive stats, ungrouped")
print(data.describe())

# Prints descriptive stats of each variable, grouped by species
print("\nDescriptive stats, grouped by species")
print(data.groupby('species').describe())

# Prints a histogram of each variable for the whole sample
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html
data.plot.hist(alpha = 0.5)
plt.show()

# Prints a histogram of each variable, grouped by species
data.groupby('species').plot.box()
plt.show()



