'''
This version uses a wordlist of about 21 000 words.
The file with the list is
    hangmanlist.py
and should be loaded on the same directory as hangman.py

The line
from hangmanlist import *

makes accessible the wordlist through its same name (homonym)

In this version the Player can choose to continue the game
if he guesses the word.

'''


import random
from hangmanlist import *

#  Need a function to choose only words having a specific length
def good_word(listw):
    alex = True
    while alex:
        cindy = random.randint(0, len(listw) - 1)
        chuck = listw[cindy]
        chucky = len(chuck)
        if chucky > 3:
            return chuck.strip().lower()
another = 'y'
while another == 'y':
    word = good_word(wordlist)
   #

    lista = list(word)
    # print(list)
    print("Now you should guess my word!")
    new_word = []
    for i in range(len(lista)):
        new_word.append("*")
    print(new_word)
    letters =[]
    switch = 0
    penalty = 0
    while '*' in new_word:
        print("enter a letter \n")
        letter = input()
        if letter in letters:
            switch = 0
        else:
            letters.append(letter)
            print(letters)
            for i in range(len(lista)):
                if lista[i] == letter:
                    new_word[i] = letter
                    switch = 1
                    # continue
        print(new_word, "\n")
        if switch == 0 :
            penalty +=1
            switch = 0
        print ("penalty = ", penalty, "\n")
        if penalty >= 7:
            print("You lost this time \n")
            print(word)
            quit()

        switch = 0

    print("Congrats, you got the word !")
    print(word)
    print("\n\n  Do you want to play another game y/n\t")
    another = input()
print("Thank you for playing hangman !")

quit()
