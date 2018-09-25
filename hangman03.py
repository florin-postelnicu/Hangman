'''
Using a SWITCH to mark whether the letter guessed
is ,or not part of the word.
penalty counts the number of "wrong" letters


'''

word = 'hangman' # Here you need to feed a new random word
                 # from a list of words

list = list(word)
print("Now you should guess my word!")
new_word = []
for i in range(len(list)):
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
        for i in range(len(list)):
            if list[i] == letter:
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
