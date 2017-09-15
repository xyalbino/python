from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
import urllib
import requests

se=requests.session()
 
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'https://tieba.baidu.com/p/3318717005'  ##开始的URL地址
all_url=urllib.request.urlopen(all_url)
html=all_url.read()
Soup=BeautifulSoup(html,"html.parser")

#start_html = requests.get(all_url,headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
#Soup = BeautifulSoup(start_html.text, 'html.parser') ##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
all_a = Soup.find_all('div', class_='d_post_content j_d_post_content ') ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
name=0
os.chdir("D:\Python34\darkcloud")
for a in all_a:
    content = '\n'.join([a.text]) #取出a标签的文本
    name=name+1
    
    f = open(str(name)+'.txt', 'w+')##写入多媒体文件必须要 b 这个参数！！必须要！！
    #with open('darkcloud.txt','wb') as f:
    f.writelines(content) ##多媒体文件要是用conctent哦！
    f.close
