from tkinter import *
from tkinter import messagebox as mb
def about_prog():
    mb.showinfo('О программе','Программа предназначена для нахождения наилучшей производительности среди сортов на основе приведенных данных')
def close():
    root.destroy()

def about_author():
    mb.showinfo('Об авторе','Курсант Троицкого АТК ГФ филиала МГТУ ГА 331 группы Миронов Даниил Сергеевич')
def dalee():
    try:
        #!Cчитывание с Entry содержимого
        
        p1=ent1.get()
        p2=ent2.get()
        p3=ent3.get()
        p4=ent4.get()
        p5=ent5.get()
        p6=ent6.get()
        p7=ent7.get()
        p8=ent8.get()
        p11=ent11.get()
        p22=ent22.get()
        p33=ent33.get()
        p44=ent44.get()
        p55=ent55.get()
        p66=ent66.get()
        p77=ent77.get()
        p88=ent88.get()
        
        #!Задание условий для вывода ошибок
        if len(p1)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "Аленушка"')
        elif len(p2)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "Левушка"')
        elif len(p3)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "Лебедушка"')
        elif len(p4)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "Мороз"')
        elif len(p5)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "Крути"')
        elif len(p6)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "На завод"')
        elif len(p7)==0:
            mb.showerror('Ошибка','Не введено себестоимость конфет "Приколист"')
        elif len(p8)==0:
            mb.showerror('Ошибка','Не введена себестоимость конфет "Алешенька"')
        elif len(p11)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Аленушка"')
        elif len(p22)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Левушка"')
        elif len(p33)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Лебедушка"')
        elif len(p44)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Мороз"')
        elif len(p55)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Крути"')
        elif len(p66)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "На завод"')
        elif len(p77)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Приколист"')
        elif len(p88)==0:
            mb.showerror('Ошибка','Не введено количество рабочих на производстве конфет "Алешенька"')

        elif int(p11)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Аленушка" слишком большое')
        elif int(p22)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Левушка" слишком большое')
        elif int(p33)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Лебедушка" слишком большое')
        elif int(p44)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Мороз" слишком большое')
        elif int(p55)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Крути" слишком большое')
        elif int(p66)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "На завод" слишком большое')
        elif int(p77)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Приколист" слишком большое')
        elif int(p88)>999:
            mb.showerror('Ошибка','Количество рабочих на производстве конфет "Алешенька" слишком большое')

        elif int(p1)<39:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p2)<29:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p3)<22:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p4)<59:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p5)<40:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p6)<50:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p7)<35:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')
        elif int(p8)<27:
            mb.showerror('Ошибка','Себестоимость не должна превышать выпускную цену')

        elif int(p1)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Аленушка" слишком большое')
        elif int(p2)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Левушка" слишком большое')
        elif int(p3)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Лебедушка" слишком большое')
        elif int(p4)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Мороз" слишком большое')
        elif int(p5)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Крути" слишком большое')
        elif int(p6)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "На завод" слишком большое')
        elif int(p7)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Приколист" слишком большое')
        elif int(p8)>999:
            mb.showerror('Ошибка','Выпускная цена на производстве конфет "Алешенька" слишком большое')

        elif int(p11)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p22)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p33)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p44)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p55)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p66)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p77)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        elif int(p88)<0:
            mb.showerror('Ошибка','Количество рабочих не должно быть ниже 0')
        #!Если все условия выполняются,то идет открытие окна и построение диаграммы
        else:

            root1=Tk()
            root.title('Chocolate dream')
            fra1=Frame(root1,width=1000,height=450)
            fra1.pack()
            lab=Label(fra1,text='"Аленушка"')#!Диаграмма производительности Аленушка
            lab.place(x=40,y=20)
            lab=Label(fra1,text='"Левушка"')#!Диаграмма производительности Левушка
            lab.place(x=40,y=70)
            lab=Label(fra1,text='"Лебедушка"')#!Диаграмма производительности Лебедушка
            lab.place(x=40,y=120)
            lab=Label(fra1,text='"Мороз"')#!Диаграмма производительности Мороз
            lab.place(x=40,y=170)
            lab=Label(fra1,text='"Крути"')#!Диаграмма производительности Крути
            lab.place(x=40,y=220)
            lab=Label(fra1,text='"На завод"')#!Диаграмма производительности На завод
            lab.place(x=40,y=270)
            lab=Label(fra1,text='"Приколист"')#!Диаграмма производительности Приколист
            lab.place(x=40,y=320)
            lab=Label(fra1,text='"Алешенька"')#!Диаграмма производительности Алешя енька
            lab.place(x=40,y=370)
            #!Формулы производительности производства конфет
            sp1=(int(p1)-39)/int(p11)
            sp1=int(sp1)
            sp2=(int(p2)-29)/int(p22)
            sp2=int(sp2)
            sp3=(int(p3)-22)/int(p33)
            sp3=int(sp3)
            sp4=(int(p4)-59)/int(p44)
            sp4=int(sp4)
            sp5=(int(p5)-40)/int(p55)
            sp5=int(sp5)
            sp6=(int(p6)-50)/int(p66)
            sp6=int(sp6)
            sp7=(int(p7)-35)/int(p77)
            sp7=int(sp7)
            sp8=(int(p8)-27)/int(p88)
            sp8=int(sp8)
            #!Вывод данных о производительности на поле напротив каждого названия
            lab=Label(fra1,text=sp1)
            lab.place(x=130,y=20)
            lab=Label(fra1,text=sp2)
            lab.place(x=130,y=70)
            lab=Label(fra1,text=sp3)
            lab.place(x=130,y=120)
            lab=Label(fra1,text=sp4)
            lab.place(x=130,y=170)
            lab=Label(fra1,text=sp5)
            lab.place(x=130,y=220)
            lab=Label(fra1,text=sp6)
            lab.place(x=130,y=270)
            lab=Label(fra1,text=sp7)
            lab.place(x=130,y=320)
            lab=Label(fra1,text=sp8)
            lab.place(x=130,y=370)
            #!Сравнение каждой производительности для выявления наиболее лучшей
            if sp1>=sp2 and sp1>=sp3 and sp1>=sp4 and sp1>=sp5 and sp1>=sp6 and sp1>=sp7 and sp1>=sp8:
                lab=Label(fra1,text='"Аленушка",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp2>=sp1  and sp2>=sp3 and sp2>=sp4 and sp2>=sp5 and sp2>=sp6 and sp2>=sp7 and sp2>=sp8:
                lab=Label(fra1,text='"Левушка",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp3>=sp2  and sp3>=sp1 and sp3>=sp4 and sp3>=sp5 and sp3>=sp6 and sp3>=sp7 and sp3>=sp8:
                lab=Label(fra1,text='"Лебедушка",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp4>=sp2 and sp4>=sp3 and sp4>=sp1 and sp4>=sp5 and sp4>=sp6 and sp4>=sp7 and sp4>=sp8:
                lab=Label(fra1,text='"Мороз",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp5>=sp2 and sp5>=sp3 and sp5>=sp4 and sp1<=sp5 and sp5>=sp6 and sp5>=sp7 and sp5>=sp8:
                lab=Label(fra1,text='"Крути",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp6>=sp2 and sp6>=sp3 and sp6>=sp4 and sp6>=sp5 and sp1<=sp6 and sp6>=sp7 and sp6>=sp8:
                lab=Label(fra1,text='"На завод",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp7>=sp2 and sp7>=sp3 and sp7>=sp4 and sp7>=sp5 and sp7>=sp6 and sp1<=sp7 and sp7>=sp8:
                lab=Label(fra1,text='"Приколист",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            elif sp8>=sp2 and sp8>=sp3 and sp8>=sp4 and sp8>=sp5 and sp8>=sp6 and sp8>=sp7 and sp1<=sp8:
                lab=Label(fra1,text='"Алешенька",это тот сорт ,\nпо которому самая высокая производительность')
                lab.place(x=680,y=220)
            #!Построение диаграмм на основе полученных данных о производительности
            lab=Label(fra1,bg='red',width=sp1)
            lab.place(x=220,y=20)
            lab=Label(fra1,bg='yellow',width=sp2)
            lab.place(x=220,y=70)
            lab=Label(fra1,bg='green',width=sp3)
            lab.place(x=220,y=120)
            lab=Label(fra1,bg='blue',width=sp4)
            lab.place(x=220,y=170)
            lab=Label(fra1,bg='brown',width=sp5)
            lab.place(x=220,y=220)
            lab=Label(fra1,bg='orange',width=sp6)
            lab.place(x=220,y=270)
            lab=Label(fra1,bg='pink',width=sp7)
            lab.place(x=220,y=320)
            lab=Label(fra1,bg='black',width=sp8)
            lab.place(x=220,y=370)

            f=open('resulti.txt','a')
            f.write('1'+' '+str(p1)+' '+str(p11))
            f.write('\n')
            f.write('2'+' '+str(p2)+' '+str(p22))
            f.write('\n')
            f.write('3'+' '+str(p3)+' '+str(p33))
            f.write('\n')
            f.write('4'+' '+str(p4)+' '+str(p44))
            f.write('\n')
            f.write('5'+' '+str(p5)+' '+str(p55))
            f.write('\n')
            f.write('6'+' '+str(p6)+' '+str(p66))
            f.write('\n')
            f.write('7'+' '+str(7)+' '+str(p77))
            f.write('\n')
            f.write('8'+' '+str(p8)+' '+str(p88))
            f.write('\n')
            f.close()
    #!Защита от ошибки ввода неправильного символа в Entry
    except ValueError:
        mb.showerror('Ошибка','Ожидалось число, а не буква')


#!Создание начального окна
root=Tk()
root.title('Chocolate dream')
fra=Frame(root,width=700,height=500)
fra.pack()
#!Меню помощи
menu = Menu(root)
root.config(menu=menu)

help_menu=Menu(menu,tearoff=0)
help_menu.add_command(label='Рассчитать',command=dalee)
help_menu.add_command(label='Об авторе',command=about_author)
help_menu.add_command(label='О программе',command=about_prog)
help_menu.add_command(label='Выход',command=close)

menu.add_cascade(label='Опции',menu=help_menu)
#!Кнопка выход
butvix=Button(fra,text='Выход',command=close)
butvix.place(x=400,y=430)
#!Стерение данных с файла
f=open('resulti.txt','w')
f.close()
#!Построение полей таблицы
lab=Label(fra,text='Наименование\nшоколадных конфет')
lab.place(x=50,y=30)
lab=Label(fra,text='Сколько кг\nвыпускается(в день)')
lab.place(x=173,y=30)
lab=Label(fra,text='Себестоимость\n(рублей/кг)')
lab.place(x=300,y=30)
lab=Label(fra,text='Выпускная цена\n(рублей/кг)')
lab.place(x=400,y=30)
lab=Label(fra,text='Количество\nрабочих')
lab.place(x=500,y=30)
#!Название каждого сорта
lab=Label(fra,text='"Аленушка"')
lab.place(x=60,y=100)
lab=Label(fra,text='"Левушка"')
lab.place(x=60,y=140)
lab=Label(fra,text='"Лебедушка"')
lab.place(x=60,y=180)
lab=Label(fra,text='"Мороз"')
lab.place(x=60,y=220)
lab=Label(fra,text='"Крути"')
lab.place(x=60,y=260)
lab=Label(fra,text='"На завод"')
lab.place(x=60,y=300)
lab=Label(fra,text='"Приколист"')
lab.place(x=60,y=340)
lab=Label(fra,text='"Алешенька"')
lab.place(x=60,y=380)
#!Создание полос для облегчения прочтения программы
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=70)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=120)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=160)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=200)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=240)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=280)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=320)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=360)
lab=Label(fra,text='____________________________________________________________________________________________________________________________________________________________________________',font='Arial 4')
lab.place(x=50,y=400)
#!Вывод данных о производстве данного сорта кг/в день
lab=Label(fra,text='30')
lab.place(x=210,y=100)
lab=Label(fra,text='53')
lab.place(x=210,y=140)
lab=Label(fra,text='32')
lab.place(x=210,y=180)
lab=Label(fra,text='68')
lab.place(x=210,y=220)
lab=Label(fra,text='123')
lab.place(x=210,y=260)
lab=Label(fra,text='256')
lab.place(x=210,y=300)
lab=Label(fra,text='667')
lab.place(x=210,y=340)
lab=Label(fra,text='214')
lab.place(x=210,y=380)
#!Ввод выпускной цены
ent1=Entry(fra,width=7)
ent1.place(x=420,y=100)

