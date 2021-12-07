import pandas as pd
import numpy as np
import openpyxl
import folium
from folium.plugins import FloatImage


### Make point for map. When map will be opened, we start from your region ###


map = folium.Map(location=[58.598171, 49.626315], zoom_start=7)
image_file = 'legend.PNG'
FloatImage(image_file, bottom=0, left=81).add_to(map)


### Coordinates collected in csv or json file. We takeing this coordinates in cycle and making points on the map ###


filename = pd.read_excel('info.xlsx')
i = 0                              
for row in filename:
    a = filename.iloc[i]

    if a["type"] == 'red':
        folium.Marker(
        location=[a['latitude'],a['longitude']],
        popup=a['description'],
        icon=folium.Icon(color='red', icon='info-sign'),
        ).add_to(map)
        i += 1
    elif a['type'] == 'green':
        folium.Marker(
        location=[a['latitude'],a['longitude']],
        popup=a['description'],
        icon=folium.Icon(color='green', icon='info-sign'),
        ).add_to(map)
        i += 1
    elif a['type'] == 'yellow':
        folium.Marker(
        location=[a['latitude'],a['longitude']],
        popup=a['description'],
        icon=folium.Icon(color='yellow', icon='info-sign'),
        ).add_to(map)
        i += 1


### Saving our map ###


map.save("index.html")

### Dont fogget, what if u will publicate this map on hosting, name will should like a INDEX.HTML ###