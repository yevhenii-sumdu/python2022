import csv
import matplotlib.pyplot as plt

try:
    with open(r'520e2a96-f025-4b88-bb8e-c0387f0c3178_Data.csv', newline='') as File: 
        reader = csv.DictReader(File)
        years = range(2002, 2017)
        ukraine = []
        usa = []
        for row in reader:
            if row['Country Name'] == 'Ukraine':
                ukraine = [float(row[f'{i} [YR{i}]']) for i in years]
            elif row['Country Name'] == 'United States':
                usa = [float(row[f'{i} [YR{i}]']) for i in years]

        plt.plot(years, ukraine, 'b-', label='Ukraine')
        plt.plot(years, usa, 'g-', label='USA')
        plt.axis([2002, 2016, 0, 100])
        plt.xlabel('Year')
        plt.ylabel('% of adults')
        plt.legend()
        plt.title('Prevalence of overweight')

        plt.show()

except:
    print('Cannot open file')