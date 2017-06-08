import glob
import pandas as pd
import re
path=r'D:\aman\testPython\PMJDY'
allFiles=glob.glob(path + "/*.csv")
columns=['Bank Type','Rural','Urban','No of A/c','No of Rupay Debit Card','Balance of Accounts(In Crores)', 'No of A/c with Zero Balance', 'Aadhaar Seeding']
check=['Balance of Accounts(In Lacs)', 'Balance of Accounts (in Lacs)' ]
frame=pd.DataFrame()
list=[]

for files in allFiles:
	date= files.split('_')[1]  # only for filename as PMJDY_30Mar15.csv
	date1=date.split('.')[0]
	month=re.search('([A-Za-z]+)', date1)
	if month and month.group():
		month=month.group()
		file=pd.read_csv(files)
		if file.columns[5] in check:
				file[file.columns[5]] = file[file.columns[5]]*0.01
		file.columns=columns
		file['Month']=month
		file['Date']=date1
		file=file[file['Bank Type'] != 'Grand Total']
		list.append(file)
frame=pd.concat(list,ignore_index=True)
frame.to_csv('./output/FinalConsolidated.csv')
	