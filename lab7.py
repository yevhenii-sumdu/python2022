import re

try:
    with open('TF14_1.txt', 'w') as f:
        f.write('line 1.23\nline 23 line 2.5\nline 17 line 12.1123 line 3.14')
except:
    print('Cannot open file')

try:
    with open('TF14_1.txt', 'r') as f1, open('TF14_2.txt', 'w') as f2:
        text = ''
        for line in f1:
            text += ' '.join(re.findall("\d+\.?\d*", line))+' '
        f2.write(text[:-1])
except:
    print('Cannot open file')

try:
    with open('TF14_2.txt', 'r') as f:
        print('Max:', max([float(i) for i in f.readline().split(' ')]))
except:
    print('Cannot open file')