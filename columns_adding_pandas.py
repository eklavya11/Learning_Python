import pandas as pd

coffee = pd.read_csv('coffee.csv')
coffee_new = coffee.copy()
coffee_new['price']=4.99

print(coffee)

#Adding new column 

coffee['price']=4.99

print(coffee)
import numpy as np

coffee['new price'] = np.where(coffee['Coffee Type']=='Espress',3.99,5.99)

print(coffee)

#removing column
coffee.drop(columns=['price'],inplace=True)
print(coffee)

print(coffee_new)

coffee['revenue']=coffee['Units Sold']*coffee['new price']
print(coffee)

coffee.rename(columns={'new price':'price'},inplace=True)
print(coffee)



