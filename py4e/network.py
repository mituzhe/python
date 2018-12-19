'''
import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) #\r\n is 'Enter'
#encode()作用是字符编码方式由 Unicode 转为 UTF-8，字符串转字节流

while True:
    data = mysock.recv(512)#内容是 Bytes，未解码
    if (len(data) < 1):
        break
    print(data.decode())#解码为 Unicode
#decode()作用于encode()相反
mysock.close()
'''
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
for k,v in counts.items():
    print(k, '\t', v)
'''
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')#http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retreive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
