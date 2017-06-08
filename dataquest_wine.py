totals = {}
year1 = world_alcohol[:,0]=='1989'
year = world_alcohol[year1,:]

for country in countries:
    country_consumption = year[:,2]==country
    country_consumption = year[country_consumption,:]
    fifth = country_consumption[:,4]
    beforetotal = fifth== ''
    fifth[beforetotal]='0'
    fifth = fifth.astype(float)
    fifth = fifth.sum()
    totals[country] = fifth
    
print(totals)