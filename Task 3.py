# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:28:18 2023

@author: Yashita
"""

# Task 3
# Write a Python program to print all positive numbers in a range.

list=[]
x = int(input("Enter list size: "))
for i in range(0,x):
    y = int(input("Enter element: "))
    list.append(y)
    
print("Positive numbers are: ")
for i in list:
    if i>=0:
        print(i, end=" ")
        
     
    
    
    



















































