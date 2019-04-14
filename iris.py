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

# Rading the csv data file, assigning variable to its content
# Attribute header=None assumes that there is no header line in the raw csv file - the first row is actual data
ids = pd.read_csv("iris_dataset.csv", header=None)

# Content of the data (commented out for clarity)
# print(ids)

# head and tail methods print out n first / last respectively lines of data, where n is an argument of the method, default argument is n=5; source: http://www.datasciencemadesimple.com/head-and-tail-in-python-pandas/
print(ids.head())
print(ids.tail())

# application of .describe() method - shows basic statistical information of the data set
print(ids.describe())

# Separation of the data per attributes (columns)
# firstcol = ids[:, 0]
