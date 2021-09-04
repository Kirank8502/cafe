from tkinter import*
import random
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
import mysql.connector

root=Tk()
root.geometry("1548x800+0+0")
root.title(" Cafe")



Tops =Frame(root,width=1548,height=100,bd=12,relief="raise",bg="cornflower blue")
Tops.pack(side=TOP)

lbltitle=Label(Tops,font=("times new roman",60,"bold"),text="\t Divan Cafe\t",bg='cornflower blue')
lbltitle.grid(row=0,column=0)

bottom_mainframe=Frame(root,width=1548,height=800,bd=12,relief="raise",bg="cornflower blue")
bottom_mainframe.pack(side=BOTTOM)


f1=Frame(bottom_mainframe,width=5,height=800,bd=12,relief="raise",bg="cornflower blue")
f1.pack(side=LEFT)


f2=Frame(bottom_mainframe,width=516,height=800,bd=12,relief="raise",bg="cornflower blue")
f2.pack(side=LEFT)

f2top =Frame(f2,width=516,height=450,bd=4,relief="raise",bg="cornflower blue")
f2top.pack(side=TOP)
f2bottom =Frame(f2,width=516,height=350,bd=4,relief="raise",bg="cornflower blue")
f2bottom.pack(side=BOTTOM)

f3=Frame(bottom_mainframe,width=516,height=800,bd=12,relief="raise",bg="cornflower blue")
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varfries=StringVar()
varsalad=StringVar()
varburger=StringVar()
varsandwich=StringVar()
varpasta=StringVar()
varpizza=StringVar()
varpunjabi=StringVar()
vargujarati=StringVar()


varbrowni=StringVar()
varpancake=StringVar()
varwaffle=StringVar()
varchocalatemuffin=StringVar()
varpastry=StringVar()

vartea=StringVar()
varcoffee=StringVar()
varjuice=StringVar()
varcola=StringVar()
varbuttermilk=StringVar()


varvanillacone=StringVar()
varchoclate=StringVar()
varstrawbery=StringVar()

vartax=StringVar()
varvat=StringVar()
vartotal=StringVar()
varsubtotal=StringVar()

varfries.set("0")
varsalad.set("0")
varburger.set("0")
varsandwich.set("0")
varpasta.set("0")
varpizza.set("0")
varpunjabi.set("0")
vargujarati.set("0")

varbrowni.set("0")
varpancake.set("0")
varwaffle.set("0")
varchocalatemuffin.set("0")
varpastry.set("0")

vartea.set("0")
varcoffee.set("0")
varjuice.set("0")
varcola.set("0")
varbuttermilk.set("0")
varvanillacone.set("0")
varchoclate.set("0")
varstrawbery.set("0")
    
vartax.set("0")
varvat.set("")
vartotal.set("0")
varsubtotal.set("0")

def iexit():
    qexit=messagebox.askyesno("Quit system","Do you want to quit?")
    if qexit> 0:
        root.destroy()
        return

def reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    varfries.set("0")
    varsalad.set("0")
    varburger.set("0")
    varsandwich.set("0")
    varpasta.set("0")
    varpizza.set("0")
    varpunjabi.set("0")
    vargujarati.set("0")

    varbrowni.set("0")
    varpancake.set("0")
    varwaffle.set("0")
    varchocalatemuffin.set("0")
    varpastry.set("0")

    vartea.set("0")
    varcoffee.set("0")
    varjuice.set("0")
    varcola.set("0")
    varbuttermilk.set("0")
    varvanillacone.set("0")
    varchoclate.set("0")
    varstrawbery.set("0")
    
    vartax.set("0")
    varvat.set("")
    
    varsubtotal.set("0")
    vartotal.set("0")
    
    txtfries.configure(state=DISABLED)
    txtsalad.configure(state=DISABLED)
    txtburger.configure(state=DISABLED)
    txtsandwich.configure(state=DISABLED)
    txtpasta.configure(state=DISABLED)
    txtpizza.configure(state=DISABLED)
    txtpunjabi_thali.configure(state=DISABLED)
    txtgujarati_thali.configure(state=DISABLED)
    txtbrowni.configure(state=DISABLED)
    txtpancake.configure(state=DISABLED)
    txtwaffle.configure(state=DISABLED)
    txtchoclate_muffin.configure(state=DISABLED)
    txtpastry.configure(state=DISABLED)
    txt_tea.configure(state=DISABLED)
    txtcoffee.configure(state=DISABLED)
    txtjuice.configure(state=DISABLED)
    txtbutter_milk.configure(state=DISABLED)
    txtvanillacone.configure(state=DISABLED)
    txtchoclate.configure(state=DISABLED)
    txtstrawberry.configure(state=DISABLED)
    txtpayment.configure(state=DISABLED)

    txttax.configure(state=DISABLED)
    txtsubtotal.configure(state=DISABLED)
    txttotal.configure(state=DISABLED)

