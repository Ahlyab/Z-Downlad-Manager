# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 490)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(110, 0, 841, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(22, 22))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(50, 40, 321, 121))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(110, 0, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 0, 111, 121))
        self.pushButton_16.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home_download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon)
        self.pushButton_16.setIconSize(QtCore.QSize(80, 70))
        self.pushButton_16.setObjectName("pushButton_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 40, 331, 121))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 0, 111, 121))
        self.pushButton_17.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QtCore.QSize(80, 70))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(110, 0, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 220, 321, 121))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(110, 0, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 0, 111, 121))
        self.pushButton_18.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/home_youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QtCore.QSize(80, 70))
        self.pushButton_18.setObjectName("pushButton_18")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 220, 331, 121))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(110, 0, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_19.setGeometry(QtCore.QRect(0, 0, 111, 121))
        self.pushButton_19.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/home_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon3)
        self.pushButton_19.setIconSize(QtCore.QSize(80, 70))
        self.pushButton_19.setObjectName("pushButton_19")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(330, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(27, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(130, 200, 571, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(-10, 0, 851, 431))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 70, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 110, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(27, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(660, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QtCore.QSize(27, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(160, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 160, 241, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(120, 260, 171, 21))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar_2.setGeometry(QtCore.QRect(120, 220, 571, 31))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 50, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 90, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_3.setGeometry(QtCore.QRect(120, 230, 561, 31))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 270, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 90, 51, 31))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(27, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(160, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(320, 140, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber.setGeometry(QtCore.QRect(260, 190, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(370, 190, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber_2.setGeometry(QtCore.QRect(540, 190, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(110, 280, 191, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 160, 181, 121))
        self.pushButton_13.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_14.setGeometry(QtCore.QRect(230, 160, 181, 121))
        self.pushButton_14.setStyleSheet("background-color: rgb(25, 35, 45);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_15.setGeometry(QtCore.QRect(430, 160, 181, 121))
        self.pushButton_15.setStyleSheet("background-color: rgb(32, 31, 31);")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(146, 50, 541, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(90)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_20.setGeometry(QtCore.QRect(630, 160, 181, 121))
        self.pushButton_20.setStyleSheet("background-color: rgb(32, 31, 31);\n"
"background-color: rgb(235, 235, 235);")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_21.setGeometry(QtCore.QRect(710, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Nokia Pure Headline Light")
        font.setPointSize(19)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_12 = QtWidgets.QLabel(self.tab_7)
        self.label_12.setGeometry(QtCore.QRect(60, 50, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Multiscript")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_7)
        self.label_13.setGeometry(QtCore.QRect(80, 110, 761, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_7)
        self.label_14.setGeometry(QtCore.QRect(60, 140, 721, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_7)
        self.label_15.setGeometry(QtCore.QRect(70, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_7)
        self.label_16.setGeometry(QtCore.QRect(360, 170, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_7)
        self.label_17.setGeometry(QtCore.QRect(70, 210, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_7)
        self.label_18.setGeometry(QtCore.QRect(530, 210, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_7)
        self.label_19.setGeometry(QtCore.QRect(70, 240, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(70, 270, 481, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.tab_7, "")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 10, 101, 81))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QtCore.QSize(90, 70))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 280, 101, 81))
        self.pushButton_10.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QtCore.QSize(90, 70))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 190, 101, 81))
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QtCore.QSize(90, 70))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 100, 101, 81))
        self.pushButton_12.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/download2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QtCore.QSize(90, 70))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 370, 101, 81))
        self.pushButton_7.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon9)
        self.pushButton_7.setIconSize(QtCore.QSize(90, 70))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Z-Download Manager"))
        self.label_8.setText(_translate("MainWindow", " Download Any Type of File"))
        self.label_9.setText(_translate("MainWindow", " Youtube Video Download"))
        self.label_10.setText(_translate("MainWindow", " Youtube Playlist Download"))
        self.label_11.setText(_translate("MainWindow", " App Themes & Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.pushButton.setText(_translate("MainWindow", "Start Download"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Paste Download Link"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Location For Downloading File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "File"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Paste Video URL"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Enter Location For Downloading File"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Download"))
        self.label_2.setText(_translate("MainWindow", " Video Quality"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Single Video"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Paste Playlist URL"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Enter Location For Downloading File"))
        self.pushButton_5.setText(_translate("MainWindow", "Start Download"))
        self.label.setText(_translate("MainWindow", "  Video Quality"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1080"))
        self.comboBox.setItemText(1, _translate("MainWindow", "720"))
        self.comboBox.setItemText(2, _translate("MainWindow", "480"))
        self.comboBox.setItemText(3, _translate("MainWindow", "360"))
        self.label_3.setText(_translate("MainWindow", "The Current Video :"))
        self.label_4.setText(_translate("MainWindow", "The Full Playlist Video :"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Full Playlist"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Video"))
        self.label_7.setText(_translate("MainWindow", "Choose Your Theme"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.pushButton_21.setText(_translate("MainWindow", "Close"))
        self.label_12.setText(_translate("MainWindow", "Z-Download Manager"))
        self.label_13.setText(_translate("MainWindow", "Z-Download Manager is an open-source tool for downloading files with high speed. "))
        self.label_14.setText(_translate("MainWindow", " It allows you to download youtube videos individually or you can download the whole "))
        self.label_15.setText(_translate("MainWindow", "youtube playlist with a single click."))
        self.label_16.setText(_translate("MainWindow", " You can select the video quality and download it."))
        self.label_17.setText(_translate("MainWindow", "All the copyrights © are reserved to Zuse Production."))
        self.label_18.setText(_translate("MainWindow", " Any change in its source code"))
        self.label_19.setText(_translate("MainWindow", "of duplication of code in any form is illegal."))
        self.label_20.setText(_translate("MainWindow", "Z-Download Manager product of Zuse Production."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page"))
import Photos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
