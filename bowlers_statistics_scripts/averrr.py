# coding: utf-8
bowlers_played_c1=bowlers_played_c.groupby(['season', 'bowler'])['overall_economy'].sum().unstack().T
bowlers_played_c1['Average']=bowlers_played_c1.mean(axis=1)

bowlers_played_c1.sort('Average', ascending=False, inplace=True)
#bowlers_played_c1.to_csv('average_econ1.csv')
bowlers_played_c1.head()
bowlers_played_c2=bowlers_played_c1[bowlers_played_c1.isnull().sum(axis=1) <5]
bowlers_played_c2.sort_values('Average',ascending=False, inplace=True)
bowlers_played_c2[:5].plot(x='bowler', y='Average',kind='bar')