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