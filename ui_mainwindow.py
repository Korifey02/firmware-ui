# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1021, 812)
        MainWindow.setMinimumSize(QSize(650, 550))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/newPrefix/res/terminator.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #404040;\n"
"")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        font = QFont()
        font.setPointSize(8)
        self.actionOpen.setFont(font)
        self.actionCompare = QAction(MainWindow)
        self.actionCompare.setObjectName(u"actionCompare")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 150))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.baseAdress = QSpinBox(self.frame)
        self.baseAdress.setObjectName(u"baseAdress")
        self.baseAdress.setStyleSheet(u"QSpinBox{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")
        self.baseAdress.setMaximum(1000)

        self.verticalLayout.addWidget(self.baseAdress)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adressTable = QTableWidget(self.frame_3)
        if (self.adressTable.columnCount() < 5):
            self.adressTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        self.adressTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.adressTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.adressTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.adressTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.adressTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.adressTable.setObjectName(u"adressTable")
        self.adressTable.setStyleSheet(u"QTableWidget{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")
        self.adressTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout.addWidget(self.adressTable)

        self.secondAdressTable = QTableWidget(self.frame_3)
        if (self.secondAdressTable.columnCount() < 5):
            self.secondAdressTable.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.secondAdressTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.secondAdressTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.secondAdressTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.secondAdressTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.secondAdressTable.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.secondAdressTable.setObjectName(u"secondAdressTable")
        self.secondAdressTable.setStyleSheet(u"QTableWidget{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")
        self.secondAdressTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.secondAdressTable.setAlternatingRowColors(False)

        self.horizontalLayout.addWidget(self.secondAdressTable)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.finishCompare = QPushButton(self.frame_2)
        self.finishCompare.setObjectName(u"finishCompare")
        self.finishCompare.setStyleSheet(u"QPushButton{\n"
"border:  2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #A4004D;\n"
"background-color: #444444;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.finishCompare)


        self.verticalLayout.addWidget(self.frame_2)

        self.Read = QPushButton(self.frame)
        self.Read.setObjectName(u"Read")
        self.Read.setStyleSheet(u"QPushButton{\n"
"border:  2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #A4004D;\n"
"background-color: #444444;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.Read)

        self.Write = QPushButton(self.frame)
        self.Write.setObjectName(u"Write")
        self.Write.setStyleSheet(u"QPushButton{\n"
"border:  2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #A4004D;\n"
"background-color: #444444;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.Write)

        self.ChoosePort = QPushButton(self.frame)
        self.ChoosePort.setObjectName(u"ChoosePort")
        self.ChoosePort.setStyleSheet(u"QPushButton{\n"
"border:  2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #A4004D;\n"
"background-color: #444444;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: #444444;\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.ChoosePort)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1021, 26))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.menuBar.setFont(font1)
        self.menuBar.setStyleSheet(u"")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCompare)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WindowTitle", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionCompare.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        ___qtablewidgetitem = self.adressTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem1 = self.adressTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem2 = self.adressTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem3 = self.adressTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem4 = self.adressTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem5 = self.secondAdressTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem6 = self.secondAdressTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem7 = self.secondAdressTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.secondAdressTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem9 = self.secondAdressTable.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"12", None));
        self.finishCompare.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.Read.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.Write.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.ChoosePort.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u043e\u0440\u0442", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