############======================####################
def chkfries():
    if (var1.get()==1):
        txtfries.configure(state=NORMAL)
        varfries.set("")
    elif(var1.get()==0):
        txtfries.configure(state=DISABLED)
        varfries.set("0")

def chksalad():
    if (var2.get()==1):
        txtsalad.configure(state=NORMAL)
        varsalad.set("")
    elif (var2.get()==0):
        txtsalad.configure(state=DISABLED)
        varsalad.set("0")

def chkburger():
    if (var3.get()==1):
        txtburger.configure(state=NORMAL)
        varburger.set("")
    elif (var3.get()==0):
        txtburger.configure(state=DISABLED)
        varburger.set("0")

def chksandwich():
    if (var4.get()==1):
        txtsandwich.configure(state=NORMAL)
        varsandwich.set("")
    elif (var4.get()==0):
        txtsandwich.configure(state=DISABLED)
        varsandwich.set("0")

def chkpasta():
    if (var5.get()==1):
        txtpasta.configure(state=NORMAL)
        varpasta.set("")
    elif (var5.get()==0):
        txtpasta.configure(state=DISABLED)
        varpasta.set("0")

def chkpizza():
    if (var6.get()==1):
        txtpizza.configure(state=NORMAL)
        varpizza.set("")
    elif (var6.get()==0):
        txtpizza.configure(state=DISABLED)
        varpizza.set("0")

def chkpunjabi():
    if (var7.get()==1):
        txtpunjabi_thali.configure(state=NORMAL)
        varpunjabi.set("")
    elif (var7.get()==0):
        txtpunjabi_thali.configure(state=DISABLED)
        varpunjabi.set("0")

def chkgujarati():
    if (var8.get()==1):
        txtgujarati_thali.configure(state=NORMAL)
        vargujarati.set("")
    elif (var8.get()==0):
        txtgujarati_thali.configure(state=DISABLED)
        vargujarati.set("0")

def chkbrowni():
    if (var9.get()==1):
        txtbrowni.configure(state=NORMAL)
        varbrowni.set("")
    elif (var9.get()==0):
        txtbrowni.configure(state=DISABLED)
        varbrowni.set("0")

def chkpancake():
    if (var10.get()==1):
        txtpancake.configure(state=NORMAL)
        varpancake.set("")
    elif (var10.get()==0):
        txtpancake.configure(state=DISABLED)
        varpancake.set("0")

def chkwaffle():
    if (var11.get()==1):
        txtwaffle.configure(state=NORMAL)
        varwaffle.set("")
    elif (var11.get()==0):
        txtwaffle.configure(state=DISABLED)
        varwaffle.set("0")

def chkmuffin():
    if (var12.get()==1):
        txtchoclate_muffin.configure(state=NORMAL)
        varchocalatemuffin.set("")
    elif (var2.get()==0):
        txtchoclate_muffin.configure(state=DISABLED)
        varchocalatemuffin.set("0")

def chkpastry():
    if (var13.get()==1):
        txtpastry.configure(state=NORMAL)
        varpastry.set("")
    elif (var13.get()==0):
        txtpastry.configure(state=DISABLED)
        varpastry.set("0")

def chktea():
    if (var14.get()==1):
        txt_tea.configure(state=NORMAL)
        vartea.set("")
    elif (var14.get()==0):
        txt_tea.configure(state=DISABLED)
        vartea.set("0")

def chkcoffee():
    if (var15.get()==1):
        txtcoffee.configure(state=NORMAL)
        varcoffee.set("")
    elif (var15.get()==0):
        txtcoffee.configure(state=DISABLED)
        varcoffee.set("0")

