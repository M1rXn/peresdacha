from tkinter import *
from tkinter import messagebox as fd
from tkinter import filedialog as mb


def openfile():
    global open_file,slo,ent
    
    ent=Entry(root)
    ent.place(x=190,y=50)
    ent.focus()
      
    open_file=mb.askopenfilename()
    f=open(open_file,encoding="utf-8")
    s=f.read()
    text.insert(1.0,s)
    f.close()
    but2=Button(fra,width=13,height=3,font='Arial 10',text='Преобразовать',command=convert)
    but2.place(x=210,y=550)
def save():
    global textp
    save_file=mb.asksaveasfilename(filetypes = (("All files","*.*"),("TXT","*.txt.*")))
    f=open(save_file,'w')
    g=textp.get(1.0,END)
    f.write(g)
    f.close
def convert():
    global text1,slo,ent,textp
    
    slo=ent.get()
    slo = str(slo)
    ff=text.get(1.0 ,END)
    ss=ff.split('\n')
    strok = []
    for i in ss:
        k = i.lower().replace('.','').replace(',','').replace(';','').replace('!','').replace('?','').replace(':','').split()
        if slo.lower() in k:
            strok.append(i)
    if len(strok)==0:
        fd.showerror('Ошибка','Данного слова нет!')
    else:
        fra.configure(width=700,height=650)
        buts=Button(text='Сохранить',font='Arial 10',command=save,width=10,height=3)
        buts.place(x=550,y=550)
        textp=Text(fra,width=40,height=30)
        textp.place(x=400,y=20)
        strok = strok[::-1]
        
        for i in strok:
                textp.insert(0.0,str(i)+'\n')

root=Tk()
root.title('Проводник')
fra=Frame(root,width=350,height=650)
fra.pack()
text=Text(fra,width=40,height=30)
text.place(x=10,y=150)

but1=Button(fra,width=10,height=1,font='Arial 8',text='Открыть',command=openfile)
but1.place(x=60,y=50)
root.mainloop()
