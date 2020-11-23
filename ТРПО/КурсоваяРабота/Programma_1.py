from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
root=Tk()

  
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 7
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))

c = Canvas(root, width=1000, height=300,bg="#25373D")
c.pack()

# создание холста для рисования


#Линии сетки по вертикали
for y in range(10):
    k=100*y
    c.create_line(0+k,610,0+k,0,width=1,fill='#555')
for x in range(5):
    k=100*x
    c.create_line(1000,0+k,0,0+k,width=1,fill='#555')
    


#fra=Frame(c,height=300,width=1000)
#fra.pack()

def nlo(event):

    
    def oks1(event):#!Расположение каждой вершины
        def check():#!Окно с Сheckbutton
            
            def check_povtor(event):
                
                global povtor,r,dic,dic_verh,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,vers3,vers4
                
                v1=var0.get()
                v2=var1.get()
                v3=var2.get()
                v4=var3.get()
                v5=var4.get()
                v6=var5.get()
                v7=var6.get()
                v8=var7.get()
                v9=var8.get()
                v10=var9.get()
                
                
               
                radios=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]#список активных вершин c неактивными
                radios1=[]#список ативных веришн 
                
                for i in radios:
                    
                    if i!=0:
                        radios1.append(i)
             
                list_dic=[]#cписок значений ключа выбранной вершины
                
                for i in radios1:
                    list_dic.append(dic.get(i))
                    
                list_dic2=[]
                
                for i in list_dic:
                    for j in i:
                        list_dic2.append(int(j))
                        
                list_glavn=[dic.get(povtor+1)]#список значений текущей вершины
                list_glavn2=[]
                
                for i in list_glavn:
                    for j in i:
                        list_glavn2.append(int(j))
                pov=povtor+1
                
                pov=str(pov)
                dic_verh[pov]=radios1#словарь вершин
                dels=[]
                for i in dic_verh.items():
                                            
                    if not i[1]:
                        dels.append(i[0])

                for i in dels:
                    dic_verh[i]=[0]
                s=0
                for i in range(len(list_dic)):#соединение путей
                       c.create_line(list_glavn2[0],list_glavn2[1], list_dic2[s], list_dic2[s+1],fill="white")
                       s+=2
                
                if r!=povtor:
                    
                    povtor+=1
                    root4.destroy()
                    check()
                   
            def ves():
                
                global vespovtor,dic_verh,v,vec
                
                v=[]#список от каких вершин
                vec=[]#список к каким вершинам
                
                for i in dic_verh:
                    
                    verch_len=len(dic_verh.get(i))#длина значений
               
                    d=dic_verh.get(i)#значения словоря
                    
                    for j in range(verch_len):#цикл по длине 

                        v.append(vespovtor)
                        vec.append(d[j])
       
                    vespovtor+=1
                
                ves1()
                
            def ves1():
                
                def ves2(event):
                    
                    global v,vespovtor2 ,vseverh,dic_verh
                    entves2=entves.get()
                    
                    if entves2.isdigit() and  int(entves2)>0:
                        
                        vseverh.append(int(entves.get()))
                        
                        if vespovtor2!=len(v):
                            root5.destroy()
                            vespovtor2+=1
                            ves1()
                    else:
                        mb.showerror("Ошибка","Должны быть введены только положительные числа.")
                def choice(event):
                    global vseverh,entves2
                    def minway(event):
                        global vseverh,dic_verh
                        
                        try:
                            nodes=[]#списко вершин ('1','2'....)
                            for i in range(1,len(dic_verh)+1,1):#добавление
                                nodes.append(str(i))
                            
                            nodes=tuple(nodes)#преобразование в кортеж
                            dels=[]
                            for i in dic_verh.items():
                                
                                if not i[1]:
                                    dels.append(i[0])

                            for i in dels:
                                del dic_verh[i]
                            distances={}
                            s=0
                            for i in dic_verh:
                                for j in dic_verh[i]:
                                    
                                    if i in distances:
                                        if j in distances[i]:
                                            distances[i][str(j)] += vseverh[s]
                                        else:
                                            distances[i].update({str(j): vseverh[s]})
                                    else:
                                        distances[i] = {str(j): vseverh[s]}
                                    
                                    s+=1
                           
                            distanse={}

                            unvisited = {node: None for node in nodes}  # using None as +inf
                            visited = {}
                            current = str(enta.get())
                            currentt = current
                            correctt = str(entb.get())
                            currentDistance = 0
                            unvisited[current] = currentDistance

                            while True:
                                for neighbour, distance in distances[current].items():
                                    if neighbour not in unvisited: continue
                                    newDistance = currentDistance + distance
                                    if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                                        unvisited[neighbour] = newDistance
                                visited[current] = currentDistance
                                del unvisited[current]
                                if not unvisited:
                                    break
                                candidates = [node for node in unvisited.items() if node[1]]
                                current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

                            root7=Toplevel()
                            root7.title("Кратчайший путь")
                            x = (root7.winfo_screenwidth() - root7.winfo_reqwidth()) / 3
                            y = (root7.winfo_screenheight() - root7.winfo_reqheight()) / 2
                            root7.wm_geometry("+%d+%d" % (x, y))
                            fra7=Frame(root7,width=450,height=120,bg='#7CA39C')
                            fra7.pack()
                            Label(fra7, text="Кратчайший путь от вершины"+ " "+str(currentt) + " "+ ' до вершины ' + " "+ str(correctt) + " "+ ' = '+ " " + str(visited[correctt]),font='Arial 12',bg='#7CA39C').place(x=20,y=30)           
                            
                            root7.mainloop()
                        except: mb.showerror("Ошибка","Введены некорректные данные.\nПроверьте, существует ли путь между указанными вершинами.")
                        
                    if vec[len(vec)-1]==0:
                        
                        entves2='0'
                    else:
                        entves2=entves.get()
                    
                    if entves2.isdigit() and  int(entves2)>=0:
                        if vec[len(vec)-1]==0:
                            vseverh.append(0)
                        else:
                            vseverh.append(int(entves.get()))
                       
                        root6=Toplevel()
                        root6.title("Выбор вершин")

                        x = (root6.winfo_screenwidth() - root6.winfo_reqwidth()) / 3
                        y = (root6.winfo_screenheight() - root6.winfo_reqheight()) / 2
                        root6.wm_geometry("+%d+%d" % (x, y))
                                            
                        fra6=Frame(root6,width=450,height=120,bg='#7CA39C')
                        fra6.pack()

                        Label(fra6, text="Выберите кратчайший путь для вершин",font='Arial 12',bg='#7CA39C').place(x=95,y=15)
                        Label(fra6, text="От",font='Arial 12',bg='#7CA39C').place(x=130,y=50)
                        Label(fra6, text="До",font='Arial 12',bg='#7CA39C').place(x=250,y=50)
                        Label(fra6, text="------->",bg='#7CA39C').place(x=200,y=50)
                        
                        enta=Entry(fra6,width=5)
                        enta.place(x=160,y=50)
                        entb=Entry(fra6,width=5)
                        entb.place(x=280,y=50)
                    
                        view1 = Label(fra6, image=img3)
                        view1.place(x=195,y=80)
                        view1.bind("<1>",minway) 
                  
                        root6.mainloop()
                    else:
                        mb.showerror("Ошибка","Должны быть введены только положительные числа.")
            

                global vespovtor,v,vec,m,vespovtor2,vseverh,entves2
                
              
                if not vec[m]==0:
                    root5=Toplevel()
                    root5.title("Расстояние")
                           
                    x = (root5.winfo_screenwidth() - root5.winfo_reqwidth()) / 3
                    y = (root5.winfo_screenheight() - root5.winfo_reqheight()) / 2
                    root5.wm_geometry("+%d+%d" % (x, y))

                    fra5=Frame(root5,width=450,height=120,bg='#7CA39C')
                    fra5.pack()
                    
                    lab5=Label(fra5,text="Укажите размер от" +" "+str(v[m])+" "+"вершины"+" "+"до"+" "+str(vec[m]),font="Arial 12",bg='#7CA39C')
                    lab5.place(x=110,y=10)
                   
                    entves=Entry(fra5)
                    entves.place(x=170,y=50)
                    
                    view1 = Label(fra5, image=img1)
                    view1.place(x=200,y=80)
                    view1.bind("<1>",ves2) 
                    m+=1
                    if vespovtor2==len(v):
                        
                        view1 = Label(fra5, image=img1)
                        view1.place(x=200,y=80)
                        view1.bind("<1>",choice) 
                        
                    root5.mainloop()
                else:
                   
                    if vec[len(vec)-1]==vec[m] :
                        
                        
                        choice(event)
                    else:
                        m+=1
                        vseverh.append(0)
                        vespovtor2+=1
                        ves1()
                
            global u,r,povtor
            
            root4=Toplevel()
            root4.title("Расположение путей")
            
            x = (root4.winfo_screenwidth() - root4.winfo_reqwidth()) / 3
            y = (root4.winfo_screenheight() - root4.winfo_reqheight()) / 2
            root4.wm_geometry("+%d+%d" % (x, y))

            fra4=Frame(root4,width=450,height=120,bg='#7CA39C')
            fra4.pack()
            
            lab3=Label(fra4,text="Выберите пути от" +" "+str(povtor+1)+" "+"вершины",font="Arial 12",bg='#7CA39C')
            lab3.place(x=110,y=10)
            global vers3,vers4,vers5
            var0 = IntVar()
            var1 = IntVar()
            var2 = IntVar()
            var3 = IntVar()
            var4 = IntVar()
            var5 = IntVar()
            var6 = IntVar()
            var7 = IntVar()
            var8 = IntVar()
            var9 = IntVar()
            var10 = IntVar()
    
            
            c1=Checkbutton(root4, text="1", variable=var0, onvalue=1,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
            c1.place(x=110,y=50)
            c2=Checkbutton(root4, text="2", variable=var1, onvalue=2 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
            c2.place(x=150,y=50)
            c3=Checkbutton(root4, text="3", variable=var2, onvalue=3 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
            c3.place(x=190,y=50)
            c4=Checkbutton(root4, text="4", variable=var3, onvalue=4 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
            c4.place(x=230,y=50)
            #!a=var0.get()
            #!print(a)
            #!if a==0:
                #!c1=Checkbutton(root4, text="1", variable=var0, onvalue=1,offvalue=0,state=DISABLED,font="Arial 12",activeforeground="red",bg='#7CA39C')

            #!print(povtor)
            if povtor==1:
                if v2==2:
                    c1.destroy()
                    c1=Checkbutton(root4, text="1", variable=var0, onvalue=1,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C',state=DISABLED)
                if v3==3:
                    vers3+=1
                    
                    

                if v4==4:
                    vers4+=1
                
                
                c1.place(x=150,y=50)
                
            if povtor==2:
                if v3==3:
                    c2.destroy()
                    c2=Checkbutton(root4, text="2", variable=var0, onvalue=2,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C',state=DISABLED)
                if vers3==1:
                    c1.destroy()
                    c1=Checkbutton(root4, text="1", variable=var0, onvalue=1,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C',state=DISABLED)
                if v4==4:
                    vers5+=1

                
                c1.place(x=150,y=50)
                c2.place(x=190,y=50)
                
                
            if povtor==3:
                if v4==4:
                    c3.destroy()
                    c3=Checkbutton(root4, text="3", variable=var0, onvalue=3,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C',state=DISABLED)
                if vers5==1:
                    c2.destroy()
                    c2=Checkbutton(root4, text="2", variable=var0, onvalue=2,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C',state=DISABLED)
                if vers4==1:
                    c1.destroy()
                    c1=Checkbutton(root4, text="1", variable=var0, onvalue=1,offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C',state=DISABLED)
                c1.place(x=150,y=50)
                c2.place(x=190,y=50)
                c3.place(x=230,y=50)
                a = var0.get()
                #!if a==0:
                    #!c1=Checkbutton(root4, text="1", variable=var0, onvalue=1,offvalue=0,state=DISABLED,font="Arial 12",activeforeground="red",bg='#7CA39C')
                    
            if r==5:
                
                c5=Checkbutton(root4, text="5", variable=var4, onvalue=5 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c5.place(x=270,y=50)
                if povtor==4:
                    c1.place(x=150,y=50)
                    c2.place(x=190,y=50)
                    c3.place(x=230,y=50)
                    c4.place(x=270,y=50)
 
            elif r==6:
                
                c5=Checkbutton(root4, text="5", variable=var4, onvalue=5 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c6=Checkbutton(root4, text="6", variable=var5, onvalue=6 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                
                if povtor==0:
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                elif povtor==1:
                    
                    c1.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                elif povtor==2:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                elif povtor==3:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c3.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                elif povtor==4:
                    c6.place(x=270,y=50)
                         
            elif r==7:
                
                c5=Checkbutton(root4, text="5", variable=var4, onvalue=5, offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c6=Checkbutton(root4, text="6", variable=var5, onvalue=6 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c7=Checkbutton(root4, text="7", variable=var6, onvalue=7 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
               
                if povtor==0:
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                if povtor==1:
                    c1.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                if povtor==2:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                if povtor==3:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c3.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                if povtor==4:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c3.place(x=190,y=50)
                    c4.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                if povtor==5:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c3.place(x=190,y=50)
                    c4.place(x=230,y=50)
                    c5.place(x=270,y=50)
                    c7.place(x=310,y=50)
                if povtor==6:
                    c1.place(x=110,y=50)
                    c2.place(x=150,y=50)
                    c3.place(x=190,y=50)
                    c4.place(x=230,y=50)
                    c5.place(x=270,y=50)
                    c6.place(x=310,y=50)
                      
            elif r==8:
                
                c5=Checkbutton(root4, text="5", variable=var4, onvalue=5 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c6=Checkbutton(root4, text="6", variable=var5, onvalue=6 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c7=Checkbutton(root4, text="7", variable=var6, onvalue=7, offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c8=Checkbutton(root4, text="8", variable=var7, onvalue=8 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                
                if povtor==0:
                    c2.place(x=70,y=50)
                    c3.place(x=110,y=50)
                    c4.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==1:
                    c1.place(x=70,y=50)
                    c3.place(x=110,y=50)
                    c4.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==2:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c4.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==3:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==4:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==5:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==6:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c8.place(x=310,y=50)
                if povtor==7:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                    
            elif r==9:
            
                c5=Checkbutton(root4, text="5", variable=var4, onvalue=5 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c6=Checkbutton(root4, text="6", variable=var5, onvalue=6 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c7=Checkbutton(root4, text="7", variable=var6, onvalue=7 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c8=Checkbutton(root4, text="8", variable=var7, onvalue=8 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c9=Checkbutton(root4, text="9", variable=var8, onvalue=9 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
         
                if povtor==0:
                    c2.place(x=70,y=50)
                    c3.place(x=110,y=50)
                    c4.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==1:
                    c1.place(x=70,y=50)
                    c3.place(x=110,y=50)
                    c4.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==2:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c4.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==3:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c5.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==4:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c6.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==5:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c7.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==6:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c8.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==7:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                    c9.place(x=350,y=50)
                if povtor==8:
                    c1.place(x=70,y=50)
                    c2.place(x=110,y=50)
                    c3.place(x=150,y=50)
                    c4.place(x=190,y=50)
                    c5.place(x=230,y=50)
                    c6.place(x=270,y=50)
                    c7.place(x=310,y=50)
                    c8.place(x=350,y=50)
                
            elif r==10:
                
                c5=Checkbutton(root4, text="5", variable=var4, onvalue=5, offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c5.place(x=140,y=50)
                c6=Checkbutton(root4, text="6", variable=var5, onvalue=6, offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c6.place(x=170,y=60)
                c7=Checkbutton(root4, text="7", variable=var6, onvalue=7, offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c7.place(x=200,y=60)
                c8=Checkbutton(root4, text="8", variable=var7, onvalue=8, offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c8.place(x=230,y=60)
                c9=Checkbutton(root4, text="9", variable=var8, onvalue=9 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c9.place(x=250,y=60)
                c10=Checkbutton(root4, text="10", variable=var9, onvalue=10 , offvalue=0,font="Arial 12",activeforeground="red",bg='#7CA39C')
                c10.place(x=280,y=60)
                if povtor==0:
                    c2.place(x=50,y=50)
                    c3.place(x=90,y=50)
                    c4.place(x=130,y=50)
                    c5.place(x=170,y=50)
                    c6.place(x=210,y=50)
                    c7.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==1:
                    c1.place(x=50,y=50)
                    c3.place(x=90,y=50)
                    c4.place(x=130,y=50)
                    c5.place(x=170,y=50)
                    c6.place(x=210,y=50)
                    c7.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==2:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c4.place(x=130,y=50)
                    c5.place(x=170,y=50)
                    c6.place(x=210,y=50)
                    c7.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==3:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c5.place(x=170,y=50)
                    c6.place(x=210,y=50)
                    c7.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==4:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c4.place(x=170,y=50)
                    c6.place(x=210,y=50)
                    c7.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==5:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c4.place(x=170,y=50)
                    c5.place(x=210,y=50)
                    c7.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==6:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c4.place(x=170,y=50)
                    c5.place(x=210,y=50)
                    c6.place(x=250,y=50)
                    c8.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==7:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c4.place(x=170,y=50)
                    c5.place(x=210,y=50)
                    c6.place(x=250,y=50)
                    c7.place(x=290,y=50)
                    c9.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==8:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c4.place(x=170,y=50)
                    c5.place(x=210,y=50)
                    c6.place(x=250,y=50)
                    c7.place(x=290,y=50)
                    c8.place(x=330,y=50)
                    c10.place(x=370,y=50)
                if povtor==9:
                    c1.place(x=50,y=50)
                    c2.place(x=90,y=50)
                    c3.place(x=130,y=50)
                    c4.place(x=170,y=50)
                    c5.place(x=210,y=50)
                    c6.place(x=250,y=50)
                    c7.place(x=290,y=50)
                    c8.place(x=330,y=50)
                    c9.place(x=370,y=50)
                    
            view1 = Label(fra4, image=img1)
            view1.place(x=190,y=85)
            view1.bind("<1>",check_povtor) 
           # ttk.Button(fra4,text="Продолжить",command=check_povtor).place(x=180,y=85)
            
            
            if r!=povtor:
                if povtor==0:
                    c1.destroy()
                elif povtor==1:
                    c2.destroy()
                elif povtor==2:
                    c3.destroy()
                elif povtor==3:
                    c4.destroy()
                elif povtor==4:
                    c5.destroy()
                elif povtor==5:
                    c6.destroy()
                elif povtor==6:
                    c7.destroy()
                elif povtor==7:
                    c8.destroy()
                elif povtor==8:
                    c9.destroy()
                elif povtor==9:
                    c10.destroy()
            else:
                
                root4.destroy()
                ves()
                

            root4.mainloop()
        
        def ok_povtor(event):#!Фунуция для повторения 
                
            global u,mass,r,mass2,dic
            enx=entx.get()
            eny=enty.get()
            if enx.isdigit() and eny.isdigit() and int(enx)<=980 and int (eny)<=280:
                
                mass.append(entx.get())
                mass.append(enty.get())

                mass2.append(entx.get())
                mass2.append(enty.get())
                  
                r=int(ent1.get())
                
                dic[u+1]=entx.get(),enty.get()#словарь вершина-рсположение
                
                if r !=u:#если не равно, то появляется новое окно для расположения
                    
                    u+=1
                    root3.destroy()
                    
                
                    lab2=Label(c,text=u,bg="#66cccc",fg="#003333",font="Arial 14")
                    
                    lab2.place(x=mass[0],y=mass[1])
                    
                    mass.clear()
                    
                    oks1(event)
            else:
                mb.showerror("Ошибка","Должны быть введены только числа: для Х- от 0 до 980, для Y- от 0 до 280.")
                
  
        a=ent1.get()
    
        if a.isdigit() and int(a)>=4 and int(a)<=10:
            
            root3=Toplevel()
            root3.title('Расположение вершин')
            
            x = (root3.winfo_screenwidth() - root3.winfo_reqwidth()) / 3
            y = (root3.winfo_screenheight() - root3.winfo_reqheight()) / 2
            root3.wm_geometry("+%d+%d" % (x, y))
            
            fra3=Frame(root3,width=450,height=120,bg='#7CA39C')
            fra3.pack()

            lab=Label(fra3,text='Введите расположение'+' '+str(u+1)+' '+'вершины (по x и y).',font='Arial 12',bg='#7CA39C')
            lab.place(x=110,y=10)
            lab1=Label(fra3,text='x=',font='Arial 12',bg='#7CA39C')
            lab2=Label(fra3,text='y=',font='Arial 12',bg='#7CA39C')
            lab1.place(x=156,y=40)
            lab2.place(x=236,y=40)
            
            entx=Entry(fra3,width=5,font='Arial 12')
            entx.place(x=180,y=43)
            
            enty=Entry(fra3,width=5,font='Arial 12')
            enty.place(x=260,y=43)
            
            #ttk.Button(fra3,text="Готово",command=ok_povtor).place(x=200,y=80)
            view2 = Label(fra3, image=img2)
            view2.place(x=190,y=75)
            view2.bind("<1>",ok_povtor)
            if u==int(ent1.get()):
                
                root3.destroy()
                root2.destroy()
                check()#!Ввызывает функцию radio
                
            root3.mainloop()
        else:
            mb.showerror("Ошибка","Должны быть введены только числа от 4 до 10.")
            
        
    view.destroy()
    #!Кол-во вершин
    root2=Toplevel()
    root2.title('Вершины')
    
    x = (root2.winfo_screenwidth() - root2.winfo_reqwidth()) / 3
    y = (root2.winfo_screenheight() - root2.winfo_reqheight()) / 2
    root2.wm_geometry("+%d+%d" % (x, y))
    
    fra1=Frame(root2,height=120,width=450,bg='#7CA39C')
    fra1.pack()

    lab1=Label(fra1,text='Сколько будет вершин (от 4 до 10)?',font='Arial 12',bg='#7CA39C')
    lab1.place(x=110,y=10)

    ent1=Entry(fra1,width=5,font='Arial 12')
    ent1.place(x=200,y=40)
   
    view1 = Label(fra1, image=img1)
    view1.place(x=190,y=75)
    view1.bind("<1>",oks1)
   # ttk.Button(fra1,text='ОК',command=oks1).place(x=190,y=70)
def ex():
    root.destroy()

def avtor():
    mb.showinfo("Об авторе","Распопова М.В, Алабужина А.В, Миронов Д - курсанты 331 группы Троицкого АТК - филиала МГТУ ГА")
def prog():
    
    mb.showinfo("О проограмме ","Программа 'Minway' предназначена для нахождения кратчайшего пути от одной вершины до другой.Для того чтобы начать пользоваться программой следует нажать кнопку Начать. В всплывающем окне пользователь должен вписать в строку ввода количество вершин цифрой(от 4 до 10). В последующих окнах вводятся координаты этих самых вершин по X и Y. Координаты вводятся для каждой вершины по отдельности. После ввода данных в строки нужно нажать кнопку Готово чтобы перейти к вводу координат следующих вершин. Далее выводятся окна с выбором до какой вершины будет проложен путь от изначальной вершины. Выбор производится путем нажатия галочек напротив нумераций всех представленных вершин. После проставления галочек следует нажать кнопку Продолжить. Для того чтобы указать размер от вершины до вершина выводится окно, в котором в строку ввода нужно цифрой ввести размер пути. Для получения конечного результата выводится последнее окно в котором пользователю нужно ввести начальную и конечную вершину.  ")
global vers3,vers4
vers3=0
vers4=0
vers5=0
vers6=0
menu=Menu(root)#создание меню
root.config(menu=menu)

m=Menu(menu)

m.add_command(label="Об авторе ",command=avtor)#создание опций меню
m.add_command(label="Инструкция к программе",command=prog)
m.add_command(label="Выход",command=ex)

menu.add_cascade(label="Меню",menu=m)
u=0
povtor=0
vespovtor=1
vespovtor2=1
mass=[]
mass2=[]
m=0
dic={}
dic_verh={}
vseverh=[]
#mb.showerror("Ошибка","Введены некорректные данные.\nПроверьте, существует ли путь между указанными вершинами.")
#butn=Button(fra,command=nlo,text='Начать',font='Arial 20')
#butn.place(x=450,y=80)
img = ImageTk.PhotoImage(Image.open('begin3.png'))
view = Label(c, image=img)
view.place(x=400,y=80)
view.bind("<1>",nlo)
img1 = ImageTk.PhotoImage(Image.open('ok.png'))
img2 = ImageTk.PhotoImage(Image.open('done.png'))
img3 = ImageTk.PhotoImage(Image.open('poisk.png'))
root.mainloop()
