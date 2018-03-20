
ANALYSIS:

1) As we approach the equator and Latitude approaches 0, max temperature goes up. Trend can be seen on plot for "City Latitude vs Max Temperature (F)".

2) There appears to be more cities on the Northern Hemisphere than the Souther Hemisphere. This is shown by our sample size of 500 and most data points residing on the latitudes of greater than 0.

3) A loose direct correlation between wind speeds and distance from the equator seems to imply that wind speeds are higher further from the equator.


```python
#Import dependencies
import pandas as pd
import requests
import numpy as np
import random
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from config import api_key
import time

world_cities = pd.read_csv('worldcities.csv')
world_cities.head()

sns.set_style("whitegrid")
sns.set_context("poster")
```


```python
#Sample 500 cities from world_cities at random (by their index)
random_cities = random.sample(set(world_cities.index), 500)
random_cities

#Append the city lat/lon into lists
lat = []
lon = []
for index in random_cities:
    lat.append(world_cities.iloc[index]['Latitude'])
    lon.append(world_cities.iloc[index]['Longitude'])
```


```python
#List to hold all city responses
all_responses = []
Name = []
Cloudiness = []
Country = []
Date = []
Humidity = []
lat_owm = []
lng_owm = []
Max_temp = []
Wind_speed = []


#Loop to request weather info by lat/lon on OWM API
#Traverse each json response to append information to list
for indexes in np.arange(len(lat)):
    time.sleep(.1)
    params = {'lat': lat[indexes],
             'lon': lon[indexes],
             'units': 'imperial',
             'appid': api_key}
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    response = requests.get(base_url, params=params)
    requested_url = response.url
    response_js = response.json()
    Name.append(response_js['name'])
    Cloudiness.append(response_js['clouds']['all'])
    Country.append(response_js['sys'].get('country', None))
    Date.append(response_js['dt'])
    Humidity.append(response_js['main']['humidity'])
    lat_owm.append(response_js['coord']['lat'])
    lng_owm.append(response_js['coord']['lon'])
    Max_temp.append(response_js['main']['temp_max'])
    Wind_speed.append(response_js['wind']['speed']) 

        
    all_responses.append(response_js)
    
    print(f"Request Successful--- City Name:{response_js['name']}, City ID:{response_js['id']}, Requested URL:{requested_url}")
    print('---------------')

```

    Request Successful--- City Name:Terrace End, City ID:2181258, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-40.35&lon=175.616667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Aparan, City ID:616953, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.5961111&lon=44.3536111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Isalnita, City ID:675489, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.4&lon=23.733333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Alegria, City ID:1731573, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=8.506667&lon=126.011944&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sosenskiy, City ID:490437, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.058991&lon=35.962282&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Francavilla Fontana, City ID:3176603, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.533333&lon=17.583333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lipki, City ID:535088, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=53.969938&lon=37.70282&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Okoneshnikovo, City ID:1496329, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.837668&lon=75.083429&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Khlevnoye, City ID:550102, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=52.195116&lon=39.093164&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Csolnok, City ID:3053986, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.691155&lon=18.716109&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Redding, City ID:5570160, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.5866667&lon=-122.3905556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Novobod, City ID:1220936, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.0077778&lon=70.1555556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Calbe, City ID:2940419, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.9&lon=11.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gurranebraher, City ID:7869980, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.8986111&lon=-8.4958333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Aleksandrovsk, City ID:583041, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=59.158043&lon=57.562414&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Thabazimbi, City ID:949683, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-24.59165&lon=27.411551&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Petrokhorion, City ID:734672, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.1166667&lon=24.8333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kazlu Ruda, City ID:598286, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.7666667&lon=23.5&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santa Maria da Vitoria, City ID:3450063, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-13.4&lon=-44.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bonneuil-en-France, City ID:6613145, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.974455&lon=2.431536&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vienna, City ID:4825976, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.3269444&lon=-81.5486111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Morki, City ID:525262, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.430278&lon=48.994722&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Scarborough, City ID:3573703, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.1833333&lon=-60.7333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lantapan, City ID:1707438, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.997778&lon=125.027778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nkhata Bay, City ID:924732, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-11.6&lon=34.3&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tinglev, City ID:2611684, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.93099&lon=9.252433&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Humberto de Campos, City ID:3398428, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-2.616667&lon=-43.45&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Brookside, City ID:4141674, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.6669444&lon=-75.7272222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Barhiya, City ID:1276954, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=25.283333&lon=86.033333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kerepehi, City ID:2188882, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-37.3&lon=175.533333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vatne, City ID:3132428, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=62.566667&lon=6.65&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Augustow, City ID:776597, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=53.844711&lon=22.980133&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gazojak, City ID:1514792, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.1833333&lon=61.4&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Teius, City ID:665318, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.2&lon=23.683333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Conil de la Frontera, City ID:2519289, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=36.277194&lon=-6.088497&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Afenga, City ID:4035432, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-13.8&lon=-171.8833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Suraia, City ID:665754, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.683333&lon=27.4&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ikeda, City ID:1861799, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=34.016667&lon=133.8&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cine, City ID:318372, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=37.611667&lon=28.061389&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vahan, City ID:616117, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.57&lon=45.3955556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dinuba, City ID:5343171, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=36.5433333&lon=-119.3861111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vila Nova de Gaia (Santa Marinha), City ID:8014049, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.133633&lon=-8.617421&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Genova, City ID:3682070, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=1.643222&lon=-77.024333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ruda nad Moravou, City ID:3066613, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.981072&lon=16.877622&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kintra, City ID:2645356, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.633333&lon=-6.183333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Alkmaar, City ID:2759899, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=52.635818&lon=4.75561&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Wahpeton, City ID:5062355, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.2652778&lon=-96.6055556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Narayanavanam, City ID:1261832, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.416667&lon=79.583333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Salcioara, City ID:668188, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.533333&lon=26.883333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gapan, City ID:1713226, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.281&lon=120.9477&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Adoni, City ID:1279335, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.633333&lon=77.283333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nolhaga, City ID:2689513, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=57.933333&lon=12.516667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kerva, City ID:550973, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.611669&lon=39.576652&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rehli, City ID:1258247, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=23.633333&lon=79.083333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kulotino, City ID:539389, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=58.45&lon=33.383333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Makariv, City ID:702337, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.464077&lon=29.811277&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jordan, City ID:1710116, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.663656&lon=122.590103&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nueva Vida Sur, City ID:1697457, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.7846&lon=124.1745&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Peremyshl, City ID:511400, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.263126&lon=36.160631&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rudozem, City ID:727552, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.4833333&lon=24.85&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mazeikiai, City ID:597188, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.3166667&lon=22.3333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sagna, City ID:668263, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.983333&lon=27.016667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Podujeva, City ID:786950, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.910556&lon=21.193056&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Castlewood, City ID:5416357, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.5847222&lon=-104.9005556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Meggen, City ID:7286468, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.04722&lon=8.369489&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hangu, City ID:676331, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.05&lon=26.033333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Merida, City ID:2513917, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=38.916109&lon=-6.343657&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:La Spezia, City ID:3175081, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.116667&lon=9.833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jovellar, City ID:1710099, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.0635&lon=126.455582&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mytilini, City ID:256866, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.11&lon=26.5547222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Courbevoie, City ID:3023141, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.897&lon=2.2564&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Promyshlennyy, City ID:1494088, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=67.583333&lon=63.916667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Harsesti, City ID:676167, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.533333&lon=24.783333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bozuyuk, City ID:320557, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.907778&lon=30.036667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vamosgyork, City ID:3043210, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.684285&lon=19.92924&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cartaxo, City ID:2270023, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.160221&lon=-8.787408&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tayport, City ID:2636158, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.45&lon=-2.883333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kalety, City ID:3096911, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.562701&lon=18.892596&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Motihari, City ID:1262710, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.65&lon=84.916667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Citrus Park, City ID:4151157, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=28.0780556&lon=-82.57&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cristalina, City ID:3465164, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-16.75&lon=-47.6&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nangka, City ID:1698281, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.4023&lon=122.8244&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nkana, City ID:900813, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-12.8166667&lon=28.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cakovec, City ID:3202888, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.3844444&lon=16.4338889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Haywards Heath, City ID:2647248, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.983333&lon=-0.1&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Aarburg, City ID:2661879, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.319634&lon=7.901413&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Verkh-Usugli, City ID:2013459, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=52.683333&lon=115.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Podivin, City ID:3068066, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.829387&lon=16.849737&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Candelaria, City ID:3687644, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=3.406711&lon=-76.348192&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Castrovillari, City ID:2525070, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.816667&lon=16.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hewitt, City ID:4697330, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=31.4622222&lon=-97.1955556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kruibeke, City ID:2793940, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.166667&lon=4.316667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Telega, City ID:665290, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.133333&lon=25.783333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kharan, City ID:1174062, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=28.583333&lon=65.416667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vimercate, City ID:3164083, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.616667&lon=9.366667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gerash, City ID:133595, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=27.6652&lon=54.1371&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Plaine des Papayes, City ID:934170, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-20.065&lon=57.5725&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Trujillo, City ID:3666680, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=4.212168&lon=-76.319454&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Wuhai, City ID:1791249, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.664722&lon=106.812222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Moerbeke, City ID:2791120, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.166667&lon=3.933333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Coria, City ID:2519234, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.987879&lon=-6.537718&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Myaundzha, City ID:2123100, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=63.033333&lon=146.833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Canubing No 2, City ID:1718828, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.3561&lon=121.1441&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Carmarthen, City ID:2653755, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.859167&lon=-4.311667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Faragau, City ID:678455, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.766667&lon=24.516667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vista Hermosa, City ID:3514633, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.516667&lon=-99.216667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Buribay, City ID:570813, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.961667&lon=58.159167&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Abidos, City ID:3393768, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-1.908333&lon=-55.518889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jabonga, City ID:1710399, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.343056&lon=125.515556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Argel, City ID:616912, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.3794444&lon=44.5994444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Svaty Jur, City ID:3057304, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.25&lon=17.2166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Massapequa, City ID:5126183, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.6805556&lon=-73.4747222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mildura, City ID:2157698, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-34.185509&lon=142.162506&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Neyagawa, City ID:6697563, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=34.75&lon=135.633333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oud-Turnhout, City ID:2789484, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.316667&lon=4.983333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kavali, City ID:1267394, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.916667&lon=79.983333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rio do Sul, City ID:3451152, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-27.2181&lon=-49.6436&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Slatinany, City ID:3065873, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.918333&lon=15.815192&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Khategaon, City ID:1266847, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=22.6&lon=76.916667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Calamba, City ID:1720683, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.103611&lon=125.594167&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Matei, City ID:673678, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.983333&lon=24.266667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Jose de Tarros, City ID:3602065, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.3&lon=-88.7&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bongor, City ID:2434910, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.2805556&lon=15.3722222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Huatabampo, City ID:4004647, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.833333&lon=-109.633333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Karasuk, City ID:1504489, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=53.737718&lon=78.040255&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oromīya Kilil, City ID:444185, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.95&lon=39.133333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kotlyarevskaya, City ID:543671, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.573442&lon=44.061344&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tarrega, City ID:3108285, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.648983&lon=1.1396&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pine Castle, City ID:4168418, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=28.4716667&lon=-81.3680556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Stellata, City ID:3166168, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.883333&lon=11.416667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Maribojoc, City ID:1700968, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.7417&lon=123.8446&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ricardo Palma, City ID:3930382, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-11.9180556&lon=-76.6663889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Leonding, City ID:2772635, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.266667&lon=14.25&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Regensdorf / Obstgarten, City ID:6291714, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.429855&lon=8.465128&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ichon, City ID:1711348, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.109722&lon=124.901667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sesquile, City ID:3668138, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=5.044628&lon=-73.797243&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cosmopolis, City ID:3465320, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-22.633333&lon=-47.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jequitinhonha, City ID:3459925, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-16.433333&lon=-41.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:El Castillo, City ID:3529243, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.533333&lon=-96.85&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Novosokolniki, City ID:517921, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.346345&lon=30.157781&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Balaogan, City ID:1728433, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.4328&lon=123.2818&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dir, City ID:1179757, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=35.205833&lon=71.875556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Alagoinha, City ID:3408094, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-6.933333&lon=-35.55&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Pedro Masahuat, City ID:3583407, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.5436111&lon=-89.0386111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Banki, City ID:1277273, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.383333&lon=85.533333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Matias, City ID:3601874, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.9833333&lon=-86.6333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bountiful, City ID:5771826, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.8894444&lon=-111.88&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Macesu de Sus, City ID:674235, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.916667&lon=23.7&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oras, City ID:1697042, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=12.1406&lon=125.4397&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sal, City ID:247061, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=32.532848&lon=35.908174&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Colesberg, City ID:1013076, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-30.719994&lon=25.097185&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vinces, City ID:3650186, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-1.55&lon=-79.7333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kistarcsa, City ID:3050290, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.542839&lon=19.263312&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Machali, City ID:3881102, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-34.183333&lon=-70.666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hamburg, City ID:5119833, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.7158333&lon=-78.8297222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mingyue, City ID:2035754, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.106944&lon=128.921667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pilisszentkereszt, City ID:3046343, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.691434&lon=18.905028&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santa Rosa, City ID:3436959, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-26.866667&lon=-56.85&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kulebaki, City ID:539555, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.334722&lon=42.421389&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Schubelbach, City ID:2658696, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.173785&lon=8.927867&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cheshire, City ID:5283837, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.4988889&lon=-72.9011111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pag-asa, City ID:1696662, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.575556&lon=125.683889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Placer, City ID:1693268, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.8687&lon=123.9184&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Abiramam, City ID:1279405, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.466667&lon=78.45&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nkpor, City ID:2328811, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=6.151641&lon=6.844585&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Buffalo, City ID:5019588, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.1719444&lon=-93.8744444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rohru, City ID:1258078, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=31.216667&lon=77.75&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Temoaya, City ID:3516030, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.470833&lon=-99.591111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pomoryany, City ID:696582, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.640924&lon=24.9307&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Volgo-Kaspiyskiy, City ID:472751, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.203064&lon=47.918691&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Banaba, City ID:1727642, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.216667&lon=120.85&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Odoreu, City ID:671966, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.8&lon=23.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mazabuka, City ID:907111, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-15.8666667&lon=27.7666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Scurtu Mare, City ID:667553, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.35&lon=25.266667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rosport, City ID:2960127, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.7977778&lon=6.5041667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rotava, City ID:3066743, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.297435&lon=12.573072&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santos Dumont, City ID:3449427, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-21.466667&lon=-43.566667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Coxquihui, City ID:3530144, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.183333&lon=-97.583333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Marsassoum, City ID:2248777, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=12.8275&lon=-15.9805556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Carroll, City ID:4850478, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.0658333&lon=-94.8666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hilton Head Island, City ID:4581833, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=32.2161111&lon=-80.7527778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:La Chapelle-sur-Erdre, City ID:6456914, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.295835&lon=-1.553093&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Silvino Lobos, City ID:1686436, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=12.3&lon=124.833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Edirne, City ID:747712, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.675745&lon=26.558665&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Visani, City ID:662709, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.15&lon=27.283333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pasarkemis, City ID:1632228, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-6.170278&lon=106.530278&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Salingogan, City ID:1690869, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.4333&lon=123.1923&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Comrie, City ID:2652478, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.366667&lon=-4.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:North Lakhimpur, City ID:1261181, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=27.233333&lon=94.116667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Osinovo, City ID:514460, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.8809&lon=48.881&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Krasnaya Zarya, City ID:542561, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=52.7825&lon=37.680556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lambayeque, City ID:3695754, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-6.7011111&lon=-79.9061111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gemeente Hellevoetsluis, City ID:2754453, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.827088&lon=4.130596&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bam, City ID:141736, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=29.106&lon=58.357&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ituporanga, City ID:3460514, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-27.416667&lon=-49.6&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Renens, City ID:2659070, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.539894&lon=6.588096&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santiago de Cuenda, City ID:3983641, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.6&lon=-100.983333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Konnur, City ID:1266178, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=16.2&lon=74.75&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nivnice, City ID:3069744, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.97692&lon=17.64596&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Uitgeest, City ID:2745978, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=52.531713&lon=4.705922&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kyabram, City ID:2160910, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-36.313351&lon=145.050354&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ambatolampy, City ID:1082992, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-19.3833333&lon=47.4166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bumba, City ID:217745, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=2.183333&lon=22.466667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sukhovolya, City ID:692233, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.824261&lon=23.837695&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Selfoss, City ID:3413604, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=63.933333&lon=-21.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Recarei, City ID:2735366, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.153559&lon=-8.411779&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tsar Ferdinand, City ID:726262, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.1166667&lon=27.2666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rania, City ID:1258477, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=29.533333&lon=74.833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Spitak, City ID:616479, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.7955556&lon=44.2783333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Miroslavesti, City ID:673096, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.15&lon=26.65&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Darpas, City ID:616763, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.8380556&lon=44.4233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Armenokhorion, City ID:736735, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.8&lon=21.4666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Morrovalle, City ID:3172564, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.316667&lon=13.566667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Seregelyes, City ID:3045386, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.110504&lon=18.565&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Saryg-Sep, City ID:1492948, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.5&lon=95.6&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Front Royal, City ID:4760232, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=38.9180556&lon=-78.1947222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pooler, City ID:4216948, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=32.1152778&lon=-81.2472222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Svendborg, City ID:2612045, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.058732&lon=10.591346&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Puerto Tejada, City ID:3671315, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=3.231136&lon=-76.416684&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Telimele, City ID:2414926, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.9&lon=-13.0333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Fundeni, City ID:677808, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.533333&lon=27.55&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ungsang-nodongjagu, City ID:2039557, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.422222&lon=130.653056&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Chino Valley, City ID:5289658, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=34.7575&lon=-112.4530556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cazin, City ID:3202822, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.9830556&lon=15.9041667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Basilio, City ID:1690257, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.0335&lon=120.5837&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Fitjar, City ID:3157436, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=59.9175&lon=5.322778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Koronadal, City ID:1708522, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=6.503056&lon=124.846944&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lynnfield, City ID:4942821, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.5388889&lon=-71.0486111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kolkhozobod, City ID:1221259, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=37.5894444&lon=68.6608333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Leegmeer, City ID:2879706, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.833333&lon=6.25&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Essex, City ID:4354428, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.3091667&lon=-76.4752778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Alzenau in Unterfranken, City ID:2956715, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.083333&lon=9.066667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pacov, City ID:3068647, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.471272&lon=15.004092&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Patan, City ID:1260174, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=23.3&lon=79.7&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Abaete, City ID:3473267, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-19.15&lon=-45.45&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Departamento de La Paz, City ID:3911924, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-15.55&lon=-68.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Richmond, City ID:5387428, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=37.9358333&lon=-122.3466667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dombasle-sur-Meurthe, City ID:3021221, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.625201&lon=6.349671&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nomós Kilkís, City ID:735735, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.9941667&lon=22.7205556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lalpur, City ID:1265150, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=22.2&lon=69.966667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Wilsonville, City ID:5761287, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.3&lon=-122.7725&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Coelho Neto, City ID:3401992, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-4.25&lon=-43.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hacienda Heights, City ID:5354819, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=33.9930556&lon=-117.9677778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Basiad, City ID:1726431, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.156174&lon=122.337487&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Aduthurai, City ID:1279318, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.033333&lon=79.483333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kuroiso, City ID:2112077, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=36.966667&lon=140.05&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kodaira, City ID:1859116, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=35.726389&lon=139.483889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hamakita, City ID:1863293, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=34.8&lon=137.783333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Punghina, City ID:669491, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.281944&lon=22.934722&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Uniara, City ID:1253751, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.15&lon=75.216667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Constancia, City ID:4012966, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=24.223056&lon=-107.186944&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kugesi, City ID:539794, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.028947&lon=47.292551&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kalamansig, City ID:1709717, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=6.55187&lon=124.051111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Városrétidűlő, City ID:3043096, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.980651&lon=18.932674&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Nicolas, City ID:3601833, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.0&lon=-88.75&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rizomilos, City ID:254283, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.4333333&lon=22.75&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cocorastii-Misli, City ID:681198, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.083333&lon=25.933333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Clyde River, City ID:5924351, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=70.45&lon=-68.566667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Waitara, City ID:2208091, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-38.925&lon=174.25&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Taipei, City ID:1668341, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=25.0391667&lon=121.525&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kursenai, City ID:597769, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.985&lon=22.9188889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oak Harbor, City ID:5805441, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.2933333&lon=-122.6419444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Porto Feliz, City ID:3452779, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-23.213333&lon=-47.523056&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kilosa, City ID:157403, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-6.8333333&lon=36.9833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Juan de la Vega, City ID:3985878, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.633333&lon=-100.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Alsweiler, City ID:2958098, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.483333&lon=7.066667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dornesti, City ID:679084, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.866667&lon=26.016667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Leuteboro, City ID:1706810, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.061&lon=121.374717&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tamazulapan del Progreso, City ID:3801045, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=17.680556&lon=-97.568889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Parincea, City ID:671337, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.483333&lon=27.1&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lauder, City ID:2644818, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.7&lon=-2.75&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Buzescu, City ID:683111, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.016667&lon=25.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bohicon, City ID:2395049, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.2&lon=2.0666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Altotonga, City ID:3532969, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.766667&lon=-97.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Calca, City ID:3946177, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-13.3333333&lon=-71.95&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bay Saint Louis, City ID:4417205, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=30.3086111&lon=-89.33&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kyrksaeterora, City ID:3148602, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=63.283333&lon=9.1&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mounds View, City ID:5038373, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.105&lon=-93.2083333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cayeli, City ID:749502, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.092275&lon=40.729235&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Danane, City ID:2290462, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.259572&lon=-8.154981&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Komatsu, City ID:1926108, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=33.921667&lon=133.088333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Buriti Bravo, City ID:3404722, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-5.833333&lon=-43.833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bloomingdale, City ID:4607177, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=36.5844444&lon=-82.4894444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oboga, City ID:672060, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.416667&lon=24.1&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Fair Lawn, City ID:5097773, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.9402778&lon=-74.1322222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Itumba, City ID:158876, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-9.4&lon=33.1833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Balvanesti, City ID:684842, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.801111&lon=22.608611&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ruza, City ID:500303, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.698977&lon=36.195219&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Essenbach, City ID:2928804, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.616667&lon=12.216667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jasmine Estates, City ID:4160100, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=28.2927778&lon=-82.6902778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Novozavidovskiy, City ID:461704, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.55&lon=36.433333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kinalaglagan, City ID:1708729, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.001493&lon=121.097716&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Riemerling, City ID:2846989, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.066667&lon=11.683333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mega, City ID:331259, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=4.05&lon=38.3&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Angoram, City ID:2100765, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-4.0666667&lon=144.0666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Isenbruch, City ID:3205578, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.062965&lon=5.851675&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pedra Branca, City ID:3392629, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-5.45&lon=-39.716667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Egg, City ID:2660942, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.300555&lon=8.687429&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:La Cañada, City ID:3119903, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.423857&lon=-3.53261&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Meadela, City ID:2737810, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.706541&lon=-8.796279&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Magrath, City ID:6064202, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.416667&lon=-112.883333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sabac, City ID:3191376, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.746667&lon=19.69&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Belmont, City ID:5327455, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=37.5202778&lon=-122.2747222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sindhnur, City ID:1256207, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.783333&lon=76.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Darjiu, City ID:679328, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.216667&lon=25.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pryozerne, City ID:696275, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.269764&lon=36.330252&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:North Potomac, City ID:4363990, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.0827778&lon=-77.2652778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Zhangaqorghan, City ID:1517323, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.915&lon=67.248056&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santa Cruz del Quiche, City ID:3589404, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.030556&lon=-91.148889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:North Druid Hills, City ID:4212995, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=33.8166667&lon=-84.3133333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Uniao, City ID:3385745, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-4.583333&lon=-42.866667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Francisco, City ID:1690024, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=8.486389&lon=125.971667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bhadrachalam, City ID:1276328, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=17.666667&lon=80.883333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Novooleksiyivka, City ID:699706, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.224718&lon=34.64031&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Raya, City ID:1258292, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=27.566667&lon=77.783333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Elbistan, City ID:315795, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=38.205909&lon=37.198295&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Iacobeni, City ID:675868, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.05&lon=24.716667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bad Hofgastein, City ID:2782053, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.166667&lon=13.1&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kubuta, City ID:935055, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-26.8833333&lon=31.4833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nemsova, City ID:3058546, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.9666667&lon=18.1166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oleiros, City ID:3115177, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.333333&lon=-8.316667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Zhigalovo, City ID:2012532, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.809722&lon=105.157778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Quemado de Guines, City ID:3543077, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=22.7852778&lon=-80.2536111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Araure, City ID:3649017, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.5666667&lon=-69.2166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kato Achaia, City ID:260644, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=38.15&lon=21.55&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Codroipo, City ID:3178496, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.96&lon=12.979167&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Willow Grove, City ID:5219619, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.1438889&lon=-75.1161111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rajpipla, City ID:1258819, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=21.783333&lon=73.566667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pamekasan, City ID:1632978, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-7.1568&lon=113.4746&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Patao, City ID:1694432, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.2202&lon=123.6925&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Janoshalma, City ID:3050967, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.298611&lon=19.325833&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Valbonne, City ID:2971117, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=43.641272&lon=7.005747&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Portel, City ID:3391412, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-1.95&lon=-50.816667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gebog, City ID:1644360, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-6.735&lon=110.8444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Beaverton, City ID:5897183, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.433333&lon=-79.15&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gorlev, City ID:2621304, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.540585&lon=11.228593&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cabul-an, City ID:1721381, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.15&lon=124.05&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Talitsy, City ID:484770, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.530118&lon=42.163202&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jiabong, City ID:1710216, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.7625&lon=124.951944&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Rampura, City ID:1258584, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=30.25&lon=75.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Caba, City ID:1722068, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=16.4316&lon=120.3446&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gamla Staden, City ID:2712995, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.6&lon=13.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Smyrna, City ID:4144764, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.2997222&lon=-75.605&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Petionville, City ID:3719028, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=18.5125&lon=-72.2852778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Narasingapuram, City ID:1261844, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.616667&lon=79.333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Anori, City ID:3665315, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-3.783333&lon=-61.633333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Khowai, City ID:1266649, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=24.1&lon=91.633333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Carastelec, City ID:682712, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.3&lon=22.7&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mufulira, City ID:905395, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-12.55&lon=28.2333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sieu-Odorhei, City ID:667235, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.15&lon=24.316667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tlalpujahua de Rayon, City ID:3981464, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.8&lon=-100.166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Vigia del Fuerte, City ID:3666042, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=6.578911&lon=-76.886278&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hrusovany nad Jevisovkou, City ID:3074764, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.833333&lon=16.4&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ngorongoro, City ID:151610, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-3.25&lon=35.5166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Corat, City ID:586631, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.5725&lon=49.706389&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bereza, City ID:577384, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=53.51833&lon=50.139671&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tekeli, City ID:1518296, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.83&lon=78.823889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nikolsk, City ID:521773, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=59.535315&lon=45.457434&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:La Gomera, City ID:3594575, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.083333&lon=-91.05&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Layou, City ID:3577879, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.2&lon=-61.2666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Leca do Bailio, City ID:2738347, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.214567&lon=-8.613484&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Balagtas, City ID:1728584, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.816667&lon=120.866667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Wilkinsburg, City ID:5219501, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.4416667&lon=-79.8822222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sainte-Suzanne, City ID:6690304, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-20.9&lon=55.6166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Haan, City ID:2913195, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.2&lon=7.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Chandwaji, City ID:1274671, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=27.166667&lon=75.716667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:El Giral, City ID:3710808, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=9.2491667&lon=-79.6927778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dubove, City ID:709516, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=48.17205&lon=23.889545&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Konskie, City ID:768218, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=51.191432&lon=20.408217&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Thohoyandou, City ID:949224, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-22.945642&lon=30.484972&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Fullerton, City ID:5190679, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.6316667&lon=-75.4736111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sladkovo, City ID:1491719, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.528348&lon=70.338545&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Filandia, City ID:3682473, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=4.674722&lon=-75.658333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Moramanga, City ID:1058532, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-18.9333333&lon=48.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Flawil, City ID:2660762, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.414611&lon=9.182838&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Besana in Brianza, City ID:3182119, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.7&lon=9.283333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Pedro Atlixco, City ID:3518019, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=18.966667&lon=-98.466667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hayanist, City ID:616632, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.1197222&lon=44.3775&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dorogino, City ID:1507239, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.299&lon=83.331&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Parish of Saint Mary, City ID:3576018, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=17.0166667&lon=-61.8333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Soars, City ID:666600, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.933333&lon=24.916667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bilwang, City ID:1725232, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.8834&lon=124.4667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lidzbark Warminski, City ID:766307, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.128687&lon=20.57807&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Berezayka, City ID:577375, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=57.988056&lon=33.873333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bali Chak, City ID:1277581, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=22.366667&lon=87.55&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ostān-e Gīlān, City ID:133349, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=36.8049&lon=49.408&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Savanur, City ID:1256967, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.966667&lon=75.35&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Haysville, City ID:4272788, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=37.5644444&lon=-97.3519444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Welkom, City ID:940909, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-27.986442&lon=26.706612&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:El Llano, City ID:3611356, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.15&lon=-87.8833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Culfa, City ID:148251, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=38.8479&lon=45.6623&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jamsa, City ID:656083, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=61.866667&lon=25.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ozark, City ID:4081936, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=31.4588889&lon=-85.6405556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bloomingdale, City ID:4885156, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.9575&lon=-88.0808333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bairro Vista Alegre, City ID:7537374, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-22.870755&lon=-43.773821&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dattapur, City ID:1273397, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.766667&lon=78.166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Townsend, City ID:4953221, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.6666667&lon=-71.7055556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Høyknes, City ID:3151545, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=64.466667&lon=11.75&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Luis, City ID:3837056, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-33.295012&lon=-66.335627&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Obshtina Elin Pelin, City ID:731674, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.6666667&lon=23.6&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Köttenich, City ID:2885163, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.9&lon=6.283333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Lom Sak, City ID:1609043, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=16.779834&lon=101.24225&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Melchor Ocampo, City ID:3827586, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.699722&lon=-99.1475&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sitamarhi, City ID:1255983, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.6&lon=85.483333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hārom, City ID:131965, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=28.5024&lon=53.5534&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Novi Sad, City ID:3194360, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.251667&lon=19.836944&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Abilay, City ID:1732426, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.733333&lon=122.5&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sao Lourenco, City ID:3448616, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-22.116667&lon=-45.05&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gornaya Zdravnitsa, City ID:708408, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.457138&lon=34.140632&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Swamimalai, City ID:1255283, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.95&lon=79.333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Jose Iturbide, City ID:3986088, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=21.0&lon=-100.383333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hathras, City ID:1270216, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=27.6&lon=78.05&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kavaratti, City ID:1267390, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=10.566667&lon=72.616667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Porto Tolle, City ID:3170070, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.933333&lon=12.366667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Amursk, City ID:2027749, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.226111&lon=136.899444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Zhize, City ID:1913375, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=21.617844&lon=111.336796&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Karlskrona, City ID:2701713, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.166667&lon=15.583333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Harsova, City ID:676163, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=44.683333&lon=27.933333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sardhana, City ID:1257196, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=29.15&lon=77.616667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bad Waldsee, City ID:2953320, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.916667&lon=9.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Horana South, City ID:1243867, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=6.7166667&lon=80.06&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Xinying, City ID:1668353, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=23.3783333&lon=120.1583333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ocho Rios, City ID:3489239, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=18.4166667&lon=-77.1166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nombre de Dios, City ID:3994863, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=23.85&lon=-104.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Laslea, City ID:675003, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.216667&lon=24.65&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Triebendorf, City ID:7872481, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.15&lon=14.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Dumarais, City ID:1714149, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.434552&lon=120.692132&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Madridejos, City ID:1704126, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.298&lon=123.7339&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Moirang, City ID:1262863, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=24.5&lon=93.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Marly, City ID:2995656, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.345561&lon=3.549588&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Adela, City ID:1732246, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=12.441643&lon=120.972913&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Samoded, City ID:499025, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=63.6083&lon=40.5111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Slimnic, City ID:666728, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.916667&lon=24.166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Meliti, City ID:735220, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.7833333&lon=21.6833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bukit Rambai, City ID:1778290, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=2.2594&lon=102.1838&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Muna, City ID:3522886, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.483333&lon=-89.716667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Na Klang, City ID:1604654, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=17.307195&lon=102.188861&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mrgashen, City ID:616399, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.285&lon=44.5422222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ubstadt-Weiher, City ID:6555615, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.170833&lon=8.618889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tisul, City ID:1489554, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.532778&lon=88.141111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kuvshinovo, City ID:538104, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=57.029532&lon=34.172518&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Asuaju de Sus, City ID:686071, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.566667&lon=23.183333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Markwaldsiedlung, City ID:2873270, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.15&lon=8.95&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Leon Postigo, City ID:1729537, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=8.1551&lon=122.9311&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Stafa, City ID:2658518, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.239059&lon=8.725646&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Valparaiso, City ID:3666291, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=1.19512&lon=-75.707053&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cavinti, City ID:1717649, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=14.244817&lon=121.507974&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Gosainganj, City ID:1270895, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.583333&lon=82.383333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Peruibe, City ID:3454061, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-24.316667&lon=-47.0&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sinja, City ID:366847, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.15&lon=33.9333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cacota, City ID:3688087, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.267872&lon=-72.641969&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Pendapolis, City ID:734719, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=41.0166667&lon=23.7&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Atulayan, City ID:1729953, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=17.6648&lon=121.6937&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Camaqua, City ID:3468014, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-30.85&lon=-51.816667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:New Yekepa, City ID:2272790, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=7.5794444&lon=-8.5377778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Mananara Avaratra, City ID:1061412, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-16.1666667&lon=49.7666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santa Maria Moyotzingo, City ID:3517231, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=19.25&lon=-98.4&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Hellange, City ID:2960470, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=49.5066667&lon=6.1505556&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sulgen, City ID:2658455, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.5377&lon=9.18497&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Xinpu, City ID:1788694, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=34.599722&lon=119.159444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sendai, City ID:1852736, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=31.816667&lon=130.3&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:San Lorenzo, City ID:3601977, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=13.4463889&lon=-87.475&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Al Janādilah, City ID:361024, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=29.0638889&lon=31.0888889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Nonoichi, City ID:1854979, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=36.533333&lon=136.616667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Corni, City ID:680746, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=45.85&lon=27.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Skoropuskovskiy, City ID:492333, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=56.366667&lon=38.166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Harrisburg, City ID:5192726, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=40.2736111&lon=-76.8847222&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tasco, City ID:3667373, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=5.910443&lon=-72.780012&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Grass Valley, City ID:5353775, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=39.2191667&lon=-121.06&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ware, City ID:4954477, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.2597222&lon=-72.2402778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Brejinho, City ID:3404924, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-6.183333&lon=-35.35&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cianorte, City ID:3466174, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-23.616667&lon=-52.616667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Paracuaro, City ID:3993455, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=20.15&lon=-100.766667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Matiompong, City ID:1700282, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=6.681667&lon=124.576944&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ambatondrazaka, City ID:1082639, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-17.8333333&lon=48.4166667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ara, City ID:1278483, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=25.566667&lon=84.666667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Oeiras, City ID:3393764, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-7.016667&lon=-42.133333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Komarikhinskiy, City ID:545938, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=58.0979&lon=57.1163&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Santa Maria, City ID:1688031, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=15.5232&lon=120.7925&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Wuxi, City ID:1797417, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.573073&lon=111.841839&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kudryashovskiy, City ID:1501573, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.0974&lon=82.7742&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Weleri, City ID:1621655, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-7.0425&lon=109.8851&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Ondoy, City ID:1697110, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=11.819167&lon=122.126111&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Jaguarari, City ID:3460225, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-10.266667&lon=-40.2&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Atocha, City ID:3923570, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-20.9333333&lon=-66.2333333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Budhlada, City ID:1275147, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=29.933333&lon=75.566667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tolmachevo, City ID:1489474, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=54.9824&lon=82.7363&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Järvamaa, City ID:591961, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=58.8855556&lon=25.4463889&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Bacesti, City ID:685934, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=46.85&lon=27.233333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kelme, City ID:598257, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=55.6338889&lon=22.9341667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Cunha, City ID:3465010, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-23.083333&lon=-44.966667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Zemen, City ID:725402, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=42.4788889&lon=22.7491667&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Strzelin, City ID:3084404, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=50.783958&lon=17.066399&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Sutto, City ID:3045045, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=47.758865&lon=18.448728&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Saurimo, City ID:145531, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-9.66078&lon=20.391553&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Enniscorthy, City ID:2964403, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=52.5008333&lon=-6.5577778&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Tikaitnagar, City ID:1254536, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=26.95&lon=81.583333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:North Miami, City ID:4166232, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=25.8897222&lon=-80.1869444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Kidodi, City ID:157826, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=-7.6&lon=36.9833333&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------
    Request Successful--- City Name:Obigarm, City ID:1220888, Requested URL:http://api.openweathermap.org/data/2.5/weather?lat=38.72&lon=69.7094444&units=imperial&appid=0e3ca66002a972af2395e8ea9b901de9
    ---------------



