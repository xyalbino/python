import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def main():
    keyword=input("请输入关键字:")
    keyword=urllib.parse.urlencode({"word":keyword})
    #print(keyword)
    response=urllib.request.urlopen("http://baike.baidu.com/search/word?%s"%keyword)
    html=response.read()
    soup=BeautifulSoup(html,"html.parser")

    for each in soup.find_all(href=re.compile("view")):
        content=each.text
        #url2=''.join(["http://baike.baidu.com",each["href"]])
        url2="http://baike.baidu.com"+each["href"]
        response2=urllib.request.urlopen(url2)
        html2=response2.read()
        soup2=BeautifulSoup(html2,"html.parser")
        if soup2.h2:
            content=''.join([content,soup2.h2.text])
        content=''.join([content,"->",url2])
        print(content)
if __name__=="__main__":
    main()
