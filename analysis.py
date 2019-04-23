# Thomas Roux
# Analysis of iris data set
# 13/04/2019

# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os

# Create a subdirectory for images
# https://smallbusiness.chron.com/make-folders-subfolders-python-38545.html
os.mkdir('images')

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
for column in data:
    if column == 'species':
        continue
    x = data[column]
    sb.distplot(x, bins = 10, kde = False)
    plt.title("Histogram of whole sample, " + str(column))
    plt.xlabel(str(column) + " in centimetres.")
    plt.ylabel("Count")
    plt.savefig('images/{}'.format(str(column)))
    plt.show()

# Prints a histogram of each variable, grouped by species
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#iterating-through-groups
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
        

# Displays a scatterplot of all variables with each other for whole sample, species color differentiated
# https://seaborn.pydata.org/examples/scatterplot_matrix.html
# Title added to top of diagram
# https://stackoverflow.com/questions/29813694/how-to-add-a-title-to-seaborn-facet-plot
g = sb.pairplot(data = data, hue = "species")
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Pairplot of variables, whole sample")
plt.savefig('images/pairplotall.png')
plt.show(g)

# Displays a scatterplot of all variables with each other, grouped by species
# https://seaborn.pydata.org/tutorial/distributions.html#visualizing-pairwise-relationships-in-a-dataset
for name, group in grouped:
    a = sb.pairplot(group)
    plt.subplots_adjust(top=0.9)
    a.fig.suptitle("Pairplot of variables, " + str(name))
    plt.savefig('images/{}'.format(str(name)))
    plt.show(a)

# Presents a correlation matrix of each variable for whole sample
# https://pythonprogramming.net/pandas-statistics-correlation-tables-how-to/
print("Correlation atrix of whole sample variables")
print(data.corr())
print()

# Presents a correlation matrix of each variable, grouped by species
for name, group in grouped:
    print("Correlation matrix of Iris " + str(name) + "'s variables.")
    print(group.corr())
    print()