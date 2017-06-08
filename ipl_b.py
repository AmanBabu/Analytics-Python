import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
matches=pd.read_csv('./IPL_Dataset/matches.csv')
matches['type'] ='pre-qualifier'
for year in range(2008, 2017):
   print matches[matches['season']==year][-1:].index.values[0]
   
    
for year in range(2008, 2017):
   print matches[matches['season']==year][-1:].index
   
for year in range(2008, 2017):
   final_match_index=matches[matches['season']==year][-1:].index.values[0]
   matches = matches.set_value(final_match_index, 'type', 'final')
   matches = matches.set_value(final_match_index-1, 'type', 'qualifier-2')
   matches = matches.set_value(final_match_index-2, 'type', 'eliminator')
   matches = matches.set_value(final_match_index-3, 'type', 'qualifier-1')
   
matches.groupby(['type'])['id'].count()
deliveries=pd.read_csv('./IPL_Dataset/deliveries.csv')
deliveries.head(2)
deliveries.shape
team_score = deliveries.groupby(['match_id','inning'])['total_runs']
team_score
print team_score
team_score = deliveries.groupby(['match_id','inning'])['total_runs'].sum()
print team_score
team_score = deliveries.groupby(['match_id','inning'])['total_runs'].sum().unstack()
print team_score
team_score = deliveries.groupby(['match_id','inning'])['total_runs'].sum().unstack().reset_index()
print team_score
team_score.columns=['match_id','Team1_score','Team2_score','Team1_superover_score','Team2_superover_score']
matches_agg=pd.merge(matches, team_score, left_on='id', right_on='match_id', how='outer')
matches_agg.head()
team_extras=deliveries.groupby(['match_id','inning'])['extra_runs'].sum().unstack().reset_index()
team_extras.columns=['match_id','Team1_extras', 'Team2_extras', 'Team1_superover_extras', 'Team2_superover_extras']
matches_agg=pd.merge(matches_agg, team_extras, on='match_id', how='outer')

col=['match_id','season', 'city','date','team1', 'team2' , 'toss_winner', 'toss_decision', 'result','dl_applied', 'winner', 'Team1_score', 'Team2_score', 'win_by_runs', 'win_by_wickets', 'Team1_extras', 'Team2_extras', 'Team1_superover_score', 'Team2_superover_score', 'Team1_superover_extras', 'Team2_superover_extras','player_of_match', 'type', 'venue', 'umpire1', 'umpire2', 'umpire3']
matches_agg=matches_agg[col]

matches_agg.head(2)

batsman_grp=deliveries.groupby(['match_id', 'inning','batting_team', 'batsman'])
batsmen = batsman_grp['batsman_runs'].sum().reset_index()

balls_faced=deliveries[deliveries['wide_runs']==0]
balls_faced
balls_faced['wide_runs']
balls_faced =balls_faced.groupby(['match_id', 'inning', 'batsman'])['batsman_runs'].count().reset_index()
balls_faced
balls_faced.columns= ['match_id', 'inning', 'batsman', 'balls_faced']

batsmen=batsmen.merge(balls_faced, left_on=["match_id", 'inning', 'batsman'], right_on=['match_id', 'inning', 'batsman'], how='left')
batsmen.head(2)
fours= deliveries[deliveries['batsman_runs']==4]
fours
sixes = deliveries[deliveries['batsman_runs']==6]
fours_per_batsman=fours.groupby(['match_id', 'inning', 'batsman'])['batsman_runs'].count().reset_index()
sixes_per_batsman=sixes.groupby(['match_id', 'inning', 'batsman'])['batsman_runs'].count().reset_index()
fours_per_batsman.head(2)
fours_per_batsman.columns=['match_id', 'inning', 'batsman', '4s']
sixes_per_batsman.columns=['match_id', 'inning', 'batsman', '6s']
batsmen=batsmen.merge(fours_per_batsman, left_on=['match_id', 'inning', 'batsman'], right_on=['match_id','inning', 'batsman'], how='left')
batsmen=batsmen.merge(sixes_per_batsman, left_on=['match_id', 'inning', 'batsman'], right_on=['match_id', 'inning', 'batsman'], how='left')
batsmen['SR'] = np.round(batsmen['batsman_runs']/batsmen['balls_faced'] * 100, 2)
for col in ['batsman_runs', '4s', '6s', 'balls_faced', 'SR']:
    batsmen[col] = batsmen[col].fillna(0)
    
