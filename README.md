# Fisher's Iris Data Set

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

Created: 13-03-2019,
Last update: 27-04-2019  

___

Project for Programming and Scripting module at GMIT 2019

This repository documents my research, project progress (inluding comments for my future reference) and findings to the Fisher's Iris Data Set Project for the Programming and Scripting module, Galway-Mayo Institute of Technology, 2019.  

Lecturer: dr Ian McLoughlin

The detailed Project instructions:
<https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf>  

___

## Project research, excecution and findings

### Research plan (initial, to be developed in due course)

1. Introduction to the project
2. Fisher's iris data set
   1. Origin
   2. Data set
   3. Raw data
   4. Meaning and significance
3. My analysis
   1. Python modules used (Numpy, Pandas, Mathplotlib, Jupyter Notebook)
   2. Program name and where it is reposited
      1. Python program file: iris.py
      2. Jupyter notebook file: PandS_Project_2019
   3. Program execution - manual and instructions
      1. How to run the program
      2. Some key variables - what is what (naming convention)
4. Iris data set analysis and specific findings
   1. General comment
   2. Basic statistical analysis
   3. Data cleance
   4. Data break down and discrimination
   5. Classification, grupping, etc.
   6. Visualisation and interpretation
   7. Pattern analysis
5. Conclusion
   1. General findings
   2. Ideas for further program development
6. References

### Tasks list (or rather just ideas catcher)

Basic statistical information

- [ ] Min and Max value  
- [ ] Average of each column
- [ ] Mean value of each column  
- [ ] Standard diviation

Data discrimination and classification

- [ ] Min and Max value with species discrimination  
- [ ] Average of each column with species discrimination  
- [ ] Mean value of each column with species discrimination
- [ ] Standard diviation of each column

Visualisation and interpretation

- [ ] Histogram
- [ ] Scattered plot

Pattern analysis

___

## 1. Introduction

This project is intened to introduce into data anlysis on example of the Fisher's Iris data set. The data set was chosen for its relative simplicity and a rich literature reference.

The intention of the project is to get practical understanding of handling data in Python environment, including data types and structures handling, data splicing, plots generation and interpretation.

## 2. Fisher's iris data set

### 2.1 Origin

The data set is named after Ronald Fisher, a biologist. He made a significant contribition to development of statistics. The Iris data set is his fameus statistical description of three species of iris flowers. It contains measurements of 50 samples consisting length and width of sepals and petals for each species.

Background of Fisher's Iris data set on Wikipedia page: <https://en.wikipedia.org/wiki/Iris_flower_data_set>, or on Machine Learning Repository of University of California: <https://archive.ics.uci.edu/ml/datasets/iris>.

### 2.2 Iris data set

The data set contains 3 classes (iris species: Iris Setosa, Iris Versicolour, Iris Virginica) of 50 instances each. The classes are described with the following attributes:

1. sepal length in cm,
2. sepal width in cm,
3. petal length in cm,
4. petal width in cm.

### 2.3 Insight into raw data

Raw dataset obtained from: <http://archive.ics.uci.edu/ml/machine-learning-databases/iris/>.

The first few rows look like this:  
![iris_dataset](iris_dataset.png)

A quick review of the raw data in the csv file reveals the following findings:

1. The data set is organised in 5 columns - first 4 containing attributes (or features) and the last one describing the class, and 150 rows - instances.
2. Each iris species has 50 instances of data.
3. Columns 1 to 4 consist of `float` type numbers (lengths and widths of sepals and petals in cm), whereas 5th column is of `string` type (iris specis).

### 2.3 Meaning and significance of the data set

### 2.4 Python as a tool for data analysis

### 2.5 Python libraries and modules

1. Numpy
   >NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. - Wikipedia
2. Pandas
   >pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. - Wikipedia
3. Matplotlib
   >DescriptionMatplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. - Wikipedia
4. Seaborn
   >Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. - seaborn.pydata.org
  
### 2.6 What, where

The analyis was initially intende to be carried out using Python scripts. However, in due course, the advantages of Jupyter Notbook tool has been  recognised, resulting in migration of the analysis from Python scripts to corresponding Jupyter Notebook.

The initial python program file name used to perform some basic data analysis is: **`iris.py`**. This program was left unfinished, however, and the work was continued in Jupyter Notebook.

A Jupyter Notebook for the project is created: **`PandS_Project_2019.ipynb`**.

The program and the Jupyter Notebook are reposited at: <https://github.com/andkoc001/PandS-Project2019>.

### 2.7 Variables

The following are the variables used throughout the project - listed here for reference.

