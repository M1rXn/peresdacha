import sys
# Импортируем наш интерфейс из файла
from untitled import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        do = []
        po = []
        f = open('txtx.txt', 'r', encoding='utf-8')
        a = f.read()
        a = a.split(' ')
        col = int(self.ui.lineEdit.text())
        for i in a:
            if col != 0:
                do.append(i)
                col -= 1
            else:
                break

        col = int(self.ui.lineEdit.text())
        for i in a:
            if col != 0:
                col -= 1
            else:
                po.append(i)

        f_do = open('do.txt', 'w', encoding='utf-8')
        for i in do:
            f_do.write(i)
            f_do.write(' ')
            
        f_do.close()

        f_po = open('po.txt', 'w', encoding='utf-8')
        for i in po:
            f_po.write(i)
            f_po.write(' ')
            
        f_po.close()
            

                    
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
