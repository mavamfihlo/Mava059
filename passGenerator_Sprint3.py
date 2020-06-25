# -*- coding: utf-8 -*-
"""
@author: Mava Mfihlo
"""
# Import random function will read python library random files that will
# come up with random numbers, characters, special characters and alphabets 

import random
# Below here are declared new variables that will be used as to define each character
upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerChars = upperChars.lower()
specialChars = "@#$%^&*!<>|?/"
numericChars = "1234567890"

# The function serves as the message class where
# message to be printed in the output is stringed and printed 

def message():
    print("Random Password Generator")
    print("-------------------------\n")
    print("Please select the length of each character")
    print("Your new random password : ", userGen())
 
# Below here is are the variables for the user input as defined for each character   

def userGen():
    upper = int(input("Amount of upper case letters: "))
    lower = int(input("Amount of lower case letters: "))
    spec = int(input("Amount of special characters: "))
    num = int(input("Amount of numbers: "))
    
# Will return the values that are being declared in the userGene() 
# and have parameter that will be used in the next function  
    
    return passwordGenerator(upper,lower,spec,num)

# Assigning the values used in the userGen into the new_password string 
# and denote parameter as the variables the user has input  

def passwordGenerator(upper,lower,spec,num):
    new_password = ""

#Use for loop as to repeat all of the characters 
#and add random chosen character to its functionable variable and randomly chose python libraries
    
    for a in range(upper):
        new_password += random.choice(upperChars)
    for b in range(lower):
        new_password += random.choice(lowerChars)
    for c in range(spec):
        new_password += random.choice(specialChars)
    for d in range(num):
        new_password += random.choice(numericChars)

#Cast a list type on to our new_password to mutate it and reshufle the list everytime the program about to read another input
    
    pass_word = list(new_password)
    shuff = random.shuffle(pass_word)
    new_pass = "".join(pass_word)
    
    return new_pass

message()
    

