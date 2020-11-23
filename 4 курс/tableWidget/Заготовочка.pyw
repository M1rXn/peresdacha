import sys
# Импортируем наш интерфейс из файла
from untitled import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem as TWI

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    sys.exit()

import traceback
sys.excepthook = log_uncaught_exceptions
class MyWin(QtWidgets.QMainWindow):
    comboBoxs = []
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.pushButton_4.clicked.connect(self.ras)
        
        

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
        self.s = 0
    def MyFunction(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        comboBox = QtWidgets.QComboBox()
        values = ['шт','л','м']
        for i in values:
            comboBox.addItem(i)
        self.comboBoxs.append(comboBox)
        #print(
                  
        self.ui.tableWidget.setCellWidget(self.s,2,comboBox)
        self.s += 1
        
    def ras(self):
        for j in range(self.ui.tableWidget.rowCount()):
            for i in range(5):
                ress = 0
                if type(self.ui.tableWidget.cellWidget(j, i)) == QtWidgets.QComboBox:
                    ress = self.ui.tableWidget.cellWidget(j, i).currentText()
                else:
                    try:
                        ress = self.ui.tableWidget.item(j,i).text()
                    except:
                        pass
                print(ress)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
