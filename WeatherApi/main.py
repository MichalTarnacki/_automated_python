import requests
def get_weather(city, key):
    city = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}").json()
    r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={city[0]['lat']}&lon={city[0]['lon']}&units=metric&appid={key}")
    r = r.json()
    weather = []
    for i in r['list']:
        weather.append(f"{city[0]['name']}, {i['dt_txt']}, {i['main']['temp']}, {i['weather'][0]['description']}")
    return weather


with open('/Users/michal/Documents/WeatherApiKey') as f:
    api_key = f.read().strip()

with open('weather.txt', 'a+') as f:
    f.seek(len(f.readline()))
    f.writelines(map(lambda x: x + '\n', get_weather('Gdansk', api_key)))

