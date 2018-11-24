import folium #import folium
map = folium.Map(location=[22.821958, 79.662094], zoom_start=6, tiles="Mapbox Bright") #Open Street Map

fg = folium.FeatureGroup(name="My Map") #Making a Feature Group

for xy in [[28.623067, 77.222180], [18.516702, 73.860213]]: #for loop to execute code twice
    fg.add_child(folium.Marker(location = xy, popup="Marker", icon=folium.Icon(color='blue'))) #Add markers to the Feature Group as a child


map.add_child(fg) #Make Featuer Group child of Map

map.save("Map1.html") #Save the HTML file of Map
