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
    translate the English words we input into their Swedish counterpart
    For example translate('merry') will return 'god'
    
    Parameters:
    words - An English word, or words, from our dictionary
    The words can either be in a string or in a list
    
    Returns: 
    The corresponding Swedish word from our dictionary
    If the word inputted in the function is not in the dictionary translate() 
    returns the original word
    
    ml2016
    
    """
    dict2 = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott",
             "new": "nytt", "year": "ar"}  #define our dictionary using the 
                                           #words given in the problem.   
    result = '' #sets our result as an empty string the function will fill.
    
    if type(words) == str: #this takes care of the case the English words
                           #we input into the function is a string
        words = words.split() #this splits the string into the individual words
        
    
    elif type(words) == list : #this is the case where words is a list
        pass #we don't need to split a list so we keep the list as is 
    
    for char in words: #loops through the words we input
        swedish = dict2.get(char, char) #.get searches through dict2 and gives  
                                        #the value of char if char is in the 
                                        #dictionary and simply returns the 
                                        #original char if it is not.



        result += ' ' + swedish #sets results as the swedish word and adds 
                                #spaces between our words
    
        
    return result
print(translate('merry christmas and happy new year'))
print(translate(['merry', 'christmas', 'and', 'happy', 'new', 'year']))
#test case       
        
#Problem 2: Write a function char_freq that takes a string and builds a 
#frequency list of the characters contained in it.
#Represent the frequency listing as a Python dictionary.

def char_freq(text):
    """
    The function char_freq() takes a string and builds a frequency
    list of the characters contained in it
    
    Parameters:
    text - a string of characters 
    
    Results:
    A Python dictionary listing the frequencies of each character
    
    ml2016
    """
    #Can once again use the .get function
    #This time .get(x,0) will look through the dictionary for x and return 
    #0 if x is not found. 
    #Then add 1 so it will put a 1 in our result dictionary if x is found
    result = {} #sets our result as an dictionary that the function will fill.
    
    for char in text: 
    #iterate through each character in our text
        result[char] = result.get(char, 0) + 1 #uses the .get function to count
                                               #the number of times 
                                               #char appears in the input text

        
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
    A string either of encoded English or decoded ROT 13
    
    ml2016
    """
    #Question is similiar to problem 1
    #solve in a similiar manner using the .get function
  
    key = {'a':'n', 'b':'o', 
               'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 
               'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
               'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 
               'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 
               'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 
               'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 
               'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 
               'Z': 'M'} #inputs our dictionary 

    result = ''  #sets result as empty string the function will fill

    for char in text:  #iterate through the characters in input text
        new = key.get(char, char) #uses .get to match our input character with
                                  #its match in our dictionary
        result += new #sets our result as the corresponding character
        
    return result
print(decoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))#test case 


#Problem 4: Define a spelling correction function that takes a string and
#1 Compresses two of more occurences of the space character into one
#2 Inserts an extra space after a period if the period is directly followed by 
#a letter.



import re #imports our regular expression functions including re.sub
def correct(InputString):  
    """
    The function correct(InputString) takes a string and does two things:
    1: Compresses two or more occurences of the space character
    into one.
    2: Inserts an extra space after a period if the period is directly 
    followed by a letter.
    
    Parameters:
    InputString - a string of characters or words
    
    Results:
    The corrected string of characters or words
    ml2016
    """
    #Use the tip and use regular expressions, specifically re.sub
    NewString= re.sub('\s+',' ',InputString) #substitute any instance of one 
                                             #or more spaces with just one space
                                            #thus removing extra spaces
    
    NewString= re.sub('\.','. ',NewString) #substitute a period in Input string 
                                          #with a period and a space after it,
                                    #effectiely adding a space after the period
    
    return NewString #returns our result 

InputString= 'This  is  very funny and cool.Indeed!'
correct(InputString) #This tests the example given in the question.


