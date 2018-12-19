import requests
import http.cookiejar as cookielib
import re

def naturoLogin(account, password):
    print("登录。。。")

    postUrl = 'https://chan.sankakucomplex.com/user/login'
    postData = {
        'name':account,
        'password':password
    }
    responseRes = naturoSession.post(postUrl, data = postData, headers = header)

def getPage_html(url):
    page = requests.get(url)
    page.encoding = 'utf-8'
    html = page.text
    return html

HOME_URL = 'https://chan.sankakucomplex.com/?tags=naruto_pixxx&page='
ALBUM_HEAD = 'https://chan.sankakucomplex.com'

naturoSession = requests.session()
naturoSession.cookies = cookielib.LWPCookieJar(filename = 'naturoCookies.txt')

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
header = {
    'referer':'https://chan.sankakucomplex.com/user/login',
    'user-agent':userAgent
}

naturoLogin('377745949@qq.com','123456')

page = 26# 已下1-25
img_source_url_list = list()

while page <= 26:
    page = page + 1
    home_html = getPage_html(HOME_URL + str(page))
    album_url = re.findall('/post/show/[0-9]+', home_html)

    for img in album_url:
        img_html = getPage_html(ALBUM_HEAD + img)
        img_source_url_list += re.findall('a href="//(cs.sankakucomplex.com/data/[^(sample)]\S+)"',img_html)

img_source_url_list = list(set(img_source_url_list))
print(len(img_source_url_list))

for index,img_source_url in enumerate(img_source_url_list):
    pos = img_source_url.find('amp;')
    img_source_url = img_source_url[:pos] + img_source_url[pos+4:]
    jpg = re.search('(\.jpg)|(\.png)|(\.gif)', img_source_url).group(0)
    #pos = img_source_url.find('jpg')
    print(img_source_url)
    response = requests.get('https://'+img_source_url)
    with open('d:/pic/%s%s'%(index, jpg), 'wb') as pic:
        pic.write(response.content)

exit()
