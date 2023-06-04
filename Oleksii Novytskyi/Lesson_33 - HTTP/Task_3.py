import requests


def weather_app(city_name):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=dbf6455ad98e3999bfaead3775d141eb&units=metric'

    resp = requests.get(url)

    if resp.status_code == 404:
        return 'Сity not found or check what you wrote :) '

    if resp.status_code:
        rez = resp.json()

        temperature = rez['main']['temp']
        feels = rez['main']['feels_like']
        max_temp = rez['main']['temp_max']
        wind_speed = rez['wind']['speed']
        sky_status = rez['weather'][0]['description']
        # print(rez)
        return (f'\n Temperature: {temperature}°C\n Feels like: {feels}°C\n The max temperature during the day: {max_temp}°C\n '
              f'The speed of the wind : {wind_speed}m/c\n The sky status: {sky_status}\n')
    else:
        print('Somthing went wrong')


if __name__ == '__main__':
    city_name = input('select the city for the Weather info for the present day: ')
    print(weather_app(city_name))