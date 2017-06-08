# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
get_ipython().magic(u'matplotlib tk')
deliveries=pd.read_csv('deliveries_raw.csv')
bowler_grp=deliveries.groupby(['match_id', 'inning', 'bowling_team', 'over', 'bowler'])
bowlers = bowler_grp['total_runs','wide_runs', 'bye_runs', 'legbye_runs', 'noball_runs'].sum().reset_index()
total_matches = bowlers.groupby('match_id').count()
total_matches = total_matches.shape[0]

ipl_matches=pd.DataFrame(columns=['match_id','inning','bowling_team', 'over', 'bowler','total_runs','wide_runs', 'bye_runs', 'legbye_runs', 'noball_runs'], index=[x for x in range(1, 578)])

last_3oversData1= []
for match in range(1, total_matches+1):
    for inning in range(1,3):
        ipl_matches=bowlers.loc[(bowlers['match_id']==match)& (bowlers['inning']==inning)]
        if(len(ipl_matches) > 0):
            last_3overs=ipl_matches['over'].max()-3
            ipl_matches=ipl_matches.iloc[last_3overs:]
            last_3oversData1.append(ipl_matches)
            last_3overs_total_matches1=pd.concat(last_3oversData1)
            

last_3overs_total_matches_a=last_3overs_total_matches1.reset_index(drop=True)