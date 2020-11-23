#если одинковые строки вывести номер 
def opens(name,spis):
    with open (name,encoding="utf-8") as f:
        for i in f:
            if i=='\n':
                pass 
            else:
                spis.append(i.rstrip('\n'))
    return spis
    
tex=[]
tex2=[]
opens('t1.txt',tex)
opens('t2.txt',tex2)
s=1
ss=1
print(tex)
print(tex2)
for i in tex:
    for j in tex2:
        
        if i==j:
            print(ss,s)
        if s==len(tex2):
            s=0
        s+=1
    ss+=1

