import os,sys,ctypes,winreg
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
class Start:
    def __init__(self):
        self.fp=fp
        if self.fp!=None:
            tmproot=tk.Tk()
            tmproot.wm_attributes('-topmost',1)
            tmproot.withdraw()
            if os.path.isfile(self.fp):
                self.Getfiles(self.fp)
            else:
                self.Getdir(self.fp)
            self.Add()
            messagebox.showinfo('添加启动项','添加启动项成功！')
        else:
            self.Root()
            self.Query()
            self.root.mainloop()
    def Getfiles(self,filesname=''):
        self.ltmp=[]
        if self.fp==None:
            filesname=filedialog.askopenfilenames()
            self.evar1.set(';'.join(filesname).replace('/','\\'))
        if filesname!='':
            if self.fp==None:
                for file in filesname:
                    self.ltmp.append(file.replace('/','\\'))
            else:
                self.ltmp.append(filesname)
    def Getdir(self,dirname=''):
        self.ltmp=[]
        if self.fp==None:
            dirname=filedialog.askdirectory()
            self.evar1.set(dirname.replace('/','\\'))
        if dirname!='':
            filesname=os.walk(dirname)
            for rootdir,subdir,files in filesname:
                for file in files:
                    self.ltmp.append(os.path.join(rootdir,file).replace('/','\\'))
    def Query(self):
        key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run')
        count=winreg.QueryInfoKey(key)[1]
        for i in range(count):
            name=winreg.EnumValue(key,i)[0]
            command=winreg.EnumValue(key,i)[1]
            self.tree.insert('',index='end',text=name,values=[command])
        winreg.CloseKey(key)
    def Add(self):
        try:
            if self.fp==None:
                par=self.evar2.get().lstrip()
            else:
                par=''
            for filepath in self.ltmp:
                filename=filepath[filepath.rfind('\\')+1:filepath.rfind('.')]
                if par=='':
                    command=r'"%s"'%filepath
                else:
                    command='"%s" %s'%(filepath,par)
                key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',access=winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(key,filename,0,winreg.REG_SZ,command)
                winreg.CloseKey(key)
                if self.fp==None:
                    self.tree.insert('',index='end',text=filename,values=[command])
        except:
            messagebox.showinfo('未选择目标','选择目标路径后再添加启动项！')
    def Delete(self):
        for i in self.tree.selection():
            name=self.tree.item(i)['text']
            key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',access=winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key,name)
            winreg.CloseKey(key)
            self.tree.delete(i)
    def Alldelete(self):
        for i in self.tree.get_children():
            name=self.tree.item(i)['text']
            key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',access=winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key,name)
            winreg.CloseKey(key)
            self.tree.delete(i)
    def Open(self):
        key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Applets\Regedit',access=winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key,'LastKey',0,winreg.REG_SZ,r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run')
        os.system('start regedit.exe')
        winreg.CloseKey(key)
    def showPopupMenu(self,event):
        self.popupmenu.post(event.x_root,event.y_root)
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
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.iconbitmap(iicon)
        self.root.title('CStart')
        self.root.protocol("WM_DELETE_WINDOW",self.callback)
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'CStart')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        self.evar1=tk.StringVar()
        self.evar2=tk.StringVar()
        panel=tk.Frame(self.root)
        panel1=tk.Frame(panel)
        tk.Label(panel1,text='目标路径:',font=('',16)).pack(side='left')
        tk.Entry(panel1,textvariable=self.evar1,font=('',16)).pack(side='left',expand=1,fill='both')
        tk.Button(panel1,text='选择文件',font=('',16),command=self.Getfiles).pack(side='left')
        tk.Button(panel1,text='选择文件夹',font=('',16),command=self.Getdir).pack(side='left')
        panel1.pack(fill='both')
        panel2=tk.Frame(panel)
        tk.Label(panel2,text='参数(可选):',font=('',16)).pack(side='left')
        tk.Entry(panel2,textvariable=self.evar2,font=('',16)).pack(side='left',expand=1,fill='both')
        tk.Button(panel2,text='添加',font=('',16),command=self.Add).pack(side='left')
        tk.Button(panel2,text='删除',font=('',16),command=self.Delete).pack(side='left')
        tk.Button(panel2,text='全部删除',font=('',16),command=self.Alldelete).pack(side='left')
        panel2.pack(fill='both')
        panel.pack(fill='both')
        ygd=tk.Scrollbar(self.root)
        ygd.pack(side='right',fill='y')
        self.tree=ttk.Treeview(self.root,columns=('2'),yscrollcommand=ygd.set)
        self.popupmenu=tk.Menu(self.root,tearoff=0)
        self.popupmenu.add_command(label=u'删除',command=self.Delete)
        self.popupmenu.add_command(label=u'全部删除',command=self.Alldelete)
        self.popupmenu.add_command(label=u'在注册表编辑器中打开',command=self.Open)
        self.tree.bind('<Button-3>',self.showPopupMenu)
        ygd.config(command=self.tree.yview)
        self.tree.heading('#0',text='名称')
        self.tree.heading('#1',text='启动参数')
        self.tree.pack(expand=1,fill='both')
if getattr(sys,'frozen',False):
    odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'CStart.ico')
exepath=sys.executable
idirCStartpy=os.path.abspath(__file__)
try:
    fp=sys.argv[1]
except:
    fp=None
try:
    key0=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'*\\shell\\用CStart添加到开机启动项')
    winreg.CloseKey(key0)
    Start()
except:
    if ctypes.windll.shell32.IsUserAnAdmin():
        menu_name='用CStart添加到开机启动项'
        if 'CStart.exe' in exepath:
                command=r'"%s"'%exepath
        else:
            command=r'"%s" "%s"'%(exepath,idirCStartpy)
        key1=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'*\\shell')
        winreg.SetValue(key1,menu_name,winreg.REG_SZ,menu_name)
        sub_key1=winreg.OpenKey(key1,menu_name)
        winreg.SetValue(sub_key1,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key1)
        winreg.CloseKey(key1)
        key2=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Directory\\shell')
        winreg.SetValue(key2,menu_name,winreg.REG_SZ,menu_name)
        sub_key2=winreg.OpenKey(key2,menu_name)
        winreg.SetValue(sub_key2,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key2)
        winreg.CloseKey(key2)
        key3=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Directory\\Background\\shell')
        winreg.SetValue(key3,menu_name,winreg.REG_SZ,menu_name)
        sub_key3=winreg.OpenKey(key3,menu_name)
        winreg.SetValue(sub_key3,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key3)
        winreg.CloseKey(key3)
        key4=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Drive\\shell')
        winreg.SetValue(key4,menu_name,winreg.REG_SZ,menu_name)
        sub_key4=winreg.OpenKey(key4,menu_name)
        winreg.SetValue(sub_key4,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key4)
        winreg.CloseKey(key4)
    else:
        tmp=ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,0)
        if tmp!=5:
            Start()