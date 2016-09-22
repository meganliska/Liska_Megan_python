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
    endstr = len(String) -1  #set variable as string length minus 1
    revStr = '' #set variable as an empty string
    for char in String: #iterate through the characters, work backwords to
                     # build the reverse string
        revStr = revStr + String[endstr] #add the letters from input word 
                                         #backwords to make the reverse word
        endstr = endstr - 1
    return revStr
    
        
    
def is_palindrome(input_word):
    """
    This function is_palindrome() that recognizes
    a palindrome
    For example is_palindrome('radar') will return True
    
    Parameters:
    inputword - a string of words
    
    Results:
    Returns True if inputstring is a palindrome
    Returns False if inputstring is not a palindrome
    
    ml2016
    """
    #use this for reference in our actual function
    palindrome = False #initialize variable to false
    
    input_word = input_word.upper() #makes the word all uppercase so words can
                                    #be compared
    input_word = input_word.replace(" ", "") #gets rid of white spaces 
    
    if not input_word.isalpha(): #if the input has numbers return false
        return palindrome
    
    if reverse(input_word) == input_word: #test if input word is the same 
        palindrome = True                #forwards and backwards using 
                                          #reverse function 
                                          #returns true if input word is a
    return palindrome                     #palindrome 

def find_palindrome(ourfile):
    """
    This function find_palindrome() takes a file from the user and points the 
    line that has a palindrom/word better
    
    Parameters:
    ourfile - a file the user inputs
    
    Results:
    Function returns the line in the
    file if the line is a palindrome 
    
    """
    ourfile = input("Enter filename")
    file = open(ourfile) #opens the file the user inputs
    for line in file.read().split("\n"): #reads the file line by line without 
                                         #the n character at the end of lines
        if is_palindrome(line): #uses the palindrome function to check if the
            print(line)          #words in the line are palindromes or not and 
                                #prints the line if it is
    file.close() 
            
    
#---------------------------------------------------------------------------
#Problem 2 

"""
This program is a semordnilap
recogniser that accepts a file name 
from the user and finds and prints all pairs of words that are
semordnilaps to the screen. 
"""
#since this is not a function need to let the user know to upload a file
#otherwise when these lines of code are run they will (blank)
filename = input("Enter filename: ") #has the user upload a file 
file = open(filename)                

text = file.read().split() #read the file and split into individual words    
text = set(text) #removes duplicate elements
semordnilap_list= [] #sets our variable as an empty list the for loop will fill        

for word1 in text: #iterates through the words in the text         
        
    #for word2 in text: #iterates again through the words in the text      
    if word1[::-1] in text and word1[::-1] != word1: 
        semordnilap_list.append(word1)#if word1 is the same as word 2 (backward thing)
        
print(semordnilap_list)    
    
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
    #need to take care of the special characters 
    result = {} #sets our result as an empty dictionary.
                #the function will fill
    
    for char in text: 
    #iterate through each character in our text
        result[char] = result.get(char, 0) + 1
    keylist = list(result.keys())
    keylist.sort()
    for k in keylist :
        print(k + ': ' + str(result[k]) + '\n')
    

filename = input('Enter filename')
file = open(filename) #opens the file

text = file.read() #.split() #reads the file and splits it into lines
char_freq(text) #uses the char_freq function to make a table 
#file.close()




#----------------------------------------------------------------------------
#Problem 4
ICAOdict = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 
'y':'yankee', 'z':'zulu'} #

import os #imports the os library which gives us the say function
import time #imports the time library which gives us the functions to pause
            #between letter and words

def speak_ICAO(text, pauseletter, pauseword):
    """
    This function speak_ICAO takes a text or string and translates it into 
    spoken ICAO words with given pause time between words and letters
    
    Parameters:
    text - a string of text the user wishes to be spoken
    pauseletter - a float indicating how long to pause between letters
    pauseword - a float indicating how long to pause between words
    
    Results:
    Function returns spoken ICAO letters for the letters in text. Function will
    pause between each letter for length indicated by pauseletter and 
    between each word for length indicated by pauseword.
    
    """
    words = text.lower() #makes the words in the file all lowercase
    words = words.split() #make text lowercase and split into individual words
    for word in words:    #iterate through the words in the text
              
        for letter in word: #iterate through the letters in each word 
            if letter in ICAOdict:    #the       
                os.system("say " + ICAOdict[letter]) #says the icao letter using
                time.sleep(pauseletter)          #the os.system functions
                
                time.sleep(pauseword) #uses the imported time.sleep function 
                                      #to pause between letters and words 
