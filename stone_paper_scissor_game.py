# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:19:45 2023

@author: Chirag Pujari
"""

#Jay Shree Ganeshaya Namah
#Jay Mata Di

#Game(Stone,Paper,Scissor)

import random

a=["Stone","Paper","Scissor"]
b=random.choice(a)
c=input("Enter your choice{Stone,Paper,Scissor}: ")
if(b==c):
    print("Computer choose: ",b)
    print("You choose: ",c)
    print("Result: tied")
else:
    print("Computer choose: ",b)
    print("You choose: ",c)
    if(b=="Stone" and c=="Paper"):
        print("Result: You Won !")
    if(b=="Stone" and c=="Scissor"):
        print("Result: Computer Won !")
    if(b=="Paper" and c=="Stone"):
        print("Result: Computer Won !") 
    if(b=="Paper" and c=="Scissor"):
        print("Result: You Won !")
    if(b=="Scissor" and c=="Stone"):
        print("Result: You Won !")
    if(b=="Scissor" and c=="Paper"):
        print("Result: Computer Won !")
        