import sys

from ex import *
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import traceback

#мматрица главная и побочная 
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
  
        self.ui.pushButton.clicked.connect(self.MyFunction)

    def MyFunction(self):
        self.ui.textEdit.clear()
        self.count=int(self.ui.lineEdit.text())
        mas=[[randint(0,9)for i in range(self.count)]for j in range(self.count)]#матрицп
        matr=[]
        
        for i in mas:
            for j in i:
                matr.append(j)

        s=0
        sums=0#сумма всей матрицы
        glavn=0#сумма главной диагонали
        pobo=0#сумма побочной диагонали


        #gl=[]
        #pob=[]
        for i in range(self.count):
            pobo+=mas[i][self.count-i-1]
            #pob.append(mas[i][self.count-i-1])
            for j in range(self.count):
                sums+=int(mas[i][j])
                if s == self.count:
                    s=0
                    self.ui.textEdit.insertPlainText('\n')#перенос на след. строку
                    
                if i==j:
                    #gl.append(mas[i][j])
                    glavn+=mas[i][j]#суммирование главной диагонали
    
                self.ui.textEdit.insertPlainText(str(mas[i][j])+' ')#добавление матрицы в текст эдит
                s+=1
        #gl=sorted(gl)
        #pob=sorted(pob)
        #print(gl,pob)
        if self.count%2==1:
            matr[len(matr)//2]
            
            self.ui.label.setText(str(sums-glavn-pobo+matr[len(matr)//2]))
        else:

            self.ui.label.setText(str(sums-glavn-pobo))
            
        #for i in range(self.count):
            
            #mas[i][self.count-i-1]=pob[i]
            #for j in range(self.count):
                #if i==j:
                   
                    #mas[i][j]=gl[j]
        #print(mas)
        
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
