import winreg,requests
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
data={'doctype':'json','i':string}
resp=requests.post('http://fanyi.youdao.com/translate',data=data,proxies={'http':proxyserver,'https':proxyserver})
result=resp.json()['translateResult'][0][0]['tgt']
print(result)