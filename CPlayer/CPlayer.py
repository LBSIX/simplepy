import os,sys,shutil,random,ctypes,winreg,chardet,platform
from threading import Thread
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu,QAction,QMessageBox,QApplication,QMainWindow,QSystemTrayIcon,QFileDialog,QDesktopWidget
from Ui_CPlayer import Ui_MainWindow
class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Tray()
        self.Vr()
        self.l=[]
        self.step=self.loop=0
        self.ratenum=1.0
        self.flag=self.voltag=self.spetag=self.keeptag=self.listtag=self.fulltag=True
        self.list.installEventFilter(self)
        self.player=vlc.MediaPlayer()
        self.timer=QTimer()
        self.timer.timeout.connect(self.Show)
        self.steptimer=QTimer()
        self.steptimer.timeout.connect(self.Step)
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.fp=fp
        if self.fp!=None:
            name=self.fp[self.fp.rfind('\\')+1:self.fp.rfind('.')]
            self.list.addItem(name)
            self.l.append(self.fp)
            self.Play()
    def Vr(self):
        if os.path.isdir(r'%s\plugins\gui'%idirvlc):
            shutil.rmtree(r'%s\plugins\gui'%idirvlc)
        tmp=['plugins','libvlc.dll','libvlccore.dll']
        for delfiles in os.listdir(idirvlc):
            if delfiles in tmp:
                continue
            else:
                delfile=os.path.join(idirvlc,delfiles)
                if os.path.isfile(delfile):
                    os.remove(delfile)
                else:
                    shutil.rmtree(delfile)
    def Tray(self):
        self.tp=QSystemTrayIcon(self)
        self.tp.setIcon(QIcon(idirCPlayer))
        self.tp.activated.connect(self.Activated)
        self.tp.setToolTip('CPlayer')
        tpMenu=QMenu()
        a1=QAction((QIcon(idirCPlayer)),'显示主页面',self,triggered=(self.Showmain))
        a2=QAction((QIcon(idirCPlayer)),'隐藏主页面',self,triggered=(self.Min))
        a3=QAction((QIcon(idirabout)),'关于',self,triggered=(self.About))
        a4=QAction((QIcon(idirexit)),'退出',self,triggered=(self.Quit))
        tpMenu.addAction(a1)
        tpMenu.addAction(a2)
        tpMenu.addAction(a3)
        tpMenu.addAction(a4)
        self.tp.setContextMenu(tpMenu)
        self.tp.show()
    def closeEvent(self,event):
        event.ignore()
        self.hide()
    def Activated(self,reason):
        if reason==QSystemTrayIcon.MiddleClick:
            self.Min()
        else:
            if reason==QSystemTrayIcon.Trigger:
                self.Showmain()
    def Showmain(self):
        self.showNormal()
        self.activateWindow()
    def Min(self):
        self.hide()
    def About(self):
        QMessageBox.information(self,'关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def Quit(self):
        self.Progresssave()
        self.tp=None
        sys.exit()
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_P:
            self.Listhide()
        if event.key()==Qt.Key_T:
            self.Fastback()
        if event.key()==Qt.Key_L:
            self.Loop()
        if event.key()==Qt.Key_Space:
            self.Play()
        if event.key()==Qt.Key_S:
            self.Stop()
        if event.key()==Qt.Key_F:
            self.Full()
        if event.key()==Qt.Key_J:
            self.Fastforward()
        if event.key()==Qt.Key_K:
            self.Keep()
        if event.key()==Qt.Key_B:
            self.Recspeed()
        if event.key()==Qt.Key_I:
            self.sspeed.setValue(self.sspeed.value()+1)
        if event.key()==Qt.Key_D:
            self.sspeed.setValue(self.sspeed.value()-1)
        if event.key()==Qt.Key_M:
            self.Mute()
        if event.key()==Qt.Key_A:
            self.svolume.setValue(self.svolume.value()+1)
        if event.key()==Qt.Key_R:
            self.svolume.setValue(self.svolume.value()-1)
    def eventFilter(self,sender,event):
        if (event.type()==event.ChildRemoved):
            self.Moved()
        return False
    def Listmenu(self,position):
        lm=QMenu()
        fileaddact=QAction("从文件导入播放列表",self,triggered=self.Listadd)
        addact=QAction("添加到播放列表",self,triggered=self.Add)
        removeact=QAction("从播放列表移除",self,triggered=self.Remove)
        renameact=QAction('重命名',self,triggered=self.Rename)
        clearact=QAction('清空播放列表',self,triggered=self.Clear)
        saveact=QAction('保存当前播放列表',self,triggered=self.Saved)
        lm.addAction(fileaddact)
        lm.addAction(addact)
        if self.list.itemAt(position):
            lm.addAction(removeact)
            lm.addAction(renameact)
        lm.addAction(clearact)
        lm.addAction(saveact)
        lm.exec_(self.list.mapToGlobal(position))
    def Listadd(self):
        self.Clear()
        fromfile,_=QFileDialog.getOpenFileName(self,'从文件导入播放列表','.','所有文件(*)')
        if os.path.isfile(fromfile):
            with open(fromfile,'rb') as f:
                playencode=(chardet.detect(f.read()))['encoding']
            with open(fromfile,encoding=playencode,errors='ignore') as f:
                for i in f:
                    i=i.strip()
                    name=i[0:i.find(',')]
                    filelist=i[i.find(',')+1:len(i)]
                    self.list.addItem(name)
                    self.l.append(filelist)
    def Add(self):
        filelists,_=QFileDialog.getOpenFileNames(self,'添加到播放列表','.','媒体文件(*)')
        for filelist in filelists:
            name=filelist[filelist.rfind('/')+1:filelist.rfind('.')]
            self.list.addItem(name)
            self.l.append(filelist)
    def Remove(self):
        ltmp=[]
        for i in self.list.selectedIndexes():
            ltmp.append(i.row())
        ltmp.sort(reverse=True)
        for j in ltmp:
            self.list.takeItem(j)
            self.l.pop(j)
        self.list.setCurrentRow(self.list.currentRow())
        self.list.scrollToItem(self.list.currentItem(),hint=1)
    def Rename(self):
        item=self.list.item(self.list.currentRow())
        item.setFlags(item.flags()|Qt.ItemIsEditable)
        self.list.editItem(item)
    def Clear(self):
        self.l=[]
        self.list.clear()
    def Saved(self):
        savedfile,_=QFileDialog.getSaveFileName(self,'保存当前播放列表','.','文本文件(*.txt)')
        if savedfile!='':
            with open(savedfile,'w',encoding='utf-8-sig',errors='ignore') as f:
                for i in range(self.list.count()):
                    f.write('%s,%s\n'%(self.list.item(i).text(),self.l[i]))
    def Drag(self):
        self.tmp1=[]
        self.tmp2=self.l[:]
        for i in range(self.list.count()):
            self.tmp1.append(self.list.item(i).text())
    def Moved(self):
        for i in range(self.list.count()):
            if self.list.item(i).text()==self.tmp1[i]:
                continue
            else:
                self.l[i]=self.tmp2[self.tmp1.index(self.list.item(i).text())]
    def Listhide(self):
        if self.listtag:
            self.list.hide()
            self.listtag=False
        else:
            self.list.show()
            self.listtag=True
    def ratio(self):
        QApplication.processEvents()
        self.player.video_set_aspect_ratio('%s:%s'%(self.lmedia.width(),self.lmedia.height()))
    def Loop(self):
        self.loop+=1
        if self.loop>3:
            self.loop=0
        if self.loop==0:
            self.bloop.setIcon(QIcon(idirwithoutloop))
            self.bloop.setToolTip('无，快捷键“l”')
        elif self.loop==1:
            self.bloop.setIcon(QIcon(idirwithorderloop))
            self.bloop.setToolTip('顺序播放，快捷键“l”')
        elif self.loop==2:
            self.bloop.setIcon(QIcon(idirwithrandomloop))
            self.bloop.setToolTip('随机播放，快捷键“l”')
        else:
            self.bloop.setIcon(QIcon(idirwithloop))
            self.bloop.setToolTip('循环播放，快捷键“l”')
    def set_window(self,winid):
        if platform.system()=='Windows':
            self.player.set_hwnd(winid)
        elif platform.system()=='Linux':
            self.player.set_xwindow(winid)
        else:
            self.player.set_nsobject(winid)
    def Play(self):
        if self.flag:
            try:
                if self.fp!=None:
                    self.playitem=self.fp
                else:
                    if self.list.currentRow()==-1:
                        self.list.setCurrentRow(self.list.count()-1)
                    self.playitem=self.l[self.list.currentRow()]
                self.Savedplay()
            except:
                QMessageBox.warning(self,'错误','找不到要播放的文件！')
        else:
            if self.l[self.list.currentRow()]==self.playitem:
                if self.player.is_playing():
                    self.player.pause()
                    self.steptimer.stop()
                    self.bplay.setIcon(QIcon(idirplay))
                    self.bplay.setToolTip('播放，快捷键“Space”')
                else:
                    self.player.play()
                    self.steptimer.start()
                    self.bplay.setIcon(QIcon(idirpause))
                    self.bplay.setToolTip('暂停，快捷键“Space”')
            else:
                self.Progresssave()
                self.playitem=self.l[self.list.currentRow()]
                self.Savedplay()
    def Savedplay(self):
        self.step=playprogress=0
        if os.path.isfile('Progress.txt'):
            with open('Progress.txt','r',encoding='utf-8-sig',errors='ignore') as f:
                for i in f:
                    i=i.strip()
                    filepath=i[0:i.find(',')]
                    tmpplayprogress=i[i.find(',')+1:i.rfind(',')]
                    step=i[i.rfind(',')+1:len(i)]
                    if self.playitem==filepath:
                        self.step=int(step)
                        playprogress=float(tmpplayprogress)
        self.player.set_mrl("%s"%self.playitem)
        self.set_window(int(self.lmedia.winId()))
        self.player.play()
        self.stime.setValue(self.step)
        self.player.set_position(playprogress)
        self.timer.start(int(100/self.ratenum))
        self.steptimer.start(int(1000/self.ratenum))
        self.flag=False
        self.bplay.setIcon(QIcon(idirpause))
        self.bplay.setToolTip('暂停，快捷键“Space”')
    def Show(self):
        self.ratio()
        self.mediatime=self.player.get_length()/1000
        self.stime.setMaximum(int(self.mediatime))
        mediamin,mediasec=divmod(self.mediatime,60)
        mediahour,mediamin=divmod(mediamin,60)
        playmin,playsec=divmod(self.step,60)
        playhour,playmin=divmod(playmin,60)
        self.ltime.setText('%02d:%02d:%02d/%02d:%02d:%02d'%(playhour,playmin,playsec,mediahour,mediamin,mediasec))
    def Stop(self):
        if self.flag==False:
            self.Progresssave()
            Thread(target=self.Threadstop,daemon=True).start()
            self.timer.stop()
            self.steptimer.stop()
            self.step=0
            self.flag=True
            self.stime.setValue(0)
            self.ltime.setText('')
            self.bplay.setIcon(QIcon(idirplay))
            self.bplay.setToolTip('播放，快捷键“Space”')
    def Threadstop(self):
        self.player.stop()
    def Full(self):
        if self.fulltag:
            self.list.hide()
            self.frame.hide()
            self.showFullScreen()
            self.fulltag=False
        else:
            self.list.show()
            self.frame.show()
            self.showNormal()
            self.fulltag=True
    def Keep(self):
        if self.keeptag:
            self.bprogress.setText('关')
            self.keeptag=False
        else:
            self.bprogress.setText('开')
            self.keeptag=True
    def Progresssave(self):
        if self.keeptag:
            if self.flag==False:
                with open('Progress.txt','a',encoding='utf-8-sig',errors='ignore') as profile:
                    try:
                        profile.write('%s,%s,%s\n'%(self.playitem,self.step/int(self.mediatime),self.step))
                    except:
                        pass
    def Curspeed(self):
        self.curspe=self.sspeed.value()
        self.spetag=False
    def Recspeed(self):
        if self.flag==False:
            if self.player.get_rate()!=1.0:
                self.ratenum=1.0
                self.bspeed.setText('1.0X')
                self.bspeed.setToolTip('恢复速率，快捷键“b”')
            else:
                if self.sspeed.value()!=50:
                    self.ratenum=self.sspeed.value()/50
                else:
                    if self.spetag==False:
                        self.ratenum=self.curspe/50
                        self.sspeed.setValue(self.curspe)
                self.bspeed.setText('%sX'%(self.sspeed.value()/50))
                self.bspeed.setToolTip('重置速率，快捷键“b”')
            self.player.set_rate(self.ratenum)
            self.timer.start(int(100/self.ratenum))
            self.steptimer.start(int(1000/self.ratenum))
    def Speed(self):
        if self.flag==False:
            if self.sspeed.value()==50:
                self.bspeed.setText('1.0X')
                self.bspeed.setToolTip('恢复速率，快捷键“b”')
            else:
                self.bspeed.setText('%sX'%(self.sspeed.value()/50))
                self.bspeed.setToolTip('重置速率，快捷键“b”')
            self.ratenum=self.sspeed.value()/50
            self.player.set_rate(self.ratenum)
            self.timer.start(int(100/self.ratenum))
            self.steptimer.start(int(1000/self.ratenum))
    def Curvol(self):
        self.curvol=self.svolume.value()
        self.voltag=False
    def Mute(self):
        if self.flag==False:
            if self.player.audio_get_volume()!=0:
                self.player.audio_set_volume(0)
                self.bmute.setText('0')
                self.bmute.setToolTip('取消静音，快捷键“m”')
            else:
                if self.svolume.value()!=0:
                    self.player.audio_set_volume(self.svolume.value())
                else:
                    if self.voltag==False:
                        self.player.audio_set_volume(self.curvol)
                        self.svolume.setValue(self.curvol)
                self.bmute.setText('%s'%self.svolume.value())
                self.bmute.setToolTip('静音，快捷键“m”')
    def Volume(self):
        if self.flag==False:
            if self.svolume.value()==0:
                self.bmute.setText('0')
                self.bmute.setToolTip('取消静音，快捷键“m”')
            else:
                self.bmute.setText('%s'%self.svolume.value())
                self.bmute.setToolTip('静音，快捷键“m”')
            self.player.audio_set_volume(self.svolume.value())
    def Step(self):
        if self.step>=int(self.mediatime):
            self.step=int(self.mediatime)
            if self.loop==0:
                if not self.player.is_playing() and self.player.get_state()!=vlc.State.Paused:
                    self.Stop()
            else:
                if self.loop==1:
                    orderrow=self.list.currentRow()+1
                    if self.list.currentRow()==-1 or orderrow==self.list.count():
                        self.Stop()
                        QMessageBox.information(self,'播放完毕','当前播放列表播放完毕！')
                    else:
                        self.playitem=self.l[orderrow]
                        self.list.setCurrentRow(orderrow)
                        self.list.scrollToItem(self.list.item(orderrow),hint=1)
                        self.Savedplay()
                elif self.loop==2:
                    randomrow=random.randrange(self.list.count())
                    self.playitem=self.l[randomrow]
                    self.list.setCurrentRow(randomrow)
                    self.list.scrollToItem(self.list.item(randomrow),hint=1)
                    self.Savedplay()
                else:
                    self.Savedplay()
        else:
            self.step+=1
            self.stime.setValue(self.step)
    def Sliderpressed(self):
        if self.flag==False:
            self.curprogress=self.stime.value()
    def Slidechanged(self):
        if self.stime.value()!=0:
            self.step=self.stime.value()
        else:
            try:
                if self.curprogress>0:
                    self.step=0
            except:
                pass
    def Slidereleased(self):
        if self.flag==False:
            self.player.set_position(self.step/int(self.mediatime))
    def Fastback(self):
        if self.flag==False:
            self.step-=10
            if self.step<=0:
                self.step=0
            self.stime.setValue(self.step)
            self.player.set_position(self.step/int(self.mediatime))
    def Fastforward(self):
        if self.flag==False:
            self.step+=10
            if self.step>=int(self.mediatime):
                self.step=int(self.mediatime)
            self.stime.setValue(self.step)
            self.player.set_position(self.step/int(self.mediatime))
if __name__=='__main__':
    if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
    else:
        odir=os.path.dirname(os.path.abspath(__file__))
    idirCPlayer=os.path.join(odir,'img\CPlayer.png')
    idirabout=os.path.join(odir,'img\gitee.png')
    idirexit=os.path.join(odir,'img\exit.png')
    idirwithoutloop=os.path.join(odir,'img\withoutloop.png')
    idirwithorderloop=os.path.join(odir,'img\withorderloop.png')
    idirwithrandomloop=os.path.join(odir,'img\withrandomloop.png')
    idirwithloop=os.path.join(odir,'img\withloop.png')
    idirpause=os.path.join(odir,'img\pause.png')
    idirplay=os.path.join(odir,'img\play.png')
    idirexpandfullscreen=os.path.join(odir,'img\expandfullscreen.png')
    exepath=sys.executable
    idirCPlayerpy=os.path.abspath(__file__)
    if 'CPlayer.exe' in exepath:
        idirvlc=os.path.join(os.path.dirname(exepath),'vlc')
    else:
        idirvlc=os.path.join(os.path.dirname(os.path.abspath(__file__)),'vlc')
    os.environ['PYTHON_VLC_MODULE_PATH']=idirvlc
    import vlc
    try:
        fp=sys.argv[1]
    except:
        fp=None
    try:
        key0=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'*\\shell\\用CPlayer打开')
        winreg.CloseKey(key0)
        app=QApplication(sys.argv)
        QApplication.setQuitOnLastWindowClosed(False)
        win=Window()
        win.show()
        sys.exit(app.exec_())
    except:
        if ctypes.windll.shell32.IsUserAnAdmin():
            menu_name='用CPlayer打开'
            if 'CPlayer.exe' in exepath:
                command=r'"%s"'%exepath
            else:
                command=r'"%s" "%s"'%(exepath,idirCPlayerpy)
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
                app=QApplication(sys.argv)
                QApplication.setQuitOnLastWindowClosed(False)
                win=Window()
                win.show()
                sys.exit(app.exec_())