| \#  | Variable | Type      | Description                                 |
| --- | -------- | --------- | ------------------------------------------- |
| 1   | `ids`    | DataFrame | iris data set - read from csv file          |
| 2   | `isd2`   | DataFrame | iris data set with species class as indices |
| 3   | `setos`  | DataFrame | subset with Iris Setosa data                |
| 4   | `versi`  | DataFrame | subset with Iris Versicolor data            |
| 5   | `virgi`  | DataFrame | subset with Iris Virginica data             |


## 3. Data set analysis

### Jupyter Notebook

Analysis progress description has been included in the Jupyter Notebook `PandS_Project_2019.ipynb`.

## 4. Findings

Iris data set analysis is primarily a classification problem. The results of the analysis, illustrated in the data plots, indicate that raw measurements of the flawers features can be a useful tool in determining the species. In some cases the raw data alone could yeald information about the iris species.

The analysis I performed demonstrated that Iris Virginica can be well  identified by measurement of its petal and sepal dimensions. When compared to the dimensions of the other two species in question and visualised on appropriate plots (e.g. line plots or scatter plots), the measurements stand out from the measurements of the other species and can be easily discriminated.

The Iris Setosa and Iris Versicolor are very similar in size of their sepald and petals. As a result it is very difficult to tell them apart. Here, again, the visualised data provide a significant help. Even thogh the interpretation of the results can be tricky and carries some level ofrisk related to inaccuracy, the graphs of the data can back the classification descision. Specificaly the petal length to petal width ratio can be helpful in distingushing the two species - compare the scatter plot in the Jupyter Notebook.

## Conclusion

Data analysis is a powerful technique in relation to objects classification and machine learning. The tools used in the project - Python language and its libraries - offer a lot of functionality, of which just few were utilised. Much more is still to be learnt.

___

## References

### Project and the data set related

- Raw dataset obtained from: <http://archive.ics.uci.edu/ml/machine-learning-databases/iris/>
- Wikipedia page on the Fisher's Iris data set: <https://en.wikipedia.org/wiki/Iris_flower_data_set>

### General Python related

- GMIT Programming and Scripting module materials: <https://learnonline.gmit.ie/course/view.php?id=1588#section-0>
- Python 3 tutorial documentation: <https://docs.python.org/3/tutorial/>
- A Whirlpool Tour of Python by Jake VanderPlas: <https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf>
- The Coder's Apprentice by Pieter Spronock: <http://spronck.net/pythonbook/pythonbook.pdf>
- Python reference: <https://www.w3schools.com/python/python_reference.asp>
- Modules vs Packages vs Libraries in Python: <https://knowpapa.com/modpaclib-py/>
- Python tutorial for beginners: <https://codewithmosh.com>, <https://youtu.be/_uQrJ0TkZlc>
- Stack Overflow forum: <https://stackoverflow.com>
- Python puzzles: <https://blog.finxter.com/>

### Python modules and packages

- Intro to Python packages: <https://data36.com/python-libraries-packages-data-scientists/>
- Anaconda User Guide: <https://docs.anaconda.com/anaconda/user-guide/>
- Matplotlib documentation: <https://matplotlib.org/contents.html>
- 10 Minutes to Pandas: <https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html>
- Pandas tutorial: <http://www.datasciencemadesimple.com/head-and-tail-in-python-pandas/>
- Pyplot Tutorial: <https://matplotlib.org/users/pyplot_tutorial.html>
- Jupyter documentation: <https://jupyter.org/documentation>
- Jupyter intro: <https://medium.com/ibm-data-science-experience/back-to-basics-jupyter-notebooks-dfcdc19c54bc>
- Jupyter tips and tricks: <https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/>
- Seaborn tutorial: <https://seaborn.pydata.org/tutorial.html>

### Data analysis

- A Complete Tutorial to Learn Data Science with Python from Scratch: <https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/>
- The ultimate machine learning course with python in 6 steps: <https://copycoding.com/d/the-practical-guide-to-learn-machine-learning-with-python-in-12-steps->
- Tutorial to data analysis: <https://machinelearningmastery.com/machine-learning-in-python-step-by-step/>
- Data visuaisation in Python: <https://medium.com/python-pandemonium/data-visualization-in-python-line-graph-in-matplotlib-9dfd0016d180>
- DataFrame tutorial: <https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python>
- iris data analysis example: <https://www.slideshare.net/thoi_gian/iris-data-analysis-with-r>
- Classifying Species of Iris Flowers: <https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers>

### Github and Markdown

- An Introduction to Version Control Using GitHub Desktop: <https://programminghistorian.org/en/lessons/getting-started-with-github-desktop>
- Mastering Markdown: <https://guides.github.com/features/mastering-markdown/>
- Markdownlint Rules: <https://github.com/DavidAnson/markdownlint/blob/v0.12.0/doc/Rules.md>
