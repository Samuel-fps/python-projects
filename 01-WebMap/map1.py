import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

def assign_color(elevation):
    if elevation < 1500:
        return 'green'
    if elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(
    location=[40, -100],
    zoom_start=4,
    tiles='CartoDB Positron'
)

lon = list(data["LON"])
lat = list(data["LAT"])
elevation = list(data["ELEV"])

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elevation):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el), fill_color=assign_color(el), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig').read())))

map.add_child(fg)

map.save("Map1.html")
