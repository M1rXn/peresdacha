import tkinter
from tkinter import messagebox as mb
from tkinter import *
import math
from tkinter import messagebox
def soch():
      root = Tk()
      root.configure(bg='red')
      root.title('Сочетание')
      root.geometry('400x150')
      lab = Label(root,text='C',fg='white',bg='red',font='Arial 52')
      lab.grid(row=0, column=0)
      bla=StringVar()
      bla1=StringVar()
      ent1=Entry(root,width=3,textvariable=bla)
      ent1.place(x=60)
      ent2=Entry(root,width=3,textvariable=bla1)
      ent2.place(x=60,y=78)
      lab1 = Label(root,text='=',fg='white',bg='red',font='Arial 32')
      lab1.place(x=70,y=24)
      lab2= Label(root,text='',bg='red',font='Arial 72')
      lab2.grid(row=0,column=2)
      def k(event):
            try:
                  m = int(ent1.get())
                  n = int(ent2.get())
                  if m >0:
                        if n > 0:     
                              otv = math.factorial(n) / (math.factorial(m)*math.factorial(n-m))      
                              lab2['text'] = str(otv)
                        else:
                              mb.showerror('Ошибка','Введите положительные значения')
                  else:
                        mb.showerror('Ошибка','Введите положительные значения')
            except ValueError:
                mb.showerror('Ошибка','Некорректный ввод данных!')
           
            
      but = Button(root,text='ОК',bg='white')
      but.bind('<Button-1>',k)
      but.place(x=120,y=50)
      
def razm():
      root = Tk()
      root.configure(bg='green')
      root.geometry('400x150')
      root.title('Размещение')
      lab = Label(root,text='A',fg='white',bg='green',font='Arial 72')
      lab.grid(row=0, column=0)
      bla=StringVar()
      bla1=StringVar()
      ent1=Entry(lab,width=5,textvariable=bla)
      ent1.place(x=60)
      ent2=Entry(lab,width=5,textvariable=bla1)
      ent2.place(x=60,y=78)
      lab1 = Label(root,text='=',fg='white',bg='green',font='Arial 32')
      lab1.grid(row=0,column=1)
      lab2= Label(root,text='',bg='green',font='Arial 72')
      lab2.grid(row=0,column=2)
      def k(event):
            try:
                  m = int(ent1.get())
                  n = int(ent2.get())
                  if m >0:
                        if n > 0: 
                              otv = math.factorial(n) / math.factorial(n-m)
                              lab2['text'] = str(otv)
                        else:
                              mb.showerror('Ошибка','Введите положительные значения')
                  else:
                        mb.showerror('Ошибка','Введите положительные значения')
            except ValueError:
                mb.showerror('Ошибка','Некорректный ввод данных!')
            
      but = Button(root,text='ОК',bg='white')
      but.bind('<Button-1>',k)
      but.grid(row=0,column=3)
        
def peres():
      root = Tk()
      root.configure(bg='blue')
      root.geometry('400x150')
      root.title('Размещение')
      lab = Label(root,text='P',fg='white',bg='blue',font='Arial 72')
      lab.grid(row=0, column=0)
      bla=StringVar()
      bla1=StringVar()
      ent2=Entry(lab,width=2,textvariable=bla1)
      ent2.place(x=60,y=78)
      lab1 = Label(root,text='=',fg='white',bg='blue',font='Arial 72')
      lab1.grid(row=0,column=1)
      lab2= Label(root,text='',bg='blue',font='Arial 72')
      lab2.grid(row=0,column=2)
      def k(event):
            try:      
                  n = int(ent2.get())
                  if n > 0: 
                        otv = math.factorial(n)
                        lab2['text'] = str(otv)
                  else:
                        mb.showerror('Ошибка','Введите положительные значения')
            except ValueError:
                mb.showerror('Ошибка','Некорректный ввод данных!')
            
      but = Button(root,text='ОК',bg='white')
      but.bind('<Button-1>',k)
      but.grid(row=0,column=3)

def ops():
      messagebox.showinfo("Информация","Программа вычисляет комбинаторику по трем формулам") 

def exet():
      root.destroy()

root = Tk()
root.configure(bg='grey')
root.title('Комбинаторика')
root.geometry('300x100')
butsoc=Button(root,text='Сочетание',command=soch)
butsoc.place(x=10,y=20)
butsoch=Button(root,text='Размещение',command=razm)
butsoch.place(x=100,y=20)
butperes=Button(root,text='Перестановка',command=peres)
butperes.place(x=200,y=20)
butex=Button(root,text='Выход',command=exet)
butex.place(x=220,y=60)
m=Menu(root)
root.config(menu=m)
sm=Menu(m,tearoff=0)
sf=Menu(m,tearoff=0)
sp=Menu(m,tearoff=0)

m.add_cascade(label='Меню',menu=sm)
m.add_cascade(label='Помощь',menu=sf)
m.add_cascade(label='Выход',menu=sp)

sf.add_command(label='Информация',command=ops)
sm.add_command(label='Сочетание',command=soch)
sm.add_command(label='Размещение',command=razm)
sm.add_command(label='Перестановка',command=peres)
sp.add_command(label='Выход',command=exet)
root.mainloop()
