# Fisher's Iris Data Set

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

Created: 13-03-2019,
Last update: 28-04-2019  

___

Project for Programming and Scripting module at GMIT 2019

This repository documents my research, project progress (including comments for my future reference) and findings to the Fisher's Iris Data Set Project for the Programming and Scripting module, Galway-Mayo Institute of Technology, 2019.  

Lecturer: dr Ian McLoughlin

The detailed Project instructions:
<https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf>  
___

## Project research plan

1. Introduction to the project
2. Fisher's iris data set
   1. Origin
   2. Iris data set
3. Python language as a tool for data analysis
   1. Python language, libraries and modules
   2. Insight into raw data
   3. The data analysis
   4. Variables
4. Data set analysis
   1. Jupyter Notebook
5. Findings
6. Conclusion  
References
___

## 1. Introduction

This project is intended to introduce into data analysis, based on example of the Fisher's Iris data set. The data set was chosen for its relative simplicity and a rich literature reference.

The intention of the project is to get practical understanding of handling data in Python environment, including data types and structures handling, data splicing, plots generation and interpretation.

## 2. Fisher's iris data set

### 2.1 Origin

The data set is named after Ronald Fisher, a biologist. He made a significant contribution to development of statistics.

The iris flower exists in a number of species. For untrained eye they may look alike.

<img src="https://upload.wikimedia.org/wikipedia/commons/4/49/Iris_germanica_%28Purple_bearded_Iris%29%2C_Wakehurst_Place%2C_UK_-_Diliff.jpg" alt="Iris_flower" width="200"/>

### 2.2 Iris data set

The data set contains 3 classes (iris species: Iris Setosa, Iris Versicolour, Iris Virginica) of 50 instances each. The classes are described with the following attributes:

1. sepal length in cm,
2. sepal width in cm,
3. petal length in cm,
4. petal width in cm.

The Iris data set is his fameus statistical description of three species of iris flowers. It contains measurements of 50 samples consisting length and width of sepals and petals for each species. The data gathered in the data set is a useful aid for the species discrimination and classification.

Background of Fisher's Iris data set on Wikipedia page: <https://en.wikipedia.org/wiki/Iris_flower_data_set>, or on Machine Learning Repository of University of California: <https://archive.ics.uci.edu/ml/datasets/iris>.

## 3 Python language as a tool for data analysis

### 3.1 Python language, libraries and modules

Python programming language is acclaimed for its capacity of handling large amount of data in scientific community of different specialisation. Its natural functionality has been extended by development of external libraries dedicated for specific purposes. Below are listed several I used for accomplishment of this project.

1. Numpy
   >NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. - Wikipedia
2. Pandas
   >Pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. - Wikipedia
3. Matplotlib
   >Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. - Wikipedia
4. Seaborn
   >Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. - seaborn.pydata.org
  
### 3.2 Insight into raw data

Raw dataset obtained from: <http://archive.ics.uci.edu/ml/machine-learning-databases/iris/>.

The first few rows look like this:  
![iris_dataset](iris_dataset.png)

A quick review of the raw data in the csv file reveals the following findings:

1. The data set is organised in 5 columns - first 4 containing attributes (or features) and the last one describing the class, and 150 rows - instances.
2. Each iris species has 50 instances of data.
3. Columns 1 to 4 consist of `float` type numbers (lengths and widths of sepals and petals in cm), whereas 5th column is of `string` type (iris species).

### 3.3 The data analisis

The analysis was initially intended to be carried out using Python scripts. However, in due course, the advantages of Jupyter Notebook tool has been  recognised, resulting in migration of the analysis from Python scripts to corresponding Jupyter Notebook.

The initial python program file name used to perform some basic data analysis is: **`iris.py`**. This program was left unfinished, however, and the work was continued in Jupyter Notebook.

A Jupyter Notebook for the project is created: **`PandS_Project_2019.ipynb`**.

The program and the Jupyter Notebook are reposited at: <https://github.com/andkoc001/PandS-Project2019>.

### 3.4 Variables

The following are the variables used throughout the project - listed here for reference.

| \#  | Variable | Type      | Description                                 |
| --- | -------- | --------- | ------------------------------------------- |
| 1   | `ids`    | DataFrame | iris data set - read from csv file          |
| 2   | `isd2`   | DataFrame | iris data set with species class as indices |
| 3   | `setos`  | DataFrame | subset with Iris Setosa data                |
| 4   | `versi`  | DataFrame | subset with Iris Versicolor data            |
| 5   | `virgi`  | DataFrame | subset with Iris Virginica data             |

## 4. Data set analysis

### 4.1 Jupyter Notebook

Analysis progress description and results have been recorded in the Jupyter Notebook `PandS_Project_2019.ipynb`.

## 5. Findings

Iris data set analysis is primarily a classification problem. The results of the analysis, illustrated in the data plots, indicate that raw measurements of the flowers features can be a useful tool in determining the species. In some cases the raw data alone could yield information about the iris species.

The analysis I performed demonstrated that Iris Virginica can be well  identified by measurement of its petal and sepal dimensions. When compared to the dimensions of the other two species in question and visualised on appropriate plots (e.g. line plots or scatter plots), the measurements stand out from the measurements of the other species and can be easily discriminated.

The Iris Setosa and Iris Versicolor are very similar in size of their sepals and petals. As a result it is very difficult to tell them apart. Here, again, the visualised data provide a significant help. Even though the interpretation of the results can be tricky and carries some level of risk related to inaccuracy, the graphs of the data can back the classification decision. Specifically the petal length to petal width ratio can be helpful in distinguishing the two species - compare the scatter plot in the Jupyter Notebook.

## 6. Conclusion

Data analysis is a powerful technique in relation to objects classification and machine learning. The tools used in the project - Python language and its libraries - offer a lot of functionality, of which just few were utilised. Much more is still to be learnt. One of many things that could yet be done is pattern analysis and machine learning algorithm. These, however, will be carried out under another project.

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
- Data visualisation in Python: <https://medium.com/python-pandemonium/data-visualization-in-python-line-graph-in-matplotlib-9dfd0016d180>
- DataFrame tutorial: <https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python>
- iris data analysis example: <https://www.slideshare.net/thoi_gian/iris-data-analysis-with-r>
- Classifying Species of Iris Flowers: <https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers>

### Github and Markdown

- An Introduction to Version Control Using GitHub Desktop: <https://programminghistorian.org/en/lessons/getting-started-with-github-desktop>
- Mastering Markdown: <https://guides.github.com/features/mastering-markdown/>
- Markdownlint Rules: <https://github.com/DavidAnson/markdownlint/blob/v0.12.0/doc/Rules.md>

### Fellow students

Much inspiration, ideas, directions and solutions throughout the project has been obtained from my fellow students of the course. Thank you all for your great help!