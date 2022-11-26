import json
import os.path
import matplotlib.pyplot as plt

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}\n({p:.2f}%)'.format(p=pct,v=val)
    return my_autopct

def show_diagram(name):
    try:
        with open(name, 'r') as f:
            json_text = f.read()
            d = json.loads(json_text)
            
            data = [v[1] for v in d.values()]
            plt.pie(data, labels=d.keys(), autopct=make_autopct(data))
            plt.title('Magazines sold')
            plt.show()
    except:
        print('File', name, 'not found')

name = ''
while True:
    name = input('Enter file name: ')
    if os.path.isfile(name):
        break
    else:
        print('No such file')

show_diagram(name)