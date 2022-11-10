def printMagazines(m):
    for k, v in m.items():
        print(f'{k}: ${v[0]}, {v[1]} pc.')

def printMagazinesSorted(m):
    for k in sorted(m):
        print(f'{k}: ${m[k][0]}, {m[k][1]} pc.')

def addMagazine(name, price, count, m):
    if name not in m:
        m[name] = (price, count)
    else:
        print('Already exists')

def delMagaxine(name, m):
    if name in m:
        del m[name]
    else:
        print('Doesn\'t exist')


magazines = {'People': (10, 11000),
            'National Geographic': (5, 9000),
            'Time': (7, 8000),
            'Reader\'s Digest': (11, 15000),
            'Cosmopolitan': (15, 20000)
}

printMagazines(magazines)
print('-'*20)
addMagazine('Vogue', 12, 7000, magazines)
delMagaxine('People', magazines)
printMagazines(magazines)
print('-'*20)
print('Sorted:')
printMagazinesSorted(magazines)

av_sum = 0
av_count = 0
for k in magazines:
    if magazines[k][1] < 10000:
        av_count += 1
        av_sum += magazines[k][0]

print('-'*20)
print('Average price (<10000 pc.):', av_sum/av_count)