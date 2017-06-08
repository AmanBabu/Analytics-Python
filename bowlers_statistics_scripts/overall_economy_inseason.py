# coding: utf-8
last_3overs_total_matches_a=matches[['id', 'season']].merge(last_3overs_total_matches_a, left_on='id', right_on='match_id', how='left').drop('id', axis=1)
last_3overs_total_matches_a.head()

bowlers_played_b=bowlers_played.merge(last_3overs_total_matches_a, on=['season','bowler'], how='inner')
bowlers_played_c=bowlers_played_b.groupby(['season','bowler','total_matches_played','bowling_team'])['Econ','over'].sum().reset_index()
bowlers_played_c.head()
bowlers_played_c['overall_economy']=(bowlers_played_c['Econ']/bowlers_played_c['over'])

bowlers_played_c=bowlers_played_c[bowlers_played_c['over']>= (bowlers_played_c['total_matches_played']/3)]
bowlers_played_c.head()
bowlers_played_c=bowlers_played_c.sort_values('overall_economy',ascending=True)
bowlers_played_c.head()
