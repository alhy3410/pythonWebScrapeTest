import requests
from bs4 import BeautifulSoup
import re
import twitter

api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='-',
    access_token_secret='')


#set up for web scraping
url = "http://www.events12.com/portland/july/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

print '\n'
# print soup.findAll('div', {"class" : "levels"})
events = soup.findAll('div', {"class" : "event"})

all_events = []

for event in events:
    all_events.append(event.get_text().encode('cp850',errors='ignore'))

for e in all_events:
    print e
