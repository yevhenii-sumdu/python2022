word1 = input('Enter word1: ')
word2 = input('Enter word2: ')

letters = set(word1)
flag = True
for l in letters:
    if l not in word2:
        flag = False
        break

if flag:
    print('Word2 contains all letters from word1')
else:
    print('Word2 does not contain all letters from word1')