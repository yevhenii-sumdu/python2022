import csv

print('Life expectancy in all countries in 2015')

try:
    with open(r'Data.csv', newline='') as File: 
        reader = csv.reader(File)
        for row in reader:
            if row[0] == 'Life expectancy at birth, total (years)':
                try:
                    print(f'{row[2]}: {round(float(row[19]), 2)}')
                except:
                    pass
except:
    print('Cannot open file')

try:     
    countries = input('Enter countries to search: ').split(', ')
    with open(r'Data.csv', newline='') as inFile, open('Result.csv', 'w', newline='') as outFile: 
        reader = csv.reader(inFile)
        writer = csv.writer(outFile)
        for row in reader:
            if row[0] == 'Life expectancy at birth, total (years)':
                if row[2] in countries:
                    print(f'{row[2]}: {round(float(row[19]), 2)}')
                    writer.writerow([row[2], round(float(row[19]), 2)])
except:
    print('Cannot open file')