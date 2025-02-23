import pandas as pd
import numpy as np

coffee = pd.read_csv('coffee.csv')
coffee['price'] = np.where(coffee['Coffee Type']=='Espresso',3.99,5.99)
coffee['revenue'] = coffee['price']*coffee['Units Sold']
coffee.loc[[0,1],'Units Sold'] = 15
coffee.loc[[2,3],'Units Sold'] = np.nan


print(coffee.isna().sum())# checks count of null values

#to remove null values

#coffee.fillna(coffee['Units Sold'].mean(),inplace=True)#fills null values with mean value of the column
coffee['Units Sold']=coffee['Units Sold'].interpolate()
print(coffee.head())

#to drop null values

coffee = coffee.dropna(subset=['Units Sold'])


print(coffee[coffee['Units Sold'].isna()])
print(coffee[coffee['Units Sold'].notna()])




