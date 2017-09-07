import urllib.request
import os
import re

def open_url(url):
    req=urllib.request.Request(url)
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')
    return html

def get_img(html):
    p=r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist=re.findall(p,html)
    try:
        os.mkdir("miku")
    except FileExitsError:
        pass
    os.chdir("miku")
    for each in imglist:
        filename= each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)

if __name__=='__main__':
    url="http://tieba.baidu.com/p/5302872134"
    get_img(open_url(url))
