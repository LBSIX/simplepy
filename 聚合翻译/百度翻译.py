import re,winreg,js2py,requests
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
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','Cookie':'BAIDUID=4650B0B34048BBAA1E0B909B42F5A564:FG=1;BIDUPSID=4650B0B34048BBAA1E0B909B42F5A564;PSTM=1537177909;BDUSS=w0VmEzUFFWTTh0bld5VWVhNVo5MEEyV2ZKdTk3U2stMGZmWVQ1TTRuSnVkOHBiQVFBQUFBJCQAAAAAAAAAAAEAAAD0GzcNaG9uZ3F1YW4xOTkxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG7qoltu6qJbTk;pgv_pvi=6774493184;uc_login_unique=19e6fd48035206a8abe89f98c3fc542a;uc_recom_mark=cmVjb21tYXJrXzYyNDU4NjM%3D;MCITY=-218%3A;cflag=15%3A3;SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02893452711;locale=zh;Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1539333192;from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D;REALTIME_TRANS_SWITCH=1;FANYI_WORD_SWITCH=1;HISTORY_SWITCH=1;SOUND_SPD_SWITCH=1;SOUND_PREFER_SWITCH=1;to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D;Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1539333307'}
html=requests.get('https://fanyi.baidu.com',headers=headers,proxies={'http':proxyserver,'https':proxyserver})
gtk=re.findall("window.gtk = '(.*?)';",html.text)[0]
js=js2py.EvalJs()
js.execute('function a(r,o){for(var t=0;t<o.length-2;t+=3){var a=o.charAt(t+2);a=a>="a"?a.charCodeAt(0)-87:Number(a),a="+"===o.charAt(t+1)?r>>>a:r<<a,r="+"===o.charAt(t)?r+a&4294967295:r^a}return r}var C=null;var hash=function(r,_gtk){var o=r.length;o>30&&(r=""+r.substr(0,10)+r.substr(Math.floor(o/2)-5,10)+r.substr(-10,10));var t=void 0,t=null!==C?C:(C=_gtk||"")||"";for(var e=t.split("."),h=Number(e[0])||0,i=Number(e[1])||0,d=[],f=0,g=0;g<r.length;g++){var m=r.charCodeAt(g);128>m?d[f++]=m:(2048>m?d[f++]=m>>6|192:(55296===(64512&m)&&g+1<r.length&&56320===(64512&r.charCodeAt(g+1))?(m=65536+((1023&m)<<10)+(1023&r.charCodeAt(++g)),d[f++]=m>>18|240,d[f++]=m>>12&63|128):d[f++]=m>>12|224,d[f++]=m>>6&63|128),d[f++]=63&m|128)}for(var S=h,u="+-a^+6",l="+-3^+b+-f",s=0;s<d.length;s++)S+=d[s],S=a(S,u);return S=a(S,l),S^=i,0>S&&(S=(2147483647&S)+2147483648),S%=1e6,S.toString()+"."+(S^h)}')
sign=js.hash(string,gtk)
token=re.findall("token: '(.+)',",html.text)[0]
landata={'query':string}
lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata,proxies={'http':proxyserver,'https':proxyserver})
lan=lanhtml.json()['lan']
if lan=='zh':
    to='en'
else:
    to='zh'
data={'from':lan,'to':to,'query':string,'sign':'%s'%sign,'token':'%s'%token}
resp=requests.post('https://fanyi.baidu.com/v2transapi',data=data,headers=headers,proxies={'http':proxyserver,'https':proxyserver})
result=resp.json()['trans_result']['data'][0]['dst']
print(result)