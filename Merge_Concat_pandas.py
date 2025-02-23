import pandas as pd
bios = pd.read_csv('./data/bios.csv')
nocs = pd.read_csv('./data/noc_regions.csv')
results = pd.read_parquet('./data/results.parquet')

print(nocs.head())

bios_new = pd.merge(bios,nocs,left_on='born_country',right_on='NOC',how='left') # how is like type of join, here we are using left join

print(bios_new)

bios_new.rename(columns={'region':'born_country_full'},inplace=True)#renaming column


print(bios_new['born_country_full'])


print(bios_new[bios_new['NOC_x']!=bios_new['born_country_full']][['name','NOC_x','born_country_full']]) #comparing


usa = bios[bios['born_country']=='USA'].copy()
gbr = bios[bios['born_country']=='GBR'].copy()

new_df = pd.concat([usa,gbr])#puts one on top of another
print(new_df.head())


combined_df = pd.merge(results,bios,on='athlete_id',how='left')
print(combined_df.head())