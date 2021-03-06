from tkinter import *
from tkinter import messagebox as mb
from random import randint
def combsort():
    pol=100
    n=ent1.get()
    n=int(n)
    f=open('result.txt','w')
    f.close()
    alist=[randint (-10,50)for  i in range(n)]
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    if len(alist)>10:
        mb.showerror('Слишком большое количество цифр','Количество цифр превышает норму для показа,вывод шагов сортировки записан в файл result.txt')
    while gap:
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
        
        lab3=Label(fra,text=('В данном цикле проверяются цифры от 1 до ',n,'между которыми\n расстояние ',gap,'цифр'),font='Arial 8')
        lab2=Label(fra,text=alist,font='Arial 12')
        lab2.place(x=15,y=pol)
        pol=pol+30
        gap = (gap * 10 // 13)
        lab3.place(x=250,y=pol-30)
        f=open('result.txt','a')
        priv=str(alist)
        f.write(priv)
        f.write('\n')
        f.close()
        
    return alist
def infaosort():
    mb.showinfo('Описание и история создания','Сортировка расчёской (англ. comb sort) — это довольно упрощённый алгоритм сортировки, изначально спроектированный Влодзимежом Добосевичем в 1980 г. Позднее он был переоткрыт и популяризован в статье Стивена Лэйси и Ричарда Бокса в журнале Byte Magazine в апреле 1991 г[1]. Сортировка расчёской улучшает сортировку пузырьком, и конкурирует с алгоритмами, подобными быстрой сортировке. Основная идея — устранить черепах, или маленькие значения в конце списка, которые крайне замедляют сортировку пузырьком (кролики, большие значения в начале списка, не представляют проблемы для сортировки пузырьком).В сортировке пузырьком, когда сравниваются два элемента, промежуток (расстояние друг от друга) равен 1. Основная идея сортировки расчёской в том, что этот промежуток может быть гораздо больше, чем единица (сортировка Шелла также основана на этой идее, но она является модификацией сортировки вставками, а не сортировки пузырьком).')
def infaoalg():
    mb.showinfo('Алгоритм','В «пузырьке», «шейкере» и «чёт-нечете» при переборе массива сравниваются соседние элементы. Основная идея «расчёски» в том, чтобы первоначально брать достаточно большое расстояние между сравниваемыми элементами и по мере упорядочивания массива сужать это расстояние вплоть до минимального. Таким образом, мы как бы причёсываем массив, постепенно разглаживая на всё более аккуратные пряди. Первоначальный разрыв между сравниваемыми элементами лучше брать с учётом специальной величины, называемой фактором уменьшения, оптимальное значение которой равно примерно 1,247[источник не указан 143 дня]. Сначала расстояние между элементами равно размеру массива, разделённого на фактор уменьшения (результат округляется до ближайшего целого). Затем, пройдя массив с этим шагом, необходимо поделить шаг на фактор уменьшения и пройти по списку вновь. Так продолжается до тех пор, пока разность индексов не достигнет единицы. В этом случае массив досортировывается обычным пузырьком.')
root=Tk()
root.title('Сортировка расческой')
fra=Frame(root,width=650,height=450)
fra.pack()
but2=Button(fra,text='Описание сортировки и история создания',font='Arial 12',command=infaosort)
but2.place(x=15,y=20)
but2=Button(fra,text='Алгоритм сортировки',font='Arial 12',command=infaoalg)
but2.place(x=380,y=20)
lab1=Label(fra,text='Введите количество рандомных чисел в массиве',font='Arial 12')
lab1.place(x=15,y=60)
ent1=Entry(fra,width=4,font='Arial 12')
ent1.place(x=400,y=60)
but1=Button(fra,text='Сортировать',font='Arial 12',command=combsort)
but1.place(x=450,y=60)
root.mainloop()
