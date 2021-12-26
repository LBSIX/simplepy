import os,sys,webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Jhso:
    def __init__(self):
        self.dcategories={}
        self.dcheckboxes={}
        self.Root()
        self.Autoadd()
        self.root.mainloop()
    def Finalall(self):
        ltmp=[]
        for tmpbool in self.dcheckboxes.values():
            ltmp.append(tmpbool.get())
        if False in ltmp:
            self.varall.set(False)
        else:
            self.varall.set(True)
    def Checkall(self):
        if self.varall.get()==True:
            categoriesbool=True
        else:
            categoriesbool=False
        for categoriescheckboxes in self.dcheckboxes.keys():
            self.dcheckboxes[categoriescheckboxes].set(categoriesbool)
    def Doubleclicked(self,event):
        openurl=self.tree.item(self.tree.selection()[0])['values'][0]
        webbrowser.open(openurl,new=0)
    def So(self):
        keyword=self.evar.get()
        for tmpcheckboxes in self.dcheckboxes.keys():
            if self.dcheckboxes[tmpcheckboxes].get()==True:
                idroot=list(self.dcategories[tmpcheckboxes])[0]
                for i in self.tree.get_children(idroot):
                    suburl=self.dcategories[tmpcheckboxes][idroot][i]%keyword
                    self.tree.item(i,values=[suburl])
                    if self.varopen.get()==True:
                        webbrowser.open(suburl,new=0)
    def Autoadd(self):
        n=-1
        with open(r'solist.txt','r',encoding='utf-8-sig',errors='ignore') as file:
            for line in file:
                line=line.strip()
                if '###' in line:
                    namecategories=line[3:line.find('，')]
                    idcategories=self.tree.insert('',index='end',text=namecategories,open=True)
                    self.dcategories[namecategories]={idcategories:{}}
                    n+=1
                else:
                    if line=='':
                        continue
                    name=line[0:line.find(',')]
                    url=line[line.find(',')+1:len(line)]
                    iidcategorie=self.tree.insert(idcategories,index='end',text=name,values=url)
                    self.dcategories[namecategories][idcategories].update({iidcategorie:url})
        for tmpcategories in self.dcategories.keys():
            self.dcheckboxes[tmpcategories]=tk.BooleanVar()
            tk.Checkbutton(self.panel2,text=tmpcategories,variable=self.dcheckboxes[tmpcategories],command=self.Finalall).pack(side='left')
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
        self.root.title('聚合搜索')
        self.root.protocol("WM_DELETE_WINDOW",self.callback)
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'聚合搜索')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        self.evar=tk.StringVar()
        panel=tk.Frame(self.root)
        panel1=tk.Frame(panel)
        tk.Label(panel1,text='关键词:').pack(side='left')
        tk.Entry(panel1,textvariable=self.evar).pack(side='left',expand=1,fill='both')
        tk.Button(panel1,text='搜索',command=self.So).pack(side='left')
        self.varopen=tk.BooleanVar()
        tk.Checkbutton(panel1,text='打开',variable=self.varopen).pack(side='left')
        panel1.pack(fill='both')
        self.panel2=tk.Frame(panel)
        self.varall=tk.BooleanVar()
        tk.Checkbutton(self.panel2,text='所有',variable=self.varall,command=self.Checkall).pack(side='left')
        self.panel2.pack()
        panel.pack(fill='both')
        ygd=tk.Scrollbar(self.root)
        ygd.pack(side='right',fill='y')
        self.tree=ttk.Treeview(self.root,columns=('1'),yscrollcommand=ygd.set)
        ygd.config(command=self.tree.yview)
        self.tree.heading('#0',text='名称')
        self.tree.heading('#1',text='地址')
        self.tree.column('#1',width=500)
        self.tree.bind('<Double-1>',self.Doubleclicked)
        self.tree.pack(expand=1,fill='both')
if getattr(sys,'frozen',False):
    odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'聚合搜索.ico')
Jhso()