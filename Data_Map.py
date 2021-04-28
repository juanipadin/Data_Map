import folium
import pandas as pd
import json
import requests

#UBICA EL MAPA
#canada_map = folium.Map(location=[56.130, -106.35],zoom_start=4)
#CREA CATEGORÍA ONTARIO
#ontario=folium.map.FeatureGroup()
#CREA UN PUNTO SOBRE ONTARIO
#ontario.add_child(folium.features.CircleMarker([51.25, -85.32],radius=5,color='red', fill_color= 'Red'))
#AÑADE EL BOTON AL MAPA PRINCIPAL
#canada_map.add_child(ontario)
#AGREGA UN BOTÓN SOBRE EL MAPA Y LO AÑADE AL MAPA PRINCIPAL
#folium.Marker([51.25, -85.32], popup='Ontario').add_to(canada_map)
#GUARDA EL MAPA COMO HTML
#canada_map.save('mapa.html')

##################--- MAPA DE COLORES ---##################

df_can= pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
                sheet_name='Canada by Citizenship',
                skiprows=range(20),
                nrows=196,
                engine= 'openpyxl',)

#SACA COLUMNAS INNECESARIAS
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis =1, inplace=True)
#CAMBIA EL NOMBRE DE LAS COLUMNAS
df_can.rename(columns={'OdName' : 'Country', 'AreaName' : 'Continent', 'RegName': 'Region'}, inplace=True)
#HACE STR TODAS LAS COLUMNAS
df_can.columns = list (map(str,df_can.columns))
#CREA LA COLUMNA TOTAL SUMANDO
df_can['Total'] = df_can.sum(axis=1)
#CREA LA VARIABLE 'YEARS'
years = list(map(str,range (1980,2014)))

#CREA EL JSON CON LOS DATOS DE LOS PAIESES Y SUS LÍMITES
url = ('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data')
mapa = f'{url}/world-countries.json'
world_geo = json.loads(requests.get(mapa).text)

#CREA EL MAPA
world_map = folium.Map(zoom_start = 2)
#PASA DE STR A DICT Y UNE LOS DATOS DE PAISES Y TOTAL
df_can = dict(zip(df_can['Country'], df_can['Total']))

 #CREACIÓN DEL MAPA
folium.Choropleth(
    geo_data=world_geo,
    data=df_can,
    name='hola',
    colums=['Country', 'Total'],
    key_on= 'feature.properties.name',
    fill_color='YlOrRd',
    line_weight=2).add_to(world_map)

world_map.save('mapacolor.html')