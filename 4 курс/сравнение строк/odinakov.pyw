import sys

from odin import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(lambda:self.opens(0))
        self.ui.pushButton_2.clicked.connect(lambda:self.opens(1))
       # self.ui.pushButton_3.clicked.connect(lambda:self.ras(1))

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
        self.tex=[]
        self.tex2=[]
    def opens(self,x):
        
        options=QtWidgets.QFileDialog.Options()
        self.fileName, _ =QtWidgets.QFileDialog.getOpenFileName(self,"Открыть файл", "","Text Files (*.txt)",options=options)#открытие диалогового окна
      
        if self.fileName:
            with open(self.fileName, encoding='utf-8') as fin:
                for i in fin:
                    if i=='\n':
                        pass 
                    else:
                        if x==0:
                            self.tex.append(i.rstrip('\n'))
                        else:
                            self.tex2.append(i.rstrip('\n'))
                    if x==0:
                        self.ui.textEdit.insertPlainText(str(i))
                    else:
                        self.ui.textEdit_2.insertPlainText(str(i))

        print(self.tex,self.tex2)
   # def ras(self):
        
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
