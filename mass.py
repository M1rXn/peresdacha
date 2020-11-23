from random import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
def start():
    global ent
    ent=Entry(root,width=20)
    ent.place(x=245,y=90)
    lab=Label(root,text='Введите числа массива\n через пробел',font='Arial 10')
    lab.place(x=230,y=40)
    butv=Button(root,text='Ok',font='Arial 10',command=vruch)
    butv.place(x=240,y=120)
def vruch():
    try:
        global ent
        c=0
        mass=ent.get()
        ss = mass.lower().replace('.',' ').replace(',',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace(':',' ').split()
        for i in ss:
            if int(i)>0:
                c+=int(i)
        lab=Label(root,text='Результат сложения',font='Arial 12')
        lab.place(x=240,y=160)
        lab=Label(root,text=c,font='Arial 12')
        lab.place(x=240,y=200)
    except ValueError:
        mb.showerror('Ошибка','Введены некорректные данные!')
def sluch():
    a=[randint(-20,20)for i in range(10)]
    labi=Label(text='Исходный массив:',font='Arial 12')
    labi.place(x=40,y=40)
    labm=Label(text=a,font='Arial 12')
    labm.place(x=12,y=90)

    c=0

    for x in a:
        if x>0:
            c+=x

    labp=Label(text='Результат сложения:',font='Arial 12')
    labp.place(x=20,y=160)
    labk=Label(text=c,font='Arial 12')
    labk.place(x=100,y=200)
def exet():
    root.destroy()
def instr():
    mb.showinfo('Инструкция','При выборе автоматического ввода элементов, программа сама выведет всю необходимую информацию. При выборе ручного ввода выводится окошко, в котором вы записываете нужное вам количество элементов через пробел. Далее нажав на кнопку Ок программа выдает вам сумму всех положительных элементов в зависимости от вашего запроса!')
def prog():
    mb.showinfo('О программе',' Программа суммирует все положительные числа в массиве. Учтен ввод массива вручную или автоматически. ')   
def avtr():
    mb.showinfo('Об авторе','Миронов Даниил Сергеевич, курсант Троицкого АТК филиала МГТУ ГА.')
def blsh():
    os.startfile('pic.png')
    
root=Tk()
root.geometry('400x300')
root.configure(bg='lightblue')
butsl=Button(root,text='Случайный вывод массива',command=sluch)
butsl.place(x=40,y=10)
butvr=Button(root,text='Ввод массива вручную',command=start)
butvr.place(x=240,y=10)
m=Menu(root)
root.config(menu=m)
sm=Menu(m,tearoff=0)
m.add_cascade(label='Меню',menu=sm)
sm.add_command(label='О программе',command=prog)
sm.add_command(label='Об авторе',command=avtr)
sm.add_command(label='Инструкция',command=instr)
sm.add_command(label='Блок-схема',command=blsh)
sm.add_command(label='Выход',command=exet)















