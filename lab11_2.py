import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5) 

df = pd.read_csv('comptagevelo2009.csv', parse_dates=['Date'], dayfirst=True)


month_df = df.groupby(df['Date'].dt.strftime('%B'))[['Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brebeuf']].sum()
print('Most popular month is', month_df.sum(axis=1).idxmax())


months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

Berri1_df = df.groupby(df['Date'].dt.strftime('%B'))['Berri1'].sum().sort_index(key = lambda x : pd.Categorical(x, categories=months, ordered=True))
Berri1_df.plot(figsize=(15, 10))
plt.xlabel('Month')
plt.ylabel('Cyclers')
plt.title('Amount of cyclers on Berri1')
plt.show()


august_df = df[df['Date'].dt.month == 8]
day_df = august_df.groupby(df['Date'].dt.strftime('%A'))[['Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brebeuf']].sum()
print('Most popular day in August is', day_df.sum(axis=1).idxmax())