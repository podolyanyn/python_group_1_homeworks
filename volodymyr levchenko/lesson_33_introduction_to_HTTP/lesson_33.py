# # Task 1
# import requests
#
# def open_and_save_to_file(url):
#     response = requests.get(url)
#     with open('common_robots.txt', 'a', encoding="utf-8") as file:
#         file.write(url + '\n')
#         file.write(response.text)
#         file.write('\n'+'~'*30 + '\n')
#
# if __name__ == '__main__':
#     wikipedia = " https://en.wikipedia.org/robots.txt"
#     twitter = "https://twitter.com/robots.txt"
#     instagram = "https://www.instagram.com/robots.txt"
#     url_list = [wikipedia, twitter, instagram]
#     for url in url_list:
#         open_and_save_to_file(url)
# # Task 3
# import os
# import requests
# import sys
#
# def weather(city):
#     weather_url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {
#         'q':city,
#         'appid':'d3c255253f33557bd50975a14be70671',
#         'units':'metric'
#     }
#     print()
#     response = requests.get(weather_url, params = params)
#     data = response.json()
#     if response.status_code == 200:
#         print(f"""Weather in {city}:
# {data['main']['temp']}°C, {data['weather'][0]['description']}""")
#     else:
#         print(f'Can\'t find weather data for {city}.\nCheck if you\'ve entered correct city name')
#
#
# if __name__ == '__main__':
#     while True:
#         city = input('Enter city name (press "q" to quit): ')
#         if city == 'q':
#             sys.exit()
#         weather(city)

