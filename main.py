from tkinter import *

window = Tk()
window.geometry("800x600")

def calculate():
    fruit=e1.get()
    fish=e2.get()
    pork=e3.get()
    egg=e4.get()
    total=((int(fruit)*20)+(int(fish)*30)+(int(pork)*50)+(int(egg)*5))
    print(total)
    label21 = Label(window,text="รวมราคา",font="50")
    label21.place(x=100,y=300)
    label22 = Label(window,text=total,font="50")
    label22.place(x=200,y=300)

#---MENU--

label1 = Label(window,text="MENU",font="times 28 bold")
label1.place(x=350,y=30)

label11 = Label(window,text="นํ้าผลไม้         20 บาท",font="50")
label11.place(x=50,y=100)

label111 = Label(window,text="ซื้อ",font="50")
label111.place(x=300,y=100)

label12 = Label(window,text="ปลาทู            30 บาท",font="50")
label12.place(x=50,y=125)

label121 = Label(window,text="ซื้อ",font="50")
label121.place(x=300,y=125)

label13 = Label(window,text="เนื้อหมู 1 โล    50 บาท",font="50")
label13.place(x=50,y=150)

label131 = Label(window,text="ซื้อ",font="50")
label131.place(x=300,y=150)

label14 = Label(window,text="ไข่ไก่ 1 ฟอง    5 บาท",font="50")
label14.place(x=50,y=175)

label141 = Label(window,text="ซื้อ",font="50")
label141.place(x=300,y=175)

#-----bill

e1=Entry(window)
e1.place(x=350,y=110)

e2=Entry(window)
e2.place(x=350,y=135)

e3=Entry(window)
e3.place(x=350,y=160)

e4=Entry(window)
e4.place(x=350,y=185)

b1=Button(window,text='บิล',font="50",width=20,command=calculate)
b1.place(x=150,y=250)

window.mainloop()
