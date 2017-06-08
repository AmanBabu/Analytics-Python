# coding: utf-8
bowlers_played=bowlers_c[bowlers_c['total_matches_played']>=3]
last_3overs_total_matches_a.head()
last_3overs_total_matches_a['runs'] = last_3overs_total_matches_a['total_runs']-(last_3overs_total_matches_a['legbye_runs'] + last_3overs_total_matches_a['bye_runs'])
last_3overs_total_matches_a['extras'] = last_3overs_total_matches_a['wide_runs'] + last_3overs_total_matches_a['noball_runs']
del(last_3overs_total_matches_a['total_runs'])
del(last_3overs_total_matches_a['bye_runs'])
del(last_3overs_total_matches_a['legbye_runs'])
dismissal_kinds_for_bowler=['bowled', 'caught', 'lbw' , 'stumped', 'caught and bowled', 'hit wicket']
dismissals=deliveries[deliveries['dismissal_kind'].isin(dismissal_kinds_for_bowler)]
dismissals=dismissals.groupby(['match_id', 'inning', 'bowling_team', 'bowler', 'over'])['dismissal_kind'].count().reset_index()
dismissals.rename(columns={'dismissal_kind':'wickets'}, inplace=True)
last_3overs_total_matches_a=last_3overs_total_matches_a.merge(dismissals, left_on=['match_id', 'inning', 'bowling_team', 'bowler','over'], right_on=['match_id', 'inning', 'bowling_team', 'bowler', 'over'],how='left')
last_3overs_total_matches_a['wickets']=last_3overs_total_matches_a['wickets'].fillna(0)
bowlers_over=last_3overs_total_matches_a.groupby(['match_id', 'inning', 'bowling_team', 'bowler'])['over'].count().reset_index()
last_3overs_total_matches_a=last_3overs_total_matches_a.groupby(['match_id', 'inning', 'bowling_team', 'bowler']).sum().reset_index().drop('over',1)
last_3overs_total_matches_a=bowlers_over.merge(last_3overs_total_matches_a, on=['match_id', 'inning', 'bowling_team', 'bowler'], how='left')
last_3overs_total_matches_a['Econ'] =np.round(last_3overs_total_matches_a['runs'] / last_3overs_total_matches_a['over'],2)