dismissals=deliveries[pd.notnull(deliveries['player_dismissed'])]
dismissals.head(2)
dismissals= dismissals[['match_id', 'inning', 'player_dismissed', 'dismissal_kind', 'fielder']]
dismissals
dismissals.rename(columns={'player_dismissed':'batsman'}, inplace=True)
dismissals
batsmen=batsmen.merge(dismissals, left_on=['match_id', 'inning', 'batsman'], right_on=['match_id', 'inning', 'batsman'], how='left')

batsmen=matches[['id', 'season']].merge(batsmen, left_on='id', right_on='match_id', how='left').drop('id', axis=1
)
batsmen.head(2)
bowler_grp=deliveries.groupby(['match_id', 'inning', 'bowling_team', 'bowler', 'over'])
bowlers = bowler_grp['total_runs', 'wide_runs', 'bye_runs', 'legbye_runs', 'noball_runs'].sum().reset_index()
bowlers['runs']= bowlers['total_runs'] - (bowlers['bye_runs'] + bowlers['legbye_runs'])
bowlers['runs']= bowlers['total_runs'] - (bowlers['bye_runs'] + bowlers['legbye_runs'])
bowlers['extras'] = bowlers['wide_runs'] + bowlers['noball_runs']
del(bowlers['bye_runs'])
del(bowlers['legbye_runs'])
del(bowlers['total_runs'])
dismissal_kinds_for_bowler = ['bowled', 'caught', 'lbw' , 'stumped', 'caught and bowled', 'hit wicket']
dismissals=deliveries[deliveries['dismissal_kind'].isin(dismissal_kinds_for_bowler)]
dismissals=dismissals.groupby(['match_id', 'inning', 'bowling_team', 'bowler', 'over'])['dismissal_kind'].count().reset_index()
dismissals.rename(columns={"dismissal_kind" : "wickets"}, inplace=True)
bowlers=bowlers.merge(dismissals, left_on=['match_id', 'inning', 'bowling_team', 'bowler', 'over'], right_on=['match_id', 'inning', 'bowling_team', 'bowler', 'over'], how='left')
bowlers['wickets'] = bowlers['wickets'].fillna(0)

bowlers_over = bowlers.groupby(['match_id', 'inning', 'bowling_team', 'bowler'])['over'].count().reset_index()

bowlers =  bowlers.groupby(['match_id', 'inning', 'bowling_team', 'bowler']).sum().reset_index().drop('over', 1)

bowlers = bowlers_over.merge(bowlers, on=['match_id', 'inning', 'bowling_team', 'bowler'], how='left')

bowlers['Econ'] = np.round(bowlers['runs']/ bowlers['over'], 2)

bowlers =  matches[['id', 'season']].merge( bowlers, left_on = 'id', right_on='match_id', how='left').drop('id', axis=1)
bowlers.head(2)

x,y=2008, 2017

%matplotlib tk

import matplotlib

while x< y:
    wins_percity=matches_agg[matches_agg['season'] ==x].groupby(['winner', 'city'])['match_id'].count().unstack()
    plot=wins_percity.plot(kind='bar', stacked=True, title='Team wins in different cities\nSeason' + str(x), figsize=(7,5))
    sns.set_palette('Paired', len(matches_agg['city'].unique()))
    plot.set_xlabel('Teams')
    plot.set_ylabel('No.of wins')
    plot.legend(loc='best', prop={'size':8})
    x +=1


batsman_runsperseason=batsmen.groupby(['season', 'batting_team', 'batsman'])['batsman_runs'].sum().reset_index()
batsman_runsperseason=batsman_runsperseason.groupby(['season', 'batsman'])['batsman_runs'].sum().unstack().T
batsman_runsperseason['Total']=batsman_runsperseason.sum(axis=1)

batsman_runsperseason = batsman_runsperseason.sort_values(by='Total', ascending=False).drop('Total', 1)

ax=batsman_runsperseason[:5].T.plot()