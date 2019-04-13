# Title: Fisher's Iris Data Set Analysis
# Description: Program is a result of the research project, as described in Readme.md file on Git Hub repository.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 31-03-2019
# Last update: 03-04-2019

###

# Importing libraries
import numpy as np
import pandas as pd

# Rading the csv data file, assigning variable to its content
# Attribute header=None assumes that there is no header line in the raw csv file - the first row is actual data
ids = pd.read_csv("iris_dataset.csv", header=None)

print(ids)  # shows content of the data set

# application of .describe() method - shows basic statistical information of the data set
print(ids.describe())
