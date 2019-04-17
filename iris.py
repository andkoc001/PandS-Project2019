# Title: Fisher's Iris Data Set Analysis
# Description: Program is a result of the research project, as described in Readme.md file on Git Hub repository.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 31-03-2019
# Last update: 14-04-2019

###

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

# Rading the csv data file, assigning variable to its content
# Attribute header=None assumes that there is no header line in the raw csv file - the first row is actual data
ids = pd.read_csv("iris_dataset.csv", header=None)

# Adding headers to attributes (columns); source: https://stackoverflow.com/a/28162530
ids.columns = ["Sepal length, cm", "Sepal width, cm",
               "Petal length, cm", "Petal width, cm", "Species"]

# Content of the data (commented out for clarity - too long)
# print(ids)

# head and tail methods print out n first / last respectively lines of data, where n is an argument of the method, default argument is n=5; source: http://www.datasciencemadesimple.com/head-and-tail-in-python-pandas/
print(ids.head())
# print(ids[49:51]) # This shows rows of index between 49 and 51 (incl. 49 bu excl. 51), where there is a change in the iris specie in the data set
# print(ids[99:101]) # Shows rows index between 100 and 101
print(ids.tail(3))

# Application of .describe() method - shows basic statistical information of the data set
# print(ids.describe())

# Separation of the data per attributes (columns)
# Confirming the type of the data set
# Currently data type is DataFrame (consists of numbers and strings), meaning it cannont be sliced
# print(type(ids)) # firstcol = ids[:, 0] # this command would produce a TypeError
