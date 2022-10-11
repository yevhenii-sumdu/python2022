sentence = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt'

flag = True

for word in sentence.split(' '):
    if len(word) > 10:
        flag = False
        break

if flag:
    print('Sentence doesn\'t have words longer than 10 letters')
else:
    print('Sentence has words longer than 10 letters')