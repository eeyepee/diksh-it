##Read the dictionary
fh = open('C:\\english-dict.txt')
dict = []
while True:
    line = fh.readline()
    dict.append(line.strip())
    if not line:
        break
fh.close()

#Enter letters to use when compile a list of words
letters = input("Please enter your letters: ")
letters_set=set(letters)

mini = input("Minimum length of the word (default is 2): ")
maks = int(input("Maximum length of the word (default is length of the input letters): "))

if mini == "":
    mini = 2 # this will be the default minimum value of words length

mini = int(mini)

newdic=[]
for words1 in dict:
    if len(words1) <= maks and len(words1)>= mini:
        newdic.append(words1)

for words in newdic:
    ok = 1
    for i in words:
        if i in letters_set:
            ok = ok * 1
        else:
            ok = ok * 0

    if ok == 1:
        print(words)