def chkjuice():
    if (var16.get()==1):
        txtjuice.configure(state=NORMAL)
        varjuice.set("")
    elif (var16.get()==0):
        txtjuice.configure(state=DISABLED)
        varjuice.set("0")

def chkbuttermilk():
    if (var17.get()==1):
        txtbutter_milk.configure(state=NORMAL)
        varbuttermilk.set("")
    elif (var17.get()==0):
        txtbutter_milk.configure(state=DISABLED)
        varbuttermilk.set("0")

def chkcola():
    if (var18.get()==1):
        txtcola.configure(state=NORMAL)
        varcola.set("")
    elif (var18.get()==0):
        txtcola.configure(state=DISABLED)
        varcola.set("0")

def chkvanillacone():
    if (var19.get()==1):
        txtvanillacone.configure(state=NORMAL)
        varvanillacone.set("")
    elif (var19.get()==0):
        txtvanillacone.configure(state=DISABLED)
        varvanillacone.set("0")

def chkchoclate():
    if (var20.get()==1):
        txtchoclate.configure(state=NORMAL)
        varchoclate.set("")
    elif (var20.get()==0):
        txtchoclate.configure(state=DISABLED)
        varchoclate.set("0")

def chkstrawberry():
    if (var21.get()==1):
        txtstrawberry.configure(state=NORMAL)
        varstrawbery.set("")
    elif (var21.get()==0):
        txtstrawberry.configure(state=DISABLED)
        varstrawbery.set("0")

def costofmeal():
    
    
    meal1=float(varfries.get())
    meal2=float(varsalad.get())
    meal3=float(varburger.get())
    meal4=float(varsandwich.get())
    meal5=float(varpasta.get())
    meal6=float(varpizza.get())
    meal7=float(varpunjabi.get())
    meal8=float(vargujarati.get())
    meal9=float(varbrowni.get())
    meal10=float(varpancake.get())
    meal11=float(varwaffle.get())
    meal12=float(varchocalatemuffin.get())
    meal13=float(varpastry.get())
    meal14=float(vartea.get())
    meal15=float(varcoffee.get())
    meal16=float(varjuice.get())
    meal17=float(varbuttermilk.get())
    meal18=float(varcola.get())
    meal19=float(varvanillacone.get())
    meal20=float(varchoclate.get())
    meal21=float(varstrawbery.get())

    itotal1=((meal1 * 100)+(meal2 * 150)+(meal3 *90)+ (meal4*170) + (meal5 *250 )+(meal6 *200)+(meal7 * 250)+(meal8*300))
    itotal2= ((meal9 *200 )+(meal10 * 150)+(meal11 *160 )+(meal12 * 200)+(meal13 *100 ))
    itotal3=((meal14 *30)+(meal15 *70 )+(meal16 *100 )+(meal17 *50)+(meal18 *50)+(meal19 *110 )+(meal20 * 100)+(meal21 *100 ))
    icost=(itotal1+itotal2+itotal3)
    itax=(icost * 5)/100
    vartax.set(itax)
    varsubtotal.set(icost)
    vartotal.set(icost+itax)

    try:
        conn=mysql.connector.connect(host='localhost',username='root',password="",port=3306,database='feedback')
        cur=conn.cursor()

        cur.execute("insert into bill (fries,salad,burger,sandwich,pasta,pizza,punjabi,gujarati,browni,pancake,waffle,chocalatemuffin,pastry,tea,coffee,juice,buttermilk,cola,vanillacone,choclate,strawbery,total) values(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)",(
                                                        txtfries.get(),
                                                        txtsalad.get(),
                                                        txtburger.get(),
                                                        txtsandwich.get(),
                                                        txtpasta.get(),
                                                        txtpizza.get(),
                                                        txtpunjabi_thali.get(),
                                                        txtgujarati_thali.get(),

                                                        txtbrowni.get(),
                                                        txtpancake.get(),
                                                        txtwaffle.get(),
                                                        txtchoclate_muffin.get(),
                                                        txtpastry.get(),

                                                        txt_tea.get(),
                                                        txtcoffee.get(),
                                                        txtjuice.get(),
                                                        txtcola.get(),
                                                        txtbutter_milk.get(),
                                                        txtvanillacone.get(),
                                                        txtchoclate.get(),
                                                        txtstrawberry.get(),
                                                        txttotal.get()

                                                        ))
                                            
        conn.commit()
        
    except Exception as es:
        messagebox.showerror("Error",f"error due to: {str(es)}")



