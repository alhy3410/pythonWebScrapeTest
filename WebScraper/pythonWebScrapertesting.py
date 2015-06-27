import requests
from bs4 import BeautifulSoup
import re

url1 = "http://www.gi.alaska.edu/AuroraForecast/NorthAmerica"
response = requests.get(url1)
html = response.content

soup = BeautifulSoup(html)

# print(soup.prettify().encode('cp850',errors='ignore'))
print '\n'
print soup.findAll('div', {"class" : "levels"})

levels = soup.findAll('div', {"class" : "levels"})

print '\n'
print soup.findAll('div', {"class" : "image"})

image = soup.findAll('div', {"class" : "image"})
print '\n'

x=str(image[0])
matches= re.findall(r'\"/sites(.+?)\"', x)

print matches
print "http://www.gi.alaska.edu/sites" + matches[0]
