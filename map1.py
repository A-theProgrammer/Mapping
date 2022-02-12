import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
nm=list(data["NAME"])
elev=list(data["ELEV"])

def color_producer(elevation):
  if elevation<1500:
    return "green"
  elif 1500<=elevation<2750:
    return "orange"
  else:
    return "red"

html="""Volcano name: 
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br><br>
Height: %s m """

map=folium.Map(location=[39.85,-95.32],zoom_start=5,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,n,el in zip(lat,lon,nm,elev):
  iframe=folium.IFrame(html=html % (n,n,el), width=400, height=85)
  # fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(iframe),fill_color=color_producer(el),color="grey"))
  fgv.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=color_producer(el))))


fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open("world.json","r",encoding='utf-8-sig').read()),style_function=lambda x:{'fillColor':'yellow' if x["properties"]["POP2005"]<10000000 else 'orange' if 10000000<= x["properties"]["POP2005"]< 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.map.LayerControl())

map.save("Map1.html")
