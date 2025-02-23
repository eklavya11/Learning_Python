import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"],index=["X","Y","Z"])
print(df)

print(df.head())#gives all rows
print(df.head(2))#gives first 2 rows
print(df.tail(1))#gives last 1 row
print(df.columns)

print(df.index.to_list())
print(df.info())
print(df.describe())
print(df.nunique())
print(df['A'].unique())
print(df.shape)