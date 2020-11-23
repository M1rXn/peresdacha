from ctypes import cast, POINTER
from tkinter import messagebox as mb
from tkinter import *
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-60.57, None)
def ok():
    try:
        if int(ent.get())>100:
            mb.showerror('0шибка','Подумай о соседях')
        elif int(ent.get())<0:
            mb.showerror('0шибка','Слишком низкие частоты для тебя, дружок!')
        
        if ent.get()=='100':
            volume.SetMasterVolumeLevel(-0.0, None)
        elif ent.get()=='99':
            volume.SetMasterVolumeLevel(-0.1, None)
        elif ent.get()=='98':
            volume.SetMasterVolumeLevel(-0.3, None)
        elif ent.get()=='97':
            volume.SetMasterVolumeLevel(-0.5, None)
        elif ent.get()=='96':
            volume.SetMasterVolumeLevel(-0.6, None)
        elif ent.get()=='95':
            volume.SetMasterVolumeLevel(-0.8, None)
        elif ent.get()=='94':
            volume.SetMasterVolumeLevel(-1.0, None)
        elif ent.get()=='93':
            volume.SetMasterVolumeLevel(-1.1, None)
        elif ent.get()=='92':
            volume.SetMasterVolumeLevel(-1.3, None)
        elif ent.get()=='91':
            volume.SetMasterVolumeLevel(-1.5, None)
        elif ent.get()=='90':
            volume.SetMasterVolumeLevel(-1.6, None)
        elif ent.get()=='89':
            volume.SetMasterVolumeLevel(-1.8, None)
        elif ent.get()=='88':
            volume.SetMasterVolumeLevel(-2.0, None)
        elif ent.get()=='87':
            volume.SetMasterVolumeLevel(-2.1, None)
        elif ent.get()=='86':
            volume.SetMasterVolumeLevel(-2.3, None)
        elif ent.get()=='85':
            volume.SetMasterVolumeLevel(-2.5, None)
        elif ent.get()=='84':
            volume.SetMasterVolumeLevel(-2.6, None)
        elif ent.get()=='83':
            volume.SetMasterVolumeLevel(-2.8, None)
        elif ent.get()=='82':
            volume.SetMasterVolumeLevel(-3.0, None)
        elif ent.get()=='81':
            volume.SetMasterVolumeLevel(-3.1, None)
        elif ent.get()=='80':
            volume.SetMasterVolumeLevel(-3.3, None)
        elif ent.get()=='79':
            volume.SetMasterVolumeLevel(-3.5, None)
        elif ent.get()=='78':
            volume.SetMasterVolumeLevel(-3.7, None)
        elif ent.get()=='77':
            volume.SetMasterVolumeLevel(-3.9, None)
        elif ent.get()=='76':
            volume.SetMasterVolumeLevel(-4.1, None)
        elif ent.get()=='75':
            volume.SetMasterVolumeLevel(-4.3, None)
        elif ent.get()=='74':
            volume.SetMasterVolumeLevel(-4.5, None)
        elif ent.get()=='73':
            volume.SetMasterVolumeLevel(-4.7, None)
        elif ent.get()=='72':
            volume.SetMasterVolumeLevel(-4.9, None)
        elif ent.get()=='71':
            volume.SetMasterVolumeLevel(-5.1, None)
        elif ent.get()=='70':
            volume.SetMasterVolumeLevel(-5.3, None)
        elif ent.get()=='69':
            volume.SetMasterVolumeLevel(-5.5, None)
        elif ent.get()=='68':
            volume.SetMasterVolumeLevel(-5.7, None)
        elif ent.get()=='67':
            volume.SetMasterVolumeLevel(-5.9, None)
        elif ent.get()=='66':
            volume.SetMasterVolumeLevel(-6.1, None)
        elif ent.get()=='65':
            volume.SetMasterVolumeLevel(-6.37, None)
        elif ent.get()=='64':
            volume.SetMasterVolumeLevel(-6.7, None)
        elif ent.get()=='63':
            volume.SetMasterVolumeLevel(-6.9, None)
        elif ent.get()=='62':
            volume.SetMasterVolumeLevel(-7.1, None)
        elif ent.get()=='61':
            volume.SetMasterVolumeLevel(-7.37, None)
        elif ent.get()=='60':
            volume.SetMasterVolumeLevel(-7.7, None)
        elif ent.get()=='59':
            volume.SetMasterVolumeLevel(-7.9, None)
        elif ent.get()=='58':
            volume.SetMasterVolumeLevel(-8.1, None)
        elif ent.get()=='57':
            volume.SetMasterVolumeLevel(-8.3, None)
        elif ent.get()=='56':
            volume.SetMasterVolumeLevel(-8.7, None)
        elif ent.get()=='55':
            volume.SetMasterVolumeLevel(-8.9, None)
        elif ent.get()=='54':
            volume.SetMasterVolumeLevel(-9.1, None)
        elif ent.get()=='53':
            volume.SetMasterVolumeLevel(-9.4, None)
        elif ent.get()=='52':
            volume.SetMasterVolumeLevel(-9.7, None)
        elif ent.get()=='51':
            volume.SetMasterVolumeLevel(-9.9, None)
        elif ent.get()=='50':
            volume.SetMasterVolumeLevel(-10.2, None)
        elif ent.get()=='49':
            volume.SetMasterVolumeLevel(-10.5, None)
        elif ent.get()=='48':
            volume.SetMasterVolumeLevel(-10.8, None)
        elif ent.get()=='47':
            volume.SetMasterVolumeLevel(-11.1, None)
        elif ent.get()=='46':
            volume.SetMasterVolumeLevel(-11.5, None)
        elif ent.get()=='45':
            volume.SetMasterVolumeLevel(-11.9, None)
        elif ent.get()=='44':
            volume.SetMasterVolumeLevel(-12.3, None)
        elif ent.get()=='43':
            volume.SetMasterVolumeLevel(-12.7, None)
        elif ent.get()=='42':
            volume.SetMasterVolumeLevel(-13.0, None)
        elif ent.get()=='41':
            volume.SetMasterVolumeLevel(-13.3, None)
        elif ent.get()=='40':
            volume.SetMasterVolumeLevel(-13.6, None)
        elif ent.get()=='39':
            volume.SetMasterVolumeLevel(-13.9, None)
        elif ent.get()=='38':
            volume.SetMasterVolumeLevel(-14.2, None)
        elif ent.get()=='37':
            volume.SetMasterVolumeLevel(-14.6, None)
        elif ent.get()=='36':
            volume.SetMasterVolumeLevel(-15.0, None)
        elif ent.get()=='35':
            volume.SetMasterVolumeLevel(-15.4, None)
        elif ent.get()=='34':
            volume.SetMasterVolumeLevel(-15.8, None)
        elif ent.get()=='33':
            volume.SetMasterVolumeLevel(-16.3, None)
        elif ent.get()=='32':
            volume.SetMasterVolumeLevel(-16.8, None)
        elif ent.get()=='31':
            volume.SetMasterVolumeLevel(-17.3, None)
        elif ent.get()=='30':
            volume.SetMasterVolumeLevel(-17.8, None)
        elif ent.get()=='29':
            volume.SetMasterVolumeLevel(-18.3, None)
        elif ent.get()=='28':
            volume.SetMasterVolumeLevel(-18.8, None)
        elif ent.get()=='27':
            volume.SetMasterVolumeLevel(-19.3, None)
        elif ent.get()=='26':
            volume.SetMasterVolumeLevel(-19.8, None)
        elif ent.get()=='25':
            volume.SetMasterVolumeLevel(-20.3, None)
        elif ent.get()=='24':
            volume.SetMasterVolumeLevel(-20.8, None)
        elif ent.get()=='23':
            volume.SetMasterVolumeLevel(-21.4, None)
        elif ent.get()=='22':
            volume.SetMasterVolumeLevel(-22.0, None)
        elif ent.get()=='21':
            volume.SetMasterVolumeLevel(-22.7, None)
        elif ent.get()=='20':
            volume.SetMasterVolumeLevel(-23.4, None)
        elif ent.get()=='19':
            volume.SetMasterVolumeLevel(-24.2, None)
        elif ent.get()=='18':
            volume.SetMasterVolumeLevel(-25.0, None)
        elif ent.get()=='17':
            volume.SetMasterVolumeLevel(-25.8, None)
        elif ent.get()=='16':
            volume.SetMasterVolumeLevel(-26.6, None)
        elif ent.get()=='15':
            volume.SetMasterVolumeLevel(-27.5, None)
        elif ent.get()=='14':
            volume.SetMasterVolumeLevel(-28.3, None)
        elif ent.get()=='13':
            volume.SetMasterVolumeLevel(-29.2, None)
        elif ent.get()=='12':
            volume.SetMasterVolumeLevel(-31.0, None)
        elif ent.get()=='11':
            volume.SetMasterVolumeLevel(-32.0, None)
        elif ent.get()=='10':
            volume.SetMasterVolumeLevel(-33.0, None)
        elif ent.get()=='9':
            volume.SetMasterVolumeLevel(-34.0, None)
        elif ent.get()=='8':
            volume.SetMasterVolumeLevel(-36.0, None)
        elif ent.get()=='7':
            volume.SetMasterVolumeLevel(-38.0, None)
        elif ent.get()=='6':
            volume.SetMasterVolumeLevel(-40.0, None)
        elif ent.get()=='5':
            volume.SetMasterVolumeLevel(-42.0, None)
        elif ent.get()=='4':
            volume.SetMasterVolumeLevel(-44.0, None)
        elif ent.get()=='3':
            volume.SetMasterVolumeLevel(-49.0, None)
        elif ent.get()=='2':
            volume.SetMasterVolumeLevel(-53.0, None)
        elif ent.get()=='1':
            volume.SetMasterVolumeLevel(-57.0, None)
        elif ent.get()=='0':
            volume.SetMasterVolumeLevel(-61.0, None)
    except ValueError:
        mb.showerror('Ошибка','Ошибка друг')
root=Tk()
fra=Frame(root,width=200,height=100)
fra.pack()
ent=Entry(fra)
ent.place(x=35,y=30)
ent.focus()
but=Button(fra,command=ok,text='OK')
but.place(x=80,y=59)
lab=Label(fra,text='Введите громкость')
lab.place(x=40,y=5)
root.mainloop()
