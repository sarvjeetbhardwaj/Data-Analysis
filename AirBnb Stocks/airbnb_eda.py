import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Airbnb.csv')

#print(df.info())

#print(df.isnull().sum())

df['Date'] = pd.to_datetime(df['Date'])
df = df.drop(columns = ['Volume'])

#dfm = df.melt('Date',var_name='Features',value_name='Values')

dfg = df.groupby(pd.Grouper(key='Date',axis = 0 , freq = 'M')).median()
dfg=dfg.reset_index()
dfg = dfg.drop(columns = ['Adj Close'])
dfg['Date'] = dfg['Date'].astype('str')
dfg['Date'] = dfg['Date'].astype('str')

dfg['Year'] = dfg['Date'].str.split('-').str[0]
dfg['Month'] = dfg['Date'].str.split('-').str[1]
#dfg = dfg.drop(columns = ['Adj Close'])

dfg['Month'] = dfg['Month'].map({'12':'Dec','01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'June',
                                 '07':'July','08':'Aug','09':'Sep','10':'Oct','11':'Nov'})

dfg['Month-Year'] = dfg['Month'] + '-' + dfg['Year']
dfg = dfg.drop(columns = ['Date','Year','Month'])

dfm = dfg.melt('Month-Year',var_name='Features',value_name='Values')

sns.catplot(data = dfm , x = 'Month-Year' , y = 'Values' , hue = 'Features' , kind = 'point')
plt.xticks(rotation = 90)
plt.show()


print(dfm)