#==============================frame1=====================================
lblmeal=Label(f1, font=("arial",18,"bold"), text="\tDIVAN CAFE MEAL\t",bg="cornflower blue")
lblmeal.grid(row=0, column=0)

fries = Checkbutton(f1, text="Fries\t\t\tRs.100",variable=var1,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),bg="cornflower blue",command=chkfries).grid(row=1,column=0,sticky=W)
txtfries=Entry(f1,font=("times new roman",18,"bold"),textvariable=varfries, width=6,justify="right",state=DISABLED)
txtfries.grid(row=1,column=1)

salad = Checkbutton(f1, text="salad\t\t\tRs.150",variable=var2,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chksalad,bg="cornflower blue").grid(row=2,column=0,sticky=W)
txtsalad=Entry(f1,font=("times new roman",18,"bold"),textvariable=varsalad, width=6,justify="right",state=DISABLED)
txtsalad.grid(row=2,column=1)

burger = Checkbutton(f1, text="Burger\t\t\tRs.90",variable=var3,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkburger,bg="cornflower blue").grid(row=3,column=0,sticky=W)
txtburger=Entry(f1,font=("times new roman",18,"bold"),textvariable=varburger, width=6,justify="right",state=DISABLED)
txtburger.grid(row=3,column=1)

sandwich = Checkbutton(f1, text="Sandwich\t\tRs.170",variable=var4,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chksandwich,bg="cornflower blue").grid(row=4,column=0,sticky=W)
txtsandwich=Entry(f1,font=("times new roman",18,"bold"),textvariable=varsandwich, width=6,justify="right",state=DISABLED)
txtsandwich.grid(row=4,column=1)

Pasta = Checkbutton(f1, text="Pasta\t\t\tRs.250",variable=var5,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkpasta,bg="cornflower blue").grid(row=5,column=0,sticky=W)
txtpasta=Entry(f1,font=("times new roman",18,"bold"),textvariable=varpasta, width=6,justify="right",state=DISABLED)
txtpasta.grid(row=5,column=1)

pizza = Checkbutton(f1, text="Pizza\t\t\tRs.200",variable=var6,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkpizza,bg="cornflower blue").grid(row=6,column=0,sticky=W)
txtpizza=Entry(f1,font=("times new roman",18,"bold"),textvariable=varpizza, width=6,justify="right",state=DISABLED)
txtpizza.grid(row=6,column=1)

lblthali=Label(f1,font=("times new roman",20,"bold"),text="\nThali\n",bg="cornflower blue")
lblthali.grid(row=7,column=0)

punjabi_thali = Checkbutton(f1, text="Punjabi hali\t\tRs.250",bg="cornflower blue",variable=var7,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkpunjabi).grid(row=8,column=0,sticky=W)
txtpunjabi_thali=Entry(f1,font=("times new roman",18,"bold"),textvariable=varpunjabi, width=6,justify="right",state=DISABLED)
txtpunjabi_thali.grid(row=8,column=1)

gujarati_thali = Checkbutton(f1,text="Gujarati Thali\t\tRs.300",variable=var8,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkgujarati,bg="cornflower blue").grid(row=9,column=0,sticky=W)
txtgujarati_thali=Entry(f1,font=("times new roman",18,"bold"),textvariable=vargujarati,width=6,justify="right",state=DISABLED)
txtgujarati_thali.grid(row=9,column=1)



