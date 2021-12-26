import json,random,winreg,base64,hashlib,requests
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
encrypt=hashlib.md5()
encrypt.update(''.join(random.choices('qweasdzxcrtyfghvbnuiopjklm1234567890',k=10)).encode())
brower_id=encrypt.hexdigest()
authdata={'browser_id':brower_id}
authdata=json.dumps(authdata)
authheaders={'X-Authorization':'token:qgemv4jr1y38jyq6vhvi','Content-Type':'application/json;charset=UTF-8'}
html=requests.post('https://api.interpreter.caiyunai.com/v1/user/jwt/generate',data=authdata,headers=authheaders,proxies={'http':proxyserver,'https':proxyserver})
auth=html.json()['jwt']
landata={'query':string}
lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata,proxies={'http':proxyserver,'https':proxyserver})
lan=lanhtml.json()['lan']
if lan=='zh':
    to='en'
else:
    to='zh'
data={'browser_id':brower_id,'detect':'true','source':string,'trans_type':'auto2%s'%to}
data=json.dumps(data)
headers={'T-Authorization':auth}
resp=requests.post('https://api.interpreter.caiyunai.com/v1/translator',data=data,headers=headers,proxies={'http':proxyserver,'https':proxyserver})
preresult=json.loads(resp.text)['target']
t='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
o='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
s=[]
for i in list(preresult):
    index=o.find(i)
    if index>-1:
        s.append(t[index])
    else:
        s.append(i)
result=base64.b64decode(''.join(s)).decode('utf-8')
print(result)