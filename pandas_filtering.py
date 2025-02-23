import pandas as pd

bios = pd.read_csv('./data/bios.csv')

print(bios.head())

print(bios.info())

#below 2 does same job
print(bios.loc[bios['height_cm']>215,["name",'height_cm']])

print(bios[bios['height_cm']>215][['name','height_cm']])

print(bios[(bios['height_cm']>215) & (bios['born_country']=='USA')][['name','height_cm','born_country']])

print(bios[bios['name'].str.contains('Keith')][["name"]])

print(bios[bios['name'].str.contains("keith|patrick",case=False)])#case doesnt matter in this in dataframe, checking for both keith and patrick

print(bios[bios['born_country'].isin(["USA","FRA"])&(bios['name'].str.startswith("Keith"))][["name","born_country"]])


print(bios.query('born_country=="USA" and born_city =="Seattle"'))