#Problem 5: 
def make_3sg_form(words):
    """
   The function make_3sg_form() takes a verb in infinite 
   form and returns its third person singular form.
   It evaluates the verb based off a set of grammatical rules for conjugation

   
   Parameters:
   words- an English verb in infinite form
   
   Results:
   An English verb in third person singular form
   ml2016
   """
   #use the .endswith('x) function which returns true if our input string ends
   #with x and false otherwise
   #use the .endswith function in conjunction with a series of if/else 
   #statements to test our grammar rules
   #remember to make the/if else statements from most speicific to most general


    if words.endswith('y'):
        return words[0:-1] + 'ies' #case one, if word ends in y return word
                                   #without the y and with ies added on


        
    elif words.endswith('o'):
        return words + 'es' #case two, if the word ends in o, 
                            #return the original word with es added to the end        
    
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
        return words + 's' #final case, if the word ends in any other letter 
                           #than the ones specified return the original word 
                           #with s added on to the end. 
print(make_3sg_form('try'))
print(make_3sg_form('brush'))
print(make_3sg_form('run'))
print(make_3sg_form('fix'))#test cases
        

#Problem 6:
Con = 'bcdfghjklmnpqrstvwxyz' #lists all consonants as one variable to simplify
Vowel = 'aeiou' #lists all vowels as one variable to simplify case 3

def make_ing_form(word):
    """
     The function make_ing_form(word) takes a verb in infinite
     form and returns its present participle form.
     
     Parameters:
     word- an English verb in infinite form
     
     Results:
     An English word in present participle form
   
     ml2016
     """
     #Use series of if/else statments to implement different grammar rules
     #remember to go from most specific case to most general case
    if word in ['be', 'see', 'flee', 'knee']: #our case of exceptions given in 
                                             #the original problem
                                            #If a word is one of these four
                                                #return orignal word with ing
                                            #added to the end
        return word + 'ing'
        
    elif word.endswith('ie'): #if word ends in ie return word with ie taken off
                              #and ying added to the end of the word
        return word[0:-2] + 'ying'    
    
    elif word.endswith('e'): #if word ends in e return word with e removed and
                             #ing added to the end, 
                             #note this have to come after
                             #the case of excpections since those end in e
        return word[0:-1] + 'ing'
        
   
    elif word[-3] in Con and word[-2] in Vowel and word[-1] in Con: 
                                        
       return word + word[-1] + 'ing' #if word ends in consonent vowel con
                                       #return word with last letter 
                                      #doubled and ing added
       
    else:
        return word + 'ing' #most general case. If word doesn't match any of 
                            #the above cases return word with ing added
print(make_ing_form('see'))
print(make_ing_form('lie'))
print(make_ing_form('move'))
print(make_ing_form('hug')) #test cases

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
    #reduce has two arguments, function and a variable, in our case a list, and
    #returns a single argument
    #for the function argument write a lambda function that finds the max number 
    #second argument is the numbers in our list
    
    result = reduce(lambda x, y: x if x > y else y, numbers ) 
    #applies our function, which gives the max number, to our list
    
    return result #return our result 

print(max_in_list([1, 50, 150, 27]))#test case
    
    
#Problem 8: Write a function that blanks in three ways
#Using a for loop
#Using the map function
#Using list comprehensions

def listlength(word):
    """
    The function listlength(word) takes a list of words and maps it to
    a list of integers representing the lengths of the corresponding 
    words using a for loop.
    Parameters:
    
    Results:
    
    ml2016
    """
    result = [] #sets result as an empty list
    for x in word: 
        #loops through our list of words  
        l = len(x) #new variable l is the length of each word x
        result.append(l) #result.append adds l to our result list
    return result

print(listlength(['The', 'class', 'teaches', 'us', 'python'])) #test case

def listlength(wordlist):
    """
    The function listlength(word) takes a list of words and maps it to
    a list of integers representing the lengths of the corresponding 
    words using the map function
    
    Parameters: 
    wordlist - a list of words
    
    Results:
    
    
    ml2016
    """
    #use the map function to apply the length function to each word in the 
    #parameters
    #return a result as a list of these lengths
    return list(map(len,wordlist)) #maps the words to their length

print(listlength(['The', 'class', 'teaches', 'us', 'python'])) #test case   
    
