N = int(input('Enter N: '))

lst = [int(el) for el in input('Enter the list: ').split()]

s = 0
for l in lst:
    if l%2 == 0 and l >= 0:
        s += l

print('Sum =', s)