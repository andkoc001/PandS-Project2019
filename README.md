# Project for Programming and Scripting module at GMIT 2019 - Fisher's Iris Data Set

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

Created: 13-03-2019,
Last update: 31-03-2019  

___

This repository documents my research, project progress (inluding comments for my future reference) and findings to the Fisher's Iris Data Set Project for the Programming and Scripting module, Galway-Mayo Institute of Technology, 2019.  

Lecturer: dr Ian McLoughlin

The detailed Project instructions:
<https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf>  

___

## Project research and findings

### Research Plan (initial, to be developed in due course)

1. Introduction (to the project, data analysis, data sets, )
2. Pythoin extensions and packages / modules
   1. Matplotlib
   2. Jupyter Notebook
3. Fisher's Iris Data Set
   1. Origin
   2. Data set
4. Data analysis
   1. Basic statistical analysis
   2. Data cleance
   3. Classification, grupping, etc.
5. Graphical interpretation
6. Findings

### Task List (just an ideas catcher)

[ ] - Average of each column  
[ ] - Average of each column with species discrimination  
[ ] - Mean value of each column  
[ ] - Mean value of each column with species discrimination  
[ ] - Min and Max value  
[ ] - Min and Max value with species discrimination
[ ] - Histogram  

### 1. Introduction

Even though Python is a general purpose programming language, it is highly acclaimed for its data anlysis capacity.

There are some modules / libraries dedicated to related activites, for example: **matplotlib**, **numpy**, or extensions, like **Jupyter Notebook**.

This project is intened to introduce into data anlysis, on example of the Fisher's Iris data set.

### 2. Fisher's Iris Data Set

Background of Fisher's Iris data set on Wikipedia page: <https://en.wikipedia.org/wiki/Iris_flower_data_set>

Raw dataset obtained from: <http://archive.ics.uci.edu/ml/machine-learning-databases/iris/> NB (quote from the website):
>"This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net). The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features."

___

A quick review of the raw data reveals the following findings:

1. The data set is organised in 5 columns and 150 rows.
2. Columns 1 to 4 consist of `float` type numbers, whereas 5th column is of `string` type.

___

___

Learning about Jupyter Notebook - mostly through YouTube tutorials.
Start Jupyter Notbook by typing in Terminal: `jupyter notebook`.

___

<https://codewithmosh.com> introductory course to Python offers a quick introduction into machine learning. Pandas package is briefly explained there. One of the methods of the Pandas package is `.describe()`. It can by called by typing: `data_set.describe()`, and `data_set` is a given name to, for example a `.csv` file (the command goes like this:

```Python
data_set = pandas.read_csv(file_name.csv))
```

The `.describe()` method, among others shows some information of the data set, like mean, average, etc.

From the lecture video, ..., regarding useful numpy methods, let's write:

```Python
data = numpy.genfromtxt('raw_data_file.csv', delimiter=',')
```

then:

```Python
firstcol = data[:,0] # subset containing data
```

and then:

```Python
meanfirstcol = numpy.mean(firstcol) # average of first column
numpy.min(firstcol) # minimum element value
numpy.max(firstcol) # maximum element value
```

To create a histogram:

```Python
import matpoltlib.pyplot as pl
pl.hist(firstcol)
pl.show() # NB. it plots **the last** calculation done
```

___

## References

### Project related

* Raw dataset obtained from: <http://archive.ics.uci.edu/ml/machine-learning-databases/iris/>
* Wikipedia page on the Fisher's Iris data set: <https://en.wikipedia.org/wiki/Iris_flower_data_set>

### General Python related

* GMIT Programming and Scripting module materials: <https://learnonline.gmit.ie/course/view.php?id=1588#section-0>
* Python 3 tutorial documentation: <https://docs.python.org/3/tutorial/>
* A Whirlpool Tour of Python by Jake VanderPlas: <https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf>
* The Coder's Apprentice by Pieter Spronock: <http://spronck.net/pythonbook/pythonbook.pdf>
* Python reference: <https://www.w3schools.com/python/python_reference.asp>
* Modules vs Packages vs Libraries in Python: <https://knowpapa.com/modpaclib-py/>
* Python tutorial for beginners: <https://codewithmosh.com>, <https://youtu.be/_uQrJ0TkZlc>
* Stack Overflow forum: <https://stackoverflow.com>
* Python puzzles: <https://blog.finxter.com/>

### Python modules and packages

* Intro to Python packages: <https://data36.com/python-libraries-packages-data-scientists/>
* Anaconda User Guide: <https://docs.anaconda.com/anaconda/user-guide/>
* Matplotlib documentation: <https://matplotlib.org/contents.html>
* 10 Minutes to Pandas: <https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html>
* Pyplot Tutorial: <https://matplotlib.org/users/pyplot_tutorial.html>
* Data visuaisation in Python: <https://medium.com/python-pandemonium/data-visualization-in-python-line-graph-in-matplotlib-9dfd0016d180>
* Jupyter documentation:

### Github and Markdown

* An Introduction to Version Control Using GitHub Desktop: <https://programminghistorian.org/en/lessons/getting-started-with-github-desktop>
* Mastering Markdown: <https://guides.github.com/features/mastering-markdown/>
* Markdownlint Rules: <https://github.com/DavidAnson/markdownlint/blob/v0.12.0/doc/Rules.md>
