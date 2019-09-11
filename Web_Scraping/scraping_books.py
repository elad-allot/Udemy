import requests
from bs4 import BeautifulSoup
# import time
page = requests.get('http://example.com/')

soup = BeautifulSoup(page.content, 'html.parser')

print("starting")
print(page.content)
print(soup.find('h1').string)