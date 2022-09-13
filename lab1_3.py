N = int(input('Enter N: '))

if not (N >=1 and N <= 9):
    print('Incorrect input')
    exit()

for i in range(1, N+1):
    print((N-i)*'  ', end=' ')
    j = N
    for _ in range(0, i):
        print(j, end=' ')
        j -= 1
    print('')