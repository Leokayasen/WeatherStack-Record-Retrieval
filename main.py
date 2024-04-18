import requests

API_KEY = "38c2d5cb977fe2306231c68517b66f22"
WS_URL = "http://api.weatherstack.com/current"

City = input("Enter a city: ")
parameters = {'access_key': API_KEY, 'query': City}
response = requests.get(WS_URL, parameters)
js = response.json()
print(js)
print()

temperature = js['current']['temperature']
date = js['location']['localtime']
city = js['location']['name']
country = js['location']['country']

print(f"The temperature in {city}, {country} on {date} is {temperature} degrees Celsius")
