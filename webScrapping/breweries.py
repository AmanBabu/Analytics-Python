# coding: utf-8
beers.head()
breweries=beers[['brewery_location','brewery_name']]
breweries
breweries=breweries.drop_duplicates().reset_index(drop=True)
breweries.head()
breweries['id']=breweries.index

beers_data=beers.merge(breweries, left_on=['brewery_name', 'brewery_location'],right_on=['brewery_name', 'brewery_location'], sort=True, suffixes=('_beer','_brewery'))
beers_data.head()
beers_data.rename(columns={"id_beer":"id", "id_brewery":"brewery_id"}, inplace=True)
beers_data.head()

breweries['city']=breweries['brewery_location'].apply(lambda location:location.split(',')[0])
breweries['state']=breweries['brewery_location'].apply(lambda location:location.split(',')[1])
breweries=breweries[['brewery_name', 'city', 'state']]
breweries.rename(columns={'brewery_name':'name'}, inplace=True)
breweries.head()
beers_data.head
beers_data.head()
breweries.head()
beers_data.to_csv('beers_data.csv')
beers_data.head()
beers_data.to_csv('beers_data.csv')
breweries.to_csv('breweries_data.csv')
beers_data.head()
