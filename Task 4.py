# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:55:01 2023

@author: Yashita
"""

# Task 4
# Write a Python Program for Fibonacci numbers.

x = int(input("Enter number: "))
a = 0
b = 1 
sum = 0
c = 1
print("Fibonacci series is: ", end=" ")
while c<=x:
    c = c+1
    print(a, end=" ")
    a = b
    b = sum
    sum = a + b
    
    








































