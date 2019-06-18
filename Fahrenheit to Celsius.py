# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:36:53 2019

@author: Samuel Venegas
"""

#Program to convert Fahrenheit to Celsius
def main():
    a = eval(input("Write the degress in Fahrenheit: " ))
    d = (a - 32)*(5/9)
    print("The degrees in Celsius is: {0:.2f} ".format(d))
main()