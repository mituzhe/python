import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

BASE_URL = 'https://chan.sankakucomplex.com/?tags=naruto_pixxx'
url = 'https://cs.sankakucomplex.com/data/3f/de/3fde36d832379d82163da1a220790a12.jpg?e=1545052335&m=0BK7FCDOGWq21yCtg1Qlfw'
NUMS = 10

html = urllib.request.urlopen(BASE_URL).read()
soup = BeautifulSoup(html,'html.parser')

#print(type(soup))
