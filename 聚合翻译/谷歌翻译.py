import re,winreg,requests
key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings')
count=winreg.QueryInfoKey(key)[1]
for i in range(count):
    name=winreg.EnumValue(key,i)[0]
    command=winreg.EnumValue(key,i)[1]
    if name=='ProxyEnable':
        proxyenable=command
    if name=='ProxyServer':
        if proxyenable==0:
            proxyserver=''
        else:
            proxyserver=command
winreg.CloseKey(key)
string=input('输入字符串：')
landata={'query':string}
lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata,proxies={'http':proxyserver,'https':proxyserver})
lan=lanhtml.json()['lan']
if lan=='zh':
    to='en'
else:
    to='zh-CN'
url='https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc&f.sid=-2984828793698248690&bl=boq_translate-webserver_20201221.17_p0&hl=zh-CN&soc-app=1&soc-platform=1&soc-device=1&_reqid=5445720&rt=c'
data={'f.req':r'[[["MkEWBc","[[\"%s\",\"auto\",\"%s\",true],[null]]",null,"generic"]]]'%(string,to)}
resp=requests.post(url,data=data,proxies={'http':proxyserver,'https':proxyserver})
result=re.findall(r'null,\[\[\\"(.+?)\\",null,null,null',resp.text)[0]
print(result)