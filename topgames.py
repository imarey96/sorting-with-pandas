import pandas as pd

df = pd.read_csv('Video_Games.csv')
print (df.head())

df1 = df[df['Genre'] =='Sports']
print(df1.head())

df1.to_csv('Sports_games.csv')

df2 = pd.read_csv('Sports_games.csv')
df1.equals(df2)

comparisondf = df1.values == df2.values
print(comparisondf)