```python
#Export Retreived data to csv file
city_df = pd.DataFrame(city_responses)
city_df.to_csv('city_responses.csv')

#Check length of responses to ensure 500 data points for every field
print(len(Name),len(Cloudiness),len(Country),len(Date),len(Humidity),len(lat_owm),len(lng_owm),len(Max_temp),len(Wind_speed))
```

    500 500 500 500 500 500 500 500 500



```python
#Convert lists to Data Frame
weather_dic = {
    'Name': Name,
    'Cloudiness %': Cloudiness,
    'Country': Country,
    'Date': Date,
    'Humidity %': Humidity,
    'Latitude': lat_owm,
    'Longitude': lng_owm ,
    'Max Temperature': Max_temp,
    'Wind Speeds': Wind_speed
}

weather_df = pd.DataFrame(weather_dic)
weather_df.head(15)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cloudiness %</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity %</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Max Temperature</th>
      <th>Name</th>
      <th>Wind Speeds</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>75</td>
      <td>NZ</td>
      <td>1521572400</td>
      <td>93</td>
      <td>-40.35</td>
      <td>175.62</td>
      <td>59.00</td>
      <td>Terrace End</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>75</td>
      <td>AM</td>
      <td>1521572400</td>
      <td>40</td>
      <td>40.60</td>
      <td>44.35</td>
      <td>53.60</td>
      <td>Aparan</td>
      <td>11.41</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>RO</td>
      <td>1521574200</td>
      <td>83</td>
      <td>44.40</td>
      <td>23.73</td>
      <td>32.00</td>
      <td>Isalnita</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20</td>
      <td>PH</td>
      <td>1521574627</td>
      <td>93</td>
      <td>8.51</td>
      <td>126.01</td>
      <td>71.36</td>
      <td>Alegria</td>
      <td>1.92</td>
    </tr>
    <tr>
      <th>4</th>
      <td>88</td>
      <td>RU</td>
      <td>1521574627</td>
      <td>71</td>
      <td>54.06</td>
      <td>35.96</td>
      <td>12.68</td>
      <td>Sosenskiy</td>
      <td>2.93</td>
    </tr>
    <tr>
      <th>5</th>
      <td>40</td>
      <td>IT</td>
      <td>1521573600</td>
      <td>82</td>
      <td>40.53</td>
      <td>17.58</td>
      <td>55.40</td>
      <td>Francavilla Fontana</td>
      <td>14.99</td>
    </tr>
    <tr>
      <th>6</th>
      <td>76</td>
      <td>RU</td>
      <td>1521574628</td>
      <td>66</td>
      <td>53.97</td>
      <td>37.70</td>
      <td>7.82</td>
      <td>Lipki</td>
      <td>2.93</td>
    </tr>
    <tr>
      <th>7</th>
      <td>92</td>
      <td>RU</td>
      <td>1521574628</td>
      <td>91</td>
      <td>54.84</td>
      <td>75.08</td>
      <td>19.07</td>
      <td>Okoneshnikovo</td>
      <td>4.61</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>RU</td>
      <td>1521572400</td>
      <td>78</td>
      <td>52.20</td>
      <td>39.09</td>
      <td>15.80</td>
      <td>Khlevnoye</td>
      <td>8.95</td>
    </tr>
    <tr>
      <th>9</th>
      <td>75</td>
      <td>HU</td>
      <td>1521571500</td>
      <td>72</td>
      <td>47.69</td>
      <td>18.72</td>
      <td>33.80</td>
      <td>Csolnok</td>
      <td>11.41</td>
    </tr>
    <tr>
      <th>10</th>
      <td>90</td>
      <td>US</td>
      <td>1521573300</td>
      <td>54</td>
      <td>40.59</td>
      <td>-122.39</td>
      <td>57.20</td>
      <td>Redding</td>
      <td>13.87</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>TJ</td>
      <td>1521574630</td>
      <td>91</td>
      <td>39.01</td>
      <td>70.16</td>
      <td>31.22</td>
      <td>Novobod</td>
      <td>1.70</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>DE</td>
      <td>1521571800</td>
      <td>80</td>
      <td>51.90</td>
      <td>11.77</td>
      <td>30.20</td>
      <td>Calbe</td>
      <td>10.29</td>
    </tr>
    <tr>
      <th>13</th>
      <td>75</td>
      <td>IE</td>
      <td>1521572400</td>
      <td>81</td>
      <td>51.90</td>
      <td>-8.50</td>
      <td>35.60</td>
      <td>Gurranebraher</td>
      <td>9.17</td>
    </tr>
    <tr>
      <th>14</th>
      <td>88</td>
      <td>RU</td>
      <td>1521574630</td>
      <td>86</td>
      <td>59.16</td>
      <td>57.56</td>
      <td>17.36</td>
      <td>Aleksandrovsk</td>
      <td>13.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Scatter plot for Lat vs Temp
plt.figure(figsize=(15,10))
plt.scatter(weather_df['Latitude'],weather_df['Max Temperature'], marker='o',color='orange', s=30)
plt.title('City Latitude vs. Max Temperature (03/19/19)')
plt.xlabel('Latitude')
plt.ylabel('Max Temp (F)')
plt.savefig('Lat_vs_Temp.png')
plt.show()
```


