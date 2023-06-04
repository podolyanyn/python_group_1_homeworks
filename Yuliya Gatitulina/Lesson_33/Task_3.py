import requests

city = input('Please enter the name of the city where you want to find out the current weather: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=83b95903dfb40272c80bcf179d493b2f&units=metric'
rec = requests.get(url)
while not rec.ok:
    city = input('A city that does not exist or there is an error in the city name; enter the city name again: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=83b95903dfb40272c80bcf179d493b2f&units=metric'
    rec = requests.get(url)
#print(rec.json())
print('The weather is: ')
weather_parameters = rec.json()['weather'][0]['description']
print ('weather parameters -', weather_parameters)
temperature = rec.json()['main']['temp']
print ('temperature -', temperature, 'degrees by Celsius')
feeling_temperature = rec.json()['main']['feels_like']
print ('feeling temperature -', feeling_temperature, 'degrees by Celsius')
pressure = rec.json()['main']['pressure']
print ('pressure -', pressure, 'hPa')
humidity = rec.json()['main']['humidity']
print ('humidity -', humidity, '%')
wind_speed = rec.json()['wind']['speed']
print ('wind speed -', wind_speed, 'meter/sec')