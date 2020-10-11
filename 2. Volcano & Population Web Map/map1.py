#-----------------------------------------------------------------------------#

#----------------        Volcanoes & Population Webmap         ---------------#

#-----------------------------------------------------------------------------#

import folium
import pandas as pd

df1 = pd.read_csv('Sumatra.csv')
df2 = pd.read_csv('Banda Sea.csv')
df3 = pd.read_csv('Halmahera.csv')
df4 = pd.read_csv('Lesser Sunda Islands.csv')
df5 = pd.read_csv('Sulawesi and Sangihe Islands.csv')
df6 = pd.read_csv('Sunda Strait and Java.csv')

file_list = [df1,df2,df3,df4,df5,df6]

def color_procedure(ele):
    if 'Pleistocene' == ele or 'BC' in ele:
        return 'green'
    elif 'ongoing' in ele or 'on going' in ele:
        return 'red'
    else:
        return 'orange'

def each_file(df):
    lat = list(df.Geolocation.apply(lambda x: x.replace(' ', '').split(',')[0]))
    long = list(df.Geolocation.apply(lambda x: x.replace(' ', '').split(',')[1]))
    info = df[df.columns[1:5]].apply(lambda x: ', '.join(x.dropna().astype(str)), axis=1)
    last_erp = list(df['Last eruption (VEI)'])

    map = folium.Map(location=[-0.659531, 113.919436], zoom_start=5, tiles="Stamen Terrain")

    fgv = folium.FeatureGroup(name='Volcanoes')

    for lt, ln, el, cl in zip(lat, long, info, last_erp):
        fgv.add_child(folium.Marker(location=[lt, ln], radius=6, popup=el,
                                    icon=folium.Icon(color=color_procedure(cl))))

    fgp = folium.FeatureGroup(name='Population')

    fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                                style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
                                else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

    map.add_child(fgv)
    map.add_child(fgp)
    map.add_child(folium.LayerControl())
    map.save("Map1.html")

frames = pd.concat(file_list)
each_file(frames)