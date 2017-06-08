# coding: utf-8
matches=pd.read_csv('matches_all.csv')
bowlers_a=bowler_grp['total_runs', 'wide_runs', 'bye_runs', 'legbye_runs', 'noball_runs'].sum().reset_index()
bowlers_a=matches[['id', 'season']].merge(bowlers_a, left_on='id', right_on='match_id', how='left').drop('id', axis=1)

bowlers_b=bowlers_a.groupby(['season','bowling_team','match_id','bowler']).count()

bowlers_b=bowlers_b.reset_index()

bowlers_c=bowlers_b.groupby(['season','bowler'])['match_id'].count()

bowlers_c=bowlers_c.reset_index()
bowlers_c.head(100)
bowlers_c=bowlers_c.rename(columns={'match_id':'total_matches_played'})