import sys

from test import *
from PyQt5 import QtCore, QtGui, QtWidgets

import traceback

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
        self.ui.pushButton.clicked.connect(self.save)
        self.otvet=['4','1000','0','86','1']
        
    def save(self):
        s=0
        ss=0
        for j in range(1,6):
            for i in eval('self.ui.buttonGroup_'+str(j)).buttons():
                if i.isChecked():
                    if i.text()==self.otvet[ss]:
                        print(self.otvet[ss])
                        s+=1
            ss+=1
                        
        if s==5:
            print('cупер')
        elif s==4:
            print('хорошо')
        elif s==3:
            print('норм')
        else :
            print('плохо')
        
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
