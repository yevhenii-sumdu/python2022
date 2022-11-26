import csv
import matplotlib.pyplot as plt
import numpy

try:
    with open(r'520e2a96-f025-4b88-bb8e-c0387f0c3178_Data.csv', newline='') as File: 
        reader = csv.DictReader(File)
        while True:
            c = ''
            years = range(2002, 2017)
            data = []
            while True:
                c = input('Enter Country: ')
                for row in reader:
                    if row['Country Name'] == c:
                        data = [float(row[f'{i} [YR{i}]']) for i in years]
                        break

                if len(data) == 0:
                    print('No such Country')
                    File.seek(0)
                else:
                    break

            plt.bar(years, data, width=0.8, color=numpy.random.rand(3,), label=c)
            plt.ylim([0,100])
            plt.xlabel('Year')
            plt.ylabel('% of adults')
            plt.legend()
            plt.title('Prevalence of overweight')

            plt.show()
            File.seek(0)

except:
    print('Cannot open file')