import os
import sys
import glob
import serial.tools.list_ports

import PySide6
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtGui

os.system('''pyside6-rcc res.qrc -o res_rc.py
pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView

from ui_mainwindow import Ui_MainWindow

# need to ask Alex, about what should I do when meet end of data in file
def checkString(data):
    if data == '':
        return "00000000"
    else:
        return data

def makeUpperLetters(data):
    for i in range(len(data)):
        if data[i].isalpha():
            data = data[:i] + data[i].upper() + data[i+1:]
    return data

def makeHexArray(data):
    hexData = []
    for i in range(len(data)):
        symbInCode = hex(data[i])[2:4]
        if len(symbInCode) == 1:
            symbInCode = '0' + symbInCode
        hexData.append(symbInCode)
    return hexData

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # make my table beautiful
        self.ui.adressTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.adressTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # for second table
        self.ui.secondAdressTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.secondAdressTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # open file, when user click button - Open
        self.ui.actionOpen.triggered.connect(self.openFile)
        # compare files
        self.ui.actionCompare.triggered.connect(self.compareFiles)
        # find all serial ports
        # self.ui.ChoosePort.clicked.connect(self.checkPorts)
        self.ui.finishCompare.clicked.connect(self.closeCompare)
        # it trigers when user change number in spinbox
        self.ui.baseAdress.valueChanged.connect(self.updateTable)

        # I hide second table
        self.ui.secondAdressTable.setVisible(0)
        self.ui.finishCompare.setVisible(0)

        # global var, which includes all data
        # self.tableData = []
        self.firstFileData = []
        self.secondFileData = []

        # code
        self.show()

    # open choosen file
    def openFile(self):
            self.ui.plainTextEdit.setPlainText("Добро пожаловать!")
            FileDial = QFileDialog(caption="Выберите файл с прошивкой", filter="Текст (*.bin)")
            if (not FileDial.exec()): return
            openedFile = FileDial.selectedFiles()[0]
            # rb for bin
            file = open(openedFile, 'rb')
            # get all data
            data = file.read()
            file.close()
            if not data:
                self.ui.plainTextEdit.setPlainText("Считывание данных не выполнено! Выбранный вами файл пуст.")
                return
            else:
                self.ui.plainTextEdit.setPlainText("Процесс выполнения")
            # flag which shows that almost is okey
            ok = True
            self.firstFileData = makeHexArray(data)
            self.fillTheTables(1, self.ui.baseAdress.value())
            # Если данные успешно считаны вывести результат в окно отчета
            if ok:
                self.ui.plainTextEdit.appendPlainText("Считывание данных успешно выполнено...")

    def updateTable(self):
        # get base and then call func -> fill two tables
        base = self.ui.baseAdress.value()
        self.fillTheTables(1, base)
        self.fillTheTables(2, base)
        self.ui.plainTextEdit.appendPlainText("Базовый адрес обновлен")

    def compareFiles(self):
        # show the second table, comparable one
        self.ui.secondAdressTable.setVisible(1)
        self.ui.finishCompare.setVisible(1)

        FileDial = QFileDialog(caption="Выберите файл с прошивкой", filter="Текст (*.bin)")
        if (not FileDial.exec()): return
        openedFile = FileDial.selectedFiles()[0]
        file = open(openedFile, 'rb')
        # get all data
        data = file.read()
        file.close()

        # flag which shows that almost is okey
        ok = True
        # data which will be introduced in the table
        self.secondFileData = makeHexArray(data)
        self.fillTheTables(2, self.ui.baseAdress.value())
        # Если данные успешно считаны вывести результат в окно отчета
        if ok:
            self.ui.plainTextEdit.appendPlainText("Считывание данных сравниваемого файла успешно выполнено...")

        # okey let's start comparing two files
        if self.firstFileData and self.secondFileData:
            difference = []
            print(len(self.firstFileData))
            if len(self.firstFileData) == len(self.secondFileData):
                for i in range(len(self.firstFileData)):
                    if self.firstFileData[i] != self.secondFileData:
                        difference.append(i)
                # print(*difference)

            else:
                print("Sizes of two files are not equal")

    def fillTheTables(self, tableNum, base):
        baseCnt = base
        if tableNum == 1:
            table = self.ui.adressTable
            fileData = self.firstFileData
        else:
            table = self.ui.secondAdressTable
            fileData = self.secondFileData
        table.setRowCount(0)

        for i in range(base, len(fileData), 16):
            # check for size before using slice
                firstStr = ''.join(fileData[i:i+4])
                secondStr = ''.join(fileData[i+4:i+8])
                threeStr = ''.join(fileData[i+8:i+12])
                forthStr = ''.join(fileData[i+12:i+16])
            # ask Alex,what to fulfiil in such case
                firstStr = checkString(firstStr)
                secondStr = checkString(secondStr)
                threeStr = checkString(threeStr)
                forthStr = checkString(forthStr)
                firstStr = makeUpperLetters(firstStr)
                secondStr = makeUpperLetters(secondStr)
                threeStr = makeUpperLetters(threeStr)
                forthStr = makeUpperLetters(forthStr)
            # if i have my strings:
                rowPosition = table.rowCount()
                table.insertRow(rowPosition)
                table.setItem(rowPosition, 0, QTableWidgetItem(str(baseCnt)))
                table.setItem(rowPosition, 1, QTableWidgetItem(firstStr))
                table.setItem(rowPosition, 2, QTableWidgetItem(secondStr))
                table.setItem(rowPosition, 3, QTableWidgetItem(threeStr))
                table.setItem(rowPosition, 4, QTableWidgetItem(forthStr))
                baseCnt += 16

    def closeCompare(self):
        # clean interface from compare and all clean data
        self.ui.secondAdressTable.setVisible(0)
        self.ui.finishCompare.setVisible(0)
        self.ui.secondAdressTable.setRowCount(0)
        self.ui.secondFileData = []
        self.ui.plainTextEdit.appendPlainText("Процесс сравнения завершен")

    def fileOpenDialog(self):
        pass

        # when something is changed in spinbox, my array also keep last opened file!
    def checkPorts(self):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))

    def readData(self):
        pass

    def writeData(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