![png](output_6_0.png)



```python
#Scatter plot for Lat vs Humidity
plt.figure(figsize=(15,10))
plt.scatter(weather_df['Latitude'],weather_df['Humidity %'], marker='p', color='skyblue', s=35)
plt.title('City Latitude vs. Humidity (03/19/19)')
plt.xlabel('Latitude')
plt.ylabel('Humidity (%)')
plt.savefig('Lat_vs_Humid.png')
plt.show()
```


![png](output_7_0.png)



```python
#Scatter plot for Lat vs Cloudiness
plt.figure(figsize=(15,10))
plt.scatter(weather_df['Latitude'],weather_df['Cloudiness %'], marker='^', color='blue', s=70)
plt.title('City Latitude vs. Cloudiness (03/19/19)')
plt.xlabel('Latitude')
plt.ylabel('Cloudiness (%)')
plt.savefig('Lat_vs_Cloud.png')
plt.show()
```


![png](output_8_0.png)



```python
#Scatter plot for Lat vs Wind Speeds
plt.figure(figsize=(15,10))
plt.scatter(weather_df['Latitude'],weather_df['Wind Speeds'], marker='x', color='purple', s=50)
plt.title('City Latitude vs. Wind Speeds (03/19/19)')
plt.xlabel('Latitude')
plt.ylabel('Wind Speeds (mph)')
plt.savefig('Lat_vs_Winds.png')
plt.show()
```


![png](output_9_0.png)

