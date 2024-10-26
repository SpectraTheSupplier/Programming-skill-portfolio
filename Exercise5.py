# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:07:22 2024

@author: USER
"""

months = {1: 31,
          2: 28,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31,}

Day= int(input("Enter a month: "))
if Day < 13:
    print(months[Day])
else:
    print("Number is not a month")
