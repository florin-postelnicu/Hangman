'''
Some work on str.split([char) the words and str.strip([list of chars in a single string])
'''


word = "VerY !acssesIble?,. ?DeNail Ain't a RiVer??"
words = word.split(" ")
print(words)
list_pr = []
for i in range(0, len(words)):
   list_pr.append((words[i].strip(",.?!'")).lower())
print(list_pr)