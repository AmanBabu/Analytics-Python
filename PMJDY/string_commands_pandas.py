# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
f2=pd.read_csv('./output/FinalConsolidated_1.csv')
f2.head()
f2.drop(f2[f2.columns[0]])
f2.head()
del(f2[f2.columns[0]])
f2.head()
f2[f2.columns[0]]
f2[f2.columns[0]][0][-2:]
f2[f2.columns[0]][0][:]
f2[f2.columns[0]][0]
f2[f2.columns[0]][0].str.contains('Banks')
f2[f2.columns[0].str.contains('Banks')]
f2[f2['Bank Type'].str.contains('Banks')]
f2['Bank Type']=f2['Bank Type'].replace('Banks','Bank')
f2.head()
f2[f2['Bank Type'].str.contains('Banks')]
f2[f2['Bank Type'].str.contains('Banks')].count()
f2[f2['Bank Type'].str.contains('Banks')]['id'].count()
f2[f2['Bank Type'].str.contains('Banks')]['Year'].count()
f2[f2['Bank Type'].str.split().str[-1]]
f2['Bank Type'].str.split().str[-1]
convertbankstobank=f2['Bank Type'].str.split().str[-1]
convertbankstobank
convertbankstobank['lastword']=f2['Bank Type'].str.split().str[-1]
convertbankstobank
convertbankstobank['lastword']
convertbankstobank['lastword']=convertbankstobank['lastword'].replace('Banks', 'Bank')
convertbankstobank['lastword']
f2['Bank Type']
f2[f2['Bank Type'].str.contains('Banks')]
f2['Bank Type']=f2['Bank Type'].str.split().str[-1].replace('Banks','Bank')
f2['Bank Type']
f2
f2=pd.read_csv('./output/FinalConsolidated_1.csv')
f2.head()
del(f2[f2.columns[0]])
f2['Bank Type'].str.split().str[-1].replace('Banks','Bank')
f2.head()
f2[f2['Bank Type'][0].str.contains('Banks')].count()
f2[f2['Bank Type'].str.contains('Banks')]
f2[f2['Bank Type'][2].str.contains('Banks')]
f2[f2['Bank Type'].str.contains('Banks')].index
f2['Bank Type'].str.split().str[-1]
f2['Bank Type'].str.split().str[-1:]
f2['Bank Type'].str.split().str[-1]
f2['Bank Type'].str.strip().str.replace('Banks','Bank')
get_ipython().magic(u'save string_commands_pandas')
