# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 702)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/CPlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setMinimumSize(QtCore.QSize(300, 0))
        self.list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list.setDragEnabled(True)
        self.list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list.setObjectName("list")
        self.horizontalLayout_2.addWidget(self.list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lmedia = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lmedia.sizePolicy().hasHeightForWidth())
        self.lmedia.setSizePolicy(sizePolicy)
        self.lmedia.setMinimumSize(QtCore.QSize(800, 600))
        self.lmedia.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lmedia.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lmedia.setText("")
        self.lmedia.setScaledContents(True)
        self.lmedia.setAlignment(QtCore.Qt.AlignCenter)
        self.lmedia.setObjectName("lmedia")
        self.verticalLayout.addWidget(self.lmedia)
        self.stime = QtWidgets.QSlider(self.centralwidget)
        self.stime.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stime.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.stime.setMaximum(2147483647)
        self.stime.setPageStep(0)
        self.stime.setOrientation(QtCore.Qt.Horizontal)
        self.stime.setObjectName("stime")
        self.verticalLayout.addWidget(self.stime)
        self.ltime = QtWidgets.QLabel(self.centralwidget)
        self.ltime.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255)")
        self.ltime.setText("")
        self.ltime.setObjectName("ltime")
        self.verticalLayout.addWidget(self.ltime)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blist = QtWidgets.QPushButton(self.frame)
        self.blist.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blist.setIcon(icon1)
        self.blist.setIconSize(QtCore.QSize(35, 35))
        self.blist.setFlat(True)
        self.blist.setObjectName("blist")
        self.horizontalLayout.addWidget(self.blist)
        self.bfastback = QtWidgets.QPushButton(self.frame)
        self.bfastback.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/fastback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bfastback.setIcon(icon2)
        self.bfastback.setIconSize(QtCore.QSize(50, 50))
        self.bfastback.setFlat(True)
        self.bfastback.setObjectName("bfastback")
        self.horizontalLayout.addWidget(self.bfastback)
        self.bloop = QtWidgets.QPushButton(self.frame)
        self.bloop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/withoutloop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloop.setIcon(icon3)
        self.bloop.setIconSize(QtCore.QSize(35, 35))
        self.bloop.setFlat(True)
        self.bloop.setObjectName("bloop")
        self.horizontalLayout.addWidget(self.bloop)
        self.bplay = QtWidgets.QPushButton(self.frame)
        self.bplay.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bplay.setIcon(icon4)
        self.bplay.setIconSize(QtCore.QSize(50, 50))
        self.bplay.setFlat(True)
        self.bplay.setObjectName("bplay")
        self.horizontalLayout.addWidget(self.bplay)
        self.bstop = QtWidgets.QPushButton(self.frame)
        self.bstop.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bstop.setIcon(icon5)
        self.bstop.setIconSize(QtCore.QSize(50, 50))
        self.bstop.setFlat(True)
        self.bstop.setObjectName("bstop")
        self.horizontalLayout.addWidget(self.bstop)
        self.bfull = QtWidgets.QPushButton(self.frame)
        self.bfull.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/expandfullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bfull.setIcon(icon6)
        self.bfull.setIconSize(QtCore.QSize(35, 35))
        self.bfull.setFlat(True)
        self.bfull.setObjectName("bfull")
        self.horizontalLayout.addWidget(self.bfull)
        self.bfastforward = QtWidgets.QPushButton(self.frame)
        self.bfastforward.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/fastforward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bfastforward.setIcon(icon7)
        self.bfastforward.setIconSize(QtCore.QSize(50, 50))
        self.bfastforward.setFlat(True)
        self.bfastforward.setObjectName("bfastforward")
        self.horizontalLayout.addWidget(self.bfastforward)
        self.bprogress = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bprogress.setFont(font)
        self.bprogress.setFlat(True)
        self.bprogress.setObjectName("bprogress")
        self.horizontalLayout.addWidget(self.bprogress)
        self.bspeed = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bspeed.setFont(font)
        self.bspeed.setFlat(True)
        self.bspeed.setObjectName("bspeed")
        self.horizontalLayout.addWidget(self.bspeed)
        self.sspeed = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sspeed.sizePolicy().hasHeightForWidth())
        self.sspeed.setSizePolicy(sizePolicy)
        self.sspeed.setMinimumSize(QtCore.QSize(150, 0))
        self.sspeed.setMaximum(100)
        self.sspeed.setProperty("value", 50)
        self.sspeed.setOrientation(QtCore.Qt.Horizontal)
        self.sspeed.setObjectName("sspeed")
        self.horizontalLayout.addWidget(self.sspeed)
        self.bmute = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bmute.setFont(font)
        self.bmute.setFlat(True)
        self.bmute.setObjectName("bmute")
        self.horizontalLayout.addWidget(self.bmute)
        self.svolume = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.svolume.sizePolicy().hasHeightForWidth())
        self.svolume.setSizePolicy(sizePolicy)
        self.svolume.setMinimumSize(QtCore.QSize(150, 0))
        self.svolume.setMaximum(100)
        self.svolume.setProperty("value", 100)
        self.svolume.setOrientation(QtCore.Qt.Horizontal)
        self.svolume.setObjectName("svolume")
        self.horizontalLayout.addWidget(self.svolume)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.list.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.Play)
        self.list.customContextMenuRequested['QPoint'].connect(MainWindow.Listmenu)
        self.list.itemEntered['QListWidgetItem*'].connect(MainWindow.Drag)
        self.blist.clicked.connect(MainWindow.Listhide)
        self.bfastback.clicked.connect(MainWindow.Fastback)
        self.bloop.clicked.connect(MainWindow.Loop)
        self.bplay.clicked.connect(MainWindow.Play)
        self.svolume.sliderPressed.connect(MainWindow.Curvol)
        self.svolume.valueChanged['int'].connect(MainWindow.Volume)
        self.sspeed.sliderPressed.connect(MainWindow.Curspeed)
        self.sspeed.valueChanged['int'].connect(MainWindow.Speed)
        self.bmute.clicked.connect(MainWindow.Mute)
        self.bspeed.clicked.connect(MainWindow.Recspeed)
        self.stime.sliderPressed.connect(MainWindow.Sliderpressed)
        self.stime.valueChanged['int'].connect(MainWindow.Slidechanged)
        self.stime.sliderReleased.connect(MainWindow.Slidereleased)
        self.bfastforward.clicked.connect(MainWindow.Fastforward)
        self.bstop.clicked.connect(MainWindow.Stop)
        self.bfull.clicked.connect(MainWindow.Full)
        self.bprogress.clicked.connect(MainWindow.Keep)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPlayer"))
        self.blist.setToolTip(_translate("MainWindow", "显示/隐藏播放列表，快捷键“p”"))
        self.blist.setShortcut(_translate("MainWindow", "P"))
        self.bfastback.setToolTip(_translate("MainWindow", "快退10秒，快捷键“t”"))
        self.bfastback.setShortcut(_translate("MainWindow", "T"))
        self.bloop.setToolTip(_translate("MainWindow", "无，快捷键“l”"))
        self.bloop.setShortcut(_translate("MainWindow", "L"))
        self.bplay.setToolTip(_translate("MainWindow", "播放，快捷键“Space”"))
        self.bplay.setShortcut(_translate("MainWindow", "Space"))
        self.bstop.setToolTip(_translate("MainWindow", "停止，快捷键“s”"))
        self.bstop.setShortcut(_translate("MainWindow", "S"))
        self.bfull.setToolTip(_translate("MainWindow", "全屏，快捷键“f”"))
        self.bfull.setShortcut(_translate("MainWindow", "F"))
        self.bfastforward.setToolTip(_translate("MainWindow", "快进10秒，快捷键“j”"))
        self.bfastforward.setShortcut(_translate("MainWindow", "J"))
        self.bprogress.setToolTip(_translate("MainWindow", "保存当前播放进度，快捷键“k”"))
        self.bprogress.setText(_translate("MainWindow", "开"))
        self.bprogress.setShortcut(_translate("MainWindow", "K"))
        self.bspeed.setToolTip(_translate("MainWindow", "重置速率，快捷键“b”"))
        self.bspeed.setText(_translate("MainWindow", "1.0X"))
        self.bspeed.setShortcut(_translate("MainWindow", "B"))
        self.sspeed.setToolTip(_translate("MainWindow", "快捷键：速率加“i”，速率减“d”"))
        self.bmute.setToolTip(_translate("MainWindow", "静音，快捷键“m”"))
        self.bmute.setText(_translate("MainWindow", "100"))
        self.bmute.setShortcut(_translate("MainWindow", "M"))
        self.svolume.setToolTip(_translate("MainWindow", "快捷键：音量加“a”，音量减“r”"))
import img_rc
