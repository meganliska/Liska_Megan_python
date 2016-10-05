# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:31:45 2016

@author: meganliska
"""

#Homework 3 
#Group C
#Most of this homework was solved using the basic panda commands found in the
#pandas online documentation 

#Question 1 
"""
Directly load the IRIS dataset from the internet into Python and add the 
column names using Python code instead of an editor.

"""
import pandas as pd #imports the pandas library as pd so use pd in commands


irisdata = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#sets url as variable to make it easier to call later

columns = ['sepal length', 'sepal width', 'petal length',
          'petal width', 'class'] # column names, we got these from the UCI 
                                  #database .name file 


dataset = pd.read_csv(irisdata, names = columns)
#directly loads irisdata from the internet using pandas read function


#-----------------------------------------------------------------------------


#Question 2
#Using Pandas, display the first ten and the last ten rows of the data.

print(dataset.head(10)) #displays the first 10 rows using panda method .head

print(dataset.tail(10)) #displays the last 10 rows

#-----------------------------------------------------------------------------

#Question 3
#Using Pandas, print simple location statistics (Count, Mean, STD, Min, 
#25%, 50%, 75%, MAX). 

#Hint - There is a single method call that will accomplish this.

dataset.describe() 


#describe is a built in panda method which prints the count, mean, 
#STD, min, ma, 25%, 50%, and 75% for our numerical variables

#------------------------------------------------------------------------------

#Question 4 

def plothistogram(binsize):
    """
    The function plothistogram accepts a list of numbers that represent numbers 
    of bins and, using Pandas, plots a histogram for each of the numeric 
    columns at each bin size. For example, plothistogram([10, 50, 100]) 
    will plot 12 histograms (3 for each numeric variable) and group the 
    histograms by the column name.
    
    Parameters: 
    binlist - a list of bin sizes
    
    Results:
    Function returns histogram plots grouped by column name
    """
    
    for col in columns[0:4]: #iterate through first four columns
        for i in binsize: #iterate through list of binsize 
            dataset.hist(column = col, bins = i) # print a histogram for each
                                                 # bin size. 
            #.hist has two arguments column and bins so set column to our four
            #numerical columns and bins to the list of binsizes


plothistogram([10,50,100]) #test case 
    

#-----------------------------------------------------------------------------

##Prof G - Great! Nice to include all of themin a single plot
#Question 5 Plot a box plot for each of the numeric columns.
import matplotlib.pyplot as plt #imports the matplot library which generates plots 
plt.figure() #make a new plot 
dataset.boxplot()  #use .boxplot to make a boxplot for each column 


#-----------------------------------------------------------------------------
#Question 6 Plot a bar chart for the nominal column

nominal_count = dataset['class'].value_counts() #dataset['class'] indexes the
#column class and .value_counts counts the frequency of each variable in the
#class column


nominal_count.plot.bar() #makes a bar chart for nominal_count

