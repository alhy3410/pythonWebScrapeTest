import requests
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# print(soup.prettify().encode('cp850',errors='ignore'))

print soup.find_all('tr')
# import requests
#
# url = 'http://www.w3schools.com/html/html_tables.asp'
# response = requests.get(url)
# html = response.content
# print html
