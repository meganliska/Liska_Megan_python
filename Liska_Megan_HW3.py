# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:31:45 2016

@author: meganliska
"""

#Homework 3 
#Group C
#import urllib.request

"""
Instead of downloading the files, figure out how to directly load the files 
from the internet into Python and add the column names using Python code instea
d of an editor.



5.Plot a box plot for each of the numeric column.
6.Plot a bar chart for the nominal column
"""
import pandas as pd #imports the pandas library as pd so we use pd in our commands
#import re
import csv #imports csv (say that it does)

...
irisnames = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names'
irisdata = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#sets url as variable to make it easier to call later
names = pd.read_csv(irisnames)
#directly loads names url from the internet
dataset = pd.read_csv(irisdata)
#directly loads irisdata from the internet using pandas read function
df = pd.DataFrame(irisdata, columns=['Names', 'Births'])

#2.Using Pandas, display the first ten and the last ten rows of the data.
df.head(10)

df.tail(10)

#3.Using Pandas, print simple location statistics (Count, Mean, STD, Min, 
#25%, 50%, 75%, MAX). There is a single method call that will accomplish this.



#dataset = pd.read_table("irisdata", header=0, sep=',') idk if you already did this
dataset.describe(percentiles=None, include=None, exclude=None)
#dataset.describe calls the function describe to our defined dataset.  describe prints the count, mean, 
#STD, min, ma, 25%, 50%, and 75% for our numerical variables


"""
4.Write a function that accepts a list of numbers that represent numbers of bins
and, using Pandas, plots a histogram for each of the numeric columns at each 
bin size. For example, if I call your function with [10, 50, 100] as bin sizes, 
the function should plot 12 histograms (3 for each numeric variable). 
Group the histograms by the column name.
"""


#using the earlier defined dataset, we are able to create a histogram of the numerical data
dataset.hist(column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False, figsize=None, layout=None, bins=10)

#next, we will create a bar chart for the nominal column
dataset.irisclass.value_counts().plot(kind='bar')


# 1. sepal length in cm
  # 2. sepal width in cm
   #3. petal length in cm
   #4. petal width in cm
   #5. class: