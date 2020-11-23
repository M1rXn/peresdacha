#! Файловый менеджер
from tkinter import messagebox as mb    
import os
from tkinter import *
import shutil
try:
    def soz():
        fra.configure(width=590,height=400)
        
        b7 = Button(fra,text='Папку',width=6,command=mkdirr)
        b7.place(x=455,y=65)

        b8 = Button(fra,text='Файл',width=6,command=sozdfile)
        b8.place(x=512,y=65)

    def mkdirr():
        os.mkdir(A+ent1.get())
        tx.delete(1.0,END)
        B = os.listdir(A)
        
        for i in B:
            tx.insert(1.0,i+'\n')
            
    def sozdfile():
        open(A+ent1.get(),'w')
        tx.delete(1.0,END)
        B = os.listdir(A)
        
        for i in B:
            tx.insert(1.0,i+'\n')

    def ydl():
        fra.configure(width=590,height=400)
        
        b7 = Button(fra,text='Папку',width=6,command=ydlpap)
        b7.place(x=455,y=95)

        b8 = Button(fra,text='Файл',width=6,command=ydlfil)
        b8.place(x=512,y=95)
        
    def ydlpap():

        os.rmdir(A+ent1.get())
        tx.delete(1.0,END)
        B = os.listdir(A)
        for i in B:
            tx.insert(1.0,i+'\n')
            
    def ydlfil():
        os.remove(A+ent1.get())
        tx.delete(1.0,END)
        B = os.listdir(A)
        for i in B:
            tx.insert(1.0,i+'\n')

    def pereim():
        global ent2
        fra.configure(width=650,height=400)
        labper=Label(fra,text='<------- Введите новое название')
        labper.place(x=450,y=5)
        ent2=Entry(fra)
        ent2.place(x=320,y=6)
        bo = Button(fra,text='Ок',command=ook)
        bo.place(x=550,y=25)
        
    def ook():
        try:
            global ent2
            os.rename(A+ent1.get(),A+ent2.get())
            tx.delete(1.0,END)
            B = os.listdir(A)
            for i in B:
                tx.insert(1.0,i+'\n')
        except FileNotFoundError:
            mb.showerror('Ошибка','Введено несуществующее название!!!!!!!!!!!')
            
    def otkr():
        os.startfile(A+ent1.get())

    def exitt():
        root.destroy()

    def skin():
        global ent2
        fra.configure(width=650,height=400)
        labskin=Label(fra,text='<------- Введите название папки')
        labskin.place(x=450,y=5)
        ent2=Entry(fra)
        ent2.place(x=320,y=6)
        boo = Button(fra,text='Ок',command=ok)
        boo.place(x=550,y=25)
        
    def ok():
        global ent2
        shutil.move(A+ent1.get(),A+ent2.get())
        tx.delete(1.0,END)
        B = os.listdir(A)
        for i in B:
            tx.insert(1.0,i+'\n')
            
    def sk():
        global ent2
        fra.configure(width=650,height=400)
        labsk=Label(fra,text='<------- Введите путь')
        labsk.place(x=450,y=5)
        ent2=Entry(fra)
        ent2.place(x=320,y=6)
        colobok = Button(fra,text='Ок',command=okk)
        colobok.place(x=550,y=25)

    def okk():
        global ent2
        os.chdir(ent2.get())
        A=os.getcwd()
        tx.delete(1.0,END)
        B = os.listdir(ent2.get())
        for i in B:
            tx.insert(1.0,i+'\n')
except FileNotFoundError:
    mb.showerror('fwfw','wfaf')
    
    
A = "C:\Games\DlyaProvProg\\"

#! Интерфейс

root=Tk()
root.title("Менеджер")

fra=Frame(root,width=455,height=400)
fra.grid(row=0,column=0)

lb1 = Label(fra,text='Введите имя файла или папки >')
lb1.place(x=5,y=5)

ent1 = Entry(fra)
ent1.place(x=190,y=6)
ent1.focus()


lb2 = Label(fra,text='Содежимое каталога:')
lb2.place(x=5,y=30)

tx = Text(fra,width=38,height=20)
tx.place(x=5,y=55)

b1 = Button(fra,text='Создать',width=15,command=soz)
b1.place(x=335,y=65)

b2 = Button(fra,text='Удалить',width=15,command=ydl)
b2.place(x=335,y=95)

b3 = Button(fra,text='Переименовать',width=15,command=pereim)
b3.place(x=335,y=125)

b4 = Button(fra,text='Переместить',width=15,command=skin)
b4.place(x=335,y=155)

b5 = Button(fra,text='Открыть',width=15,command=otkr)
b5.place(x=335,y=185)

b6 = Button(fra,text='Выход',width=15,command=exitt)
b6.place(x=335,y=355)

b7 = Button(fra,text='Смена каталога',width=15,command=sk)
b7.place(x=335,y=215)

lbAV = Label(fra,text='Шабалин Дмитрий Алексеевич|Миронов Даниил Сергеевич')
lbAV.place(x=5,y=379)

#! Первоначальное отображение
B = os.listdir(A)

for i in B:
    tx.insert(1.0,i+'\n')



    
