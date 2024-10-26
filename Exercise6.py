# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:26:22 2024

@author: USER
"""

CorrectPassword="Yoimiya"
password= ""

while password != CorrectPassword:
    password=input("Enter password: ")
    if password != CorrectPassword:
        print("Incorrect password")
    else:
        print("Correct password")