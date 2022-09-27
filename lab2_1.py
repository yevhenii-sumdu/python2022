from math import sqrt, sin

def get_z(x):
    if x > 45:
        return -sqrt(x)
    else:
        return sin(2*x)

def Fibonacci(p):
    if p < 2:
        print('Error: p < 2')
        return 0
    n1 = 0
    n2 = 1
    while True:
        n_ = n1+n2
        if n_ > p:
            return n_
        n1 = n2
        n2 = n_

print('Function 1')
x = int(input('Enter x: '))
print('z =', round(get_z(x), 2))

print('Function 2')
p = int(input('Enter p: '))
f = Fibonacci(p)
if f != 0:
    print('Answer:', f)