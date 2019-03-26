# Project for Programming and Scripting module at GMIT 2019 - Fisher's Iris Data Set

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

Created: 13-03-2019,
Last update: 26-03-2019  

___

This repository contains my research and findings to the Fisher's Iris Data Set Project for the Programming and Scripting module, Galway-Mayo Institute of Technology, 2019.  
Lecturer: dr Ian McLoughlin

The detailed Project instructions:  
<https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf>  

~~Disclaimer: As I am only learning the Python programming language, my code is naturally imperfect. However, some comments or redundant pieces of code, etc. are left intentionally for the purpose of learning, testing and future reference.~~

___

## Project research and findings

### Research Plan (initial)

1. Introduction
2. Fisher's Iris Data Set
3. Pythoin extensions
   1. Matplotlib
   2. Jupyter Notebook
4. Statistical analysis
5. Graphical interpretation
6. Findings

### 1. Introduction

Python is acclaimed programming language for data anlysis.

There are some modules / libraries dedicated to related activites, for example: **matplotlib**, **numpy**, or extensions, like **Jupyter Notebook**.

### 2. Fisher's Iris Data Set

Raw dataset obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
NB. "This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net ). The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features."

Learning about Jupyter Notebook - mostly through YouTube tutorials.
Start Jupyter Notbook by typing in Terminal: "jupyter notebook".

https://codewithmosh.com offers a quick introduction into machine learning. Pandas package is briefly explain there. One of the methods of the Pandas package is .describe(). It can by called by typing: "data_set.describe()", and data_set is a given name to, for example a .csv file (the command goes like this: "data_set = pandas.read_csv(file_name.csv)). The .describe() methods, among others shows some information of the data set, like mean, average, etc.

From lecture video, ..., regarding useful numpy methods:
`data = numpy.genfromtxt('raw_data_file.csv', delimiter=',')`
then:
`firstcol = data[:,0]` # subset containing data 

from first column
`meanfirstcol = numpy.mean(firstcol)` # average of first column
`numpy.min(firstcol)` # minimum element value
`numpy.max(firstcol)` # maximum element value

To create a histogram:
`import matpoltlib.pyplot as pl`
`pl.hist(firstcol)`
`pl.show()` # NB. it plots **the last** calculation done


___

## Project research and findings

* Raw dataset obtained from: <http://archive.ics.uci.edu/ml/machine-learning-databases/iris/>
* Python tutorial: <https://codewithmosh.com>
* Jupyter documentation: