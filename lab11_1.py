import pandas as pd

magazines = {'People': (10, 11000, 'USA'),
            'National Geographic': (5, 9000, 'USA'),
            'Time': (7, 8000, 'GB'),
            'Reader\'s Digest': (11, 15000, 'Australia'),
            'Cosmopolitan': (15, 20000, 'GB')
}

df = pd.DataFrame.from_dict(magazines, orient='index', columns=['Price', 'Sold', 'Country'])
print('DataFrame:')
print(df)
print('\nMean by Country:')
print(df.groupby('Country').mean())