lblspace=Label(f1,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",bg="cornflower blue")
lblspace.grid(row=10,column=0)


#=======================frame2===============

lblmeal=Label(f2top, font=("times new roman",18,"bold"), text="\t\tDesserts\t\t",bg="cornflower blue")
lblmeal.grid(row=0, column=0)

browni = Checkbutton(f2top, text="Browni\t\t\tRs.200",variable=var9,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkbrowni,bg="cornflower blue").grid(row=1,column=0,sticky=W)
txtbrowni=Entry(f2top,font=("times new roman",18,"bold"),textvariable=varbrowni, width=6,justify="left",state=DISABLED)
txtbrowni.grid(row=1,column=1)

pancake = Checkbutton(f2top, text="Pancake\t\t\tRs.150",variable=var10,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkpancake,bg="cornflower blue").grid(row=2,column=0,sticky=W)
txtpancake=Entry(f2top,font=("times new roman",18,"bold"),textvariable=varpancake, width=6,justify="left",state=DISABLED)
txtpancake.grid(row=2,column=1)

waffle = Checkbutton(f2top, text="Waffle\t\t\tRs.160",variable=var11,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkwaffle,bg="cornflower blue").grid(row=3,column=0,sticky=W)
txtwaffle=Entry(f2top,font=("times new roman",18,"bold"),textvariable=varwaffle, width=6,justify="left",state=DISABLED)
txtwaffle.grid(row=3,column=1)

Choclate_muffin= Checkbutton(f2top, text="Choclate Muffin\t\tRs.200",variable=var12,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkmuffin,bg="cornflower blue").grid(row=4,column=0,sticky=W)
txtchoclate_muffin=Entry(f2top,font=("times new roman",18,"bold"),textvariable=varchocalatemuffin, width=6,justify="left",state=DISABLED)
txtchoclate_muffin.grid(row=4,column=1)

pastry= Checkbutton(f2top, text="Pastry\t\t\tRs.100",variable=var13,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkpastry,bg="cornflower blue").grid(row=5,column=0,sticky=W)
txtpastry=Entry(f2top,font=("times new roman",18,"bold"),textvariable=varpastry, width=6,justify="left",state=DISABLED)
txtpastry.grid(row=5,column=1)

lblspace=Label(f2top,text="\n\n\n\n\n",bg="cornflower blue")
lblspace.grid(row=6,column=0)



#============================frame3==========================
lblmeal=Label(f3, font=("arial",18,"bold"), text="\tDivan Drinks\t",bg="cornflower blue")
lblmeal.grid(row=0, column=0)

tea = Checkbutton(f3, text="Tea\t\t\tRs.30",variable=var14,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chktea,bg="cornflower blue").grid(row=1,column=0,sticky=W)
txt_tea=Entry(f3,font=("times new roman",18,"bold"),textvariable=vartea,justify="left", width=6,state=DISABLED)
txt_tea.grid(row=1,column=1)

coffee = Checkbutton(f3, text="coffee\t\t\tRs.70",variable=var15,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkcoffee,bg="cornflower blue").grid(row=2,column=0,sticky=W)
txtcoffee=Entry(f3,font=("times new roman",18,"bold"),textvariable=varcoffee, width=6,justify="left",state=DISABLED)
txtcoffee.grid(row=2,column=1)

juice = Checkbutton(f3, text="Juice\t\t\tRs.100",variable=var16,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkjuice,bg="cornflower blue").grid(row=3,column=0,sticky=W)
txtjuice=Entry(f3,font=("times new roman",18,"bold"),textvariable=varjuice, width=6,justify="left",state=DISABLED)
txtjuice.grid(row=3,column=1)

butter_milk= Checkbutton(f3, text="Butter Milk\t\tRs.50",variable=var17,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkbuttermilk,bg="cornflower blue").grid(row=4,column=0,sticky=W)
txtbutter_milk=Entry(f3,font=("times new roman",18,"bold"),textvariable=varbuttermilk, width=6,justify="left",state=DISABLED)
txtbutter_milk.grid(row=4,column=1)

cola= Checkbutton(f3, text="Cola\t\t\tRs.50",variable=var18,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkcola,bg="cornflower blue").grid(row=5,column=0,sticky=W)
txtcola=Entry(f3,font=("times new roman",18,"bold"),textvariable=varcola, width=6,justify="left",state=DISABLED)
txtcola.grid(row=5,column=1)

lblshakes=Label(f3,font=("times new roman",20,"bold"),text="Shakes",bg="cornflower blue")
lblshakes.grid(row=6,column=0)

vanillacone= Checkbutton(f3, text="Vanilla cone\t\tRs.110",variable=var19,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkvanillacone,bg="cornflower blue").grid(row=7,column=0,sticky=W)
txtvanillacone=Entry(f3,font=("times new roman",18,"bold"),textvariable=varvanillacone, width=6,justify="left",state=DISABLED)
txtvanillacone.grid(row=7,column=1)

choclate= Checkbutton(f3, text="Choclate Milkshake\tRs.100",command=chkchoclate,variable=var20,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),bg="cornflower blue").grid(row=8,column=0,sticky=W)
txtchoclate=Entry(f3,font=("times new roman",18,"bold"),textvariable=varchoclate, width=6,justify="left",state=DISABLED)
txtchoclate.grid(row=8,column=1)

