# -*- coding: utf-8 -*-
"""
@author: Mava Mfihlo
"""
# below we are importing all of the functions that were created in the CalculatorFunctions.py file

from CalculatorFunctions import*

#this function import sys from os which will allow exit or quit the program

from os import sys

# while loop will remain true as the program run until the input decide to exit

while True: 

#new variables are initialised and declared as to allow the user to input values and operators 
    
    num1 = float(input("Enter number: "))
    op = input("Enter operator:  ")
    num2 = float(input("Enter second number: " ))
    
# if statement has been created to validate the input of the user and 
#to check if correct operations and numbers format have been entered   
#variable that have been imported form the CalculatorFunctions.py files have been initialised as well as parameter below
    
    if op == "+":
        addition(num1,num2)
    
    elif op == "-":
        subtraction(num1,num2)
    
    elif op == "*":
        multiplication(num1,num2)

    elif op == "/":
        division(num1,num2) 
        
# if invalid operator other than the one initialised above have been entered the it will print the message below  
        
    else:
        print("Invalid operator")
        
#below the new delared variable will allow the user to have a choice of exiting the program if all the operation have be executed 
        
    choice = input("Press E To EXIT: ")
    if choice == "e" or choice == "E":
        print("You have EXITED")
        sys.exit(0)
        

    
    
    

