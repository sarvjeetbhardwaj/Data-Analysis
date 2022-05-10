import pandas as pd

dataset = pd.read_csv('Data_Train.csv')

dataset['Day'] = dataset['Date_of_Journey'].str.split('/').str[0]
dataset['Month'] = dataset['Date_of_Journey'].str.split('/').str[1]
dataset['Year'] = dataset['Date_of_Journey'].str.split('/').str[2]

for temp in ['Day', 'Month', 'Year']:
    dataset[temp] = dataset[temp].astype('int')

dataset.drop(columns=['Date_of_Journey'],axis = 1, inplace= True)

dataset['Arrival_Time'] = dataset['Arrival_Time'].str.split(' ').str[0]
dataset['Arrival_Hour'] = dataset['Arrival_Time'].str.split(':').str[0]
dataset['Arrival_Minute'] = dataset['Arrival_Time'].str.split(':').str[1]

dataset['Dep_Hour'] = dataset['Dep_Time'].str.split(':').str[0]
dataset['Dep_Minute'] = dataset['Dep_Time'].str.split(':').str[1]
dataset.drop(columns = ['Dep_Time','Arrival_Time'],axis=1, inplace = True)

for temp in ['Arrival_Hour','Arrival_Minute','Dep_Hour', 'Dep_Minute']:
    dataset[temp] = dataset[temp].astype('int')

dataset['Total_Stops'] = dataset['Total_Stops'].map({'non-stop':0 , '2 stops': 2 , '1 stop': 1, '3 stops':1 , '4 stops' :4})
dataset['Total_Stops'] = dataset['Total_Stops'].fillna(1) #We are filling the missing value with '1' as 1 is the mode for total_stops
dataset['Total_Stops'] = dataset['Total_Stops'].astype('int')

dataset.drop(columns = ['Route'],axis=1, inplace = True)

dataset['Duration_hours'] = dataset['Duration'].str.split().str[0]
dataset['Duration_hours'] = dataset['Duration_hours'].str.replace('h','')
dataset['Duration_hours'] = dataset['Duration_hours'].str.replace('5m','0')
dataset['Duration_hours'] = dataset['Duration_hours'].astype('int')

dataset['Duration_Minutes'] = dataset['Duration'].str.split().str[1]
dataset['Duration_Minutes'] = dataset['Duration_Minutes'].str.replace('m','')
dataset['Duration_Minutes'] = dataset['Duration_Minutes'].fillna(0)
dataset['Duration_Minutes'] = dataset['Duration_Minutes'].astype('int')

dataset['Total_Duration_in_Mins'] = (60 * dataset['Duration_hours']) + dataset['Duration_Minutes']

df = pd.get_dummies(dataset , columns=['Airline','Source','Destination','Additional_Info'],drop_first=True)
df.drop(columns = ['Duration','Duration_hours','Duration_Minutes'],axis = 1 , inplace = True)

print(df.head(10))
print(df.info())

