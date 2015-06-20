import requests
from bs4 import BeautifulSoup

url = 'http://www.w3schools.com/html/html_tables.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()

# import requests
#
# url = 'http://www.w3schools.com/html/html_tables.asp'
# response = requests.get(url)
# html = response.content
# print html
