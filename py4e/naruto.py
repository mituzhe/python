import requests
import http.cookiejar as cookielib
import re
# session代表某一次连接
naturoSession = requests.session()
# 原始session.cookies没有save()方法，所以用到cookielib中的LWPCookieJar
naturoSession.cookies = cookielib.LWPCookieJar(filename='naturoCookies.txt')

HOME_URL = 'https://chan.sankakucomplex.com/?tags=naruto_pixxx&page='
ALBUM_HEAD = 'https://chan.sankakucomplex.com'

# 模拟登录


def naturoLogin(account, password):
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    header = {
        'referer': 'https://chan.sankakucomplex.com/user/login',
        'user-agent': userAgent
    }
    print("登录。。。")
    postUrl = 'https://chan.sankakucomplex.com/user/authenticate'
    postData = {
        'user[name]': account,
        'user[password]': password}
    # 使用session直接post请求
    responseRes = naturoSession.post(postUrl, data=postData, headers=header)
    #print(f"statusCode = {responseRes.status_code}")
    #print(f"text = {responseRes.text}")
    # 登陆成功后，将cookie保存在本地
    naturoSession.cookies.save()
    print('登入成功！！！')


def isLogin():
    routeUrl = 'https://chan.sankakucomplex.com/user/home'
    # 下面有两个关键点
    # 第一个是header，如果不设置，会返回500的错误
    # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
    # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
    # allow_redirects = False  就是不允许重定向
    # , headers = header, allow_redirects = False)
    responseRes = naturoSession.get(routeUrl)
    print(f'isLogin Status = {responseRes.status_code}')
    if responseRes.status_code != 200:
        return False
    else:
        return True


def getPage_html(url):
    page = naturoSession.get(url)
    page.encoding = 'utf-8'
    return page.text


if __name__ == '__main__':
    naturoSession.cookies.load()
    isLogin = isLogin()
    print(f'Login Naturo: {isLogin}')
    if isLogin == False:
        print('cookie失效, 正在重新登录。。。')
        naturoLogin('377745949@qq.com', '1234567')

    page = 0
    img_source_url_list = list()
    while page <= 50:
        page = page + 1
        home_html = getPage_html(HOME_URL + str(page))
        album_url = re.findall('/post/show/[0-9]+', home_html)

        for img in album_url:
            img_html = getPage_html(ALBUM_HEAD + img)
            img_source_url_list += re.findall(
                'a href="//(cs.sankakucomplex.com/data/[^(sample)]\S+)"', img_html)

    img_source_url_list = list(set(img_source_url_list))
    print(len(img_source_url_list))

    for index, img_source_url in enumerate(img_source_url_list):
        pos = img_source_url.find('amp;')
        img_source_url = img_source_url[:pos] + img_source_url[pos + 4:]
        jpg = re.search('(\.jpg)|(\.png)|(\.gif)', img_source_url).group(0)
        #pos = img_source_url.find('jpg')
        print(img_source_url)
        response = requests.get('https://' + img_source_url)
        with open('d:/pic/%s%s' % (index, jpg), 'wb') as pic:
            pic.write(response.content)

    exit()
