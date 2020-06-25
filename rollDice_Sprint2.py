# -*- coding: utf-8 -*-
"""
@author: Mava Mfihlo
"""
# Import random function will read python library random files that will allow
# us to roll dice and thus come up with random numbers 

import random

#This function will be used to pause the code in certain places as to make it seem like the dice is rolling

import time

#This function returns a boolean which is either "True" or "'False"

roll_Dice = "Yes"
roll_Dice2 = "N"

#The while loop function will return the True boolean as the dice is being roolled
# and keep on reading each line indented on the while true loop until the user press a False input

while roll_Dice == "Yes" or roll_Dice == "Y" or roll_Dice == "yes" or roll_Dice == "y" or roll_Dice == "YES":
    
    print("\nThe dice is rolling......\n")
    time.sleep(3)
    
    roll1 = random.randint (1, 6)
    roll2 = random.randint (1, 6)
    
    print("The results are : ")
    print("******************\n")
    print("Dice 1 : ", roll1, "\nDice 2 : ", roll2)
    
    if roll1 == roll2:
        print ("Wow Your rolls are equal!")
    else:
        print("\nKeep on trying!")
    roll_Dice = input("\nDo you want to roll the Dice Again? (Y/N): ")
    
    if roll_Dice2 == "N" or roll_Dice2 == "No" or roll_Dice2 == "n" or roll_Dice2 == "NO" or roll_Dice2 == "no":
        print("Thank you for playing")
    

