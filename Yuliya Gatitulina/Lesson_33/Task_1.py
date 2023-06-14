import requests

urlwiki = 'https://en.wikipedia.org/robots.txt'
urltwit = 'https://twitter.com/robots.txt'
wiki = requests.get(urlwiki)
twit = requests.get(urltwit)

with open('wiki_robots.txt', 'w', encoding='utf-8') as wiki_r:
    wiki_r.write(wiki.text)
with open('twit_robots.txt', 'w', encoding='utf-8') as twit_r:
    twit_r.write(twit.text)