def listlength(word):
    """
    The function listlength() takes a list of words and maps it to a list of 
    integers representing the lengths of the corresponding words using
    list comprehensions
    
    Parameters:
    
    Results:
    
    ml2016
    """
    #Use list comprehensions to apply the length function len() to each
    #list comprehension uses square brackets and a for statement inside(?)
    #x, or word, in our list of words
    length = [len(x) for x in word]
    return length

print(listlength(['The', 'class', 'teaches', 'us', 'python'])) #test case

    
#Problem 9: 


def find_longest_word(words):
    """
    Write a function find_longest_word that takes a list of words
    and returns the length of the longest one
    Parameters:
    
    Results:
    
    ml2016
    """
    #First use the length function to find the length of each word
    #then use map to apply len() to each word in our list
    #finally use max function to find biggest length 
   
    return max(map(len, words))
print(find_longest_word(['the', 'runner','came','in', 'eleventh']))#test case
    
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
    #filter function has two arguments a function and a list
    #filter function takes a list and returns a new list where the new list
    #is made of elements in the original list for which the function in the 
    #first argument of filter was true
    
    
    return list(filter(lambda x: len(x) > n, wordlist)) #returns a list made up
                                                        #of the elements in 
                                                        #wordlist for which 
                                                        #len(x) > n
    
print(filter_long_words(['the','runner','finished', 'in', 'second','place'], 4))
#test case

#Problem 11: Solve problem 1 again except this time use the map function
#This time, as speicified in the problem we use the map function
 

def translatemap(words):
    """
    The function translatemap uses the higher order function map to take a list
    of English words and translate them to Swedish words.
    
    Paramters:
    words - English words contained in our dictionary, words must be
    inputted in the function as a list
    
    Results:
    The Swedish word corresponding to the English word in our dictionary
    If a word is not in our dictionary function returns original word
    
    ml2016
    """
    dict2={"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", 
           "new": "nytt", "year": "ar"} #input the dictionary of english and 
                                        #swedish words

    result = map(lambda x: dict2[x], words) #applies the lambda function to
                                            #each word in the list we input
   
    return list(result) #return result as a list 

print(translatemap(['merry', 'christmas', 'and', 'happy', 'new', 'year']))


#Problem 12: Implement the higher order functions map, filter and reduce
def ourmap(func, it):
    """
    The function ourmap(func, word) implements the map function
    Parameters:
    func - a function we apply to our element
    it - an iterable, namely a list of either numbers or strings
    
    Result:
    A list 
    
    ml2016
    """
    #since map applies a function to every element in a list we want to use a 
    #for loop to implement map
    #we will apply our function func() to each x in our second parameter, word
    
    result = [] #sets our result as an empty list intially
    for x in it:
        newelm = func(x) #set a new element as our function func() acting on x
        result.append(newelm) #add newelm or func(x) to our list
    return result #return our resultant list

print(ourmap(lambda x: x-1, [6, 7, 7, 44, 21])) #test case

def ourfilter(func, iterable):
    """
    The function ourfilter(func, iterable) implements the filter function
    Parameters:
    func - a function we apply to our element
    iterable - a string, or list
    
    Result
    Returns a list where the items in the list where the ones that met the
    requirement of our function
    
    ml2016
    """
    #use an approach similar to the one used for implementing the map function
    #since filter returns a list 
    result = [] #sets our result as an empty list intially
    for x in iterable:
        if func(x) == True: #if our function is True (ask)
            result.append(x) #add x to our list
    return result #return our resultant list

print(ourfilter(lambda x: x > 2, [0, 3, 1, 30, 4])) #test case
    
def ourreduce(func, it):
    """
    The function ourreduce(func, word) implements the reduce function
    Parameters:
    func - a function we apply to our element
    it - a list or iterable of some sort
    
    Result:
    One element which met the requirements of the function in the first 
    argument
    
    ml2016
    """
    result = it[0] #sets our result as the first element in our iterator 
    for x in it[1:]: 
        #iterates through x starting with the blank position
        result = func(result, x) #makes our result the function applied to x
    return result
print(ourreduce(min,[1, 20, -4, 111, 67]))#test case
        