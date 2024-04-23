import requests
from bs4 import BeautifulSoup
import folium
from models.data_source import users

def single_map(user_location:str)->None:
    url: str = f'https://pl.wikipedia.org/wiki/{user_location}'
    responsse = requests.get(url)
    responsse_html = BeautifulSoup(responsse.text, 'html.parser')
    latitude = responsse_html.select('.latitude')[1].text.replace(",",".")
    longitude = responsse_html.select('.longitude')[1].text.replace(",",".")
    map = folium.Map(location=[latitude, longitude], zoom_start=11)
    folium.Marker(location=[latitude, longitude], popup=f"{user_location} rządzi !!??").add_to(map)
    map.save(f'./{user_location}.html')

for user in users:
    single_map(user['location'])

def full_map(users:str)->None:
    lista_wsplrzednych = []
    map = folium.Map(location=[52, 21], zoom_start=8)
    for user in users:
        url: str = f'https://pl.wikipedia.org/wiki/{user['location']}'
        responsse = requests.get(url)
        responsse_html = BeautifulSoup(responsse.text, 'html.parser')
        latitude = responsse_html.select('.latitude')[1].text.replace(",",".")
        longitude = responsse_html.select('.longitude')[1].text.replace(",",".")
        lista_wsplrzednych.append([latitude, longitude])
    for wsplrzedne in lista_wsplrzednych:
        folium.Marker(location=wsplrzedne).add_to(map)
    map.save(f'./common_map.html')