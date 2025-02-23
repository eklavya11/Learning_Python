import pandas as pd

coffee = pd.read_csv('coffee.csv')

print(coffee.head()) #gives first 5 rows
print(coffee)

results = pd.read_parquet('./data/results.parquet')

print(results.head())

#excel file takes longer time to load, parquet files works fast

#olympics_data = pd.read_excel('./data/olympics-data.xlsx',sheet_name="results") #takes long time
#print(olympics_data.head())

bios = pd.read_csv('./data/bios.csv')

print(coffee)

print(coffee.sample(10, random_state=1))

#to access rows or cplumns loc and iloc

print(coffee.loc[[0,1,2]])
print(coffee.loc[5:12,["Day","Units Sold"]])
print(coffee.iloc[:,[0,2]])


#coffee.index = coffee["Day"] to set a column as index 

#to change value
coffee.loc[1:3,"Units Sold"]=10 

coffee.at[0,"Units Sold"] #for specific values and cant use for multiple values
coffee.iat[0,2] #for specific values

coffee["Day"]
coffee.Day # for columns with single word

print(coffee.sort_values("Units Sold"))#sorting based on column
print(coffee.sort_values("Units Sold",ascending=False)) # for descending
print(coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1])) # 0,1 for first column descending anf 2nd column ascending

#iterating - not mainly pandas syntax
for index, row in coffee.iterrows():
    print(index)
    print(row["Units Sold"])
    print("\n\n")