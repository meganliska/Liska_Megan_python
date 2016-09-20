# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:04:36 2016

@author: meganliska
"""

#Problem 1
#Use the reference tip and create is_palindrome fucntio
#First create reverse function to use in the is_palindrome
#Use Is_palindrome in the palindrom recogniser function

def reverse(String):
    """
    This function reverse(String) takes a string and reverses
    it
    
    Parameters:
    String - a text string 
    
    Results:
    Returns the reverse of the text string String
    """
    endstr = len(String) -1  #set variable as string length minus 1?
    revStr = '' #set variable as an empty string
    for char in str: #iterate through the characters
        revStr = revStr + String[endstr] #
        endstr = endstr - 1
    return revStr
    
        
    
def is_palindrome(inputword):
    """
    This function is_palindrome() that recognizes
    a palindrome
    For example is_palindrome('radar') will return True
    
    Parameters:
    inputword - a string of words
    
    Results:
    Returns True if inputstring is a palindrome
    
    ml2016
    """
    #use this for reference in our actual function
    palindrome = False #initialize variable to false
    
    input_word = input_word.upper()
    input_word = input_word.replace(" ", "")
    
    if not input_word.isalpha: #if the input is blank return false
        return palindrome
    
    if reverse(input_word) == input_word: #test if input word is the same 
        palindrome == True                #forwards and backwards us
                                          #reutrns true if input word is a
    return palindrome                     #palindrome 

def find_palindrome(ourfile):
    """
    This function find_palindrome() takes a file from the user and points the 
    line that has a palindrom/word better
    
    Parameters:
    ourfile - a file the user inputs
    
    REsults:
    Function returns
    """
    file = open(ourfile) #opens the file the user inputs
    for line in file.read().split("\n"): #reads the file line by line without 
                                         #the n character at the end of lines
        if is_palindrome(line): #uses the palindrome function to check if the
            print(line)          #words in the line are palindromes or not and 
                                #prints the line if it is
    #file.close() 
            
    
#---------------------------------------------------------------------------
#Problem 2 

"""
This program is a semordnilap
recogniser that accepts a file name 
from the user and finds and prints all pairs of words that are
semordnilaps to the screen. 
"""
filename = input("Enter filename: ") #has the user input a file 
file = open(filename)                #puts the message on the screen 

text = file.read().split() #read the file and split into individual lines/words    

semordnilap_list= [] #sets our variable as an empty list the for loop will fill        

for word1 in text: #iterates through the words in the text         
    for word2 in text: #iterates again through the words in the text (nested loop)     
        if word1 == word2[::-1]: #if word1 is the same as word 2 (backward thing)
            print(word1, word2)  #returns both words as a pair   
    
file.close() #closes file

#---------------------------------------------------------------------------
#Problem 3
#use the function we made in HW one as it gives a frequency table for a string

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
    result = {} #sets our result as an empty dictionary.
                #the function will fill
    
    for char in text: 
    #iterate through each character in our text
        result[char] = result.get(char, 0) + 1
    return result 


file = open(filename) #opens the file

text = file.read.split() #reads the file and splits it into blanl
char_freq(text) #uses the char_freq function to make a table 
#close file?

#----------------------------------------------------------------------------
#Problem 4
ICAOdict = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 
'y':'yankee', 'z':'zulu'} #

import os #imports the os things
import time #imports the time things (find specific word for these)

def speak_ICAO(text, pauseletter, pauseword):
    """
    This function speak_ICAO takes a text or string and translates it into 
    spoken ICAO words with given pause time between words and letters
    
    Parameters:
    
    Results:
    
    """
    words = text.lower()
    words = words.split() #make text lowercase and split the text
    for word in words:    #into individual words
              
        for letter in word:      #nest for loop to check for the letters in 
            if letter in ICAOdict:          
                os.system("say " + ICAOdict[letter]) #says the icao letter using
                time.sleep(pauseletter)          #the os.system functions
                
                time.sleep(pauseword) #uses the imported time.sleep function to pause between
                      #letters and words 
#------------------------------------------------------------------------------
#Problem 5 
import re
def hapaxfinder(filepath):
    """
    The function hapaxfinder() will return all the hapaxes found in the file
    that the user inputs.
    
    Parameters:
    filepath - a file uploaded by the user
    
    Results:
    The function returnsa list of hapaxes
    
    """
    #make sure to ignore capitalization (use .lower)
    #need to split file into somethings, regular expressions will be helpful

    file = open(filepath) #open our file
    text = file.read().lower() #we want to read the file and put it all into 
                               #lowercase words to ignore capitalization
    words = re.findall('\w+', text) #uses regular expression re.findall to
                                    #find all words in text
    freqs = {key: 0 for key in words} 
    
    for word in words:
        freqs[word] += 1
    
    for word in freqs:
        if freqs[word] == 1:
        
    print(word)
    

    
#----------------------------------------------------------------------------

#Problem 6
#Write a program that given a text file will create a new text file in which 
#all the lines from the original file are numbered from 
#1 to n
file = open(filename)
text = file.read.split()


#-----------------------------------------------------------------------------

#Problem 7
import re


def avg_word_length(filepath):
    """
    The function avg_word_length takes a file and 
    Parameters:
    
    Results:
    
    ml2016
    """
    file = open(filepath)
    text = file.read().split()
    
    words = re.findall('\w+', file.read())
    avgword = sum([len(word) for word in words]) / len(words)
    return avgword

#Ask him tomorrow how to do this without the regular expressions

#Problem 8 
#Guess the number game
import random
correctnum = random.randint(1, 20)
print('Hello, what is your name?')
name = input('Enter you name: ')
print("Well, %s, I am thinking of a number between 1 and 20.") % name



guesses = 0 #not 1?

while guess!= correctnum:
    guess = int(input('Your guess(integer): '))
    if guess > correctnum:
        guesses = guesses + 1
        print('Your guess is too high. Take a guess')
        
    elif guess < correctnum:
        guesses = guesses + 1
        print('Your guess is too low. Take a guess')
        
    elif guess == correctnum:
        guesses = guesses + 1
        print('Good job %s! You guessed my number in %d guesses!') % name % guesses 
        
        





#Problem 10 (9 was not assigned)

#Problem 11

 



