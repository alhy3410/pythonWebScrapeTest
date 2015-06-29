import requests
from bs4 import BeautifulSoup
import re
import twitter
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)

api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='-',
    access_token_secret='')


#set up for web scraping
url = "http://www.gi.alaska.edu/AuroraForecast/NorthAmerica"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

# print(soup.prettify().encode('cp850',errors='ignore'))
print '\n'
# print soup.findAll('div', {"class" : "levels"})
levels = soup.findAll('div', {"class" : "levels"})
levnum = str(levels[0])
lev = re.findall(r'\a*l">(.+?)\</span>', levnum)
num = re.findall(r'\a*n">(.+?)\</span>', levnum)

# lev = re.sub('<[^>]*>', '', levnum)
# print '\n'

# For the Image
# print soup.findAll('div', {"class" : "image"})
image = soup.findAll('div', {"class" : "image"})
x=str(image[0])
matches= re.findall(r'\"/sites(.+?)\"', x)
finalSite = "http://www.gi.alaska.edu/sites" + matches[0]
# print matches
# print finalSite


# For the time
timestamp = "Aurora Forecast for "  + time.strftime("%x")
result = " " + lev[0] + num[0] + "/9. Link: "
# Final Result
tweetIt = timestamp + result + url
# print tweetIt


##scheduler
def tweetItOut():
    status = api.PostUpdate(tweetIt)
    print status.text

def scheduler_tweetItOut():
    scheduler.enter(0, 1, tweetItOut, ())
    scheduler.run()
    time.sleep(14400)

# print 4 times a day for a year
for i in range(100):
    scheduler_tweetItOut()
