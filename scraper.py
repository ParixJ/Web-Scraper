from bs4 import BeautifulSoup
import requests as re
from geopy.geocoders import Nominatim

city = str(input('Enter city name with state : '))

locator = Nominatim(user_agent=('project'))

coordinates = locator.geocode(city)
lat,lon = coordinates.latitude,coordinates.longitude
mt = []

request = re.get(f'https://weather.com/en-IN/weather/today/l/{lat},{lon}').text

soup = BeautifulSoup(request,'lxml')

temp = soup.find('span',class_='CurrentConditions--tempValue--zUBSz').text
info = soup.find_all('div',class_='ListItem--listItem--UuEqg WeatherDetailsListItem--WeatherDetailsListItem--HLP3I')

print(f'\n\nTemperatue in {city} is {temp}\n')

print(f'Following is the wheather info for {city} : \n')
for i in info:
    mt.append(i.text)
    print(i.text,'\n')

with open(f'{city}_Temperature.csv','w') as c:
    for m in mt:
        c.write(m)