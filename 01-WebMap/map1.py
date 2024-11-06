import folium
import pandas
import json

# Función para asignar colores según la elevación de los volcanes
def assign_color(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'
    
def population_color(population):
    if population < 1000000:
        return 'lightgreen'
    elif population < 5000000:
        return 'green'
    elif population < 10000000:
        return 'orange'
    elif population < 20000000:
        return 'red'
    else:
        return 'darkred'

# Crear el mapa base
map = folium.Map(
    location=[40, -100],
    zoom_start=4,
    tiles='CartoDB Positron'
)

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elevation = list(data["ELEV"])

# Capa de volcanes
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elevation):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln], 
        radius=6, 
        popup=str(el) + " m", 
        fill_color=assign_color(el), 
        color='darkgrey', 
        fill_opacity=0.7
    ))

# Cargar el archivo GeoJSON con información de países y población
with open('world.json', 'r', encoding='utf-8-sig') as f:
    geo_data = json.load(f)

# Capa de población con colores y popups
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=geo_data,
    style_function=lambda x: {
        'fillColor': population_color(x['properties'].get('POP2005', 0)),
        'color': 'black',
        'weight': 0.5,
        'fillOpacity': 0.5
    },
    popup=folium.GeoJsonPopup(
        fields=['NAME', 'POP2005'],
        aliases=['Name', 'Population (2005):'],
        localize=True
    )
))

# Añadir los grupos de características y control de capas
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")
