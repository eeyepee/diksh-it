#Read the dictionary
fh = open('C:\\Users\\ibrahim.nezar\\Desktop\\english-dict2.txt')
dict = []
while True:
    line = fh.readline()
    dict.append(line.strip())
    if not line:
        break
fh.close()

'''with open('C:\\Users\\ibrahim.nezar\\Desktop\\english-dict2.txt') as fh:
    file = fh.readlines()
    dict = set(file)'''

#Input letters
letters = input("Please enter your letters: ")
letters_set=set(letters)
#for l in letters:
#    letters_list.append(l)

mini = 2 #default value
maks = len(letters_set)
mini = input("Minimum length of the word (default is 2): ")


if mini == "":
    mini = 2 #default value

mini = int(mini)

#main functionality
newdic=[]
for words1 in dict:
    if len(words1) <= maks and len(words1)>= mini:
        newdic.append(words1)

for words2 in newdic:
    ok = 1
    for i in words2:
        if i in letters_set:
            ok = ok * 1
        else:
            ok = ok * 0

    if ok == 1:
        print(words2)
