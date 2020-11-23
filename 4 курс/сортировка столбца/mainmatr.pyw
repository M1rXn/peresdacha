import sys

from matr import *
from PyQt5 import QtCore, QtGui, QtWidgets
import traceback

#сортировка таблицы по номеру
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    sys.exit()
sys.excepthook = log_uncaught_exceptions

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton_2.clicked.connect(self.MyFunction)
        self.ui.pushButton.clicked.connect(self.sort)
        self.ui.pushButton_3.clicked.connect(self.save)
    def save(self):
        options=QtWidgets.QFileDialog.Options()
        self.fileNamesave, _ =QtWidgets.QFileDialog.getSaveFileName(self,"Сохранить файл", "","Text Files (*.txt)",options=options)
                
        if self.fileNamesave:
            self.writeFile=open(self.fileNamesave,"w",encoding="utf-8")
            w=self.ui.textEdit.toPlainText().split('\n')
            for i in w:
               
                self.writeFile.write(str(i)+'\n')
            self.writeFile.close()

    def MyFunction(self):
        options=QtWidgets.QFileDialog.Options()
        self.fileName, _ =QtWidgets.QFileDialog.getOpenFileName(self,"Открыть файл", "","Text Files (*.txt)",options=options)#открытие диалогового окна
        matr=[]
        
        if self.fileName:
            with open(self.fileName, encoding='utf-8') as fin:#открываем файл 
            
                for line in fin:
                    matr.append(list(line.rstrip('\n').split(' ')))
                    self.ui.textEdit.insertPlainText(str(line))
                    
        self.mas=[[int(i) for i in j]for j in matr]#преобразуем все элементы в число
        
            
        
    def sort(self):
        self.sortmas=[]
        n=int(self.ui.lineEdit.text())-1
        for i in range(len(self.mas)):
            self.sortmas.append(self.mas[i][n])
            
        self.sortmas=sorted(self.sortmas)
        
        for i in range(len(self.mas)):
            self.mas[i][n]=self.sortmas[i]
        print(self.mas)
        s=0
        for i in range(len(self.mas)):
            for j in range(len(self.mas[0])):
                print(self.mas[i][j])
                if s==len(self.mas[0])-1:
                    self.ui.textEdit_2.insertPlainText(str(self.mas[i][j])+'\n')
                    s=0
                else:
                    self.ui.textEdit_2.insertPlainText(str(self.mas[i][j]))
                    s+=1
        
                
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
