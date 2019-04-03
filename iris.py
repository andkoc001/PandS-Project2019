# Title: Fisher's Iris Data Set Analysis
# Description: Program is a playground for data analysis, as described in Readme.md file on Git Hub repository.
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
iris_dataset = pd.read_csv('iris_dataset.csv')

print(iris_dataset)  # shows content of the data set

# application of .describe() method - shows basic statistical information of the data set
print(iris_dataset.describe())
