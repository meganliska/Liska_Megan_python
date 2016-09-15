# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:04:59 2016

@author: meganliska
"""
#Math 510 Homework 1 Group C
#Problem 1: Write a function translate that takes a list of English words and 
#returns a list of Swedish words.


def translate(words):
    """
    
    This function translate() will 
    translate the English words we input into Swedish
    For example translate('merry') will return 'god'
    
    Parameters:
    words- An English word from our dictionary
    
    Returns: 
    The corresponding Swedish word from our dictionary
    If word inputted in function is not in the dictionary function returns
    original word
    
    ml2016
    
    """
    dict2 = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott",
             "new": "nytt", "year": "ar"} #We define our dictionary using the words given in the problem.   
    result = '' #sets our result as an empty string the function will fill.

    for char in words: #loops through the words we input
        swedish = dict2.get(char, char) #searches through dictionary and

#the dictionary dict2, and will return the char that matches something

        result += swedish #sets results as blank plus swedish 
    
        
    return result 
#This displays the result so we can confirm that our function worked correctly.
print(translate('merry christmas and happy new year'))        
        
#Problem 2: Write a function char_freq that takes a string and builds a 
#frequency list of the characters contained in it.
#Represent the frequency listing as a Python dictionary.

def char_freq(text):
    """
    The function char_freq() takes a string and builds a frequency
    list of the characters contained in it
    
    Parameters:
    text- a string of characters 
    
    Results:
    A Python dictionary listing the frequencies of each character
    
    ml2016
    """
    result = {} #sets our result as an dictionary that the function will fill.
    
    for char in text: #loop will iterate through each character in our text
        result[char] = result.get(char, 0) + 1 #sets result as  
        
    return result
print(char_freq('abbabcbdbabdbdbabababcbcbab')) #test case
    

#Problem 3: Implement an encoder/decoder of ROT-13
def decoder(text):
    """
    The function decoder(text) takes an English word or sentence and encodes it
    using ROT 13. It can also decode ROT 13 back in regular English
    
    Parameters:
    text- a string of characters either in English or already encoded
    
    Results:
    a string either of encoded English or decoded ROT 13
    
    ml2016
    """
  
    key = {'a':'n', 'b':'o', 
               'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 
               'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
               'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 
               'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 
               'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 
               'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 
               'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 
               'Z': 'M'}

    result = ''  

    for char in text:  #iterate through the text we input
        new = key.get(char, char)
        result += new
        
    return result
print(decoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))


#Problem 4: Define a spelling correction function that takes a string and
#1 Compresses two of more occurences of the space character into one
#2 Inserts an extra space after a period if the period is directly followed by 
#a letter.
#As stated in the tip, we will complete this problem using regular expressions, namely the function


import re #imports our regular expression functions including re.sub
def correct(InputString):  
    """
    The function correct(InputString) takes a string and does two things
    1:Compresses two or more occurences of the space character
    into one.
    2: Inserts an extra space after a period if the period is directly 
    folloed by a letter.
    
    Parameters:
    InputString- a string of characters or words
    
    Results:
    The corrected string of characters or words
    ml2016
    """
    NewString= re.sub('\s+',' ',InputString) #substitute any instance of one or more spaces with just one space
    
    NewString= re.sub('\.','. ',NewString) #substitute a period in Input string with a period and a space after it, effectiely adding a space after a period
    
    return NewString #returns our result 

InputString= 'This  is  very funny and cool.Indeed!'
correct(InputString) #This tests the example given in the question.


#Problem 5: 
def make_3sg_form(words):
    """
   The function make_3sg_form() takes a verb in infinite 
   form returns its third person singular form.
   our function will be a series of if else statements that run through the
   three (or more) statements that we are given/really they are more like rules
   and provide a different return for each grammar situation. 
   
   Parameters:
   words- an English verb in infinite form
   
   Results:
   An English verb in third person singular form
   ml2016
   """


    if words.endswith('y'):
        return words[0:-1] + 'ies'
#we are using the .endswith function which returns blank if our input string 
   #ends with y and 
  #blank if it doesn't
#If our input word does end in y our return will be our original word without the last character
#and with ies added on, thus replacing the y with ies
        
    elif words.endswith('o'):
        return words + 'es' #case two, if the word ends in o, return the original word with es added to the end        
    
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
        return words + 's' #final case, if the word ends in any other letter than the ones specified
#our function will return the original words with s added on to the end. 
        

#Problem 6:
Con = 'bcdfghjklmnpqrstvwxyz'
Vowel = 'aeiou'

def make_ing_form(word):
    """
     The function make_ing_form(word) takes a verb in infinite
     form and returns its present participle form.
     
     Parameters:
     word- an English verb in infinite form
     
     Results:
     An English word in present participle form
   
     
     """
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
    

#Problem 7: 
from functools import reduce #imports reduce funtion since it is not in 
                             #Python 3.5
def max_in_list(numbers):
    """
    The function max_in_list(numbers) uses the higher order function reduce to
    take a list a numbers and return the largest one.
    
    Parameters:
    numbers- a list of numbers
    
    Results:
    A number, namely the largest number in our list
    
    
   
    ml2016
    """    

    
    result = reduce(lambda x,y: x if x > y else y, numbers )
    
    return result
    
    
#Problem 8: Write a function that blanks in three ways
#Using a for loop
#Using the map function
#Using list comprehensions

def listlength(word):
    """
    The function listlength(word) takes a blank and does blank using a 
    for loop.
    Parameters:
    
    Results:
    
    ml2016
    """
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

    
#Problem 9: 
#this is three functions in one, first is the max function which blank
#then is the map function which takes a function and applies to each blank
#third is the len function which yields the length of our input, in
#this case our list of words
#so the map function will apply the length function to each of the words
#then the max function will take the largest of the lengths and display it

def find_longest_word(words):
    """
    Write a function find_longest_word that takes a list of words
    and returns the length of the longest one
    Parameters:
    
    Results:
    
    ml2016
    """
    return max(map((len, words)))
    
#Problem 10: 
def filter_long_words(wordlist, n):
    """
    Use the higher order function filter to define a function that
    takes a list of words and an integer n and returns the list of words
    that are longer than n. 
    
    We define our function and indicate
    that it will have two inputs, our string of words and integer n
    
    ml2016
    """
    return(list(filter(lambda x: len(x) > n, wordlist)))
    

#Problem 11: Solve problem 1 again except this time use the map function
 #This time, as speicified in the problem we use the map function
 
 #In this case it is our lambda function which takes something and spits out the 
 #swedish
def translatemap(words):
    """
    The function translatemap uses the higher order function map to take a list
    of English words and translate them to Swedish words.
    
    Paramters:
    words - English words contained in our dictionary
    
    Results:
    The Swedish word corresponding to the English word in our dictionary
    If a word is not in our dictionary function returns original word
    
    ml2016
    """
    dict2={"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", 
           "new": "nytt", "year": "ar"} #input the dictionary of english and swedish words

    result = map(lambda x: dict2[x], words) #applies the lambda function to
                                            #the words put into the function
   
    return list(result) #return result, we have to return it using list 
                        #because we want blank


#Problem 12: Implement the higher order functions map, filter and reduce
def ourmap(func, word):
    """
    The function ourmap(func, word) implements the map function
    Parameters:
    func - a function we apply to our element
    word - a string
    
    Result- 
    
    ml2016
    """
    
    result = []
    for x in word:
        newelm = func(x)
        result.append(newelm)
    return result

def ourfilter(func, word):
    """
    The function ourfilter(func, word) implements the filter function
    Parameters:
    func - a function we apply to our element
    word - a string
    
    Result- 
    
    ml2016
    """
    result = []
    for x in word:
        if func(x) == True:
            result.append(x)
    return result
    
def ourreduce(func, word):
    """
    The function ourreduce(func, word) implements the reduce function
    Parameters:
    func - a function we apply to our element
    word - a string
    
    Result- 
    
    ml2016
    """
    result = word[0]
    for x in word[1:]:
        result = func(result, x)
    return result
        