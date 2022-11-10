def func(lst):
    max_f = 0
    num = 0
    for i in [1,2,3,4,5,6,7,8,9,0]:
        frequency = lst.count(i)
        if frequency > max_f:
            max_f = frequency
            num = i

    return num

print(func([1,2,3,4,2,1,5,6,2]))