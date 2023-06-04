import requests

url_1 = 'https://uk.wikipedia.org/robots.txt'
url_2 = 'https://twitter.com/robots.txt'


rez_1 = requests.get(url_1)
rez_2 = requests.get(url_2)

if rez_1.status_code:
    with open("robots_wiki.txt", "wb") as file_1:
        file_1.write(rez_1.content)
        print("You are legendary downloader :)")
else:
    print('somthing wrong')

if rez_2.status_code:
    with open("robots_twit.txt", "wb") as file_2:
        file_2.write(rez_1.content)
        print("You are legendary downloader twice:)")
else:
    print('Somthing went wrong')

