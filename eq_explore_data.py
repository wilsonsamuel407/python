import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
#The address for filename references the folder data in the same directory as this program
filename ='data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, hover_texts =[], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	title = eq_dict['properties']['title']
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_texts.append(title)

#Plot the earthquakes

data = [{
'type': 'scattergeo',
'lon': lons,
'lat': lats,
'text': hover_texts,
'marker':{
	'size': [5*mag for mag in mags],
	'color': mags,
	'colorscale': 'Viridis',
	'reversescale': True,
	'colorbar': {'title': 'Magnitude'},
	},
}]
my_layout = Layout(title='Global Earthquakes last 30 days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakess.html')