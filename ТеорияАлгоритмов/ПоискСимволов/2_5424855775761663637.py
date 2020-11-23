from random import randint
'''
#Binary
a=[randint(1,100) for i in range(11)]
a=sorted(a)
n=a[1]
print(n)
print(a)
while True:
    m = len(a) // 2 + 1
    if a[m - 1] < n:
        a = a[m:]
        print(a)
    elif a[m - 1] > n:
        a = a[:m-1]
        print(a)
    elif a[m - 1] == n:
        print('!')
        break
'''
#Fibonachi
a=[3,5,8,9,11,14,15,19,21,22,28,33,35,37,42,45,48,52]
k=11
fib=[0,1,2,3,5,8,13,21,34]
h=0
hh=0
count=0
f=True
while f:
    
    # print(a)
    for j in fib:
        count+=1
        # print(j)
        try:
            # print(a[j-1])

            if a[j]==k:
                rezz=a[j]
                f = False
                break
            elif a[j]>k:
                hh=a[j]
                hh=a.index(hh)
                break
            elif a[j]<k:
                h = a[j]
                h=a.index(h)
        except IndexError:
            hh=a[-1]
            hh = a.index(hh)
            break
    
    #print('h',h)
    #print('hh',hh)
    a=a[h+1:hh+1]
    print(a)
    

print(rezz)
print('Count iteration:',count)
'''
#Interpolation

mass=[4,5,10,23,24,30,47,59,60,64,65,77,90,95,98,102]
k=10
while True:
    print(mass)
    j=mass.index(mass[-1])
    i=mass.index(mass[0])
    ki=mass[0]
    kj=mass[-1]
    d=(j-i)*(k-ki)//(kj-ki)

    print('Индекс сравниваемого элемента в массиве',d)
    print('Сравниваемый элемент в массиве',mass[d])

    if mass[d]==k:
        print('Congratulations!')
        break
    elif mass[d]>k:
        mass=mass[:d]
    elif mass[d]<k:
        mass=mass[d+1:]

'''
    

