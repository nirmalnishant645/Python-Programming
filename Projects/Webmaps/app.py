import folium #import folium
map = folium.Map(location=[28.6, 77.1], zoom_start=6, tiles="Mapbox Bright") #Open Street Map

fg = folium.FeatureGroup(name="My Map") #Making a Feature Group
fg.add_child(folium.Marker(location=[28.6, 77.1], popup="Marker", icon=folium.Icon(color='green'))) #Add marker to the Feature Group as a child

map.add_child(fg) #Make Featuer Group child of Map

map.save("Map1.html") #Save the HTML file of Map
