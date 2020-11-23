from tkinter import*
import pygame
pygame.init()


def col1(event):
    do=pygame.mixer.Sound("do.wav")
    do.play()
def col2(event):
    do=pygame.mixer.Sound("re.wav")
    do.play()
def col3(event):
    do=pygame.mixer.Sound("mi.wav")
    do.play()
def col4(event):
    do=pygame.mixer.Sound("fa.wav")
    do.play()
def col5(event):
    do=pygame.mixer.Sound("sol.wav")
    do.play()
def col6(event):
    do=pygame.mixer.Sound("lja.wav")
    do.play()
def col7(event):
    do=pygame.mixer.Sound("si.wav")
    do.play()
    


w=Tk()
w.title("Пианино")
fra=Frame(w,width=250,height=100)
fra.pack()
im = PhotoImage(file='wdw.gif')
l=Label(fra,image=im)
l.pack()
w.bind("<q>",col1)
w.bind("<w>",col2)
w.bind("<e>",col3)
w.bind("<r>",col4)
w.bind("<t>",col5)
w.bind("<y>",col6)
w.bind("<u>",col7)
w.mainloop()
w.mainloop()
