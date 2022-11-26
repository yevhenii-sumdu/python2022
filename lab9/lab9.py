import json
import os.path

def m_print(name):
    try:
        with open(name, 'r') as f:
            json_text = f.read()
            d = json.loads(json_text)
            
            for k, v in d.items():
                print(f'{k}: ${v[0]}, {v[1]} pc.')
    except:
        print('File', name, 'not found')

def m_add(name, k, v1, v2):
    try:
        with open(name, 'r+') as f:
            json_text = f.read()
            d = json.loads(json_text)
            
            if k not in d:
                d[k] = (v1, v2)
                new_json_text = json.dumps(d, indent=4)
                f.truncate(0)
                f.seek(0)
                f.write(new_json_text)
            else:
                print('Already exists')
    except:
        print('File', name, 'not found')

def m_del(name, k):
    try:
        with open(name, 'r+') as f:
            json_text = f.read()
            d = json.loads(json_text)
            
            if k in d:
                del d[k]
                new_json_text = json.dumps(d, indent=4)
                f.truncate(0)
                f.seek(0)
                f.write(new_json_text)
            else:
                print('Doesn\'t exist')
    except:
        print('File', name, 'not found')

def m_get(name, k):
    try:
        with open(name, 'r') as f:
            json_text = f.read()
            d = json.loads(json_text)
            
            if k in d:
                print(f'{k}: ${d[k][0]}, {d[k][1]} pc.')
            else:
                print('Not found')
    except:
        print('File', name, 'not found')

def m_find_av(name):
    try:
        with open(name, 'r') as f, open('av.json', 'w') as f2:
            json_text = f.read()
            d = json.loads(json_text)
            
            av_sum = 0
            av_count = 0
            for k in d:
                if d[k][1] < 10000:
                    av_count += 1
                    av_sum += d[k][0]

            new_json_text = json.dumps({'Average price (<10000 pc.)': av_sum/av_count}, indent=4)
            f2.write(new_json_text)
            print('Written to av.json')
    except:
        print('File', name, 'not found')

name = ''
while True:
    name = input('Enter file name: ')
    if os.path.isfile(name):
        break
    else:
        print('No such file')

print('If you want to print enter 1')
print('If you want to add enter 2')
print('If you want to delete enter 3')
print('If you want to get info about magazine enter 4')
print('If you want to find average price (<10000 pc.) enter 5')
print('If you want to change filename enter 6')
print('If you want to exit enter 7')

while True:
    num = input('Enter 1-7: ')
    if num.isdigit():
        num = int(num)
        
        if num == 1:
            m_print(name)
        elif num == 2:
            k = input('Enter name: ')
            v1 = int(input('Enter price: '))
            v2 = int(input('Enter count: '))
            m_add(name, k, v1, v2)
        elif num == 3:
            k = input('Enter name: ')
            m_del(name, k)
        elif num == 4:
            k = input('Enter name: ')
            m_get(name, k)
        elif num == 5:
            m_find_av(name)
        elif num == 6:
            while True:
                name = input('Enter file name: ')
                if os.path.isfile(name):
                    break
                else:
                    print('No such file')
        elif num == 7:
            break
        else:
            print('No such choise')
    else:
        print('Not a digit')