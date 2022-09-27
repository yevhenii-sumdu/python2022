from mod import Fibonacci

p = int(input('Enter p: '))
f = Fibonacci(p)
if f != 0:
    print('Answer:', f)