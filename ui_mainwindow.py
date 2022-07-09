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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 810)
        MainWindow.setMinimumSize(QSize(650, 650))
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
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 120))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.baseAdress = QSpinBox(self.frame_8)
        self.baseAdress.setObjectName(u"baseAdress")
        self.baseAdress.setStyleSheet(u"QSpinBox{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")
        self.baseAdress.setMaximum(255)
        self.baseAdress.setValue(29)

        self.gridLayout.addWidget(self.baseAdress, 1, 0, 1, 1)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.fileSize = QLabel(self.frame_8)
        self.fileSize.setObjectName(u"fileSize")
        self.fileSize.setStyleSheet(u"QLabel{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")

        self.gridLayout.addWidget(self.fileSize, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 180))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adressTable = QTableWidget(self.frame_3)
        if (self.adressTable.columnCount() < 5):
            self.adressTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
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
"}\n"
"QHeaderView::section\n"
"{\n"
"	background-color: #404040;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: #404040;\n"
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
"}\n"
"QHeaderView::section\n"
"{\n"
"	background-color: #404040;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: #404040;\n"
"}")
        self.secondAdressTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.secondAdressTable.setAlternatingRowColors(False)

        self.horizontalLayout.addWidget(self.secondAdressTable)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.compareToolsFrame = QFrame(self.frame_2)
        self.compareToolsFrame.setObjectName(u"compareToolsFrame")
        self.compareToolsFrame.setFrameShape(QFrame.StyledPanel)
        self.compareToolsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.compareToolsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(258, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.frame_7 = QFrame(self.compareToolsFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.startCompare = QPushButton(self.frame_7)
        self.startCompare.setObjectName(u"startCompare")
        self.startCompare.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_5.addWidget(self.startCompare)

        self.finishCompare = QPushButton(self.frame_7)
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

        self.verticalLayout_5.addWidget(self.finishCompare)

        self.compareResult = QLabel(self.frame_7)
        self.compareResult.setObjectName(u"compareResult")
        self.compareResult.setStyleSheet(u"color: rgb(0, 255, 127);\n"
"\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.compareResult)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.compareToolsFrame)


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

        self.ShowReadData = QPushButton(self.frame)
        self.ShowReadData.setObjectName(u"ShowReadData")
        self.ShowReadData.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.ShowReadData)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(817, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ChoosePort = QPushButton(self.frame_6)
        self.ChoosePort.setObjectName(u"ChoosePort")
        self.ChoosePort.setMinimumSize(QSize(100, 25))
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

        self.verticalLayout_3.addWidget(self.ChoosePort)

        self.portList = QComboBox(self.frame_6)
        self.portList.setObjectName(u"portList")
        self.portList.setMinimumSize(QSize(130, 0))
        self.portList.setStyleSheet(u"QComboBox{\n"
"border: 2px solid #A4004D;\n"
"background-color: #404040;\n"
"color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.portList)

        self.warningPorts = QLabel(self.frame_6)
        self.warningPorts.setObjectName(u"warningPorts")
        self.warningPorts.setStyleSheet(u"color: rgb(255, 6, 43);")

        self.verticalLayout_3.addWidget(self.warningPorts)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1051, 26))
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
        self.menuFile.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WindowTitle", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionCompare.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.fileSize.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442 \u0438\u043b\u0438 \u043d\u0435 \u0441\u0447\u0438\u0442\u0430\u043d", None))
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
        self.startCompare.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c", None))
        self.finishCompare.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.compareResult.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0432\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u044b \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442", None))
        self.Read.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.Write.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.ShowReadData.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.ChoosePort.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u043e\u0440\u0442", None))
        self.warningPorts.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0445 \u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

