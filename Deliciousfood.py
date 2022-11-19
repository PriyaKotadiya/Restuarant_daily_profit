from tkinter import *
from tkinter import messagebox
import sqlite3



def showre():
    root1 = Tk()
    root1.geometry("1000x1000")
    root1.title("BILL")
    connection = sqlite3.connect("Bill0.db")
    cur = connection.cursor()

    cur.execute("SELECT * FROM bill2")
    data = cur.fetchall()

    
    Label(root1, text = "Name", width=10, fg="Maroon", bg="pink").grid(row=0, column=0)
    Label(root1, text = "Burger", width=10, fg="maroon", bg="pink").grid(row=0, column=1)
    Label(root1, text = "Sandwich", width=10, fg="maroon", bg="pink").grid(row=0, column=2)
    Label(root1, text = "South Indian", width=10, fg="maroon", bg="pink").grid(row=0, column=3)
    Label(root1, text = "Punjabi", width=10, fg="maroon", bg="pink").grid(row=0, column=4)
    Label(root1, text = "Chinese", width=10, fg="maroon", bg="pink").grid(row=0, column=5)
    Label(root1, text = "Sizzler", width=10, fg="maroon", bg="pink").grid(row=0, column=6)
    Label(root1, text = "Gujrati Thali", width=10, fg="maroon", bg="pink").grid(row=0, column=7)
    Label(root1, text = "Pizza", width=10, fg="maroon", bg="pink").grid(row=0, column=8)
    Label(root1, text = "Butter Milk", width=10, fg="maroon", bg="pink").grid(row=0, column=9)
    Label(root1, text = "Cold Drinks", width=10, fg="maroon", bg="pink").grid(row=0, column=10)
    Label(root1, text = "TOTAL", width=10, fg="BLUE", font=("bold", 10), bg="pink").grid(row=0, column=11)
    
    trs1=0

    for index, dat in enumerate(data):
        Label(root1, text=dat[0]).grid(row=index + 1, column=0)
        Label(root1, text=dat[1]).grid(row=index + 1, column=1)
        Label(root1, text=dat[2]).grid(row=index + 1, column=2)
        Label(root1, text=dat[3]).grid(row=index + 1, column=3)
        Label(root1, text=dat[4]).grid(row=index + 1, column=4)
        Label(root1, text=dat[5]).grid(row=index + 1, column=5)
        Label(root1, text=dat[6]).grid(row=index + 1, column=6)
        Label(root1, text=dat[7]).grid(row=index + 1, column=7)
        Label(root1, text=dat[8]).grid(row=index + 1, column=8)
        Label(root1, text=dat[9]).grid(row=index + 1, column=9)
        Label(root1, text=dat[10]).grid(row=index + 1, column=10)
        Label(root1, text=dat[11]).grid(row=index + 1, column=11)
        
        trs1 = trs1+float(dat[11])
    Label(root1, text="TOTAL", fg="RED", font=("bold", 10), bg="Yellow").grid(row=index + 2, column=10)
    Label(root1, text=trs1, fg="RED", font=("bold", 10), bg="Yellow").grid(row=index + 2, column=11)
        
        

