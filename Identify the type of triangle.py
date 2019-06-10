2
2# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:19:55 2019

@author: Samuel Venegas
"""
def main():
    a = input("Enter the first side of the triangle: ")
    b = input("Enter the second side of the triangle: ")
    c = input("Enter the third side of the triangle: ")
    if a==b and b==c:
        print ("The triangle es equilateral")
    elif (a==b or a==c or b==c):
        print ("The triangle is isosceles")
    else:
        print ("The triangle is scalene")
                    
main()