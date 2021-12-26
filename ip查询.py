import os,re,winreg,requests
def main():
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
    i=int(input('输入数字：\n1、查询本机ip\n2、查询外网ip\n'))
    if i==1:
        os.system('ipconfig>ip.txt')
        with open('ip.txt') as tmps:
            for tmp in tmps:
                if 'IPv4 地址' in tmp:
                    ip=tmp[tmp.rfind(' ')+1:len(tmp)].strip()
        print(ip)
        os.remove('ip.txt')
    elif i==2:
        resp=requests.get('https://2021.ip138.com',headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'},proxies={'http':proxyserver,'https':proxyserver})
        ip=re.findall(r'>(.+)</a>](.+)',resp.text)
        print(' '.join(ip[0]))
    else:
        print('请输入对应数字！')
main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        os.system('cls')
        main()