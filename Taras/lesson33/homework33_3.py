import requests

API_KEY = '6ad07ee3a415791ad05c75005345f831'


def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'  # forming a URL
    # for a weather request
    response = requests.get(url)
    data = response.json()  # receive the response in JSON format and save it
    if response.status_code == 200:  # check whether the request status code is 200 which indicates a successful request
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        result = f'Weather in the city: {city_name}:\n'  # initialize the variable result with the initial text about
        # the weather in the city
        result += f'Temperature: {temperature}°C\n'  # add information about the temperature
        result += f'Humidity: {humidity}%\n'
        result += f'Description: {description}\n'
        return result
    else:
        return None


city = input('Enter the name of the city: ')  # ask the user about the name of the city
weather = get_weather(city)
if weather:  # check whether the "weather" variable contains weather data
    print(weather)
else:
    print('Failed to get weather. Try again.')

# з цим просив допомоги трішки, але до кінця так і не зміг розібратися. Не хоче виводити информацію :(

