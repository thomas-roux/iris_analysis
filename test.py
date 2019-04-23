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

# Plot box whiskers
# sb.catplot(x = "species", y = "sepal_length", kind = box, data = data)
# plt.show()

# https://stackoverflow.com/a/29432741
import os

os.mkdir('images')

grouped = data.groupby(['species'])
for name, group in grouped:
    print(name)
    for column in group:
        if column == 'species':
            continue
        x = group[column]
        sb.distplot(x, bins = 10, kde = False)
        plt.title("Histogram of Iris " + str(name) + "'s " + str(column))
        plt.xlabel(str(column) + " in centimetres.")
        plt.ylabel("Count")
        plt.savefig('images/{}'.format(str(name) + str(column)))
        plt.show()