ent2=Entry(fra,width=7)
ent2.place(x=420,y=140)

ent3=Entry(fra,width=7)
ent3.place(x=420,y=180)

ent4=Entry(fra,width=7)
ent4.place(x=420,y=220)

ent5=Entry(fra,width=7)
ent5.place(x=420,y=260)

ent6=Entry(fra,width=7)
ent6.place(x=420,y=300)

ent7=Entry(fra,width=7)
ent7.place(x=420,y=340)

ent8=Entry(fra,width=7)
ent8.place(x=420,y=380)
#!Ввод количества рабочих на производстве
ent11=Entry(fra,width=7)
ent11.place(x=510,y=100)

ent22=Entry(fra,width=7)
ent22.place(x=510,y=140)

ent33=Entry(fra,width=7)
ent33.place(x=510,y=180)

ent44=Entry(fra,width=7)
ent44.place(x=510,y=220)

ent55=Entry(fra,width=7)
ent55.place(x=510,y=260)

ent66=Entry(fra,width=7)
ent66.place(x=510,y=300)

ent77=Entry(fra,width=7)
ent77.place(x=510,y=340)

ent88=Entry(fra,width=7)
ent88.place(x=510,y=380)

#!Вывод данных о себестоимости
lab=Label(fra,text='39')
lab.place(x=320,y=100)
lab=Label(fra,text='29')
lab.place(x=320,y=140)
lab=Label(fra,text='22')
lab.place(x=320,y=180)
lab=Label(fra,text='59')
lab.place(x=320,y=220)
lab=Label(fra,text='40')
lab.place(x=320,y=260)
lab=Label(fra,text='50')
lab.place(x=320,y=300)
lab=Label(fra,text='35')
lab.place(x=320,y=340)
lab=Label(fra,text='27')
lab.place(x=320,y=380)

#!Кнопка,расчитывающая все данные по формуле и открытия нового окна с диаграммами(ф-ия dalee)
but=Button(fra,text='Рассчитать',font='Arial 10',command=dalee)
but.place(x=290,y=430)


root.mainloop()#!Закрытие окон


