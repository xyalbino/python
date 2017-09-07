import urllib.request
import urllib.parse
import json

content=input("输入内容：")
url="http://fanyi.youdao.com/translate?samrtresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
##设置head参数，伪造成浏览器访问
head={}
head['Referer']='http://fanyi.youdao.com'
head['User-Agent']='Mozilla/5.0(Macintosh; Intel Mac OS X 10_10_1)AppleWebKit/537.36(KHTML,like Gecko) Chrome/39.9.2171.95 Safari/537.36X-Requested-With:XMLHttpRequest'
##data参数赋值，为POST方式
data={
    'type':'AUTO',
    'i':content,
    'doctype':'json',
    'xmlVersion':'1.6',
    'keyfrom':'fanyi.web',
    'ue':'UTF-8',
    'typoResult':'true'
    }
#data['type']='AUTO'
#data['i']=content
#data['doctype']='json'
#data['xmlVersion']='1.6'
#data['keyfrom']='fanyi.web'
#data['ue']='UTF-8'
#data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')
target=json.loads(html)
print("翻译结果:%s"% (target['translateResult'][0][0]['tgt']))

