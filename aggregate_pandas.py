import pandas as pd

bios = pd.read_csv('./data/bios.csv')
coffee = pd.read_csv('./warmup-data/coffee.csv')

print(bios.head())

print(bios['born_city'].value_counts())
print(bios[bios['born_country']=='USA']['born_region'].value_counts())
import numpy as np
coffee['price']= np.where(coffee['Coffee Type']=='Espresso',3.99,5.99)
coffee['revenue']=coffee['price']*coffee['Units Sold']
#group by
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())
#avg
print(coffee.groupby(['Coffee Type'])['Units Sold'].mean())
print(coffee.groupby(['Coffee Type']).agg({'Units Sold':'sum','price':'mean'}))
print(coffee.groupby(['Coffee Type','Day'])['Units Sold'].sum())


#pivoting table

pivot  = coffee.pivot(columns='Coffee Type', index = 'Day',values='revenue')

print(pivot)

print(pivot.loc['Monday','Latte'])

print(pivot.sum())
print(pivot.sum(axis=1))

bios['born_date'] = pd.to_datetime(bios['born_date'])
print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index().sort_values('name',ascending=False))
#print(bios.info())



#Advance funcionality

print(coffee.head())

coffee['yesterday revenue']=coffee['revenue'].shift(2)
coffee['pct_change']=coffee['revenue']/coffee['yesterday revenue']*100
print(coffee.head())

bios['height_rank']=bios['height_cm'].rank(ascending=False)#as we want tallest person to have rank 1
print(bios[['height_cm','height_rank']].sort_values(['height_rank']))


coffee['cumulative_revenue'] = coffee['revenue'].cumsum()
print(coffee.head())

latte = coffee[coffee['Coffee Type']=="Latte"].copy()


latte['3day']=latte['Units Sold'].rolling(3).sum()
print(latte)


