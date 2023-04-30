# Section 17 
import folium
import pandas as pd


def set_color(elevation):
    if elevation <= 1000:
        return "lightblue"
    elif elevation <= 2000:
        return "blue"
    elif elevation <= 3000:
        return "green"
    elif elevation <= 4000:
        return "orange"
    else:
        return "red"

    
data = pd.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup="Elevation: "+str(el)+ "m", icon=folium.Icon(color=set_color(el), icon='info-sign')))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
