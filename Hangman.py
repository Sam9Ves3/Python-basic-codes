# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:37:23 2019

@author: Samuel Venegas
"""
import random
word_list = ["Awkward","Bagpipes","Banjo","Bungler","Croquet","Crypt","Dwarves","Fervid","Fishhook","Fjord","Gazebo","Gypsy","Haiku","Haphazard","Hyphen","Ivory","Jazzy","Jiffy","Jinx","Jukebox","Kayak","Kiosk","Klutz","Memento","Mystify","Numbskull","Ostracize","Oxygen","Pajama","Phlegm","Pixel","Polka","Quad","Quip","Rhythmic","Rogue","Sphinx","Squawk","Swivel","Toady","Twelfth","Unzip","Waxy","Wildebeest","Yacht","Zealous","Zigzag","Zippy","Zombie"]

#welcoming the user
name = input("Write your name: ")
print ("\nHello, " + name)
print ("Let's play hangman!\n")
print("---Instructions---")
print("»If the input string has more than one character or zero elements, the life counter will be reduce by one.")
print("»If the character is not in the alphabet, the life counter will be reduced by one.")
print("»If the word is not in the word, the life counter will be reduced by one\n")
#we chose the word
x= word_list[random.randrange(len(word_list))]
word = str(x)

#variable with an empty value
guesses = ''
lives = 5
while lives > 0:
    #counter
    failed = 0
    for char in word:
        if char in guesses:
            print (char, )
            print("Good attemp!")
        else:
            print ("*", )
            failed += 1
    if failed == 0: 
        print ("You won")
        break
    print
    # ask the user to guess a character
    guess = input("Your input is: ")
    if len(guess)>2:
        lives = 1
    guesses += guess
    # if the character is not found in the word
    if guess not in word:
        lives -= 1
        print ("Wrong!")
        print ("You have", + lives, 'more attempts' )
        if lives == 0:
            print ("Sorry, you loose! :c")
            print ("The word was:", word)


