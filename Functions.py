# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:57:59 2020

@author: Mava Mfihlo
"""
# below are the new declared functions that will perform the additions, subtraction, multiplication
#that will be enter by the user. It will also show on the output how the two number where perfomed and show the results 
# as to display the out of the calculated numbers. 
def addition(num1,num2):
    results = num1 + num2
    print("{0} + {1} = {2}".format(num1,num2,results))

def subtraction(num1,num2):
    results = num1 - num2
    print("{0} - {1} = {2}".format(num1,num2,results))

def multiplication(num1,num2):
    results = num1 * num2
    print("{0} * {1} = {2}".format(num1,num2,results))

def division(num1,num2):
# an if statement have been performed to check if the second number that have been entered is equal to zero
# division by zero can not be executed, so the program will print the below message.    
    if num2 == 0.0:
        print("Can not do division by zero !")
    else:
        results = num1 / num2
        print("{0} / {1} = {2}".format(num1,num2,results))        