import os,sys,time,chardet,pywifi,itertools,threading,subprocess,more_itertools
import tkinter as tk
from tkinter import ttk
from pywifi import const
from tkinter import filedialog,messagebox
from time import gmtime,strftime
class Crack:
    def __init__(self):
        self.flag=True
        self.__flag=threading.Event()
        wifi=pywifi.PyWiFi()
        self.iface=wifi.interfaces()[0]
        self.iface.disconnect()
        self.stringnum='0123456789'
        self.stringlletter='abcdefghijklmnopqrstuvwxyz'
        self.stringuletter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def Doubleclicked(self,event):
        wifiname=self.tree.item(self.tree.selection()[0])['text']
        self.vartarget.set(wifiname)
        self.win.destroy()
    def Choosetarget(self):
        if self.vartargetfunc.get()==1:
            self.win=tk.Toplevel()
            self.win.iconbitmap(iicon)
            self.win.title('wifi列表')
            ygd=tk.Scrollbar(self.win)
            ygd.pack(side='right',fill='y')
            tk.Label(self.win,text='双击选择wifi；信号强度数字越小信号越好，wifi连接延时可以设置的越小；密码是指附近的wifi如果已经连接过并且保存了就会显示').pack()
            self.tree=ttk.Treeview(self.win,columns=('0','1'),yscrollcommand=ygd.set)
            ygd.config(command=self.tree.yview)
            self.tree.pack(expand=1,fill='both')
            self.tree.heading('#0',text='wifi名称')
            self.tree.heading('#1',text='信号强度')
            self.tree.heading('#2',text='密码')
            self.tree.column('#1',anchor='center')
            self.tree.column('#2',anchor='center')
            self.tree.bind('<Double-1>',self.Doubleclicked)
            self.iface.scan()
            bsses=self.iface.scan_results()
            for pjwifi in bsses:
                ssid=pjwifi.ssid.encode('raw_unicode_escape').decode()
                signal=pjwifi.signal
                wifiprofile=subprocess.Popen('netsh wlan show profiles "%s" key=clear'%ssid,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                if wifiprofile.wait()==1:
                    self.tree.insert('',index='end',text=ssid,values=[signal,'未保存'])
                else:
                    details=wifiprofile.communicate()[0]
                    for detail in details.splitlines():
                        try:
                            detail=detail.decode('gbk')
                        except:
                            detail=detail.decode('gb18030')
                        if '关键内容' in detail:
                            key=detail[detail.find(':')+2:len(detail)]
                            self.tree.insert('',index='end',text=ssid,values=[signal,key])
                        if '安全密钥' in detail:
                            keybool=detail[detail.find(':')+2:len(detail)]
                            if keybool=='不存在':
                                self.tree.insert('',index='end',text=ssid,values=[signal,'无密码'])
        if self.vartargetfunc.get()==2:
            compressfile=filedialog.askopenfilename()
            self.vartarget.set(compressfile)
        if self.vartargetfunc.get()==3:
            passwordbook=filedialog.askdirectory()
            if passwordbook!='':
                self.vartarget.set('%s/密码本.txt'%passwordbook)
    def Switchtarget(self):
        if self.vartargetfunc.get()==1:
            self.ltarget.config(text='wifi名称：')
            self.bchoosetarget.config(text='选择wifi')
            self.panelwifidelay.pack_forget()
            self.panelfunc.pack_forget()
            self.panelwifidelay.pack(side='left')
            self.panelfunc.pack(side='left')
            self.Switchcrackmode()
        if self.vartargetfunc.get()==2:
            self.ltarget.config(text='压缩包路径：')
            self.bchoosetarget.config(text='选择压缩包文件')
            self.panelwifidelay.pack_forget()
            self.Switchcrackmode()
        if self.vartargetfunc.get()==3:
            self.ltarget.config(text='密码本路径：')
            self.bchoosetarget.config(text='选择密码本保存路径')
            self.panelwifidelay.pack_forget()
            self.Repack()
            self.panel3.pack_forget()
            self.panel6.pack_forget()
    def Switchcrackmode(self):
        if self.varcrackmode.get()==1:
            self.Repack()
            self.panel6.pack_forget()
        if self.varcrackmode.get()==2:
            self.Repack()
            self.panel4.pack_forget()
            self.panel5.pack_forget()
    def Finalall(self):
        if self.varotherbool.get() and self.varnumbool.get() and self.varlletterbool.get() and self.varuletterbool.get():
            self.varallbool.set(True)
        else:
            self.varallbool.set(False)
        if self.varotherbool.get():
            self.estring.config(state='normal')
        else:
            self.estring.config(state='disabled')
        if self.varnumbool.get():
            if self.stringnum in self.varexhaustivestring.get():
                pass
            else:
                self.varexhaustivestring.set(self.varexhaustivestring.get()+self.stringnum)
        else:
            self.varexhaustivestring.set(self.varexhaustivestring.get().replace(self.stringnum,''))
        if self.varlletterbool.get():
            if self.stringlletter in self.varexhaustivestring.get():
                pass
            else:
                self.varexhaustivestring.set(self.varexhaustivestring.get()+self.stringlletter)
        else:
            self.varexhaustivestring.set(self.varexhaustivestring.get().replace(self.stringlletter,''))
        if self.varuletterbool.get():
            if self.stringuletter in self.varexhaustivestring.get():
                pass
            else:
                self.varexhaustivestring.set(self.varexhaustivestring.get()+self.stringuletter)
        else:
            self.varexhaustivestring.set(self.varexhaustivestring.get().replace(self.stringuletter,''))
    def Checkall(self):
        if self.varallbool.get():
            self.estring.config(state='normal')
            self.varexhaustivestring.set(self.stringnum+self.stringlletter+self.stringuletter)
            self.varotherbool.set(True)
            self.varnumbool.set(True)
            self.varlletterbool.set(True)
            self.varuletterbool.set(True)
        else:
            self.estring.delete(0,'end')
            self.estring.config(state='disabled')
            self.varotherbool.set(False)
            self.varnumbool.set(False)
            self.varlletterbool.set(False)
            self.varuletterbool.set(False)
    def Switchstarttoexhaustiondict(self):
        if self.varprogressstartbool.get():
            self.varexhaustionstartbool.set(False)
            self.vardictstartbool.set(False)
            self.eexhaustionstart.config(state='disabled')
            self.edictstart.config(state='disabled')
    def Switchexhaustiondicttostart(self):
        if self.varexhaustionstartbool.get():
            self.varprogressstartbool.set(False)
            self.eexhaustionstart.config(state='normal')
        else:
            self.eexhaustionstart.config(state='disabled')
        if self.vardictstartbool.get():
            self.varprogressstartbool.set(False)
            self.edictstart.config(state='normal')
        else:
            self.edictstart.config(state='disabled')
    def Dictpath(self):
        dictfile=filedialog.askopenfilename()
        self.vardictpath.set(dictfile)
    def Repack(self):
        self.panel1.pack_forget()
        self.panel2.pack_forget()
        self.panel3.pack_forget()
        self.panel4.pack_forget()
        self.panel5.pack_forget()
        self.panel6.pack_forget()
        self.panel7.pack_forget()
        self.panel8.pack_forget()
        self.panel1.pack()
        self.panel2.pack(fill='both')
        self.panel3.pack()
        self.panel4.pack(fill='both')
        self.panel5.pack(fill='both')
        self.panel6.pack(fill='both')
        self.panel7.pack()
        self.panel8.pack(fill='both',expand=1)
    def Textinsert(self,progressstring):
        self.textprogress.insert('end','%s'%progressstring)
        self.textprogress.see('end')
    def test_connect(self,testkey):
        profile=pywifi.Profile()
        profile.ssid=self.vartarget.get().encode('utf-8').decode('gb18030')
        profile.auth=const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher=const.CIPHER_TYPE_CCMP
        profile.key=testkey
        self.iface.remove_all_network_profiles()
        tmp_profile=self.iface.add_network_profile(profile)
        self.iface.connect(tmp_profile)
        time.sleep(int(self.varwifidelay.get()))
        if self.iface.status()==const.IFACE_CONNECTED:
            isOK=True
        else:
            isOK=False
        self.iface.disconnect()
        time.sleep(1)
        return isOK
    def readPassWord(self):
        crackprogress=0
        if self.varcrackmode.get()!=2:
            string=self.varexhaustivestring.get()
            pwdnum=int(self.varpwdnum.get())
            pwds=itertools.product(string,repeat=pwdnum)
            if self.varexhaustionstartbool.get():
                exhaustionstartstr=self.varexhaustionstartposition.get()
                crackprogress=more_itertools.product_index(exhaustionstartstr,*[string]*pwdnum)
                pwds=itertools.islice(pwds,crackprogress,None)
        else:
            dictfile=self.vardictpath.get()
            if self.vardictstartbool.get():
                crackprogress=int(self.vardictstartposition.get())
            if os.path.isfile(dictfile):
                with open(dictfile,'rb') as f:
                    dictencode=(chardet.detect(f.read()))['encoding']
                f=open(dictfile,encoding=dictencode,errors='ignore')
                pwds=itertools.islice(f,crackprogress,None)
        if self.varprogressstartbool.get() and self.vartargetfunc.get()!=3:
            if os.path.isfile('Progress.txt'):
                with open('Progress.txt','r',encoding='utf-8-sig',errors='ignore') as f:
                    for i in f:
                        i=i.strip()
                        crackprogress=int(i[0:i.find(',')])
                pwds=itertools.islice(pwds,crackprogress,None)
        for readnum,readpwd in enumerate(pwds,crackprogress):
            readpwd=''.join(readpwd).replace('\n','')
            self.num=readnum
            self.pwd=readpwd
            yield readpwd
    def Formaterr(self):
        if self.varcrackmode.get()!=2:
            if self.vartargetfunc.get()==1:
                try:
                    int(self.varwifidelay.get())
                except ValueError:
                    self.Textinsert('wifi连接延时不能为空并且必须是整数\n')
                    return True
            try:
                int(self.varpwdnum.get())
            except ValueError:
                self.Textinsert('密码位数不能为空并且必须是整数\n')
                return True
        else:
            if self.vardictstartbool.get():
                try:
                    int(self.vardictstartposition.get())
                except ValueError:
                    self.Textinsert('字典起始行不能为空并且必须是整数\n')
                    return True
        return False
    def Run(self):
        target=self.vartarget.get()
        if self.vartargetfunc.get()!=3:
            self.Textinsert('开始破解 %s\n'%target)
        else:
            self.Textinsert('开始生成密码本 %s\n'%target)
        stm=time.time()
        tmp=self.readPassWord()
        while True:
            if self.flag:
                return
            self.__flag.wait()
            try:
                pwd=next(tmp)
                if self.vartargetfunc.get()==1:
                    connectedbool=self.test_connect(pwd)
                    if connectedbool:
                        self.Textinsert('密码正确：%s\n'%pwd)
                        ent=time.time()
                        structtime=gmtime(ent-stm)
                        self.Textinsert('%s 破解成功！用时%s时:%s分:%s秒！'%(target,strftime('%H',structtime),strftime('%M',structtime),strftime('%S',structtime)))
                        self.Stop()
                    else:
                        self.Textinsert('密码错误：%s\n'%pwd)
                if self.vartargetfunc.get()==2:
                    exepath=sys.executable
                    if 'Crack.exe' in exepath:
                        idirwinrar=os.path.join(os.path.dirname(exepath),'WinRAR.exe')
                    else:
                        idirwinrar=os.path.join(os.path.dirname(os.path.abspath(__file__)),'WinRAR.exe')
                    compressfile=self.vartarget.get()
                    decompresspath=os.path.splitext(compressfile)[0]
                    if os.path.exists(decompresspath)==False:
                        os.mkdir(decompresspath)
                    if os.path.isfile(compressfile):
                        jy=r'"%s" -ibck -y x -p"%s" "%s" "%s"'%(idirwinrar,pwd,compressfile,decompresspath)
                        if subprocess.Popen(jy).wait()==0:
                            self.Textinsert('密码正确：%s\n'%pwd)
                            ent=time.time()
                            structtime=gmtime(ent-stm)
                            self.Textinsert('%s 破解成功！用时%s时:%s分:%s秒！'%(target,strftime('%H',structtime),strftime('%M',structtime),strftime('%S',structtime)))
                            self.Stop()
                        else:
                            self.Textinsert('密码错误：%s\n'%pwd)
                if self.vartargetfunc.get()==3:
                    if os.path.isdir(os.path.splitext(target)[0]):
                        with open(target,'a',encoding='utf-8-sig',errors='ignore') as f:
                            self.Textinsert('正在写入密码：%s\n'%pwd)
                            f.write('%s\n'%pwd)
            except ValueError:
                if self.varexhaustionstartbool.get():
                    self.Textinsert('穷举起始字符串不能为空或者穷举起始字符串过大\n')
                if self.vardictstartbool.get():
                    self.Textinsert('字典起始行不能为空并且必须是整数或者字典起始行过大\n')
            except:
                ent=time.time()
                structtime=gmtime(ent-stm)
                if self.vartargetfunc.get()!=3:
                    self.Textinsert('%s 破解失败，用时%s时:%s分:%s秒'%(target,strftime('%H',structtime),strftime('%M',structtime),strftime('%S',structtime)))
                else:
                    self.Textinsert('%s 密码本生成成功！用时%s时:%s分:%s秒！'%(target,strftime('%H',structtime),strftime('%M',structtime),strftime('%S',structtime)))
                self.Stop()
    def Start(self):
        formaterrbool=self.Formaterr()
        if formaterrbool:
            return
        if self.flag:
            self.textprogress.delete(1.0,'end')
            self.__flag.set()
            self.flag=False
            threading.Thread(target=self.Run,daemon=True).start()
            self.bstartpause.config(text='暂停')
        else:
            if self.__flag.isSet():
                self.__flag.clear()
                self.bstartpause.config(text='恢复')
            else:
                self.__flag.set()
                self.bstartpause.config(text='暂停')
    def Stop(self):
        if self.flag==False:
            self.Progresssaved()
            self.flag=True
            self.bstartpause.config(text='开始')
    def Progresssaved(self):
        if self.varprogresssavedbool.get() and self.vartargetfunc.get()!=3:
            if self.flag==False:
                try:
                    with open('Progress.txt','a',encoding='utf-8-sig',errors='ignore') as profile:
                        profile.write('%s,%s\n'%(self.num,self.pwd))
                except:
                    pass
    def Cleartext(self):
        self.textprogress.delete(1.0,'end')
    def callback(self):
        self.root.withdraw()
    def menuf(self,event,x,y):
        if event=='WM_RBUTTONDOWN':
            self.menu.tk_popup(x,y)
        if event=='WM_LBUTTONDOWN':
            self.root.deiconify()
        if event=='WM_MBUTTONDOWN':
            self.root.withdraw()
    def about(self):
        messagebox.showinfo('关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def allquit(self):
        self.Progresssaved()
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.iconbitmap(iicon)
        self.root.title('Crack')
        self.root.protocol("WM_DELETE_WINDOW",self.callback)
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'Crack')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        self.panel1=tk.Frame(self.root)
        self.panelwifidelay=tk.Frame(self.panel1)
        tk.Label(self.panelwifidelay,text='wifi连接延时：',font=('',16)).pack(side='left')
        self.varwifidelay=tk.StringVar()
        self.varwifidelay.set('5')
        tk.Entry(self.panelwifidelay,textvariable=self.varwifidelay,font=('',16)).pack(side='left')
        self.panelwifidelay.pack(side='left')
        self.panelfunc=tk.Frame(self.panel1)
        self.vartargetfunc=tk.IntVar()
        self.vartargetfunc.set(1)
        tk.Radiobutton(self.panelfunc,text='wifi破解',font=('',16),variable=self.vartargetfunc,value=1,command=self.Switchtarget).pack(side='left')
        tk.Radiobutton(self.panelfunc,text='压缩包破解',font=('',16),variable=self.vartargetfunc,value=2,command=self.Switchtarget).pack(side='left')
        tk.Radiobutton(self.panelfunc,text='生成密码本',font=('',16),variable=self.vartargetfunc,value=3,command=self.Switchtarget).pack(side='left')
        self.panelfunc.pack(side='left')
        self.panel1.pack()
        self.panel2=tk.Frame(self.root)
        self.ltarget=tk.Label(self.panel2,text='wifi名称：',font=('',16))
        self.ltarget.pack(side='left')
        self.vartarget=tk.StringVar()
        tk.Entry(self.panel2,textvariable=self.vartarget,font=('',16)).pack(side='left',expand=1,fill='both')
        self.bchoosetarget=tk.Button(self.panel2,text='选择wifi',font=('',16),command=self.Choosetarget)
        self.bchoosetarget.pack(side='left')
        self.panel2.pack(fill='both')
        self.panel3=tk.Frame(self.root)
        tk.Label(self.panel3,text='选择破解方式：',font=('',16)).pack(side='left')
        self.varcrackmode=tk.IntVar()
        self.varcrackmode.set(1)
        tk.Radiobutton(self.panel3,text='穷举破解',font=('',16),variable=self.varcrackmode,command=self.Switchcrackmode,value=1).pack(side='left')
        tk.Radiobutton(self.panel3,text='字典破解',font=('',16),variable=self.varcrackmode,command=self.Switchcrackmode,value=2).pack(side='left')
        self.varprogressstartbool=tk.BooleanVar()
        self.varprogressstartbool.set(True)
        tk.Checkbutton(self.panel3,text='从上次进度开始破解',font=('',16),variable=self.varprogressstartbool,command=self.Switchstarttoexhaustiondict).pack(side='left')
        self.varprogresssavedbool=tk.BooleanVar()
        self.varprogresssavedbool.set(True)
        tk.Checkbutton(self.panel3,text='保存破解进度',font=('',16),variable=self.varprogresssavedbool).pack(side='left')
        self.panel3.pack()
        self.panel4=tk.Frame(self.root)
        tk.Label(self.panel4,text='穷举字符串：',font=('',16)).pack(side='left')
        self.varexhaustivestring=tk.StringVar()
        self.varexhaustivestring.set(self.stringnum+self.stringlletter+self.stringuletter)
        self.estring=tk.Entry(self.panel4,font=('',16),textvariable=self.varexhaustivestring)
        self.estring.pack(side='left',expand=1,fill='both')
        self.varallbool=tk.BooleanVar()
        self.varallbool.set(True)
        tk.Checkbutton(self.panel4,text='所有',font=('',16),variable=self.varallbool,command=self.Checkall).pack(side='left')
        self.varotherbool=tk.BooleanVar()
        self.varotherbool.set(True)
        tk.Checkbutton(self.panel4,text='自定义',font=('',16),variable=self.varotherbool,command=self.Finalall).pack(side='left')
        self.varnumbool=tk.BooleanVar()
        self.varnumbool.set(True)
        tk.Checkbutton(self.panel4,text='数字',font=('',16),variable=self.varnumbool,command=self.Finalall).pack(side='left')
        self.varlletterbool=tk.BooleanVar()
        self.varlletterbool.set(True)
        tk.Checkbutton(self.panel4,text='小写字母',font=('',16),variable=self.varlletterbool,command=self.Finalall).pack(side='left')
        self.varuletterbool=tk.BooleanVar()
        self.varuletterbool.set(True)
        tk.Checkbutton(self.panel4,text='大写字母',font=('',16),variable=self.varuletterbool,command=self.Finalall).pack(side='left')
        self.panel4.pack(fill='both')
        self.panel5=tk.Frame(self.root)
        tk.Label(self.panel5,text='密码位数：',font=('',16)).pack(side='left')
        self.varpwdnum=tk.StringVar()
        tk.Entry(self.panel5,textvariable=self.varpwdnum,font=('',16)).pack(side='left',expand=1,fill='both')
        self.varexhaustionstartbool=tk.BooleanVar()
        tk.Checkbutton(self.panel5,text='设置穷举起始字符串：',font=('',16),variable=self.varexhaustionstartbool,command=self.Switchexhaustiondicttostart).pack(side='left')
        self.varexhaustionstartposition=tk.StringVar()
        self.eexhaustionstart=tk.Entry(self.panel5,state='disabled',textvariable=self.varexhaustionstartposition,font=('',16))
        self.eexhaustionstart.pack(side='left',expand=1,fill='both')
        self.panel5.pack(fill='both')
        self.panel6=tk.Frame(self.root)
        tk.Label(self.panel6,text='字典路径：',font=('',16)).pack(side='left')
        self.vardictpath=tk.StringVar()
        tk.Entry(self.panel6,textvariable=self.vardictpath,font=('',16)).pack(side='left',expand=1,fill='both')
        tk.Button(self.panel6,text='选择字典文件',font=('',16),command=self.Dictpath).pack(side='left')
        self.vardictstartbool=tk.BooleanVar()
        tk.Checkbutton(self.panel6,text='设置字典起始行（第一行为0）：',font=('',16),variable=self.vardictstartbool,command=self.Switchexhaustiondicttostart).pack(side='left')
        self.vardictstartposition=tk.StringVar()
        self.edictstart=tk.Entry(self.panel6,state='disabled',textvariable=self.vardictstartposition,font=('',16))
        self.edictstart.pack(side='left',expand=1,fill='both')
        self.panel7=tk.Frame(self.root)
        self.bstartpause=tk.Button(self.panel7,text='开始',font=('',16),width=10,command=self.Start)
        self.bstartpause.pack(side='left')
        tk.Button(self.panel7,text='停止',font=('',16),width=10,command=self.Stop).pack(side='left')
        tk.Button(self.panel7,text='清除',font=('',16),width=10,command=self.Cleartext).pack(side='left')
        self.panel7.pack()
        self.panel8=tk.Frame(self.root)
        ygd=tk.Scrollbar(self.panel8)
        ygd.pack(side='right',fill='y')
        self.textprogress=tk.Text(self.panel8,font=('',16),wrap='none',yscrollcommand=ygd.set)
        self.textprogress.pack(fill='both',expand=1)
        self.panel8.pack(fill='both',expand=1)
        ygd.config(command=self.textprogress.yview)
        self.root.mainloop()
if getattr(sys,'frozen',False):
    odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'Crack.ico')
Crack().Root()