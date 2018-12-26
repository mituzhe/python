import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import re
import threading
import threadpool
import time
#page = 0
naturoSession = requests.session()
naturoSession.cookies = cookielib.LWPCookieJar(filename='naturoCookies.txt')

# class myThread(threading.Thread):
#    def __init__(self, thread_id, name, counter):
#    super(myThread,self).__init__()
#self.thread_id = thread_id
#self.name = name
#self.counter = counter
#    def run(self):
#        print('start '+self.name)
#        downLoad(self.name,self.counter)
#        print('end '+self.name)


def naturoLogin(account, password):
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    header = {
        'referer': 'https://chan.sankakucomplex.com/user/login',
        'user-agent': userAgent
    }
    postUrl = 'https://chan.sankakucomplex.com/user/authenticate'
    postData = {
        'user[name]': account,
        'user[password]': password}
    # 使用session直接post请求
    print("登录。。。")
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
    # headers = header, allow_redirects = False)
    responseRes = naturoSession.get(routeUrl)
    print(f'isLogin Status = {responseRes.status_code}')
    if responseRes.status_code != 200:
        return False
    else:
        return True


def downLoad(page):
    album_url = []
    imgUrl_list = []
    imgUrl_Source = []
    print('Thread-', page, 'start')
    PARAMS = {'tags': 'naruto_pixxx', 'page': str(page)}
    
    homePage = naturoSession.get(HOME_URL, params=PARAMS)
    while homePage.status_code != 200:
        print('waiting...')
        time.sleep(200)
        homePage = naturoSession.get(HOME_URL, params=PARAMS)
        
    soup = BeautifulSoup(homePage.text, 'lxml')
    for link in soup.find_all('a'):
        album_url += re.findall('/post/show/[0-9]+', link.get('href'))
    album_url = list(set(album_url))
    print('post:', page, len(album_url))

    for url in album_url:
        postPage = naturoSession.get(ALBUM_HEAD + url)
        while postPage.status_code != 200:
            print('waiting...')
            time.sleep(200)
            postPage = naturoSession.get(ALBUM_HEAD + url)
        soup = BeautifulSoup(postPage.text, 'lxml')
        imgUrl_list += soup.find_all('a', id='highres',
                                     href=re.compile('//cs.sankakucomplex.com/data/'))
        time.sleep(2)
    print('imgurls:', page, len(imgUrl_list))

    for index, url in enumerate(imgUrl_list):
        tmpUrl = 'https:' + url.get('href')
        jpg = re.search('(\.jpg)|(\.png)|(\.gif)', tmpUrl).group(0)
        rsp = naturoSession.get(tmpUrl)
        while rsp.status_code != 200:
            print('waiting...')
            time.sleep(200)
            rsp = naturoSession.get(tmpUrl)
        with open('d:/pic/%s-%s%s' % (page, index, jpg), 'wb') as f:
            f.write(rsp.content)
        time.sleep(2)
        # print(thName,url.get('href'))


if __name__ == '__main__':

    naturoSession.cookies.load()
    isLogin = isLogin()
    print(f'Login Naturo: {isLogin}')
    if isLogin == False:
        print('cookie失效, 正在重新登录。。。')
        naturoLogin('377745949@qq.com', '1234567')
        naturoSession.cookies.load()

    HOME_URL = 'https://chan.sankakucomplex.com/'
    ALBUM_HEAD = 'https://chan.sankakucomplex.com'

    pages = [28]  # [page+28 for page in range(1)]
    pool = threadpool.ThreadPool(2)
    tasks = threadpool.makeRequests(downLoad, pages)
    [pool.putRequest(task) for task in tasks]
    pool.wait()
    #threads = [threading.Thread(target=downLoad,args=(page,)) for page in range(5)]
    # for t in threads:
    #    t.start()
    # for t in threads:
    # t.join()
    # while page < 5:
    #page = page + 1
    #    t = myThread(page,'Thread-'+str(page),page)
    # t.start()
    # t.join()
