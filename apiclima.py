import requests

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

BASE_URL = 'api.openweathermap.org/data/2.5/weather?'
API_KEY = '245ae14e177ce5454d6ee079807d7cb9' 

city = input('Bote o nome da cidade: ')
request_url = f'{BASE_URL}q={city}&appid={API_KEY}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15)
    
    print("Weather", weather,)
    print("Temperature", temperature, "celsius")
else:
    print("Um erro aconteceu")