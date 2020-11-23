from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os
import sys
import operator
from MainWindow import Ui_MainWindow
from tkinter import *
             

def calculator(event):
   READY = 0
   INPUT = 1


   class MainWindow(QMainWindow, Ui_MainWindow):
       def __init__(self, *args, **kwargs):
           super(MainWindow, self).__init__(*args, **kwargs)
           self.setupUi(self)

           
           for n in range(0, 10):
               getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))

           
           self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
           self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
           self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
           self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv)) 

           self.pushButton_pc.pressed.connect(self.operation_pc)
           self.pushButton_eq.pressed.connect(self.equals)

           
           self.actionReset.triggered.connect(self.reset)
           self.pushButton_ac.pressed.connect(self.reset)

           self.actionExit.triggered.connect(self.close)

           self.pushButton_m.pressed.connect(self.memory_store)
           self.pushButton_mr.pressed.connect(self.memory_recall)

           self.memory = 0
           self.reset()

           self.show()

       def display(self):
           self.lcdNumber.display(self.stack[-1])

       def reset(self):
           self.state = READY
           self.stack = [0]
           self.last_operation = None
           self.current_op = None
           self.display()

       def memory_store(self):
           self.memory = self.lcdNumber.value()

       def memory_recall(self):
           self.state = INPUT
           self.stack[-1] = self.memory
           self.display()

       def input_number(self, v):
           if self.state == READY:
               self.state = INPUT
               self.stack[-1] = v
           else:
               self.stack[-1] = self.stack[-1] * 10 + v

           self.display()

       def operation(self, op):
           if self.current_op:  
               self.equals()

           self.stack.append(0)
           self.state = INPUT
           self.current_op = op

       def operation_pc(self):
           self.state = INPUT
           self.stack[-1] *= 0.01
           self.display()

       def equals(self):
           if self.state == READY and self.last_operation:
               s, self.current_op = self.last_operation
               self.stack.append(s)

           if self.current_op:
               self.last_operation = self.stack[-1], self.current_op

               try:
                   self.stack = [self.current_op(*self.stack)]
               except Exception:
                   self.lcdNumber.display('Err')
                   self.stack = [0]
               else:
                   self.current_op = None
                   self.state = READY
                   self.display()


   if __name__ == '__main__':
       app = QApplication([])
       app.setApplicationName("Calculon")

       window = MainWindow()
       app.exec_()


