'''
The chosen text is not always split in individual words.
In some situations , two wodrs appear as a single one,
and that it happens, when the respective words are on two diffwrent consecutive rows.
like in example:
   wolf
   met

It has to be related to the type of file and its format.
Most likely  using json files  the problem would be eliminated.

'''

import random
import urllib.request  # the library that handles the url

#  Need a function to choose only words having a specific length
def good_word(listw):
    alex = True
    while alex:
        cindy = random.randint(0, len(listw) - 1)
        chuck = listw[cindy].strip("             ")
        chucky = len(chuck)
        if (5 < chucky) and (chucky < 10):
            return chuck.strip(".").lower()


index = random.randint(1, 209)
data = urllib.request.urlopen("https://www.cs.cmu.edu/~spok/grimmtmp/{:003d}.txt".format(index)).read()
data = data.decode("utf-8")
f = open("NewFile", "w")
f.write(data)
f.close()

f = open("NewFile", "r")
text1 = f.read()
words = text1.rstrip("  ").strip(",!?.").lstrip(",").rsplit(" ")
f.close()

word = good_word(words).strip(",")
print(word)

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
                continue
    print(new_word, "\n")
    if switch == 0 :
        penalty +=1
        switch = 0
    print ("penalty = ", penalty, "\n")
    if penalty >= 7:
        print("You lost this time \n")

    switch = 0

quit()
