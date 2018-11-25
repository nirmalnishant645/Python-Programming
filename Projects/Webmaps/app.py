import folium #import folium
map = folium.Map(location=[22.821958, 79.662094], zoom_start=6, tiles="Mapbox Bright") #Open Street Map

fg = folium.FeatureGroup(name="Population Density") #Making a Feature Group

for xy in [[28.623067, 77.222180], [18.516702, 73.860213]]: #for loop to execute code twice
    fg.add_child(folium.Marker(location = xy, popup="Marker", icon=folium.Icon(color='blue'))) #Add markers to the Feature Group as a child

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), #Reading Geo json file and making a new layer of the map
style_function = lambda x: {'fillColor':'green' if x ['properties']['POP2005'] < 10000000 #Change colours based on Population
else 'orange' if 10000000 <= x ['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fg) #Make Featuer Group child of Map
map.add_child(folium.LayerControl()) #Layer Control Panel

map.save("Map1.html") #Save the HTML file of Map
