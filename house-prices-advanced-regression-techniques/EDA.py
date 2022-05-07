import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#pd.pandas.set_options('display.max_columns', None) to be used only in Jypyter notebook

dataset = pd.read_csv('train.csv')

#print(dataset.head()) # printing first 5 rows of the data

#print(dataset.shape) # getting the shape of the dataset , no_of rows & columns

#print(dataset.isnull().sum()) # getting the number if mising values in each columns

#getting the names of columns where there are more than 1 or more missing values and storing in features list
features_with_nan = []
for f in dataset.columns:
    if dataset[f].isnull().sum()>=1:
        features_with_nan.append(f)
#print(features_with_nan)

#getting the percentage of missing values in features in features with nan
#for feature in features_with_nan:
#    print(feature, np.round(dataset[feature].isnull().mean(),4)*100, '% missing values')

#In order to fill missing values we need to check the relationship between independent and dependent variable

data=dataset.copy()
for feature in features_with_nan:
    # Lets make a variable that indicate 1 if the observation was missing and 0 otherwise
    data[feature] = np.where(data[feature].isnull(),1,0)

    #Lets calculate the median sales pricee where data is missing 
    #data.groupby(feature)['SalePrice'].median().plot.bar() # sales price is the dependent column
    #plt.title(feature)
    #plt.show()

###### Numerical variables
num_features = []
for f in dataset.columns:
    if dataset[f].dtype != 'object':
        num_features.append(f)

#print(dataset[num_features].head())

######## temporal variables (eg datetime variables)
year_feature = []
for feature in num_features:
    if 'Yr' in feature or 'Year' in feature:
        year_feature.append(feature)

#print(year_feature)

#getting the unique value in temporal columns 
#for f in year_feature:
#    print(f,dataset[f].unique())

#gb=dataset.groupby('YrSold')
#print(gb.agg(['sum','median'])['SalePrice'])

#plotting the price of the house with the year sold
#dataset.groupby('YrSold')['SalePrice'].median().plot()
#plt.xlabel('Year Sold')
#plt.ylabel('Median House Price')
#plt.title('House price vs year sold')
#plt.show()

#plotting the age of the house with sales price

data = dataset.copy()
for feature in year_feature:
    if feature != 'YrSold':
        data[feature] = data['YrSold'] - data[feature]

        #sns.scatterplot(data = data , x = feature , y = 'SalePrice')
        #plt.show()