speak_ICAO('My name is python',1,2) #test case
#------------------------------------------------------------------------------
#Problem 5 
import re
def hapaxfinder(filename):
    """
    The function hapaxfinder() will return all the hapaxes found in the file
    that the user inputs.
    
    Parameters:
    filepath - a file uploaded by the user
    
    Results:
    The function returns a list of hapaxes
    
    """
    #make sure to ignore capitalization (use .lower)
    #need to split file into individual letters, 
    #regular expressions will be helpful
    
    file = open(filename) #open our file
    text = file.read().lower() #we want to read the file and put it all into 
                               #lowercase words to ignore capitalization
    words = re.findall('\w+', text) #uses regular expression re.findall to
                                    #find all words in text
    freqs = {key: 0 for key in words} #makes a dictionary that will keep track
                                      #of the times each word appears
    for word in words: #loops through the word in our list of words in the text
        freqs[word] += 1 #adds 1 to the frequency dictionary
    
    for word in freqs: #loops through the words in our dictionary
        if freqs[word] == 1: #if the word only appears once. i.e has 1 for its
                            #dictionary entry then print that word as it is a 
            print(word)             #hapaxes
    

    
#----------------------------------------------------------------------------

#Problem 6
"""
This is a program that takes a text file and creates a new text file in which 
all the lines from the original file are numbered from 
1 to n
"""
filename = input('Enter a file name') #Prompts user to enter a filename
file = open(filename) 
text = file.read().splitlines() #read the file and splits it by line
file.close() 
newtext = '' #sets a new variable as an empty string the for loop will fill
for number, line in enumerate(text) : #iterate throught the lines in blank
    newline = str(number +1) + ' ' + line #makes number a string and adds it to line
                                 #why?
    newtext = newtext + newline + '\n' #adds newline to newtext variable

new_filename = input('Enter a new file name: ') #lets user name the new file
new_file = open(new_filename, 'w') #opens the new file in write mode
new_file.write(newtext) #adds newtext to our file
new_file.close() #saves the file and closes it 
    


#-----------------------------------------------------------------------------

#Problem 7
import re


def avg_word_length(filename):
    """
    The function avg_word_length takes a file and finds the average length
    of a word in the file 
    
    Parameters:
    A file that the user uploads
    
    Results:
    The average length of a word in the file (say if this is list or string
    or variable)
    
    ml2016
    """
    
    file = open(filename) #opens the input file
    text = file.read() #reads the file
    
    words = re.findall(r'\b[A-Za-z]+\b', text)
    print(words)#finds all instances of 
    avgword = sum([len(word) for word in words]) / len(words) #the average 
    #formula using the length function. The sum of the words divided by the
    #number of words in the document 
    return avgword



#Problem 8 

"""
This is a procedure which plays the guess the number game. The user guesses a
number 1 to 20 and the game tells them if the number is too high or to low.
Once the player guesses the correct number the game tells them they are right
and how many guesses it took to get them to the right number.
"""
import random #imports the random library so a random number can be generated
correctnum = random.randint(1, 20) #generates a random integer between 1 and 20
print('Hello, what is your name?') #prints this string
name = input('Enter you name: ') #prompts the user to enter their name
print("Well, %s, I am thinking of a number between 1 and 20." % name) #prints 
                                                                #this message
guess = 0   #intiates guess to 0 so the while loop will run. 0 is not in the
#range so we know the loop will run intially.                                                 
guesses = 0 #initializes variable that keeps track of the guesses to 0

