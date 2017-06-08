# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
f2=pd.read_csv('./output/FinalConsolidated.csv')
f2.head()
del(f2[f2.columns[0]])
f2
data_agg_month=f2.groupby('Date')['Bank Type','Rural', 'Urban', 'No of A/c', 'No of Rupay Debit Card', 'No of A/c with Zero Balance','Aadhaar Seeding'].sum()
data_agg_month.plot(kind='bar', title='Monthly wise stats of PMJDY 2015-16')
plt.xlabel('Dates')
plt.show()
