import os,sys,glob,shutil,winreg,requests
import tkinter as tk
from tkinter import messagebox
from subprocess import Popen
class CAria:
    def __init__(self):
        key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings')
        count=winreg.QueryInfoKey(key)[1]
        for i in range(count):
            name=winreg.EnumValue(key,i)[0]
            command=winreg.EnumValue(key,i)[1]
            if name=='ProxyEnable':
                proxyenable=command
            if name=='ProxyServer':
                if proxyenable==0:
                    self.proxyserver=''
                else:
                    self.proxyserver=command
        winreg.CloseKey(key)
    def Update(self):
        resp=requests.get('https://ngosang.github.io/trackerslist/trackers_best_ip.txt',proxies={'http':self.proxyserver,'https':self.proxyserver})
        tracker=resp.text.replace('\n\n',',')[:-1]
        with open('aria2.conf','r',encoding='utf-8',errors='ignore') as conffile:
            with open('tmp.conf','w',encoding='utf-8',errors='ignore') as tmpfile:
                for conf in conffile:
                    if 'bt-tracker=' in conf:
                        tmpfile.write('bt-tracker=%s\n'%tracker)
                    else:
                        tmpfile.write(conf)
        os.remove('aria2.conf')
        shutil.move('tmp.conf','aria2.conf')
        messagebox.showinfo('更新conf','更新conf完成！')
    def Run(self):
        Popen('start "" /b aria2c --conf-path=aria2.conf -D',shell=True)
        Popen('start "" /b "..\AriaNg\index.html"',shell=True)
    def Close(self):
        Popen('taskkill /f /t /im aria2c.exe',shell=True)
    def Delete(self):
        if os.path.isfile('aria2.session'):
            with open('aria2.session','w',encoding='utf-8') as sessionfile:
                sessionfile.write('')
        if os.path.isfile('aria2.conf'):
            with open('aria2.conf','r',encoding='utf-8') as conffile:
                for conf in conffile:
                    if 'dir=' in conf:
                        tmpdir=conf.strip()
                        downdir=tmpdir[tmpdir.find('=')+1:len(tmpdir)]
        delsufs=['aria2','torrent']
        for delsuf in delsufs:
            if downdir=='':
                delfiles='*.%s'%delsuf
            else:
                delfiles='%s\*.%s'%(downdir,delsuf)
            for delfile in glob.glob(r'%s'%delfiles):
                if os.path.isfile(delfile):
                    os.remove(delfile)
        messagebox.showinfo('删除残留文件','删除残留文件完成！')
    def menuf(self,event,x,y):
        if event=='WM_RBUTTONDOWN':
            self.menu.tk_popup(x,y)
    def about(self):
        messagebox.showinfo('关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def allquit(self):
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.withdraw()
        self.root.iconbitmap(iicon)
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'CAria')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'更新conf',command=self.Update)
        self.menu.add_command(label=u'启动AriaNg',command=self.Run)
        self.menu.add_command(label=u'关闭AriaNg',command=self.Close)
        self.menu.add_command(label=u'删除残留文件',command=self.Delete)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'退出',command=self.allquit)
        self.root.mainloop()
if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'CAria.ico')
CAria().Root()