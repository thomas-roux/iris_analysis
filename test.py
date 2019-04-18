# Thomas Roux
# Test program to try out features before incorporating into full analysis program

# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Increases output display to show all columns and rows
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# Imports data set, headings automatically ascribed from .csv file
# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
# Headings: sepal_length; sepal_width; petal_length; petal_width; species
data = pd.read_csv('data/irisdataset.csv', delimiter = ',')

# Plot pairplot table
#sb.pairplot(data)
#plt.show()

# Plot box whiskers
# sb.catplot(x = "species", y = "sepal_length", kind = box, data = data)
# plt.show()

grouped = data.groupby(['species'])
for name, group in grouped:
    print(name)
    for column in group:
        if column == 'species':
            continue
        x = data[column]
        sb.distplot(x, bins = 10)
        plt.show()