def database():
    name1 = Fullname.get()
    varr1=""
    varr2=""
    varr3=""
    varr4=""
    varr5=""
    varr6=""
    varr7=""
    varr8=""
    varr9=""
    varr10=""
    total =float(0)
    
    if var1.get() == 1:
        varr1="Burger"
        total+=1.07*(a1.get())

    if var2.get() == 1:
        varr2="Sandwich"
        total+=1.07*(a2.get())

    if var3.get() == 1:
        varr3="South Indian"
        total+=4.29*(a3.get())

    if var4.get() == 1:
        varr4="Punjabi"
        total+=3.22*(a4.get())

    if var5.get() == 1:
        varr5="Chinese"
        total+=4.29*(a5.get())

    if var6.get() == 1:
        varr6="Sizzler"
        total+=2.40*(a6.get())

    if var7.get() == 1:
        varr7="Gujrati Thali"
        total+=1.30*(a7.get())

    if var8.get() == 1:
        varr8="Pizza"
        total+=2.56*(a8.get())

    if var9.get() == 1:
        varr9="Butter Milk"
        total+=0.20*(a9.get())

    if var10.get() == 1:
        varr10="Cold drinks"
        total+=0.20*(a10.get())
    
    conn = sqlite3.connect('Bill0.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS bill2 (Fullname TEXT, varr1 TEXT, varr2 TEXT, varr3 TEXT, varr4 TEXT, varr5 TEXT, varr6 TEXT, varr7 TEXT, varr8 TEXT, varr9 TEXT, varr10 TEXT, total TEXT)')
        cursor.execute('INSERT INTO bill2 (FullName, varr1, varr2, varr3, varr4, varr5, varr6, varr7, varr8, varr9, varr10, total) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(name1, varr1, varr2, varr3, varr4, varr5, varr6, varr7, varr8, varr9, varr10, total))
        conn.commit()

        Fullname.set("")
        
        messagebox.showinfo("Message...", "Record Added Successfully............")

    a1.set("")
    a2.set("")
    a3.set("")
    a4.set("")
    a5.set("")
    a6.set("")
    a7.set("")
    a8.set("")
    a9.set("")
    a10.set("")


        


def data():
    root1 = Tk()
    root1.geometry("800x800")
    root1.title("YOUR BILL")
    
    nm = Fullname.get()
    Label(root1, text = nm, font=("Bold", 10), fg="Blue").place(x=20, y=20)
   
    dy=70
    trs=0
    trs1=0
   
    if var1.get() == 1:
        Label(root1, text = "Burger", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$1.07", font=("bold", 12), fg="Green",).place(x=200, y=dy)
        Label(root1, text = a1.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=1.07*(a1.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30

        
    if var2.get() == 1:
        Label(root1, text = "Sandwich", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$1.07", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a2.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=1.07*(a2.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30
        
    if var3.get() == 1:        
        Label(root1, text = "South Indian", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$4.29", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a3.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=4.29*(a3.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30
        
    if var4.get() == 1:
        Label(root1, text = "Punjabi", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$3.22", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a4.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=3.22*(a4.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30

    if var5.get() == 1:
        Label(root1, text = "Chinese", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$4.29", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a5.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=4.29*(a5.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30

    if var6.get() == 1:
        Label(root1, text = "Sizzler", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$2.40", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a6.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=2.40*(a6.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30

    if var7.get() == 1:
        Label(root1, text = "Gujrati Thali", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$1.30", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a7.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=1.30*(a7.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30

    if var8.get() == 1:
        Label(root1, text = "Pizza", font=(15), fg="Green").place(x=50, y=dy)
        Label(root1, text = "$2.56", font=("bold", 12), fg="Green").place(x=200, y=dy)
        Label(root1, text = a8.get(), font=(10), fg="Green").place(x=260,y=dy)
        trs+=2.56*(a8.get())
        Label(root1, text = round(trs,2), font=(10), fg="Green").place(x=280, y=dy)
        dy+=30

    if var9.get() == 1:
        Label(root1, text = "Butter milk", font=(15), fg="maroon").place(x=50, y=dy)
        Label(root1, text = "$0.20", font=("bold", 12), fg="maroon").place(x=200, y=dy)
        Label(root1, text = a9.get(), font=(12), fg="maroon").place(x=260,y=dy)
        trs+=0.20*(a9.get())
        Label(root1, text = round(trs,2), font=(12), fg="maroon").place(x=280, y=dy)
        dy+=30

    if var10.get() == 1:
        Label(root1, text = "Cold drinks", font=(15), fg="maroon").place(x=50, y=dy)
        Label(root1, text = "$0.20", font=("bold", 12), fg="maroon").place(x=200, y=dy)
        Label(root1, text = a10.get(), font=(10), fg="maroon").place(x=260,y=dy)
        trs+=0.20*(a10.get())
        Label(root1, text = round(trs,2), font=(10), fg="maroon").place(x=280, y=dy)
        dy+=30

    Label(root1, text = "__________________________________________________").place(x=30,y=1.2*dy)
    Label(root1, text = "Total", font =(15)).place(x=50, y=1.5*dy)
    Label(root1, text = round(trs,2), font=(12)).place(x=200, y=1.5*dy)


   

    


root = Tk()
root.geometry("800x800")
root.title("DELICIOUS FOOD MENU")

Fullname = StringVar()
a1 = IntVar()
a2 = IntVar()
a3 = IntVar()
a4 = IntVar()
a5 = IntVar()
a6 = IntVar()
a7 = IntVar()
a8 = IntVar()
a9 = IntVar()
a10 = IntVar()

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
var11 = IntVar()

a1.set("")
a2.set("")
a3.set("")
a4.set("")
a5.set("")
a6.set("")
a7.set("")
a8.set("")
a9.set("")
a10.set("")




Label(root, text = "DILICIOUS FOOOD", font=("bold", 20), fg="Blue").place(x=200,y=10)

Label(root, text = "Name:", font=("bold",15)).place(x=20,y=60)
label=Entry(root, textvar = Fullname, width = 70).place(x=110,y=65)

lbl1=Checkbutton(root, text = "Burger", font=("bold",15), fg="Green", variable = var1).place(x=50, y=100)
Label(root, text = "$1.07", font=("bold", 12), fg="Green",).place(x=200, y=100)
Entry(root, textvar=a1, width = 5).place(x=250,y=100)

lbl2=Checkbutton(root, text = "Sandwich", font=("bold",15), fg="Green", variable = var2).place(x=50, y=150)
Label(root, text = "$1.07", font=("bold", 12), fg="Green").place(x=200, y=150)
Entry(root, textvar=a2, width = 5).place(x=250,y=150)

lbl3=Checkbutton(root, text = "South Indian", font=("bold",15), fg="Green", variable = var3).place(x=50, y=200)
Label(root, text = "$4.29", font=("bold", 12), fg="Green").place(x=200, y=200)
l1=Entry(root, textvar=a3, width = 5).place(x=250,y=200)

lbl4=Checkbutton(root, text = "Punjabi", font=("bold",15), fg="Green",  variable = var4 ).place(x=50, y=250)
Label(root, text = "$3.22", font=("bold", 12), fg="Green").place(x=200, y=250)
l1=Entry(root, textvar=a4, width = 5).place(x=250,y=250)

lbl5=Checkbutton(root, text = "Chinese", font=("bold",15), fg="Green",  variable = var5).place(x=50, y=300)
Label(root, text = "$4.29", font=("bold", 12), fg="Green").place(x=200, y=300)
l1=Entry(root, textvar=a5, width = 5).place(x=250,y=300)

lbl6=Checkbutton(root, text = "Sizzler", font=("bold",15), fg="Green",  variable = var6).place(x=50, y=350)
Label(root, text = "$2.40", font=("bold", 12), fg="Green").place(x=200, y=350)
l1=Entry(root, textvar=a6, width = 5).place(x=250,y=350)

lbl7=Checkbutton(root, text = "Gujrati Thali", font=("bold",15), fg="Green",  variable = var7).place(x=50, y=400)
Label(root, text = "$1.30", font=("bold", 12), fg="Green").place(x=200, y=400)
l1=Entry(root, textvar=a7, width = 5).place(x=250,y=400)

lbl8=Checkbutton(root, text = "Pizza", font=("bold",15), fg="Green",  variable = var8).place(x=50, y=450)
Label(root, text = "$2.56", font=("bold", 12), fg="Green").place(x=200, y=450)
l1=Entry(root, textvar=a8, width = 5).place(x=250,y=450)

lbl9=Checkbutton(root, text = "Butter milk", font=("bold",15), fg="dark red",  variable = var9).place(x=350, y=150)
Label(root, text = "$0.20", font=("bold", 12), fg="maroon").place(x=500, y=150)
l1=Entry(root, textvar=a9, width = 5).place(x=550,y=150)

lbl10=Checkbutton(root, text = "Cold Drinks", font=("bold",15), fg="dark red",  variable = var10).place(x=350, y=100)
Label(root, text = "$0.20", font=("bold", 12), fg="maroon").place(x=500, y=100)
l1=Entry(root, textvar=a10, width = 5).place(x=550,y=100)

Button(root, text = "OK", font=("bold",17), fg= "white",bg="Maroon", command = data ).place(x=100, y=600)
Button(root, text = "ADD", font=("bold",17), fg= "white",bg="Maroon", command = database ).place(x=200, y=600)
Button(root, text = "VIEW ", font=("bold",17), fg= "white",bg="Maroon", command = showre ).place(x=300, y=600)


root.mainloop()
 
