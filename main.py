import os
import sys
import glob
import time
import serial.tools.list_ports
import serial
import math as m

import PySide6
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtGui
from PySide6.QtGui import Qt, QPalette, QColor

os.system('''pyside6-rcc res.qrc -o res_rc.py
pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView, QStyleFactory, QMessageBox

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
        self.ui.actionSave.triggered.connect(self.saveReadData)
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

        self.ui.ShowReadData.setEnabled(False)
        self.ui.ShowReadData.setStyleSheet("QPushButton {color: rgb(198, 198, 198);}")

        self.ui.actionSave.setEnabled(False)

        self.ui.warningPorts.setVisible(0)

        # global var, which includes all data
        # self.tableData = []
        self.firstFileData = []
        self.secondFileData = []
        self.readDataArray = [] 
        self.readFromDataForSave = []

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
            # flag which shows that almost is okey
            ok = True
            
            self.firstFileData = makeHexArray(data)
            self.fillTheTables(1, self.ui.baseAdress.value())

            self.ui.fileSize.setText(str(self.openedDataSize))
            # Если данные успешно считаны вывести результат в окно отчета
            if ok:
                self.ui.plainTextEdit.appendPlainText("Считывание данных успешно выполнено...")

    def updateTable(self):
        # get base and then call func -> fill two tables
        base = self.ui.baseAdress.value()
        self.fillTheTables(1, base)
        self.fillTheTables(2, base)
        self.ui.plainTextEdit.appendPlainText(f"Базовый адрес обновлен на {base}")

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

        if result:
            self.ui.warningPorts.setVisible(0)
            self.ui.portList.clear()
            self.ui.portList.addItems(result)
            self.AvalaiblePorts = result
        else:
            self.ui.warningPorts.setVisible(1)

    def readData(self):
        myRequest = []
        if self.AvalaiblePorts:
            self.ChoosenPort = self.ui.portList.currentText()
            # then we ready to start communication
            weReadyMessage = bytes([0x1A]) + bytes([self.ui.baseAdress.value()])
            print(weReadyMessage)
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
            # print(sum , '  szeeeee ')
            amountOfSends = int(m.ceil(sum/128))
            amountOfBig = sum // 128
            readData = []
            for i in range(amountOfSends):
                newString = []
                if (i + 1) == amountOfSends:
                    correctLine = ser.read(2 + sum - (128 * amountOfBig))[2:]
                    for j in range(len(correctLine)):
                        newString.append(correctLine[j])
                    readData.append(newString)
                else:
                    correctLine = ser.read(130)[2:]
                    for j in range(len(correctLine)):
                        newString.append(correctLine[j])
                    readData.append(newString)
            
            configuratedData = []
            for i in range(len(readData)):
                for j in range(len(readData[i])):
                    configuratedData.append(readData[i][j])
            self.readFromDataForSave = configuratedData

            ser.close()
            self.readDataArray = configuratedData
            self.ui.ShowReadData.setEnabled(True)
            self.ui.plainTextEdit.appendPlainText("Считывание данных с контроллера успешно выполнено...")
            # we allows to save read data
            self.ui.actionSave.setEnabled(True)
        else:
            print("Ports are not choosen")
            self.ui.warningPorts.setVisible(1)


    def showReadData(self):
        if self.readDataArray:
            hexArray  = []
            # I can use makeHexArrayHere
            for i in range(len(self.readDataArray)):
                hexSymb = hex(self.readDataArray[i])
                hexArray.append(hexSymb)
            # rewrite it

            hexData = []
            for i in range(len(hexArray)):
                symbInCode = hexArray[i][2:4]
                if len(symbInCode) == 1:
                    symbInCode = '0' + symbInCode
                hexData.append(symbInCode)
                
            self.readDataArray = hexData
            self.fillTheTables(3, self.ui.baseAdress.value())
            ################### ?
            self.ui.fileSize.setText(str(len(self.readFromDataForSave)))
        
    def saveReadData(self):
        fileData = []
        for i in range(len(self.readFromDataForSave)):
            fileData.append(chr(self.readFromDataForSave[i]))
        # need to open file dialog
        
    def writeData(self):
        if self.AvalaiblePorts:
            if self.firstFileData:
                self.ChoosenPort = self.ui.portList.currentText()

                thirdSignal = []
                # mass = [chr(0x1B), bytes([self.ui.baseAdress.value()])]
                weReadyMessage = bytes([0x1B]) + bytes([self.ui.baseAdress.value()])

                firmwareSize = self.openedDataSize

                while firmwareSize:
                    buffer = firmwareSize % 256
                    firmwareSize //= 256
                    thirdSignal.append(bytes([buffer]))
                    print(bytes([buffer]))
                # print(chr(buffer))
            
                if not firmwareSize and len(thirdSignal) == 2:
                    thirdSignal.append(bytes([0]))

            # mass.extend(thirdSignal[::-1])
                weReadyMessage += thirdSignal[-1] + thirdSignal[-2] + thirdSignal[-3]
                # message += thirdSignal[-1]
                # message += thirdSignal[-2]
                # message += thirdSignal[-3]

                ser = serial.Serial()
                ser.baudrate = 115200
                ser.port = self.ChoosenPort
                ser.open()
                print(ser.is_open)
                ser.write(weReadyMessage)
            # TO DO 
                a = ser.read(2)
                result = a[1:]
                print(result)
                result = bytes([0x10])
                if result == bytes([0x10]):
                    pass
                    for i in range(0, self.openedDataSize, 256):
                        arrayToSend = self.DataToSend[i:i+256]
                        component = bytes([0x1E])
                        if len(arrayToSend) == 256:
                            component += bytes([0])
                        else:
                            component += bytes([len(arrayToSend)])
                        fullMassege = component + arrayToSend
                        ser.write(fullMassege)
                        time.sleep(0.05)
                    ser.close()
                # ok
                    self.ui.plainTextEdit.appendPlainText("Запись данных на контроллер успешно выполнено...")

                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("На стороне контроллера что-то пошло не так")
                    msgBox.setWindowTitle("Ошибка записи")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    returnValue = msgBox.exec()
                    ser.close()
                    return
                    # warning
                                
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Вы не открыли файл")
                msgBox.setWindowTitle("Ошибка записи")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
                return

        else:
            print("Ports are not choosen")
            self.ui.warningPorts.setVisible(1)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
