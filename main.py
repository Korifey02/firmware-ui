import os
import sys
import glob
from tkinter.ttk import Style
from unittest import findTestCases
from numpy import MAY_SHARE_EXACT, byte, full
import serial.tools.list_ports
import serial
import math as m

import PySide6
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtGui
from PySide6.QtGui import Qt, QPalette, QColor

os.system('''pyside6-rcc res.qrc -o res_rc.py
pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView, QStyleFactory

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
        self.ui.ChoosePort.clicked.connect(self.checkPorts)
        self.ui.finishCompare.clicked.connect(self.closeCompare)
        # it trigers when user change number in spinbox
        self.ui.baseAdress.valueChanged.connect(self.updateTable)

        self.ui.Write.clicked.connect(self.writeData)
        self.ui.Read.clicked.connect(self.readData)
        self.ui.startCompare.clicked.connect(self.startCompareFiles)

        self.ui.ShowReadData.clicked.connect(self.showReadData)

        # I hide second table
        self.ui.secondAdressTable.setVisible(0)
        self.ui.finishCompare.setVisible(0)
        self.ui.startCompare.setVisible(0)
        self.ui.compareResult.setVisible(0)

        

        self.ui.warningPorts.setVisible(0)

        # global var, which includes all data
        # self.tableData = []
        self.firstFileData = []
        self.secondFileData = []
        self.readDataArray = [] 
        self.openedDataSize = 0 
        
        self.ChoosenPort = 'Порт не выбран'
        self.ui.portList.clear()
        self.ui.portList.addItems([self.ChoosenPort])

        self.AvalaiblePorts = []

        self.FileData = ''
        self.DataToSend = ''

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
            self.openedDataSize = len(data)
            self.DataToSend = data

            if not data:
                self.ui.plainTextEdit.setPlainText("Считывание данных не выполнено! Выбранный вами файл пуст.")
                return
            else:
                self.ui.plainTextEdit.setPlainText("Процесс выполнения")
            # flag which shows that almost is okey
            ok = True
            
            # bufMass = []
            # for i in range(len(data)):
            #     print(data[i])
            #     print(chr(data[i]))
            #     bufMass.append(chr(data[i]))
            
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
        self.ui.startCompare.setVisible(1)

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

    def startCompareFiles(self):
        if self.firstFileData and self.secondFileData:
            difference = []
            ok = 1 
            if len(self.firstFileData) == len(self.secondFileData):
                for i in range(len(self.firstFileData)):
                    if self.firstFileData[i] != self.secondFileData[i]:
                        difference.append(i)
                        ok = 0
                        break
                if not ok:
                    self.ui.compareResult.setText("Выбранные файлы не совпадают")
                    self.ui.compareResult.setStyleSheet("QLabel {color: rgb(255, 6, 43);}")
                else:
                    self.ui.compareResult.setText("Выбранные вами файлы совпадают")
                    self.ui.compareResult.setStyleSheet("QLabel {color: rgb(0, 255, 127);}")
            else:
                self.ui.compareResult.setText("Размеры файлов не совпадают")
                self.ui.compareResult.setStyleSheet("QLabel {color: rgb(255, 6, 43);}")
        else:
            self.ui.compareResult.setText("Один из файлов пуст")
            self.ui.compareResult.setStyleSheet("QLabel {color: rgb(255, 6, 43);}")
        self.ui.compareResult.setVisible(1)


    def fillTheTables(self, tableNum, base):
        baseCnt = base
        if tableNum == 1:
            table = self.ui.adressTable
            fileData = self.firstFileData
        elif tableNum == 2:
            table = self.ui.secondAdressTable
            fileData = self.secondFileData
        else:
            table = self.ui.adressTable
            fileData = self.readDataArray
        table.setRowCount(0)

        for i in range(base, len(fileData), 16):
            # check for size before using slice
                firstStr = ''.join(fileData[i:i+4])
                secondStr = ''.join(fileData[i+4:i+8])
                threeStr = ''.join(fileData[i+8:i+12])
                forthStr = ''.join(fileData[i+12:i+16])
            # ask Alex,what to fulfiil in such case
                # firstStr = checkString(firstStr)
                # secondStr = checkString(secondStr)
                # threeStr = checkString(threeStr)
                # forthStr = checkString(forthStr)
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
        self.ui.startCompare.setVisible(0)
        self.ui.compareResult.setVisible(0)
        self.ui.plainTextEdit.appendPlainText("Процесс сравнения завершен")

    def fileOpenDialog(self):
        pass

        # when something is changed in spinbox, my array also keep last opened file!
    def checkPorts(self):

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        
        self.ui.portList.clear()
        self.ui.portList.addItems(result)
        self.AvalaiblePorts = result

        if result:
            self.ui.warningPorts.setVisible(0)
        else:
            pass

    def readData(self):
        myRequest = []
        if self.AvalaiblePorts:
            self.ChoosenPort = self.ui.portList.currentText()
            # then we ready to start communication
            mass = [chr(0x1A), chr(self.ui.baseAdress.value())]
            weReadyMessage = bytes(''.join(mass), 'utf8')
            # open communication
            ser = serial.Serial()
            ser.baudrate = 115200
            ser.port = self.ChoosenPort
            ser.open()
            # send wirst command - we are ready
            ser.write(weReadyMessage)
            a = ser.read(4)
            result = a[1:]
            # notInBytes = result.decode("utf-8")

            resultNums = []
            for i in range(len(result)):
                resultNums.append(result[i])


            sum = 0
            for i in range(len(resultNums)):
                # print(ord(notInBytes[i]))
                if i + 1 == len(resultNums):
                    sum += resultNums[i]
                else:   
                    sum += resultNums[i] * 256
            
            amountOfSends = int(m.ceil(sum/128))
            amountOfBig = sum // 128
            readData = []
            for i in range(amountOfSends):
                newString = []
                if (i + 1) == amountOfSends:
                    correctLine = ser.read(2 + sum - (128 * amountOfBig))[2:]
                    for i in range(len(correctLine)):
                        newString.append(correctLine[i])
                    readData.append(newString)
                else:
                    correctLine = ser.read(130)[2:]
                    for i in range(len(correctLine)):
                        newString.append(correctLine[i])
                    readData.append(newString)
            ser.close()
            self.readDataArray = readData

        else:
            print("Ports are not choosen")
            self.ui.warningPorts.setVisible(1)


    def showReadData(self):
        if self.readDataArray:
            configuratedData = []
            hexArray  = []
            for i in range(len(self.readDataArray)):
                for j in range(len(self.readDataArray[i])):
                    configuratedData.append(self.readDataArray[i][j])
            for i in range(len(configuratedData)):
                hexSymb = hex(configuratedData[i])
                hexArray.append(hexSymb)
            
            hexData = []
            for i in range(len(hexArray)):
                symbInCode = hexArray[i][2:4]
                if len(symbInCode) == 1:
                    symbInCode = '0' + symbInCode
                hexData.append(symbInCode)
                
            self.readDataArray = hexData
            self.fillTheTables(3, self.ui.baseAdress.value())
            
        
    def writeData(self):
        if self.AvalaiblePorts:

            self.ChoosenPort = self.ui.portList.currentText()
            # then we ready to start communication

            thirdSignal = []
            mass = [chr(0x1B), chr(self.ui.baseAdress.value())]

            firmwareSize = self.openedDataSize

            while firmwareSize:
                buffer = firmwareSize % 256
                firmwareSize //= 256
                thirdSignal.append(chr(buffer))
            
            if not firmwareSize and len(thirdSignal) == 2:
                thirdSignal.append(chr(0))

            
            mass.extend(thirdSignal[::-1])
            message = bytes(''.join(mass), 'utf8')


            ser = serial.Serial()
            ser.baudrate = 115200
            ser.port = self.ChoosenPort
            ser.open()
            print(ser.is_open)
            # ser.write(message)
            
            # TODO 
            # ser.read(2)
            # check for signal is ready and almost is OK!
            
            # send info packs
            for i in range(0, self.openedDataSize, 127):
                arrayToSend = self.DataToSend[i:i+127]
                component = bytes(chr(0x1E), 'utf8')
                component += bytes(chr(len(arrayToSend)), 'utf8')
                fullMassege = component + arrayToSend
                ser.write(fullMassege)
            ser.close()
        else:
            print("Ports are not choosen")
            self.ui.warningPorts.setVisible(1)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()



    # app.setStyle(QStyleFactory.create('Fusion'))
    # darkPalette = QPalette()

    # darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
    # darkPalette.setColor(QPalette.WindowText, Qt.white)
    # darkPalette.setColor(QPalette.Base, QColor(35, 35, 35))
    # darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))

    # darkPalette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    # darkPalette.setColor(QPalette.ToolTipText, Qt.white)
    # darkPalette.setColor(QPalette.Text, Qt.white)
    # darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
    # darkPalette.setColor(QPalette.ButtonText, Qt.white)
    # darkPalette.setColor(QPalette.BrightText, Qt.red)
    # darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
    # darkPalette.setColor(QPalette.Highlight, QColor(0, 160, 255))
    # darkPalette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
    # darkPalette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    # darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    # darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
    # darkPalette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    # darkPalette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
    # darkPalette.setColor(QPalette.PlaceholderText, QColor(100, 100, 100))

    # app.setPalette(darkPalette)
    # app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    sys.exit(app.exec())
