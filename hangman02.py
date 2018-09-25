'''
word is the word player needs to guess

new_word is the "guessed" word, as the game starts
At the beginning every missing letter is substituted by a '*'
As the game progresses , the letters that are correctly discovered are
replacing the stars'*' in the new _word
The program asks for a new letter to be guessed as long as there is at least
an asterisk left


'''

word = 'hangman' # Here you need to feed a new random word
                 # from a list of words

list = list(word)
print("Now you should guess my word!")
new_word = []
for i in range(len(list)):
    new_word.append("*")
print(new_word)
print(len(new_word))


while '*' in new_word:
    print("enter a letter\n\n")
    letter = input()
    for i in range(len(list)):
        if list[i] == letter:
            new_word[i] = letter
            continue
    print(new_word)