strawberry= Checkbutton(f3, text="strawberry Milkshake\tRs.100",variable=var21,onvalue=1,offvalue=0,font=("times new roman",18,"bold"),command=chkstrawberry,bg="cornflower blue").grid(row=9,column=0,sticky=W)
txtstrawberry=Entry(f3,font=("times new roman",18,"bold"),textvariable=varstrawbery, width=6,justify="left",state=DISABLED)
txtstrawberry.grid(row=9,column=1)

def feedback():
    root.destroy()
    import feedback


lblspace=Label(f3,text="\n\n\n\n\n\n\n",bg="cornflower blue")
lblspace.grid(row=10,column=0)


btnfeed=Button(f3,command=feedback,padx=16,pady=1,bd=4,fg="black",font=("times new roman",16,"bold"),width=5,text="Feedback",bg="cornflower blue")
btnfeed.grid(row=11,column=0)

lblspace=Label(f3,text="\n\n\n\n\n\n",bg="cornflower blue")
lblspace.grid(row=12,column=0)



#=======================frame2 bottom==================
lblpaymentmethod=Label(f2bottom,font=("times new roman",14,"bold"),text="Payment Method",bg="cornflower blue",bd=10,width=16,anchor='w')
lblpaymentmethod.grid(row=0,column=0)



cmbpaymentmethod=ttk.Combobox(f2bottom,textvariable=var22,state="readonly",font=("times new roman",10,"bold"),width=20)
cmbpaymentmethod["value"]=("cash","credit card","debit card","Paytm")
cmbpaymentmethod.current(0)
cmbpaymentmethod.grid(row=1,column=0)

lbltax =Label(f2bottom,font=("times new roman",14,"bold"),bg="cornflower blue",text="Tax",bd=10,anchor="w")
lbltax.grid(row=1,column=1)
txttax=Entry(f2bottom,font=("times new roman",18,"bold"),bg="cornflower blue",textvariable=vartax,width=6,justify="left",state=DISABLED)
txttax.grid(row=1,column=2)



lblsubtotal=Label(f2bottom,font=("times new roman",14,"bold"),bg="cornflower blue",text="sub total",bd=10,width=8,anchor="w")
lblsubtotal.grid(row=2,column=1)
txtsubtotal=Entry(f2bottom,font=("times new roman",18,"bold"),bg="cornflower blue",textvariable=varsubtotal,width=6,justify="left",state=DISABLED)
txtsubtotal.grid(row=2,column=2)

lbltotal=Label(f2bottom,font=("times new roman",14,"bold"),bg="cornflower blue",text="Total",bd=10,width=8,anchor="w")
lbltotal.grid(row=3,column=1)
txttotal=Entry(f2bottom,font=("times new roman",18,"bold"),textvariable=vartotal,bg="cornflower blue",width=6,justify="left",state=DISABLED)
txttotal.grid(row=3,column=2)


#========================frame button============================
btntotal=Button(f2bottom,command=costofmeal,padx=16,pady=1,bd=4,fg="black",bg="cornflower blue",font=("times new roman",16,"bold"),width=5,text="Total").grid(row=4,column=0)

btnreset=Button(f2bottom,command=reset,padx=16,pady=1,bd=4,fg="black",bg="cornflower blue",font=("times new roman",16,"bold"),width=5,text="Reset").grid(row=4,column=1)

btnexit=Button(f2bottom,command=iexit,padx=16,pady=1,bd=4,fg="black",bg="cornflower blue",font=("times new roman",16,"bold"),width=5,text="Exit").grid(row=4,column=2)

lblspace=Label(f2bottom,text="\n\n\n\n\n\n\n\n",bg="cornflower blue")
lblspace.grid(row=5,column=0)

root.mainloop()
