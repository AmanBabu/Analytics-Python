import pandas as pd

file=pd.read_csv('./output/FinalConsolidated.csv')
for i in range(0,24):
	if file['Date'][i][-2:]=='16':
		file.loc[i, 'Year']=2016
	elif file['Date'][i][-2:]=='15':
		file.loc[i, 'Year']=2015
file['Year']=file['Year'].astype(int)
del(file[file.columns[0]])
file['Bank Type']=file['Bank Type'].str.strip().str.replace('Banks','Bank')
file.to_csv('./output/FinalConsolidated_2.csv')