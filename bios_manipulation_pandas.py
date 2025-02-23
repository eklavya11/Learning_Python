import pandas as pd
bios = pd.read_csv('./data/bios.csv')

print(bios.head())

bios_new = bios.copy()
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
print(bios_new)

print(bios_new.query('first_name=="Keith"'))

bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])

print(bios_new.head())

print(bios_new[["born_date","born_datetime"]])

bios_new['born_year']=bios_new['born_datetime'].dt.year
print(bios_new.head())

#to save data as csv after cleaning and adding column

bios_new.to_csv('./data/bios_new.csv',index=False)#index false to not get that index columnn

bios['height_category']=bios['height_cm'].apply(lambda x: 'Short' if x<165 else('Average' if x<185 else 'Tall'))

print(bios['height_category'].head())


def categorize_athelete(row):
    if(row['height_cm']<175 and row['weight_kg']<70):
        return 'Lightweight'
    elif row['height_cm']<185 or row['weight_kg']<80:
        return 'Middleweight'
    else:
        return 'Heavyweight'
    

bios['Category'] = bios.apply(categorize_athelete,axis=1)# axis - 1 is row, 0 is column
print(bios.head())
