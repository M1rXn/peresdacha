import sys

from sortedd import *
from PyQt5 import QtCore, QtGui, QtWidgets

#сортировка по длине строки
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.MyFunction)

    def MyFunction(self):
        options=QtWidgets.QFileDialog.Options()
        self.fileName, _ =QtWidgets.QFileDialog.getOpenFileName(self,"Открыть файл", "","Text Files (*.txt)",options=options)#открытие диалогового окна
        tex=[]
        if self.fileName:
            with open (self.fileName,encoding="utf-8") as f:
                for i in f:
                    print(len(i)-1)
                    if i=='\n':
                        pass
                    else:
                        tex.append(i.rstrip('\n'))

        text=sorted(tex, key=len)
        for i in text:
            self.ui.textEdit.insertPlainText(str(i)+'\n')

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