while guess!= correctnum: #while guess is not correct loops through guesses
    guess = int(input('Your guess(integer): '))#prompts user to enter a guess
    if guess > correctnum: #if guess is bigger than correct interger 
        guesses = guesses + 1 #add one to the list of guesses
        print('Your guess is too high. Take a guess') #print this message
        
    elif guess < correctnum: #if guess is smaller than the correct number
        guesses = guesses + 1 #add one to the list of guesses
        print('Your guess is too low. Take a guess') #print this message
        
    elif guess == correctnum: #if guess is correct
        guesses = guesses + 1 #add one to number of guesses and print following
        #message which shows how many guess it took 
        print('Good job %s! You guessed my number in %d guesses!' % (name, guesses)) 
        
        
#Problem 10 (9 was not assigned)
#Write a program with which one can play Lingo

"""
This procedure plays the game Lingo.
Lingo is a game where there is a hidden word, 5 characters long.
The player must guess the word. For each guess the player receives two clues.
1. The characters that are fully correct, given in square brackets and 
2. The characters that are in the word but in the wrong position, given in
   parenthesis.
"""
#Need to deal with both hints 
#Use square brackets for 1.
#Use parantheses for 2.

print('Welcome to lingo!')
lingo = input('Enter the hidden word: ') #Prompts the user to enter the hidden word
                                   #since there is not a good way to generate
                                   #a random word like how there is to generate
stop = False   #initialize stop to false
                      

while stop == False: #we set up a while loop which runs as long as stop is False
    word = input('Enter a 5-letter word: ') #prompts the user to enter their guess
    char_lingo = list(lingo)  #convert lingo word and the guess word
    char_word = list(word)   #into lists of characters            
    if lingo == word:       #if the word matches with lingo, show lingo
        print('Yes, the word is : '+lingo)
        print('Congrats, you guessed it!')
        break #this breaks our while loop which we do because the game is over
   
    for i in range(len(char_word)):     # iterates through the characters in 
                                       #the range of the length of the words
       if char_word[i] == char_lingo[i]: #if the ith character in the guess 
                                         #is the same as the ith character in 
                                           #the lingo word
            hint1 = ('[',char_word[i],']') #the hint will be the character in
                                            #the ith spot in brackets
            char_word[i] = ''.join(hint1) 
            print(char_word[i]) 
       
       elif char_word[i] in lingo:  #the second condition checks for the second
                                    #hint. If the ith character is in the 
                                    #hidden word somewhere then
            hint2 = ('(',char_word[i],')') #gives the ith character in 
                                           #parenthesis
            char_word[i] = ''.join(hint2)
    clue = ''.join(char_word)
    print('Clue: ',clue) #Prints the string Clue, followed by our clue variable we
                     #made using the if/else statements.
#--------------------------------------------------------------------------

#Problem 11
""" a program that given the name of a text 
file is able to write its content with each sentence on a separate 
line.
"""


import re #we want to use regular expressions to complete this problem
def sentence_splitter(filename):
    """
    The function sentence_splitter will take the name of a text file the user
    uploads and write its contents with each sentence on a seperate line.
    
    Parameters:
    filename - a file uploaded by the user
    
    Results:
    Function will return a new file with each sentence on a seperate line
    
    """
    #Make sure to address each of the rules (say how many there are)
    #Use re.sub which was utilized in the last homework
    filename = input("Enter filename: ")    
    with open(filename, 'r') as f: #this opens the file and reads it
                                       #explain the with and as
        file_content = f.read() #sets our variable as the contents of the file
        
        #now we go through the file and deal with each of the rules given in
        #the problem 
    sentence = re.sub(r'\n', '', file_content) #first use re.sub to get rid of 
    # all instances of spaces and lines in the file. 

    sentence = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentence)
    #Use re.sub to add a new line after a period. However, do not add the new
    #line if the period is 

    sentence = re.sub(r'!\s', '!\n', sentence) #use re.sub replace ! in the 
    #the text with ! and a new line. This adds a line after !

    sentence = re.sub(r'\?\s', '?\n', sentence) #use re.sub to replace ? with
    #? and a new line. This adds a new line after ?
    print(sentence)


    

 



