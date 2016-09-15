# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:04:59 2016

@author: meganliska
"""
#Math 510 Homework 1 Group C
#Problem 1: Write a function translate that takes a list of English words and returns a list of Swedish words.
#For this problem we define a function called translate which will translate the English words we input into Swedish

def transtoswed(words):
    dict2={"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
#We define our dictionary using the words given in the problem.   
    result = ''
#This sets our result as an empty string the function will fill.

    for char in words:
        swedish = dict2.get(char, char)
#the .get is a python function that works with dictionaries. It searches through
#the dictionary dict2, and will return the char that matches something

        result += swedish
#This sets the results as blank plus swedish, which is defined above. 
    
        
    return result 
#This displays the result so we can confirm that our function worked correctly.
print(transtoswed('merry christmas and happy new year'))        
        
#Problem 2: Write a function char_freq that takes a string and builds a frequency list of the characters contained in it.
#Represent the frequency listing as a Python dictionary.
#For this problem we create a function called char_freq using the .get function that we used in Problem 1
def char_freq(text):
#we define our function and indicate that the input for the 
#functino will be text or a string

    result = {} #This indicates/defines our result as an dictionary, hence the {}, that the function will fill.
    
    for char in text: #we start a for loop will will iterate through each character in our text
        result[char] = result.get(char, 0) + 1 #the result will be 
        
    return result
print(char_freq('abbabcbdbabdbdbabababcbcbab'))
    

#Problem 3: Implement an encoder/decoder of ROT-13
def decoder(text):
    key = {'a':'n', 'b':'o', 
               'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 
               'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
               'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 
               'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 
               'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 
               'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 
               'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 
               'Z': 'M'}
#Like in problem 1 we define our dictionary
#We will solve this problem in the exact same manner as problem 1 since it is essentially
#asking the same thing, namely to take an input string and return its corresponding entry in our Python dictionary.
    result = '' #This indicates that our result will be a string/python will display 

    for char in text:  #our for loop will iterate through the text we input
        new = key.get(char, char)
        result += new
        
    return result
print(decoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))
#This prints the test string given in the assignment to make sure our program worked.

#Problem 4: Define a spelling correction function that takes a string and
#1 Compresses two of more occurences of the space character into one
#2 Inserts an extra space after a period if the period is directly followed by a letter.
#As stated in the tip, we will complete this problem using regular expressions, namely the function


import re
#This imports our regular expressions so Python will recognize the re.sub function.
def correct(InputString):  #We define our function indicating that our input will be a string.
    NewString= re.sub('\s+',' ',InputString) #This uses the regular expressions re.sub. This will search through Input string and substitute any instance of one or more spaces with just one space
    
    NewString= re.sub('\.','. ',NewString) #This will substitute a period in Input string with a period and a space after it, effectiely adding a space after a period
    
    print(NewString) #This will print the new string so we can see that our corrections have been made

InputString= 'This  is  very funny and cool.Indeed!'
correct(InputString) #This tests the example given in the question.

#Problem 5: Define a function make_3sg_form which, given a verb in infinite 
#form returns its third person singular form.
#our function will be a series of if else statements that run through the
#three (or more) statements that we are given/really they are more like rules
#and provide a different return for each grammar situation. 

def make_3sg_form(words):
#We define the function using the name given in the problem.

    if words.endswith('y'):
        return words[0:-1] + 'ies'
#we are using the .endswith function which returns blank if our input string ends with y and blank if it doesn't
#If our input word does end in y our return will be our original word without the last character
#and with ies added on, thus replacing the y with ies
        
    elif words.endswith('o'):
        return words + 'es' #This is case two, if the word ends in o our function will return the original word with es added to the end        
    
    elif words.endswith('ch'):
        return words + 'es' #This is the same as the case above.   
    elif words.endswith('s'):
        return words + 'es' #This is the same as the case above.    
    elif words.endswith('sh'):
        return words + 'es' #This is the same as the case above.    
    elif words.endswith('x'):
        return words + 'es' #This is the same as the case above.    
    elif words.endswith('z'):
        return words + 'es' #This is the same as the case above.    
    else: 
        return words + 's' #This is our final case, if the word ends in any other letter than the ones specified
#our function will return the original words with s added on to the end. 
        

#Problem 6: Define a function make_ing_form which, given a verb in infinite
#form, returns its present participle form.
#We solve this problem in a manner similiar to problem 5, using a series of if/else statements to
#test the different grammatical cases for our words
Con = 'bcdfghjklmnpqrstvwxyz'
Vowel = 'aeiou'

def make_ing_form(word):
    if word in ['be', 'see', 'flee', 'knee']:
        return word + 'ing'
        
    elif word.endswith('ie'):
        return word[0:-2] + 'ying'    
    
    elif word.endswith('e'):
        return word[0:-1] + 'ing'
        
   
    elif word[-3] in Con and word[-2] in Vowel and word[-1] in Con:
       return word + word[-1] + 'ing'
       
    else:
        return word + 'ing'
    

#Problem 7: Using the higher order function reduce, write a function max_in_list
#which takes a list a numbers and returns the largest one.
#we use the reduce function which does (state what it does)
#Inside the brackets we first use lamda beacuse the reduce function
#does that thing where one of its arguments is a function
#this is where we could have used the max function but didn't
# Lamda just does blank. the stuff following lamda is the new little function
#which is an if else statement which does blank
from functools import reduce  #since the reduce function is not built in in python 3.5 we have to first import
#it from ()
def max_in_list(numbers): #we define or function using the name given in the homework question
    result = reduce(lambda x,y: x if x > y else y, numbers )
    
    return result
    
    
#Problem 8: Write a function that blanks in three ways
#Using a for loop
#Using the map function
#Using list comprehensions

def listlength(word):
    result = []
    for x in word:
        l = len(x)
        result.append(l)
    return result

print(listlength(['The', 'class', 'is', 'teaching', 'python']))

def listlength(word):
    return list(map(len,word))

print(listlength(['The', 'class', 'is', 'teaching', 'python']))    
    
def listlength(word):
    length = [len(i) for i in word]
    return length

print(listlength(['The', 'class', 'is', 'teaching', 'python']))

    
#Problem 9: Write a function find_longest_word that takes a list of words
#and returns the length of the longest one
#this is three functions in one, first is the max function which blank
#then is the map function which takes a function and applies to each blank
#third is the len function which yields the length of our input, in
#this case our list of words
#so the map function will apply the length function to each of the words
#then the max function will take the largest of the lengths and display it
#from functools import reduce
def find_longest_word(words):
    return max(map((len, words)))
    
#Problem 10: Use the higher order function filter to define a function that
#takes a list of words and an integer n and returns the list of words
#that are longer than n. 
    def filter_long_words(wordlist, n):#We define our function and indicate
    #that it will have two inputs, our string of words and integer n
        return(list(filter(lambda x: len(x) > n, wordlist)))
    

#Problem 11: Solve problem 1 again except this time use the map function
 #This time, as speicified in the problem we use the map function
 #like the reduce function, map is also a higher order function and thus
 #one of its arguments is a function itself. 
 #In this case it is our lambda function which takes something and spits out the 
 #swedish
def translatemap(words):
#We define our translate function
    dict2={"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
#As in problem one we input the dictionary of english and swedish words
#We were given, again note the curly brackets since it is a dectionary
    result = map(lambda x: dict2[x], words)
   
    return list(result)
#We return our result, we have to return it using list because we want blank
#and not just the spot it mapped it too (get clarification on this)

#Problem 12: Implement the higher order functions map, filter and reduce
def ourmap(func, word):
    result = []
    for x in word:
        newelm = func(x)
        result.append(newelm)
    return result

def ourfilter(func, word):
    result = []
    for x in word:
        if func(x) == True:
            result.append(x)
    return result
    
def ourreduce(func, word):
    result = word[0]
    for x in word[1:]:
        result = func(result, x)
    return result
        