def bloknot(event):
   class MainWindow(QMainWindow):

       def __init__(self, *args, **kwargs):
           super(MainWindow, self).__init__(*args, **kwargs)

           layout = QVBoxLayout()
           self.editor = QPlainTextEdit()  


           
           fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
           fixedfont.setPointSize(12)
           self.editor.setFont(fixedfont)

           
           self.path = None

           layout.addWidget(self.editor)

           container = QWidget()
           container.setLayout(layout)
           self.setCentralWidget(container)

           self.status = QStatusBar()
           self.setStatusBar(self.status)

           file_toolbar = QToolBar("Файл")
           file_toolbar.setIconSize(QSize(27, 27
                                          ))
           self.addToolBar(file_toolbar)
           file_menu = self.menuBar().addMenu("&Файл")

           open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
           open_file_action.setStatusTip("Открыть файл")
           open_file_action.triggered.connect(self.file_open)
           file_menu.addAction(open_file_action)
           file_toolbar.addAction(open_file_action)

           save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
           save_file_action.setStatusTip("Сохранить текущую страницу")
           save_file_action.triggered.connect(self.file_save)
           file_menu.addAction(save_file_action)
           file_toolbar.addAction(save_file_action)

           saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
           saveas_file_action.setStatusTip("Сохранить текущую страницу в указанный файл")
           saveas_file_action.triggered.connect(self.file_saveas)
           file_menu.addAction(saveas_file_action)
           file_toolbar.addAction(saveas_file_action)

           print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
           print_action.setStatusTip("Распечатать текущую страницу")
           print_action.triggered.connect(self.file_print)
           file_menu.addAction(print_action)
           file_toolbar.addAction(print_action)

           edit_toolbar = QToolBar("редактировать")
           edit_toolbar.setIconSize(QSize(16, 16))
           self.addToolBar(edit_toolbar)
           edit_menu = self.menuBar().addMenu("&редактировать")

           undo_action = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
           undo_action.setStatusTip("Отменить последнее изменение")
           undo_action.triggered.connect(self.editor.undo)
           edit_menu.addAction(undo_action)

           redo_action = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
           redo_action.setStatusTip("Повторить последнее изменение")
           redo_action.triggered.connect(self.editor.redo)
           edit_toolbar.addAction(redo_action)
           edit_menu.addAction(redo_action)

           edit_menu.addSeparator()

           cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
           cut_action.setStatusTip("Вырезать выделенный текст")
           cut_action.triggered.connect(self.editor.cut)
           edit_toolbar.addAction(cut_action)
           edit_menu.addAction(cut_action)

           copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
           copy_action.setStatusTip("Скопировать выделенный текст")
           copy_action.triggered.connect(self.editor.copy)
           edit_toolbar.addAction(copy_action)
           edit_menu.addAction(copy_action)

           paste_action = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
           paste_action.setStatusTip("Вставить из буфера обмена")
           paste_action.triggered.connect(self.editor.paste)
           edit_toolbar.addAction(paste_action)
           edit_menu.addAction(paste_action)

           select_action = QAction(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
           select_action.setStatusTip("Выделить весь текст")
           select_action.triggered.connect(self.editor.selectAll)
           edit_menu.addAction(select_action)

           edit_menu.addSeparator()

           wrap_action = QAction(QIcon(os.path.join('images', 'arrow-continue.png')), "Wrap text to window", self)
           wrap_action.setStatusTip("Переключить текст переноса в окно")
           wrap_action.setCheckable(True)
           wrap_action.setChecked(True)
           wrap_action.triggered.connect(self.edit_toggle_wrap)
           edit_menu.addAction(wrap_action)

           self.update_title()
           self.show()

       def dialog_critical(self, s):
           dlg = QMessageBox(self)
           dlg.setText(s)
           dlg.setIcon(QMessageBox.Critical)
           dlg.show()

       def file_open(self):
           path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

           if path:
               try:
                   with open(path, 'rU') as f:
                       text = f.read()

               except Exception as e:
                   self.dialog_critical(str(e))

               else:
                   self.path = path
                   self.editor.setPlainText(text)
                   self.update_title()

       def file_save(self):
           if self.path is None:
               
               return self.file_saveas()

           self._save_to_path(self.path)

       def file_saveas(self):
           path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

           if not path:
               
               return

           self._save_to_path(path)

       def _save_to_path(self, path):
           text = self.editor.toPlainText()
           try:
               with open(path, 'w') as f:
                   f.write(text)

           except Exception as e:
               self.dialog_critical(str(e))

           else:
               self.path = path
               self.update_title()

       def file_print(self):
           dlg = QPrintDialog()
           if dlg.exec_():
               self.editor.print_(dlg.printer())

       def update_title(self):
           self.setWindowTitle("%s - No2Pads" % (os.path.basename(self.path) if self.path else "Блокнот"))

       def edit_toggle_wrap(self):
           self.editor.setLineWrapMode( 1 if self.editor.lineWrapMode() == 0 else 0 )


   if __name__ == '__main__':

       app = QApplication(sys.argv)
       app.setApplicationName("No2pads")

       window = MainWindow()
       app.exec_()
def calendar(event):
   class Example(QWidget):
       
       def __init__(self):
           super().__init__()
           
           self.initUI()
           
           
       def initUI(self):      
           
           vbox = QVBoxLayout(self)

           cal = QCalendarWidget(self)
           cal.setGridVisible(True)
           cal.clicked[QDate].connect(self.showDate)
           
           vbox.addWidget(cal)
           
           self.lbl = QLabel(self)
           date = cal.selectedDate()
           self.lbl.setText(date.toString())
           
           vbox.addWidget(self.lbl)
           
           self.setLayout(vbox)
           
           self.setGeometry(600, 600, 650, 600)
           self.setWindowTitle('Календарь')
           self.show()
           
           
       def showDate(self, date):     
           
           self.lbl.setText(date.toString())
           
           
   if __name__ == '__main__':
       
       app = QApplication(sys.argv)
       ex = Example()
       sys.exit(app.exec_())

root = Tk()
root.title("Органайзер")
root.geometry("400x200")
ramk=Frame(root,width=400,height=200)
ramk.pack()
kalk = PhotoImage(file='Calk.gif')
block = PhotoImage(file='Block.gif')
kalen = PhotoImage(file='Calen.gif')

but=Button(ramk,image=kalk)
but.place(x=20,y=30)
but.bind("<1>",calculator)

but1=Button(ramk,image=block)
but1.place(x=135,y=30)
but1.bind("<1>",bloknot)

but2=Button(ramk,image=kalen)
but2.place(x=280,y=30)
but2.bind("<1>",calendar)

root.mainloop()




