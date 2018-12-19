import urllib.request,urllib.parse,urllib.error
#import urllib2
import os
from bs4 import BeautifulSoup

def getAllImageLink():
    html = urllib2.request.urlopen('http://ac.qq.com/').read()
    soup = BeautifulSoup(html,'html.parser')

    liResult = soup.findall('img')

    count = 0
    for image in liResult:
        count += 1
        link = image.get('src')
        imageName = count
        fileSavePath = 'd:/pic/%s.jpg'%imageName
        print(fileSavePath)
        urllib.urlretrieve(link,fileSavePath)
        print(fileSavePath)
if __name__ == '__main__':
    getAllImageLink()
