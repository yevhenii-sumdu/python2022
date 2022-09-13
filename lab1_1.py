a = int(input('Enter a: '))
if not (a >=1 and a <= 100):
    print('Incorrect input')
    exit()

b = int(input('Enter b: '))
if not (b >=1 and b <= 100):
    print('Incorrect input')
    exit()

if a > b:
    X = 2*a + b
elif a == b:
    X = -2
else:
    X = (a - 5)/b

print(f'X = {round(X, 2)}')