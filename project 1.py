from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
import mysql.connector as mys
user1=""
i_d1=""
seluser=""
final=0
seatmoney=0
snckmoney=0
nseat=0
pop=0
nacho=0
pepsi=0
burger=0
hotdog=0
ver=0
end=0
n=[]
seataqua=[]
seatwonka=[]
seatdunki=[]
seatanimal=[]
seatneru=[]
seatraastha=[]


def MENUSCREEN():
        
    root = tk.Tk() 
    root.geometry("1000x800")
    root.title(" KALAVAMPARA THEATER")
    img = ImageTk.PhotoImage(Image.open("theatre.jpg"))
    label=Label(root, image = img)
    label.pack()
    root.configure(bg='light green')
    lblmenu = tk.Label(root, text ="KALAVAMPARA THEATRE", fg= 'white', bg= 'black',font=('MV Boli',40,'bold'))
    lblmenu.place(x = 180, y = 10)
    lbllan = tk.Label(root, text ="Select your language preference:", bg= 'white',font=('MV Boli',20, "underline"))
    lbllan.place(x = 320, y = 200)
    
    def admin():
        def funclear():
                txtUser.delete(0,END)
                txtpass.delete(0,END)
                txtUser.focus()
        def funlogin():
                if txtUser.get()=="adis" and txtpass.get()=="54321":
                    login.destroy()
                    root.destroy()                               
                    def movie():
                        mov = tk.Tk() 
                        mov.geometry("500x600")
                        mov.title("ADMIN MOVIES")
                        mov.configure(bg='dark red')
                        
                        def details():
                            userwin=tk.Tk()
                            userwin.geometry("300x300")
                            userwin.title("User Details")
                            userwin.configure(bg='black')
                            global seluser
                            lbluser = tk.Label(userwin, text ="Username -",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                            lbluser.place(x = 30, y = 20)
                            lblseluser = tk.Label(userwin, text =seluser,fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                            lblseluser.place(x = 100, y = 20)
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from customer where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs=mycur.fetchone()
                            lblpass = tk.Label(userwin, text ="Password -",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                            lblpass.place(x = 30, y = 40)
                            lbluserpass = tk.Label(userwin, text =rs[2],fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                            lbluserpass.place(x = 100, y = 40)
                            lblid = tk.Label(userwin, text ="Account id -",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                            lblid.place(x = 30, y = 60)
                            lblaccid = tk.Label(userwin, text =rs[1],fg="white",bg='black',font=("Times New Roman Bold", 7) ) 
                            lblaccid.place(x = 100, y = 60)
                            lblmovie = tk.Label(userwin, text ="Movies booked -",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                            lblmovie.place(x = 30, y = 80)
                            
                            z=0
                            
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from wonka where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs1=mycur.fetchone()
                            if rs1!=None:
                                lblwonka = tk.Label(userwin, text ="Wonka",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                                lblwonka.place(x = 130, y = 80+z)
                                z+=20
                                
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from dunki where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs2=mycur.fetchone()
                            if rs2!=None:
                                lbldunki = tk.Label(userwin, text ="Dunki",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                                lbldunki.place(x = 130, y = 80+z)
                                z+=20
                                
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from aquaman where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs3=mycur.fetchone()
                            if rs3!=None:
                                lblaqua = tk.Label(userwin, text ="Aquaman",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                                lblaqua.place(x = 130, y = 80+z)
                                z+=20
                                
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from animal where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs4=mycur.fetchone()
                            if rs4!=None:
                                lblanimal = tk.Label(userwin, text ="Animal",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                                lblanimal.place(x = 130, y = 80+z)
                                z+=20
                                
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from neru where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs5=mycur.fetchone()
                            if rs5!=None:
                                lblneru = tk.Label(userwin, text ="Neru",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                                lblneru.place(x = 130, y = 80+z)
                                z+=20
                                
                            myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                            mycur=myconn.cursor()
                            query="select * from raastha where c_name='{}'".format(seluser)
                            mycur.execute(query)
                            rs6=mycur.fetchone()
                            if rs6!=None:
                                lblraastha = tk.Label(userwin, text ="Raastha",fg="white",bg='black',font=("Times New Roman Bold", 10) ) 
                                lblraastha.place(x = 130, y = 80+z)
                                z+=20
            
                            
                        def wonka():
                            wonka = tk.Tk() 
                            wonka.geometry("940x500")
                            wonka.title("WONKA MOVIE")
                            
                            table = ttk.Treeview(wonka, columns = ('c_name', 'acc_id','snacks', 'number of seats','seats','cost'), show = 'headings')
                            table.heading('c_name', text = 'Name')
                            table.heading('acc_id', text = 'Account id')
                            table.heading('snacks', text = 'Snacks')
                            table.heading('number of seats', text = 'Number of Seats')
                            table.heading('seats', text = 'Seats')
                            table.heading('cost', text = 'Cost')                          
                            table.place(x=20,y=50)
                            
                            table.column('c_name', width=100)
                            table.column('acc_id', width=300)
                            table.column('snacks', width=200)
                            table.column('number of seats', width=100)
                            table.column('seats', width=100)
                            table.column('cost', width=100)
                            
                            try:
                                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                mycur=myconn.cursor()
                                query="select * from wonka"
                                mycur.execute(query)
                                rs=mycur.fetchall()
                                
                                def insert():
                                    n=len(rs)
                                    for i in range(0,n):
                                        table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                def search():
                                    x=srchbar.get()
                                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                    mycur=myconn.cursor()
                                    query="select * from wonka where c_name='{}'".format(x)
                                    mycur.execute(query)
                                    rs=mycur.fetchall()
                                    if rs!=None:                                        
                                        for item in table.get_children():
                                            table.delete(item)
                                        n=len(rs)
                                        for i in range(0,n):
                                            table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                    else:
                                        messagebox.showinfo("Search Failed", "The entered user has not be found")
                                def exit():
                                    for item in table.get_children():
                                            table.delete(item)
                                    srchbar.delete(0,END)
                                    insert()
                                insert()
                                                               
                                srchbar = tk.Entry(wonka, width = 800,fg="blue",font=("Times New Roman Bold", 10)) 
                                srchbar.place(x = 20, y = 20, width = 800)
                                btsrch= tk.Button(wonka, text ="Search",fg ='black', bg='blue', font=("Times New Roman Bold", 10),command=search)
                                btsrch.place(x = 820, y = 20, height = 20, width = 50)
                                btexit= tk.Button(wonka, text ="Exit Search",fg ='black', bg='red', font=("Times New Roman Bold", 10),command=exit)
                                btexit.place(x = 873, y = 20, height = 20, width = 66) 
                                
                                def on_select(event):
                                    global seluser
                                    seluser=""
                                    sel = table.selection()[0]
                                    selitems = table.item(sel)
                                    sellist = selitems['values']
                                    seluser+=sellist[0]
                                    details()
                                                           
                                table.bind('<<TreeviewSelect>>', on_select)
                            except Exception as e:
                                print(e)
                        
                        def aqua():
                            aqua = tk.Tk() 
                            aqua.geometry("940x500")
                            aqua.title("AQUA MOVIE")
                            
                            table = ttk.Treeview(aqua, columns = ('c_name', 'acc_id','snacks', 'number of seats','seats','cost'), show = 'headings')
                            table.heading('c_name', text = 'Name')
                            table.heading('acc_id', text = 'Account id')
                            table.heading('snacks', text = 'Snacks')
                            table.heading('number of seats', text = 'Number of Seats')
                            table.heading('seats', text = 'Seats')
                            table.heading('cost', text = 'Cost')
                            table.place(x=20,y=50)
                            
                            table.column('c_name', width=100)
                            table.column('acc_id', width=300)
                            table.column('snacks', width=200)
                            table.column('number of seats', width=100)
                            table.column('seats', width=100)
                            table.column('cost', width=100)
                            
                            try:
                                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                mycur=myconn.cursor()
                                query="select * from aquaman"
                                mycur.execute(query)
                                rs=mycur.fetchall()
                                
                                def insert():
                                    n=len(rs)
                                    for i in range(0,n):
                                        table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                def search():
                                    x=srchbar.get()
                                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                    mycur=myconn.cursor()
                                    query="select * from aquaman where c_name='{}'".format(x)
                                    mycur.execute(query)
                                    rs=mycur.fetchall()
                                    if rs!=None:                                        
                                        for item in table.get_children():
                                            table.delete(item)
                                        n=len(rs)
                                        for i in range(0,n):
                                            table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                    else:
                                        messagebox.showinfo("Search Failed", "The entered user has not be found")
                                def exit():
                                    for item in table.get_children():
                                            table.delete(item)
                                    srchbar.delete(0,END)
                                    insert()
                                insert()
                                                               
                                srchbar = tk.Entry(aqua, width = 800,fg="blue",font=("Times New Roman Bold", 10)) 
                                srchbar.place(x = 20, y = 20, width = 800)
                                btsrch= tk.Button(aqua, text ="Search",fg ='black', bg='blue', font=("Times New Roman Bold", 10),command=search)
                                btsrch.place(x = 820, y = 20, height = 20, width = 50)
                                btexit= tk.Button(aqua, text ="Exit Search",fg ='black', bg='red', font=("Times New Roman Bold", 10),command=exit)
                                btexit.place(x = 873, y = 20, height = 20, width = 66) 
                                
                                def on_select(event):
                                    global seluser
                                    seluser=""
                                    sel = table.selection()[0]
                                    selitems = table.item(sel)
                                    sellist = selitems['values']
                                    seluser+=sellist[0]
                                    details()
                                                           
                                table.bind('<<TreeviewSelect>>', on_select)
                            except Exception as e:
                                print(e)
                        
                        def dunki():
                            dunki = tk.Tk() 
                            dunki.geometry("940x500")
                            dunki.title("dunkiI MOVIE")
                            
                            table = ttk.Treeview(dunki, columns = ('c_name', 'acc_id','snacks', 'number of seats','seats','cost'), show = 'headings')
                            table.heading('c_name', text = 'Name')
                            table.heading('acc_id', text = 'Account id')
                            table.heading('snacks', text = 'Snacks')
                            table.heading('number of seats', text = 'Number of Seats')
                            table.heading('seats', text = 'Seats')
                            table.heading('cost', text = 'Cost')
                            #table.pack()
                            table.place(x=20,y=50)
                            
                            table.column('c_name', width=100)
                            table.column('acc_id', width=300)
                            table.column('snacks', width=200)
                            table.column('number of seats', width=100)
                            table.column('seats', width=100)
                            table.column('cost', width=100)
                            
                            try:
                                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                mycur=myconn.cursor()
                                query="select * from dunki"
                                mycur.execute(query)
                                rs=mycur.fetchall()
                                
                                def insert():
                                    n=len(rs)
                                    for i in range(0,n):
                                        table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                def search():
                                    x=srchbar.get()
                                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                    mycur=myconn.cursor()
                                    query="select * from dunki where c_name='{}'".format(x)
                                    mycur.execute(query)
                                    rs=mycur.fetchall()
                                    if rs!=None:                                        
                                        for item in table.get_children():
                                            table.delete(item)
                                        n=len(rs)
                                        for i in range(0,n):
                                            table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                    else:
                                        messagebox.showinfo("Search Failed", "The entered user has not be found")
                                def exit():
                                    for item in table.get_children():
                                            table.delete(item)
                                    srchbar.delete(0,END)
                                    insert()
                                insert()
                                                               
                                srchbar = tk.Entry(dunki, width = 800,fg="blue",font=("Times New Roman Bold", 10)) 
                                srchbar.place(x = 20, y = 20, width = 800)
                                btsrch= tk.Button(dunki, text ="Search",fg ='black', bg='blue', font=("Times New Roman Bold", 10),command=search)
                                btsrch.place(x = 820, y = 20, height = 20, width = 50)
                                btexit= tk.Button(dunki, text ="Exit Search",fg ='black', bg='red', font=("Times New Roman Bold", 10),command=exit)
                                btexit.place(x = 873, y = 20, height = 20, width = 66) 
                                
                                def on_select(event):
                                    global seluser
                                    seluser=""
                                    sel = table.selection()[0]
                                    selitems = table.item(sel)
                                    sellist = selitems['values']
                                    seluser+=sellist[0]
                                    details()
                                                           
                                table.bind('<<TreeviewSelect>>', on_select)
                                
                            except Exception as e:
                                print(e)
                        
                        def animal():
                            animal = tk.Tk() 
                            animal.geometry("940x500")
                            animal.title("animalAL MOVIE")
                            
                            table = ttk.Treeview(animal, columns = ('c_name', 'acc_id','snacks', 'number of seats','seats','cost'), show = 'headings')
                            table.heading('c_name', text = 'Name')
                            table.heading('acc_id', text = 'Account id')
                            table.heading('snacks', text = 'Snacks')
                            table.heading('number of seats', text = 'Number of Seats')
                            table.heading('seats', text = 'Seats')
                            table.heading('cost', text = 'Cost')
                            #table.pack()
                            table.place(x=20,y=50)
                            
                            table.column('c_name', width=100)
                            table.column('acc_id', width=300)
                            table.column('snacks', width=200)
                            table.column('number of seats', width=100)
                            table.column('seats', width=100)
                            table.column('cost', width=100)
                            
                            try:
                                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                mycur=myconn.cursor()
                                query="select * from animal"
                                mycur.execute(query)
                                rs=mycur.fetchall()
                                
                                def insert():
                                    n=len(rs)
                                    for i in range(0,n):
                                        table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                def search():
                                    x=srchbar.get()
                                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                    mycur=myconn.cursor()
                                    query="select * from animal where c_name='{}'".format(x)
                                    mycur.execute(query)
                                    rs=mycur.fetchall()
                                    if rs!=None:                                        
                                        for item in table.get_children():
                                            table.delete(item)
                                        n=len(rs)
                                        for i in range(0,n):
                                            table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                    else:
                                        messagebox.showinfo("Search Failed", "The entered user has not be found")
                                def exit():
                                    for item in table.get_children():
                                            table.delete(item)
                                    srchbar.delete(0,END)
                                    insert()
                                insert()
                                                               
                                srchbar = tk.Entry(animal, width = 800,fg="blue",font=("Times New Roman Bold", 10)) 
                                srchbar.place(x = 20, y = 20, width = 800)
                                btsrch= tk.Button(animal, text ="Search",fg ='black', bg='blue', font=("Times New Roman Bold", 10),command=search)
                                btsrch.place(x = 820, y = 20, height = 20, width = 50)
                                btexit= tk.Button(animal, text ="Exit Search",fg ='black', bg='red', font=("Times New Roman Bold", 10),command=exit)
                                btexit.place(x = 873, y = 20, height = 20, width = 66) 
                                
                                def on_select(event):
                                    global seluser
                                    seluser=""
                                    sel = table.selection()[0]
                                    selitems = table.item(sel)
                                    sellist = selitems['values']
                                    seluser+=sellist[0]
                                    details()
                                                           
                                table.bind('<<TreeviewSelect>>', on_select)
                                
                            except Exception as e:
                                print(e)
                        
                        def neru():
                            neru = tk.Tk() 
                            neru.geometry("940x500")
                            neru.title("neru MOVIE")
                            
                            table = ttk.Treeview(neru, columns = ('c_name', 'acc_id','snacks', 'number of seats','seats','cost'), show = 'headings')
                            table.heading('c_name', text = 'Name')
                            table.heading('acc_id', text = 'Account id')
                            table.heading('snacks', text = 'Snacks')
                            table.heading('number of seats', text = 'Number of Seats')
                            table.heading('seats', text = 'Seats')
                            table.heading('cost', text = 'Cost')
                            #table.pack()
                            table.place(x=20,y=50)
                            
                            table.column('c_name', width=100)
                            table.column('acc_id', width=300)
                            table.column('snacks', width=200)
                            table.column('number of seats', width=100)
                            table.column('seats', width=100)
                            table.column('cost', width=100)
                            
                            try:
                                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                mycur=myconn.cursor()
                                query="select * from neru"
                                mycur.execute(query)
                                rs=mycur.fetchall()
                                
                                def insert():
                                    n=len(rs)
                                    for i in range(0,n):
                                        table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                def search():
                                    x=srchbar.get()
                                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                    mycur=myconn.cursor()
                                    query="select * from neru where c_name='{}'".format(x)
                                    mycur.execute(query)
                                    rs=mycur.fetchall()
                                    if rs!=None:                                        
                                        for item in table.get_children():
                                            table.delete(item)
                                        n=len(rs)
                                        for i in range(0,n):
                                            table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                    else:
                                        messagebox.showinfo("Search Failed", "The entered user has not be found")
                                def exit():
                                    for item in table.get_children():
                                            table.delete(item)
                                    srchbar.delete(0,END)
                                    insert()
                                insert()
                                                               
                                srchbar = tk.Entry(neru, width = 800,fg="blue",font=("Times New Roman Bold", 10)) 
                                srchbar.place(x = 20, y = 20, width = 800)
                                btsrch= tk.Button(neru, text ="Search",fg ='black', bg='blue', font=("Times New Roman Bold", 10),command=search)
                                btsrch.place(x = 820, y = 20, height = 20, width = 50)
                                btexit= tk.Button(neru, text ="Exit Search",fg ='black', bg='red', font=("Times New Roman Bold", 10),command=exit)
                                btexit.place(x = 873, y = 20, height = 20, width = 66) 
                                
                                def on_select(event):
                                    global seluser
                                    seluser=""
                                    sel = table.selection()[0]
                                    selitems = table.item(sel)
                                    sellist = selitems['values']
                                    seluser+=sellist[0]
                                    details()
                                                           
                                table.bind('<<TreeviewSelect>>', on_select)
                                
                            except Exception as e:
                                print(e)
                        
                        def raastha():
                            raastha = tk.Tk() 
                            raastha.geometry("940x500")
                            raastha.title("RAASTHA MOVIE")
                            
                            table = ttk.Treeview(raastha, columns = ('c_name', 'acc_id','snacks', 'number of seats','seats','cost'), show = 'headings')
                            table.heading('c_name', text = 'Name')
                            table.heading('acc_id', text = 'Account id')
                            table.heading('snacks', text = 'Snacks')
                            table.heading('number of seats', text = 'Number of Seats')
                            table.heading('seats', text = 'Seats')
                            table.heading('cost', text = 'Cost')
                            #table.pack()
                            table.place(x=20,y=50)
                            
                            table.column('c_name', width=100)
                            table.column('acc_id', width=300)
                            table.column('snacks', width=200)
                            table.column('number of seats', width=100)
                            table.column('seats', width=100)
                            table.column('cost', width=100)
                            
                            try:
                                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                mycur=myconn.cursor()
                                query="select * from raastha"
                                mycur.execute(query)
                                rs=mycur.fetchall()
                                
                                def insert():
                                    n=len(rs)
                                    for i in range(0,n):
                                        table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                def search():
                                    x=srchbar.get()
                                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                                    mycur=myconn.cursor()
                                    query="select * from raastha where c_name='{}'".format(x)
                                    mycur.execute(query)
                                    rs=mycur.fetchall()
                                    if rs!=None:                                        
                                        for item in table.get_children():
                                            table.delete(item)
                                        n=len(rs)
                                        for i in range(0,n):
                                            table.insert(parent='', index=tk.END, values=(rs[i][0],rs[i][1],rs[i][2],rs[i][3],rs[i][4],rs[i][5]))
                                
                                    else:
                                        messagebox.showinfo("Search Failed", "The entered user has not be found")
                                def exit():
                                    for item in table.get_children():
                                            table.delete(item)
                                    srchbar.delete(0,END)
                                    insert()
                                insert()
                                                               
                                srchbar = tk.Entry(raastha, width = 800,fg="blue",font=("Times New Roman Bold", 10)) 
                                srchbar.place(x = 20, y = 20, width = 800)
                                btsrch= tk.Button(raastha, text ="Search",fg ='black', bg='blue', font=("Times New Roman Bold", 10),command=search)
                                btsrch.place(x = 820, y = 20, height = 20, width = 50)
                                btexit= tk.Button(raastha, text ="Exit Search",fg ='black', bg='red', font=("Times New Roman Bold", 10),command=exit)
                                btexit.place(x = 873, y = 20, height = 20, width = 66) 
                                
                                def on_select(event):
                                    global seluser
                                    seluser=""
                                    sel = table.selection()[0]
                                    selitems = table.item(sel)
                                    sellist = selitems['values']
                                    seluser+=sellist[0]
                                    details()
                                                           
                                table.bind('<<TreeviewSelect>>', on_select)
                                
                            except Exception as e:
                                print(e)
                                
                        btwonka = tk.Button(mov, text ="Wonka",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20), command=wonka) 
                        btwonka.place(x = 15, y = 50, height = 100, width = 180)
                        btaqua = tk.Button(mov, text ="Aquaman",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20), command=aqua) 
                        btaqua.place(x = 300, y = 50, height = 100, width = 180)
                        btdunki = tk.Button(mov, text ="Dunki",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20), command=dunki) 
                        btdunki.place(x = 15, y = 250, height = 100, width = 180)
                        btanimal = tk.Button(mov, text ="Animal",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20), command=animal) 
                        btanimal.place(x = 300, y = 250, height = 100, width = 180)
                        btneru = tk.Button(mov, text ="Neru",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20), command=neru) 
                        btneru.place(x = 15, y = 450, height = 100, width = 180)
                        btraastha = tk.Button(mov, text ="Raastha",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20), command=raastha) 
                        btraastha.place(x = 300, y = 450, height = 100, width = 180)
                    movie()
                else:
                    messagebox.showinfo("Login Failed", "The entered info for admin is incorrect")
                    
        
        messagebox.showinfo("ADMIN", "ONLY ALLOWED FOR ADMINS!!!")
        login = tk.Tk() 
        login.geometry("300x300")
        login.title("Login Page")
        login.configure(bg='red')
        C = Canvas(login, bg ="Red", height = 250, width = 300) 
        lbluser = tk.Label(login, text ="Admin Username -",fg="black",bg='red',font=("Times New Roman Bold", 10) ) 
        lbluser.place(x = 30, y = 20) 
        txtUser = tk.Entry(login, width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
        txtUser.place(x = 150, y = 20, width = 100) 
        lblpass = tk.Label(login, text ="Password -",fg="black", bg='red',font=("Times New Roman Bold", 10)) 
        lblpass.place(x = 30, y = 50) 
        txtpass = tk.Entry(login,show="*", width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
        txtpass.place(x = 150, y = 50, width = 100) 
        loginbtn = tk.Button(login, text ="Login", fg ='blue', font=("Times New Roman Bold", 10),command = funlogin) 
        loginbtn.place(x = 140, y = 135, width = 55)
        clearbtn = tk.Button(login, text ="Clear",fg ='blue', font=("Times New Roman Bold", 10),command = funclear) 
        clearbtn.place(x = 200, y = 135, width = 55)


    def English():
        root.destroy()
        frmeng=tk.Tk()
        frmeng.geometry("600x600")
        frmeng.title("English Movies")
        frmeng.configure(bg='black')
        def loginscreen():
            def funclear():
                txtUser.delete(0,END)
                txtpass.delete(0,END)
                txtUser.focus()

            def funlogin():
                user = txtUser.get() 
                passw = txtpass.get()
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()
                    query="select * from customer where c_name='{}' and pass='{}'".format(user,passw)
                    mycur.execute(query)
                    rs=mycur.fetchone()
                    if rs!=None and user==rs[0] and passw==rs[2]:
                        global ver
                        ver=1
                        global user1
                        user1=user
                        passw=txtpass.get()
                        l=user+passw
                        global i_d1
                        for ch in l:
                            i_d1+=str(ord(ch))
    
                        messagebox.showinfo("Login ", "Login Successful")
                        login.destroy()
                        btlogin.destroy()
                        lblacc = tk.Label(frmeng, text ="Account name:", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                        lblacc.place(x = 470, y = 5)
                        lblus = tk.Label(frmeng, text =user1, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                        lblus.place(x = 555, y = 5)
                    else:
                        messagebox.showinfo("Login", "Login Failed")
                except Exception as e:
                    print(e)
            
            def register():
                i_d=''
                user=txtUser.get() 
                passw=txtpass.get()
                l=user+passw
                for ch in l:
                    i_d+=str(ord(ch))
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()
                    query="insert into customer values('{}',{},'{}')".format(user,i_d,passw)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Registration", "Registration Successful, you may Login now")
                    funclear()
                except Exception as e:
                    messagebox.showinfo("Registration", "Registration Successful, you may Login now")
                
        
            login = tk.Tk() 
            login.geometry("300x300")
            login.title("Login Page") 
            C = Canvas(login, bg ="Red", height = 250, width = 300) 
            lbluser = tk.Label(login, text ="Username -",fg="red",font=("Times New Roman Bold", 10) ) 
            lbluser.place(x = 50, y = 20) 
            txtUser = tk.Entry(login, width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
            txtUser.place(x = 150, y = 20, width = 100) 
            lblpass = tk.Label(login, text ="Password -",fg="red",font=("Times New Roman Bold", 10)) 
            lblpass.place(x = 50, y = 50) 
            txtpass = tk.Entry(login,show="*", width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
            txtpass.place(x = 150, y = 50, width = 100) 
            loginbtn = tk.Button(login, text ="Login", fg ='blue', font=("Times New Roman Bold", 10),command = funlogin) 
            loginbtn.place(x = 140, y = 135, width = 55)
            regbtn = tk.Button(login, text ="Register", fg ='blue', font=("Times New Roman Bold", 10),command = register) 
            regbtn.place(x = 80, y = 135, width = 55)
            clearbtn = tk.Button(login, text ="Clear",fg ='blue', font=("Times New Roman Bold", 10),command = funclear) 
            clearbtn.place(x = 200, y = 135, width = 55)
        
        def showtimes1():
            frmtime=tk.Tk()
            frmtime.geometry("400x300")
            frmtime.title("Movie")
            frmtime.configure(bg='light green')
            def end():
                global nseat,final
                global user1, i_d1
                seat1=snacks1=''
                for ele in seataqua:
                    seat1+= ele + ', '
                for ele in n:
                    snacks1+= ele + ', '
                  
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()

                    query = "INSERT INTO aquaman (c_name, acc_id, snacks, `number of seats`, seats, cost) VALUES ('{}', '{}', '{}', {}, '{}',{})".format(user1, i_d1, snacks1, nseat, seat1,final)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Booking Successful", "Booking Successful, Enjoy your Movie")
                
                except Exception as e:
                    print(e)
                    
            def book():
                global nseat
                if nseat>=1 and ver==1:
                    book = tk.Tk() 
                    book.geometry("400x400")
                    book.title("Booking")
                    
                    global user1
                    global pop,nacho,pepsi,burger,hotdog
                          
                    btb=Button(book,text="book",fg='black',bg='red', command=end)
                    btb.place(x=200,y=370)
                       
                    table = ttk.Treeview(book, columns = ('name', 'movie','snack', 'seat'), show = 'headings')
                    table.heading('name', text = 'Name')
                    table.heading('movie', text = 'Movie')
                    table.heading('snack', text = 'Snacks')
                    table.heading('seat', text = 'Seats')
                    table.pack()
                    
                    table.column('name', width=100)
                    table.column('movie', width=100)
                    table.column('snack', width=100)
                    table.column('seat', width=100)
                    
                    if pop==1:
                        n.append('Popcorn')
                    if nacho==1:
                        n.append('Nachos')
                    if pepsi==1:
                        n.append('Pepsi')
                    if burger==1:
                        n.append('Burger')
                    if hotdog==1:
                        n.append('Hotdog')

                    name = user1
                    movie = "Aquaman"
                    table.insert(parent='', index=tk.END, values=(name, movie,'',''))
 
                    max_items = max(len(n), len(seataqua))
                    for i in range(max_items):
                        snack_value = n[i] if i < len(n) else ''
                        seat_value = seataqua[i] if i < len(seataqua) else ''
                        table.insert(parent='', index=tk.END, values=('','',snack_value, seat_value))
                        
                    global seatmoney,snckmoney,final
                    total=seatmoney+snckmoney
                    t=pop+nacho+pepsi+burger+hotdog
                    d1=d2=0
                    if nseat>3 and t>2:
                        d1=seatmoney-(0.2*seatmoney)
                        d2=snckmoney-(0.1*snckmoney)
                        final=d1+d2
                    #Discount 1 : 10% off total if seats are greater than 3
                    elif nseat>3:
                        d1=seatmoney-(0.2*seatmoney)
                        final=d1+snckmoney
                    #Discount 2 : 10% off snckmoney if snacks are greater than 2
                    elif t>2:
                        d2=snckmoney-(0.1*snckmoney)
                        final=d2+seatmoney
                    else:
                        final=total
                    
                    lblcost = tk.Label(book, text ="Cost :",fg="black",font=("Arial", 12)) 
                    lblcost.place(x = 100, y = 200)
                    lbl1 = tk.Label(book, text ="$"+str(snckmoney),fg="black",font=("Arial", 12)) 
                    lbl1.place(x = 250, y = 200)
                    lbl2 = tk.Label(book, text ="$"+str(seatmoney),fg="black",font=("Arial", 12)) 
                    lbl2.place(x = 350, y = 200)
                    lbltot = tk.Label(book, text ="Total :",fg="black",font=("Arial", 12)) 
                    lbltot.place(x = 200, y = 230)
                    lbl3 = tk.Label(book, text ="$"+str(total),fg="black",font=("Arial", 12)) 
                    lbl3.place(x = 250, y = 230)
                    lblfinal = tk.Label(book, text ="Total after discount :",fg="black",font=("Arial", 12)) 
                    lblfinal.place(x = 200, y = 260)
                    lbl4 = tk.Label(book, text ="$"+str(final),fg="black",font=("Arial", 12)) 
                    lbl4.place(x = 350, y = 260)
                    lbldis = tk.Label(book, text ="Discounts",fg="black", borderwidth=2, relief='solid', font=("Arial", 10,'underline','bold')) 
                    lbldis.place(x = 180, y = 310)
                    lbldis1 = tk.Label(book, text ="1. For booking more than 3 seats: Reduction of 20% from the cost of seats\n 2. For selecting more than 2 snacks: Reduction of 10% from the cost of snacks",fg="black", borderwidth=2, relief='solid', font=("Times New Roman", 8)) 
                    lbldis1.place(x = 20, y = 330)

                                        
                elif nseat<1:
                        messagebox.showinfo("Booking failed ", "Please Book Seats")
                elif ver==0:
                        messagebox.showinfo("Booking failed ", "Please Login First")

            def snacks():
                global snckmoney
                snack_quantities = {'Popcorn': 0, 'Nachos': 0, 'Pepsi': 0, 'Burger': 0, 'Hotdog': 0}
                def update_display():
                    global snckmoney
                    snckmoney = sum(snack_quantities[snack] * prices[snack] for snack in snacks_list)
                    b1.config(text="$" + str(snckmoney))

                def clear():
                    for snack in snacks_list:
                        scale_vars[snack].set(0)
                        snack_quantities[snack] = 0
                    update_display()

                def on_scale_change(event):
                    snack = event.widget.snack
                    snack_quantities[snack] = scale_vars[snack].get()
                    update_display()
                    global pop,hotdog,nacho,pepsi,burger
                    if snack == 'Popcorn' and snack_quantities[snack] > 0:
                        pop = 1 
                    if snack == 'Hotdog' and snack_quantities[snack] > 0:
                        hotdog = 1 
                    if snack == 'Burger' and snack_quantities[snack] > 0:
                        burger = 1 
                    if snack == 'Pepsi' and snack_quantities[snack] > 0:
                        pepsi = 1 
                    if snack == 'Nachos' and snack_quantities[snack] > 0:
                        nacho = 1 

                frmsnck = tk.Tk()
                frmsnck.geometry("400x500")
                frmsnck.title("Snacks")
                frmsnck.configure(bg='black')

                btclr = tk.Button(frmsnck, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmsnck, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                lbltot = tk.Label(frmsnck, text="Total : ", fg='black', bg='white', font=('Times New Roman', 12, 'bold', 'underline'))
                lbltot.place(x=180, y=350)

                b1 = tk.Label(frmsnck, text="$" + str(snckmoney))
                b1.place(x=230, y=350, width=70)

                snacks_list = ['Popcorn', 'Nachos', 'Pepsi', 'Burger', 'Hotdog']
                prices = {'Popcorn': 5, 'Nachos': 7, 'Pepsi': 2, 'Burger': 15, 'Hotdog': 10}
                scale_vars = {}

                for idx, snack in enumerate(snacks_list):
                    lbl = tk.Label(frmsnck, text=f"{snack} (Cost: ${prices[snack]})", fg='black', bg='grey', font=('Times New Roman', 10, 'bold'))
                    lbl.place(x=50, y=100 + idx * 40)

                    scale_vars[snack] = tk.Scale(frmsnck, from_=0, to=5, orient=tk.HORIZONTAL, length=150)
                    scale_vars[snack].place(x=200, y=100 + idx * 40)
                    scale_vars[snack].snack = snack 
                    scale_vars[snack].bind("<ButtonRelease-1>", on_scale_change)                 
                    
            def booking():
                def taken():
                    nonlocal buttons
                    try:
                        myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                        mycur=myconn.cursor()

                        query = "select seats from aquaman"
                        mycur.execute(query)
                        result=mycur.fetchall()
                        booked_seats = []
                        for tup in result:
                            elements = [elem.strip() for elem in tup[0].split(',')]
                            booked_seats.extend([elem for elem in elements if elem])
                        myconn.commit()
                        for row in range(len(buttons)):
                            for col in range(len(buttons[row])):
                                seat_label = chr(ord('a') + row) + str(col + 1)
                                if seat_label in booked_seats:
                                    buttons[row][col].configure(bg="grey", state=tk.DISABLED)

                    except Exception as e:
                        print(e)
                        
                def clear():
                    for button_row in buttons:
                        for button in button_row:
                            if button["bg"] == "red":
                                button.configure(bg="green")
                    global seatmoney, nseat
                    seatmoney = 0
                    nseat = 0
                    update_display()
                    seataqua.clear()

                def update_display():
                    b1.config(text="$" + str(seatmoney))

                def button_click(row, col):
                    global seatmoney, nseat
                    button = buttons[row][col]
                    seat_label = chr(ord('a') + row) + str(col + 1)
                    if button["bg"] == "green":
                        button.configure(bg="red")
                        seatmoney += 20
                        nseat += 1
                        seataqua.append(seat_label)
               
                    else:
                        button.configure(bg="green")
                        seatmoney -= 20
                        nseat -= 1
                        seataqua.remove(seat_label)
                    
                    update_display()
                    
                frmbook = tk.Tk()
                frmbook.geometry("400x450")
                frmbook.title("Seat")
                frmbook.configure(bg='black')
                lblscr = tk.Label(frmbook, text="-----------------screen-------------------", fg='white', bg='black',
                                  font=('Times New Roman', 20))
                lblscr.place(x=5, y=100)

                btclr = tk.Button(frmbook, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmbook, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                b1 = tk.Button(frmbook, text="$" + str(seatmoney))
                b1.place(x=120, y=400, width=70)
                
                lbla = tk.Label(frmbook, text="a", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbla.place(x=5, y=150)
                lblb = tk.Label(frmbook, text="b", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblb.place(x=5, y=200)
                lblc = tk.Label(frmbook, text="c", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblc.place(x=5, y=250)
                lbld = tk.Label(frmbook, text="d", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbld.place(x=5, y=300)
                lblno = tk.Label(frmbook, text="1   2   3   4   5   6   7   8   9  10  11 12 13 14 15 16 17 18", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblno.place(x=20, y=325)
            
                buttons = []
            
                for row in range(4):
                    button_row = []
                    for col in range(18):
                        seat_label = chr(ord('a') + row) + str(col + 1)          
                        button = tk.Button(frmbook, bg='green', height=1, width=1, command=lambda r=row, c=col: button_click(r, c))
                        button.place(x=20 + col * 20, y=150 + row * 50)
                        button_row.append(button)
                    buttons.append(button_row)
                taken()

            btbook= tk.Button(frmtime, text ="Book seat",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=booking) 
            btbook.place(x = 250, y = 155, width = 100)
            btsnack= tk.Button(frmtime, text ="Snacks",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=snacks) 
            btsnack.place(x = 250, y = 185, width = 100)
            lblhd = tk.Label(frmtime, text ="Aquaman & The Lost Kingdom", bg= 'light green',font=('MV Boli',15,'bold','underline'))
            lblhd.place(x = 40, y = 10)
            lbldescrpt = tk.Label(frmtime, text ="Description", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lbldescrpt.place(x = 2, y = 40)            
            lbldes = tk.Label(frmtime, text ="When an ancient power is unleashed, Aquaman must forge an uneasy\n alliance with an unlikely ally to protect Atlantis, and the world,\n from irreversible devastation.",
                              bg= 'light green',font=('Times New Roman',10))
            lbldes.place(x = 2, y = 65)
            lblgenre = tk.Label(frmtime, text ="Genre", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblgenre.place(x = 2, y = 110)
            lblgen = tk.Label(frmtime, text ="Action", bg= 'light green',font=('Times New Roman',10))
            lblgen.place(x = 2, y = 135)
            lblrt = tk.Label(frmtime, text ="Running time", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblrt.place(x = 2, y = 155)
            lblrun = tk.Label(frmtime, text ="125 mins", bg= 'light green',font=('Times New Roman',10))
            lblrun.place(x = 2, y = 180)
            lblstar = tk.Label(frmtime, text ="Starring", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblstar.place(x = 2, y = 200)
            lblact = tk.Label(frmtime, text ="Jason Momoa, Amber Heard, Patrick Wilson,\n Dolph Lundgren, Yahya Abdul Mateen II", bg= 'light green',font=('Times New Roman',10))
            lblact.place(x = 2, y = 225)
            
            link = tk.Label(frmtime, text="Trailer", 
            fg="blue", bg="light green", cursor="hand2",font=['Times',15,'underline'])
            link.place(x=160, y=155)
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://youtu.be/UGc5Tzz19UY?si=sPxYM3b9lWpQ_j0H"))
        
            
        def showtimes2():
            frmtime=tk.Tk()
            frmtime.geometry("400x300")
            frmtime.title("Wonka")
            frmtime.configure(bg='light green')
            def end():
                global nseat,final
                global user1, i_d1
                seat1=snacks1=''
                for ele in seatwonka:
                    seat1+= ele + ', '
                for ele in n:
                    snacks1+= ele + ', '
                  
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()

                    query = "INSERT INTO wonka (c_name, acc_id, snacks, `number of seats`, seats, cost) VALUES ('{}', '{}', '{}', {}, '{}',{})".format(user1, i_d1, snacks1, nseat, seat1,final)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Booking Successful", "Booking Successful, Enjoy your Movie")
                
                except Exception as e:
                    print(e)
                    
            def book():
                global nseat
                if nseat>=1 and ver==1:
                    book = tk.Tk() 
                    book.geometry("400x400")
                    book.title("Booking")
                    
                    global user1
                    global pop,nacho,pepsi,burger,hotdog
                          
                    btb=Button(book,text="book",fg='black',bg='red', command=end)
                    btb.place(x=200,y=370)
                       
                    table = ttk.Treeview(book, columns = ('name', 'movie','snack', 'seat'), show = 'headings')
                    table.heading('name', text = 'Name')
                    table.heading('movie', text = 'Movie')
                    table.heading('snack', text = 'Snacks')
                    table.heading('seat', text = 'Seats')
                    table.pack()
                    
                    table.column('name', width=100)
                    table.column('movie', width=100)
                    table.column('snack', width=100)
                    table.column('seat', width=100)
                    
                    if pop==1:
                        n.append('Popcorn')
                    if nacho==1:
                        n.append('Nachos')
                    if pepsi==1:
                        n.append('Pepsi')
                    if burger==1:
                        n.append('Burger')
                    if hotdog==1:
                        n.append('Hotdog')

                    name = user1
                    movie = "Wonka"
                    table.insert(parent='', index=tk.END, values=(name, movie,'',''))
 
                    max_items = max(len(n), len(seatwonka))
                    for i in range(max_items):
                        snack_value = n[i] if i < len(n) else ''
                        seat_value = seatwonka[i] if i < len(seatwonka) else ''
                        table.insert(parent='', index=tk.END, values=('','',snack_value, seat_value))
                        
                    global seatmoney,snckmoney,final
                    total=seatmoney+snckmoney
                    t=pop+nacho+pepsi+burger+hotdog
                    d1=d2=0
                    if nseat>3 and t>2:
                        d1=seatmoney-(0.2*seatmoney)
                        d2=snckmoney-(0.1*snckmoney)
                        final=d1+d2
                    #Discount 1 : 10% off total if seats are greater than 3
                    elif nseat>3:
                        d1=seatmoney-(0.2*seatmoney)
                        final=d1+snckmoney
                    #Discount 2 : 10% off snckmoney if snacks are greater than 2
                    elif t>2:
                        d2=snckmoney-(0.1*snckmoney)
                        final=d2+seatmoney
                    else:
                        final=total
                    
                    lblcost = tk.Label(book, text ="Cost :",fg="black",font=("Arial", 12)) 
                    lblcost.place(x = 100, y = 200)
                    lbl1 = tk.Label(book, text ="$"+str(snckmoney),fg="black",font=("Arial", 12)) 
                    lbl1.place(x = 250, y = 200)
                    lbl2 = tk.Label(book, text ="$"+str(seatmoney),fg="black",font=("Arial", 12)) 
                    lbl2.place(x = 350, y = 200)
                    lbltot = tk.Label(book, text ="Total :",fg="black",font=("Arial", 12)) 
                    lbltot.place(x = 200, y = 230)
                    lbl3 = tk.Label(book, text ="$"+str(total),fg="black",font=("Arial", 12)) 
                    lbl3.place(x = 250, y = 230)
                    lblfinal = tk.Label(book, text ="Total after discount :",fg="black",font=("Arial", 12)) 
                    lblfinal.place(x = 200, y = 260)
                    lbl4 = tk.Label(book, text ="$"+str(final),fg="black",font=("Arial", 12)) 
                    lbl4.place(x = 350, y = 260)
                    lbldis = tk.Label(book, text ="Discounts",fg="black", borderwidth=2, relief='solid', font=("Arial", 10,'underline','bold')) 
                    lbldis.place(x = 180, y = 310)
                    lbldis1 = tk.Label(book, text ="1. For booking more than 3 seats: Reduction of 20% from the cost of seats\n 2. For selecting more than 2 snacks: Reduction of 10% from the cost of snacks",fg="black", borderwidth=2, relief='solid', font=("Times New Roman", 8)) 
                    lbldis1.place(x = 20, y = 330)

                                        
                elif nseat<1:
                        messagebox.showinfo("Booking failed ", "Please Book Seats")
                elif ver==0:
                        messagebox.showinfo("Booking failed ", "Please Login First")

            def snacks():
                global snckmoney
                snack_quantities = {'Popcorn': 0, 'Nachos': 0, 'Pepsi': 0, 'Burger': 0, 'Hotdog': 0}
                def update_display():
                    global snckmoney
                    snckmoney = sum(snack_quantities[snack] * prices[snack] for snack in snacks_list)
                    b1.config(text="$" + str(snckmoney))

                def clear():
                    for snack in snacks_list:
                        scale_vars[snack].set(0)
                        snack_quantities[snack] = 0
                    update_display()

                def on_scale_change(event):
                    snack = event.widget.snack
                    snack_quantities[snack] = scale_vars[snack].get()
                    update_display()
                    global pop,hotdog,nacho,pepsi,burger
                    if snack == 'Popcorn' and snack_quantities[snack] > 0:
                        pop = 1 
                    if snack == 'Hotdog' and snack_quantities[snack] > 0:
                        hotdog = 1 
                    if snack == 'Burger' and snack_quantities[snack] > 0:
                        burger = 1 
                    if snack == 'Pepsi' and snack_quantities[snack] > 0:
                        pepsi = 1 
                    if snack == 'Nachos' and snack_quantities[snack] > 0:
                        nacho = 1 

                frmsnck = tk.Tk()
                frmsnck.geometry("400x500")
                frmsnck.title("Snacks")
                frmsnck.configure(bg='black')

                btclr = tk.Button(frmsnck, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmsnck, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                lbltot = tk.Label(frmsnck, text="Total : ", fg='black', bg='white', font=('Times New Roman', 12, 'bold', 'underline'))
                lbltot.place(x=180, y=350)

                b1 = tk.Label(frmsnck, text="$" + str(snckmoney))
                b1.place(x=230, y=350, width=70)

                snacks_list = ['Popcorn', 'Nachos', 'Pepsi', 'Burger', 'Hotdog']
                prices = {'Popcorn': 5, 'Nachos': 7, 'Pepsi': 2, 'Burger': 15, 'Hotdog': 10}
                scale_vars = {}

                for idx, snack in enumerate(snacks_list):
                    lbl = tk.Label(frmsnck, text=f"{snack} (Cost: ${prices[snack]})", fg='black', bg='grey', font=('Times New Roman', 10, 'bold'))
                    lbl.place(x=50, y=100 + idx * 40)

                    scale_vars[snack] = tk.Scale(frmsnck, from_=0, to=5, orient=tk.HORIZONTAL, length=150)
                    scale_vars[snack].place(x=200, y=100 + idx * 40)
                    scale_vars[snack].snack = snack 
                    scale_vars[snack].bind("<ButtonRelease-1>", on_scale_change)                 
                    
            def booking():
                def taken():
                    nonlocal buttons
                    try:
                        myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                        mycur=myconn.cursor()

                        query = "select seats from wonka"
                        mycur.execute(query)
                        result=mycur.fetchall()
                        booked_seats = []
                        for tup in result:
                            elements = [elem.strip() for elem in tup[0].split(',')]
                            booked_seats.extend([elem for elem in elements if elem])
                        myconn.commit()
                        for row in range(len(buttons)):
                            for col in range(len(buttons[row])):
                                seat_label = chr(ord('a') + row) + str(col + 1)
                                if seat_label in booked_seats:
                                    buttons[row][col].configure(bg="grey", state=tk.DISABLED)

                    except Exception as e:
                        print(e)
                        
                def clear():
                    for button_row in buttons:
                        for button in button_row:
                            if button["bg"] == "red":
                                button.configure(bg="green")
                    global seatmoney, nseat
                    seatmoney = 0
                    nseat = 0
                    update_display()
                    seatwonka.clear()

                def update_display():
                    b1.config(text="$" + str(seatmoney))

                def button_click(row, col):
                    global seatmoney, nseat
                    button = buttons[row][col]
                    seat_label = chr(ord('a') + row) + str(col + 1)
                    if button["bg"] == "green":
                        button.configure(bg="red")
                        seatmoney += 20
                        nseat += 1
                        seatwonka.append(seat_label)
               
                    else:
                        button.configure(bg="green")
                        seatmoney -= 20
                        nseat -= 1
                        seatwonka.remove(seat_label)
                    
                    update_display()
                    
                frmbook = tk.Tk()
                frmbook.geometry("400x450")
                frmbook.title("Seat")
                frmbook.configure(bg='black')
                lblscr = tk.Label(frmbook, text="-----------------screen-------------------", fg='white', bg='black',
                                  font=('Times New Roman', 20))
                lblscr.place(x=5, y=100)

                btclr = tk.Button(frmbook, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmbook, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                b1 = tk.Button(frmbook, text="$" + str(seatmoney))
                b1.place(x=120, y=400, width=70)
                
                lbla = tk.Label(frmbook, text="a", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbla.place(x=5, y=150)
                lblb = tk.Label(frmbook, text="b", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblb.place(x=5, y=200)
                lblc = tk.Label(frmbook, text="c", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblc.place(x=5, y=250)
                lbld = tk.Label(frmbook, text="d", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbld.place(x=5, y=300)
                lblno = tk.Label(frmbook, text="1   2   3   4   5   6   7   8   9  10  11 12 13 14 15 16 17 18", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblno.place(x=20, y=325)
                

                buttons = []
                

                for row in range(4):
                    button_row = []
                    for col in range(18):
                        seat_label = chr(ord('a') + row) + str(col + 1)          
                        button = tk.Button(frmbook, bg='green', height=1, width=1, command=lambda r=row, c=col: button_click(r, c))
                        button.place(x=20 + col * 20, y=150 + row * 50)
                        button_row.append(button)
                    buttons.append(button_row)
                taken()
            lblhd = tk.Label(frmtime, text ="Wonka", bg= 'light green',font=('MV Boli',15,'bold','underline'))
            lblhd.place(x = 170, y = 10)
            btbook= tk.Button(frmtime, text ="Book seat",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=booking) 
            btbook.place(x = 250, y = 155, width = 100)
            btsnack= tk.Button(frmtime, text ="Snacks",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=snacks) 
            btsnack.place(x = 250, y = 185, width = 100)
            lbldescrpt = tk.Label(frmtime, text ="Description", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lbldescrpt.place(x = 2, y = 40)            
            lbldes = tk.Label(frmtime, text ="The Story will focus on a young Willy Wonka and his adventures prior\n to opening the world’s most famous chocolate factory.",
                              bg= 'light green',font=('Times New Roman',10))
            lbldes.place(x = 2, y = 65)
            lblgenre = tk.Label(frmtime, text ="Genre", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblgenre.place(x = 2, y = 110)
            lblgen = tk.Label(frmtime, text ="Adventure", bg= 'light green',font=('Times New Roman',10))
            lblgen.place(x = 2, y = 135)
            lblrt = tk.Label(frmtime, text ="Running time", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblrt.place(x = 2, y = 155)
            lblrun = tk.Label(frmtime, text ="120 mins", bg= 'light green',font=('Times New Roman',10))
            lblrun.place(x = 2, y = 180)
            lblstar = tk.Label(frmtime, text ="Starring", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblstar.place(x = 2, y = 200)
            lblact = tk.Label(frmtime, text ="Rowan Atkinson, Timothee Chalamet,\n Calah Lane, Keegan Michael Key", bg= 'light green',font=('Times New Roman',10))
            lblact.place(x = 2, y = 225)
            
            link = tk.Label(frmtime, text="Trailer", 
            fg="blue", bg="light green", cursor="hand2",font=['Times',15,'underline'])
            link.place(x=160, y=155)
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://youtu.be/otNh9bTjXWg?si=o9SxmqegS5VsVcEg"))
        
        bg = ImageTk.PhotoImage(Image.open("bg2.jpg"))
        button3= Button(frmeng, image = bg)
        button3.pack()
        lbllan = tk.Label(frmeng, text ="ENGLISH MOVIES", fg= 'white', bg= 'black',font=('MV Boli',25,'bold','underline'))
        lbllan.place(x = 160, y = 15)
        img = ImageTk.PhotoImage(Image.open("aqua.jpg"))
        button1= Button(frmeng, image = img, command=showtimes1)
        button1.place(x = 50, y = 150)
        img2 = ImageTk.PhotoImage(Image.open("wonka.jpg"))
        button2= Button(frmeng, image = img2, command=showtimes2)
        button2.place(x = 350, y = 150)   
        if ver==0:
            btlogin = tk.Button(frmeng, text ="login",fg ='white',bg= 'red',font=("Times New Roman Bold", 10),command=loginscreen) 
            btlogin.place(x = 530, y = 5, width = 60)
        if ver==1:
            lblacc = tk.Label(frmeng, text ="Account name:", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
            lblacc.place(x = 470, y = 5)
            lblus = tk.Label(frmeng, text =user1, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
            lblus.place(x = 555, y = 5)
        root.mainloop()
        
    def Hindi():
        root.destroy()
        frmhin=tk.Tk()
        frmhin.geometry("600x600")
        frmhin.title("Hindi Movies")
        frmhin.configure(bg='light blue')
        bg = ImageTk.PhotoImage(Image.open("bg2.jpg"))
        button3= Button(frmhin, image = bg)
        button3.pack()
        lbllan = tk.Label(frmhin, text ="HINDI MOVIES", fg= 'white', bg= 'black',font=('MV Boli',25,'bold','underline'))
        lbllan.place(x = 170, y = 15)
        
        def loginscreen():
            def funclear():
                txtUser.delete(0,END)
                txtpass.delete(0,END)
                txtUser.focus()

            def funlogin():
                user = txtUser.get() 
                passw = txtpass.get()
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()
                    query="select * from customer where c_name='{}' and pass='{}'".format(user,passw)
                    mycur.execute(query)
                    rs=mycur.fetchone()
                    if rs!=None and user==rs[0] and passw==rs[2]:
                        global ver
                        ver=1
                        global user1
                        user1=user
                        passw=txtpass.get()
                        l=user+passw
                        global i_d1
                        for ch in l:
                            i_d1+=str(ord(ch))
                        messagebox.showinfo("Login ", "Login Successful")
                        login.destroy()
                        btlogin.destroy()
                        lblacc = tk.Label(frmhin, text ="Account name:", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                        lblacc.place(x = 470, y = 5)
                        lblus = tk.Label(frmhin, text =user1, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                        lblus.place(x = 555, y = 5)
                    else:
                        messagebox.showinfo("Login", "Login Failed")
                except Exception as e:
                    print(e)
            
            def register():
                i_d=''
                user=txtUser.get() 
                passw=txtpass.get()
                l=user+passw
                for ch in l:
                    i_d+=str(ord(ch))
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()
                    query="insert into customer values('{}',{},'{}')".format(user,i_d,passw)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Registration", "Registration Successful, you may Login now")
                    funclear()
                except Exception as e:
                    messagebox.showinfo("Registration", "Registration Successful, you may Login now")
                
        
            login = tk.Tk() 
            login.geometry("300x300")
            login.title("Login Page") 
            C = Canvas(login, bg ="Red", height = 250, width = 300) 
            lbluser = tk.Label(login, text ="Username -",fg="red",font=("Times New Roman Bold", 10) ) 
            lbluser.place(x = 50, y = 20) 
            txtUser = tk.Entry(login, width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
            txtUser.place(x = 150, y = 20, width = 100) 
            lblpass = tk.Label(login, text ="Password -",fg="red",font=("Times New Roman Bold", 10)) 
            lblpass.place(x = 50, y = 50) 
            txtpass = tk.Entry(login,show="*", width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
            txtpass.place(x = 150, y = 50, width = 100) 
            loginbtn = tk.Button(login, text ="Login", fg ='blue', font=("Times New Roman Bold", 10),command = funlogin) 
            loginbtn.place(x = 140, y = 135, width = 55)
            regbtn = tk.Button(login, text ="Register", fg ='blue', font=("Times New Roman Bold", 10),command = register) 
            regbtn.place(x = 80, y = 135, width = 55)
            clearbtn = tk.Button(login, text ="Clear",fg ='blue', font=("Times New Roman Bold", 10),command = funclear) 
            clearbtn.place(x = 200, y = 135, width = 55)
        
        if ver==0:
            btlogin = tk.Button(frmhin, text ="login",fg ='white',bg= 'red',font=("Times New Roman Bold", 10),command=loginscreen) 
            btlogin.place(x = 530, y = 5, width = 60)
        if ver==1:
            lblacc = tk.Label(frmhin, text ="Account name:", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
            lblacc.place(x = 470, y = 5)
            lblus = tk.Label(frmhin, text =user1, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
            lblus.place(x = 555, y = 5)
        
        def showtimes1():
            frmtime=tk.Tk()
            frmtime.geometry("400x300")
            frmtime.title("Dunki")
            frmtime.configure(bg='light green')
            def end():
                global nseat,final
                global user1, i_d1
                seat1=snacks1=''
                for ele in seatdunki:
                    seat1+= ele + ', '
                for ele in n:
                    snacks1+= ele + ', '
                  
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()

                    query = "INSERT INTO dunki (c_name, acc_id, snacks, `number of seats`, seats, cost) VALUES ('{}', '{}', '{}', {}, '{}',{})".format(user1, i_d1, snacks1, nseat, seat1,final)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Booking Successful", "Booking Successful, Enjoy your Movie")
                
                except Exception as e:
                    print(e)
                    
            def book():
                global nseat
                if nseat>=1 and ver==1:
                    book = tk.Tk() 
                    book.geometry("400x400")
                    book.title("Booking")
                    
                    global user1
                    global pop,nacho,pepsi,burger,hotdog
                          
                    btb=Button(book,text="book",fg='black',bg='red', command=end)
                    btb.place(x=200,y=370)
                       
                    table = ttk.Treeview(book, columns = ('name', 'movie','snack', 'seat'), show = 'headings')
                    table.heading('name', text = 'Name')
                    table.heading('movie', text = 'Movie')
                    table.heading('snack', text = 'Snacks')
                    table.heading('seat', text = 'Seats')
                    table.pack()
                    
                    table.column('name', width=100)
                    table.column('movie', width=100)
                    table.column('snack', width=100)
                    table.column('seat', width=100)
                    
                    if pop==1:
                        n.append('Popcorn')
                    if nacho==1:
                        n.append('Nachos')
                    if pepsi==1:
                        n.append('Pepsi')
                    if burger==1:
                        n.append('Burger')
                    if hotdog==1:
                        n.append('Hotdog')

                    name = user1
                    movie = "dunki"
                    table.insert(parent='', index=tk.END, values=(name, movie,'',''))
 
                    max_items = max(len(n), len(seatdunki))
                    for i in range(max_items):
                        snack_value = n[i] if i < len(n) else ''
                        seat_value = seatdunki[i] if i < len(seatdunki) else ''
                        table.insert(parent='', index=tk.END, values=('','',snack_value, seat_value))
                        
                    global seatmoney,snckmoney,final
                    total=seatmoney+snckmoney
                    t=pop+nacho+pepsi+burger+hotdog
                    d1=d2=0
                    if nseat>3 and t>2:
                        d1=seatmoney-(0.2*seatmoney)
                        d2=snckmoney-(0.1*snckmoney)
                        final=d1+d2
                    #Discount 1 : 10% off total if seats are greater than 3
                    elif nseat>3:
                        d1=seatmoney-(0.2*seatmoney)
                        final=d1+snckmoney
                    #Discount 2 : 10% off snckmoney if snacks are greater than 2
                    elif t>2:
                        d2=snckmoney-(0.1*snckmoney)
                        final=d2+seatmoney
                    else:
                        final=total
                    
                    lblcost = tk.Label(book, text ="Cost :",fg="black",font=("Arial", 12)) 
                    lblcost.place(x = 100, y = 200)
                    lbl1 = tk.Label(book, text ="$"+str(snckmoney),fg="black",font=("Arial", 12)) 
                    lbl1.place(x = 250, y = 200)
                    lbl2 = tk.Label(book, text ="$"+str(seatmoney),fg="black",font=("Arial", 12)) 
                    lbl2.place(x = 350, y = 200)
                    lbltot = tk.Label(book, text ="Total :",fg="black",font=("Arial", 12)) 
                    lbltot.place(x = 200, y = 230)
                    lbl3 = tk.Label(book, text ="$"+str(total),fg="black",font=("Arial", 12)) 
                    lbl3.place(x = 250, y = 230)
                    lblfinal = tk.Label(book, text ="Total after discount :",fg="black",font=("Arial", 12)) 
                    lblfinal.place(x = 200, y = 260)
                    lbl4 = tk.Label(book, text ="$"+str(final),fg="black",font=("Arial", 12)) 
                    lbl4.place(x = 350, y = 260)
                    lbldis = tk.Label(book, text ="Discounts",fg="black", borderwidth=2, relief='solid', font=("Arial", 10,'underline','bold')) 
                    lbldis.place(x = 180, y = 310)
                    lbldis1 = tk.Label(book, text ="1. For booking more than 3 seats: Reduction of 20% from the cost of seats\n 2. For selecting more than 2 snacks: Reduction of 10% from the cost of snacks",fg="black", borderwidth=2, relief='solid', font=("Times New Roman", 8)) 
                    lbldis1.place(x = 20, y = 330)

                                        
                elif nseat<1:
                        messagebox.showinfo("Booking failed ", "Please Book Seats")
                elif ver==0:
                        messagebox.showinfo("Booking failed ", "Please Login First")

            def snacks():
                global snckmoney
                snack_quantities = {'Popcorn': 0, 'Nachos': 0, 'Pepsi': 0, 'Burger': 0, 'Hotdog': 0}
                def update_display():
                    global snckmoney
                    snckmoney = sum(snack_quantities[snack] * prices[snack] for snack in snacks_list)
                    b1.config(text="$" + str(snckmoney))

                def clear():
                    for snack in snacks_list:
                        scale_vars[snack].set(0)
                        snack_quantities[snack] = 0
                    update_display()

                def on_scale_change(event):
                    snack = event.widget.snack
                    snack_quantities[snack] = scale_vars[snack].get()
                    update_display()
                    global pop,hotdog,nacho,pepsi,burger
                    if snack == 'Popcorn' and snack_quantities[snack] > 0:
                        pop = 1 
                    if snack == 'Hotdog' and snack_quantities[snack] > 0:
                        hotdog = 1 
                    if snack == 'Burger' and snack_quantities[snack] > 0:
                        burger = 1 
                    if snack == 'Pepsi' and snack_quantities[snack] > 0:
                        pepsi = 1 
                    if snack == 'Nachos' and snack_quantities[snack] > 0:
                        nacho = 1 

                frmsnck = tk.Tk()
                frmsnck.geometry("400x500")
                frmsnck.title("Snacks")
                frmsnck.configure(bg='black')

                btclr = tk.Button(frmsnck, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmsnck, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                lbltot = tk.Label(frmsnck, text="Total : ", fg='black', bg='white', font=('Times New Roman', 12, 'bold', 'underline'))
                lbltot.place(x=180, y=350)

                b1 = tk.Label(frmsnck, text="$" + str(snckmoney))
                b1.place(x=230, y=350, width=70)

                snacks_list = ['Popcorn', 'Nachos', 'Pepsi', 'Burger', 'Hotdog']
                prices = {'Popcorn': 5, 'Nachos': 7, 'Pepsi': 2, 'Burger': 15, 'Hotdog': 10}
                scale_vars = {}

                for idx, snack in enumerate(snacks_list):
                    lbl = tk.Label(frmsnck, text=f"{snack} (Cost: ${prices[snack]})", fg='black', bg='grey', font=('Times New Roman', 10, 'bold'))
                    lbl.place(x=50, y=100 + idx * 40)

                    scale_vars[snack] = tk.Scale(frmsnck, from_=0, to=5, orient=tk.HORIZONTAL, length=150)
                    scale_vars[snack].place(x=200, y=100 + idx * 40)
                    scale_vars[snack].snack = snack 
                    scale_vars[snack].bind("<ButtonRelease-1>", on_scale_change)                 
                    
            def booking():
                def taken():
                    nonlocal buttons
                    try:
                        myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                        mycur=myconn.cursor()

                        query = "select seats from dunki"
                        mycur.execute(query)
                        result=mycur.fetchall()
                        booked_seats = []
                        for tup in result:
                            elements = [elem.strip() for elem in tup[0].split(',')]
                            booked_seats.extend([elem for elem in elements if elem])
                        myconn.commit()
                        for row in range(len(buttons)):
                            for col in range(len(buttons[row])):
                                seat_label = chr(ord('a') + row) + str(col + 1)
                                if seat_label in booked_seats:
                                    buttons[row][col].configure(bg="grey", state=tk.DISABLED)

                    except Exception as e:
                        print(e)
                        
                def clear():
                    for button_row in buttons:
                        for button in button_row:
                            if button["bg"] == "red":
                                button.configure(bg="green")
                    global seatmoney, nseat
                    seatmoney = 0
                    nseat = 0
                    update_display()
                    seatdunki.clear()

                def update_display():
                    b1.config(text="$" + str(seatmoney))

                def button_click(row, col):
                    global seatmoney, nseat
                    button = buttons[row][col]
                    seat_label = chr(ord('a') + row) + str(col + 1)
                    if button["bg"] == "green":
                        button.configure(bg="red")
                        seatmoney += 20
                        nseat += 1
                        seatdunki.append(seat_label)
               
                    else:
                        button.configure(bg="green")
                        seatmoney -= 20
                        nseat -= 1
                        seatdunki.remove(seat_label)
                    
                    update_display()
                    
                frmbook = tk.Tk()
                frmbook.geometry("400x450")
                frmbook.title("Seat")
                frmbook.configure(bg='black')
                lblscr = tk.Label(frmbook, text="-----------------screen-------------------", fg='white', bg='black',
                                  font=('Times New Roman', 20))
                lblscr.place(x=5, y=100)

                btclr = tk.Button(frmbook, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmbook, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                b1 = tk.Button(frmbook, text="$" + str(seatmoney))
                b1.place(x=120, y=400, width=70)
                
                lbla = tk.Label(frmbook, text="a", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbla.place(x=5, y=150)
                lblb = tk.Label(frmbook, text="b", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblb.place(x=5, y=200)
                lblc = tk.Label(frmbook, text="c", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblc.place(x=5, y=250)
                lbld = tk.Label(frmbook, text="d", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbld.place(x=5, y=300)
                lblno = tk.Label(frmbook, text="1   2   3   4   5   6   7   8   9  10  11 12 13 14 15 16 17 18", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblno.place(x=20, y=325)
                

                buttons = []
                

                for row in range(4):
                    button_row = []
                    for col in range(18):
                        seat_label = chr(ord('a') + row) + str(col + 1)          
                        button = tk.Button(frmbook, bg='green', height=1, width=1, command=lambda r=row, c=col: button_click(r, c))
                        button.place(x=20 + col * 20, y=150 + row * 50)
                        button_row.append(button)
                    buttons.append(button_row)
                taken()
                    
            lblhd = tk.Label(frmtime, text ="Dunki", bg= 'light green',font=('MV Boli',15,'bold','underline'))
            lblhd.place(x = 170, y = 10)
            btbook= tk.Button(frmtime, text ="Book seat",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=booking) 
            btbook.place(x = 250, y = 155, width = 100)
            btsnack= tk.Button(frmtime, text ="Snacks",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=snacks) 
            btsnack.place(x = 250, y = 185, width = 100)
            lbldescrpt = tk.Label(frmtime, text ="Description", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lbldescrpt.place(x = 2, y = 40)            
            lbldes = tk.Label(frmtime, text ="4 friends from a village in Punjab share a common dream: to go England.\n Dunki is a hilarious and heartwarming saga of a perilous journey, borders,\n friendships, nostalgia for home, and love that towers\n above it all.",
                              bg= 'light green',font=('Times New Roman',10))
            lbldes.place(x = 2, y = 65)
            lblgenre = tk.Label(frmtime, text ="Genre", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblgenre.place(x = 2, y = 120)
            lblgen = tk.Label(frmtime, text ="Adventure", bg= 'light green',font=('Times New Roman',10))
            lblgen.place(x = 2, y = 145)
            lblrt = tk.Label(frmtime, text ="Running time", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblrt.place(x = 2, y = 165)
            lblrun = tk.Label(frmtime, text ="120 mins", bg= 'light green',font=('Times New Roman',10))
            lblrun.place(x = 2, y = 190)
            lblstar = tk.Label(frmtime, text ="Starring", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblstar.place(x = 2, y = 210)
            lblact = tk.Label(frmtime, text ="Rowan Atkinson, Timothee Chalamet,\n Calah Lane, Keegan Michael Key", bg= 'light green',font=('Times New Roman',10))
            lblact.place(x = 2, y = 235)
            
            link = tk.Label(frmtime, text="Trailer", 
            fg="blue", bg="light green",cursor="hand2",font=['Times',15,'underline'])
            link.place(x=160, y=155)
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://youtu.be/ACKQDAlAfFE?si=FarPE9zOrQwU6ijq"))

        def showtimes2():
            frmtime=tk.Tk()
            frmtime.geometry("400x300")
            frmtime.title("Animal")
            frmtime.configure(bg='light green')
            def end():
                global nseat,final
                global user1, i_d1
                seat1=snacks1=''
                for ele in seatanimal:
                    seat1+= ele + ', '
                for ele in n:
                    snacks1+= ele + ', '
                  
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()

                    query = "INSERT INTO animal (c_name, acc_id, snacks, `number of seats`, seats, cost) VALUES ('{}', '{}', '{}', {}, '{}',{})".format(user1, i_d1, snacks1, nseat, seat1,final)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Booking Successful", "Booking Successful, Enjoy your Movie")
                
                except Exception as e:
                    print(e)
                    
            def book():
                global nseat
                if nseat>=1 and ver==1:
                    book = tk.Tk() 
                    book.geometry("400x400")
                    book.title("Booking")
                    
                    global user1
                    global pop,nacho,pepsi,burger,hotdog
                          
                    btb=Button(book,text="book",fg='black',bg='red', command=end)
                    btb.place(x=200,y=370)
                       
                    table = ttk.Treeview(book, columns = ('name', 'movie','snack', 'seat'), show = 'headings')
                    table.heading('name', text = 'Name')
                    table.heading('movie', text = 'Movie')
                    table.heading('snack', text = 'Snacks')
                    table.heading('seat', text = 'Seats')
                    table.pack()
                    
                    table.column('name', width=100)
                    table.column('movie', width=100)
                    table.column('snack', width=100)
                    table.column('seat', width=100)
                    
                    if pop==1:
                        n.append('Popcorn')
                    if nacho==1:
                        n.append('Nachos')
                    if pepsi==1:
                        n.append('Pepsi')
                    if burger==1:
                        n.append('Burger')
                    if hotdog==1:
                        n.append('Hotdog')

                    name = user1
                    movie = "animal"
                    table.insert(parent='', index=tk.END, values=(name, movie,'',''))
 
                    max_items = max(len(n), len(seatanimal))
                    for i in range(max_items):
                        snack_value = n[i] if i < len(n) else ''
                        seat_value = seatanimal[i] if i < len(seatanimal) else ''
                        table.insert(parent='', index=tk.END, values=('','',snack_value, seat_value))
                        
                    global seatmoney,snckmoney,final
                    total=seatmoney+snckmoney
                    t=pop+nacho+pepsi+burger+hotdog
                    d1=d2=0
                    if nseat>3 and t>2:
                        d1=seatmoney-(0.2*seatmoney)
                        d2=snckmoney-(0.1*snckmoney)
                        final=d1+d2
                    #Discount 1 : 10% off total if seats are greater than 3
                    elif nseat>3:
                        d1=seatmoney-(0.2*seatmoney)
                        final=d1+snckmoney
                    #Discount 2 : 10% off snckmoney if snacks are greater than 2
                    elif t>2:
                        d2=snckmoney-(0.1*snckmoney)
                        final=d2+seatmoney
                    else:
                        final=total
                    
                    lblcost = tk.Label(book, text ="Cost :",fg="black",font=("Arial", 12)) 
                    lblcost.place(x = 100, y = 200)
                    lbl1 = tk.Label(book, text ="$"+str(snckmoney),fg="black",font=("Arial", 12)) 
                    lbl1.place(x = 250, y = 200)
                    lbl2 = tk.Label(book, text ="$"+str(seatmoney),fg="black",font=("Arial", 12)) 
                    lbl2.place(x = 350, y = 200)
                    lbltot = tk.Label(book, text ="Total :",fg="black",font=("Arial", 12)) 
                    lbltot.place(x = 200, y = 230)
                    lbl3 = tk.Label(book, text ="$"+str(total),fg="black",font=("Arial", 12)) 
                    lbl3.place(x = 250, y = 230)
                    lblfinal = tk.Label(book, text ="Total after discount :",fg="black",font=("Arial", 12)) 
                    lblfinal.place(x = 200, y = 260)
                    lbl4 = tk.Label(book, text ="$"+str(final),fg="black",font=("Arial", 12)) 
                    lbl4.place(x = 350, y = 260)
                    lbldis = tk.Label(book, text ="Discounts",fg="black", borderwidth=2, relief='solid', font=("Arial", 10,'underline','bold')) 
                    lbldis.place(x = 180, y = 310)
                    lbldis1 = tk.Label(book, text ="1. For booking more than 3 seats: Reduction of 20% from the cost of seats\n 2. For selecting more than 2 snacks: Reduction of 10% from the cost of snacks",fg="black", borderwidth=2, relief='solid', font=("Times New Roman", 8)) 
                    lbldis1.place(x = 20, y = 330)

                                        
                elif nseat<1:
                        messagebox.showinfo("Booking failed ", "Please Book Seats")
                elif ver==0:
                        messagebox.showinfo("Booking failed ", "Please Login First")

            def snacks():
                global snckmoney
                snack_quantities = {'Popcorn': 0, 'Nachos': 0, 'Pepsi': 0, 'Burger': 0, 'Hotdog': 0}
                def update_display():
                    global snckmoney
                    snckmoney = sum(snack_quantities[snack] * prices[snack] for snack in snacks_list)
                    b1.config(text="$" + str(snckmoney))

                def clear():
                    for snack in snacks_list:
                        scale_vars[snack].set(0)
                        snack_quantities[snack] = 0
                    update_display()

                def on_scale_change(event):
                    snack = event.widget.snack
                    snack_quantities[snack] = scale_vars[snack].get()
                    update_display()
                    global pop,hotdog,nacho,pepsi,burger
                    if snack == 'Popcorn' and snack_quantities[snack] > 0:
                        pop = 1 
                    if snack == 'Hotdog' and snack_quantities[snack] > 0:
                        hotdog = 1 
                    if snack == 'Burger' and snack_quantities[snack] > 0:
                        burger = 1 
                    if snack == 'Pepsi' and snack_quantities[snack] > 0:
                        pepsi = 1 
                    if snack == 'Nachos' and snack_quantities[snack] > 0:
                        nacho = 1 

                frmsnck = tk.Tk()
                frmsnck.geometry("400x500")
                frmsnck.title("Snacks")
                frmsnck.configure(bg='black')

                btclr = tk.Button(frmsnck, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmsnck, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                lbltot = tk.Label(frmsnck, text="Total : ", fg='black', bg='white', font=('Times New Roman', 12, 'bold', 'underline'))
                lbltot.place(x=180, y=350)

                b1 = tk.Label(frmsnck, text="$" + str(snckmoney))
                b1.place(x=230, y=350, width=70)

                snacks_list = ['Popcorn', 'Nachos', 'Pepsi', 'Burger', 'Hotdog']
                prices = {'Popcorn': 5, 'Nachos': 7, 'Pepsi': 2, 'Burger': 15, 'Hotdog': 10}
                scale_vars = {}

                for idx, snack in enumerate(snacks_list):
                    lbl = tk.Label(frmsnck, text=f"{snack} (Cost: ${prices[snack]})", fg='black', bg='grey', font=('Times New Roman', 10, 'bold'))
                    lbl.place(x=50, y=100 + idx * 40)

                    scale_vars[snack] = tk.Scale(frmsnck, from_=0, to=5, orient=tk.HORIZONTAL, length=150)
                    scale_vars[snack].place(x=200, y=100 + idx * 40)
                    scale_vars[snack].snack = snack 
                    scale_vars[snack].bind("<ButtonRelease-1>", on_scale_change)                 
                    
            def booking():
                def taken():
                    nonlocal buttons
                    try:
                        myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                        mycur=myconn.cursor()

                        query = "select seats from animal"
                        mycur.execute(query)
                        result=mycur.fetchall()
                        booked_seats = []
                        for tup in result:
                            elements = [elem.strip() for elem in tup[0].split(',')]
                            booked_seats.extend([elem for elem in elements if elem])
                        myconn.commit()
                        for row in range(len(buttons)):
                            for col in range(len(buttons[row])):
                                seat_label = chr(ord('a') + row) + str(col + 1)
                                if seat_label in booked_seats:
                                    buttons[row][col].configure(bg="grey", state=tk.DISABLED)

                    except Exception as e:
                        print(e)
                        
                def clear():
                    for button_row in buttons:
                        for button in button_row:
                            if button["bg"] == "red":
                                button.configure(bg="green")
                    
                    global seatmoney, nseat
                    seatmoney = 0
                    nseat = 0
                    update_display()
                    seatanimal.clear()

                def update_display():
                    b1.config(text="$" + str(seatmoney))

                def button_click(row, col):
                    global seatmoney, nseat
                    button = buttons[row][col]
                    seat_label = chr(ord('a') + row) + str(col + 1)
                    if button["bg"] == "green":
                        button.configure(bg="red")
                        seatmoney += 20
                        nseat += 1
                        seatanimal.append(seat_label)
               
                    else:
                        button.configure(bg="green")
                        seatmoney -= 20
                        nseat -= 1
                        seatanimal.remove(seat_label)
                    
                    update_display()
                    
                frmbook = tk.Tk()
                frmbook.geometry("400x450")
                frmbook.title("Seat")
                frmbook.configure(bg='black')
                lblscr = tk.Label(frmbook, text="-----------------screen-------------------", fg='white', bg='black',
                                  font=('Times New Roman', 20))
                lblscr.place(x=5, y=100)

                btclr = tk.Button(frmbook, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmbook, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                b1 = tk.Button(frmbook, text="$" + str(seatmoney))
                b1.place(x=120, y=400, width=70)
                
                lbla = tk.Label(frmbook, text="a", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbla.place(x=5, y=150)
                lblb = tk.Label(frmbook, text="b", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblb.place(x=5, y=200)
                lblc = tk.Label(frmbook, text="c", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblc.place(x=5, y=250)
                lbld = tk.Label(frmbook, text="d", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbld.place(x=5, y=300)
                lblno = tk.Label(frmbook, text="1   2   3   4   5   6   7   8   9  10  11 12 13 14 15 16 17 18", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblno.place(x=20, y=325)
                

                buttons = []
                

                for row in range(4):
                    button_row = []
                    for col in range(18):
                        seat_label = chr(ord('a') + row) + str(col + 1)          
                        button = tk.Button(frmbook, bg='green', height=1, width=1, command=lambda r=row, c=col: button_click(r, c))
                        button.place(x=20 + col * 20, y=150 + row * 50)
                        button_row.append(button)
                    buttons.append(button_row)
                taken()
                    
            lblhd = tk.Label(frmtime, text ="Animal", bg= 'light green',font=('MV Boli',15,'bold','underline'))
            lblhd.place(x = 170, y = 10)
            btbook= tk.Button(frmtime, text ="Book seat",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=booking) 
            btbook.place(x = 250, y = 155, width = 100)
            btsnack= tk.Button(frmtime, text ="Snacks",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=snacks) 
            btsnack.place(x = 250, y = 185, width = 100)
            lbldescrpt = tk.Label(frmtime, text ="Description", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lbldescrpt.place(x = 2, y = 40)            
            lbldes = tk.Label(frmtime, text ="Animal revolves around a troubled father-son relationship, set in the\n backdrop of extreme bloodshed of the underworld which leads to the\n protagonist to turn into a psychopath.",
                              bg= 'light green',font=('Times New Roman',10))
            lbldes.place(x = 2, y = 65)
            lblgenre = tk.Label(frmtime, text ="Genre", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblgenre.place(x = 2, y = 110)
            lblgen = tk.Label(frmtime, text ="Action", bg= 'light green',font=('Times New Roman',10))
            lblgen.place(x = 2, y = 135)
            lblrt = tk.Label(frmtime, text ="Running time", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblrt.place(x = 2, y = 155)
            lblrun = tk.Label(frmtime, text ="210 mins", bg= 'light green',font=('Times New Roman',10))
            lblrun.place(x = 2, y = 180)
            lblstar = tk.Label(frmtime, text ="Starring", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblstar.place(x = 2, y = 200)
            lblact = tk.Label(frmtime, text ="Ranbir Kapoor, Tripti Dimri,\n Anil Kapoor, Rashmika Mandana", bg= 'light green',font=('Times New Roman',10))
            lblact.place(x = 2, y = 225)
            
            link = tk.Label(frmtime, text="Trailer", 
            fg="blue", bg="light green",cursor="hand2",font=['Times',15,'underline'])
            link.place(x=160, y=155)
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://youtu.be/8FkLRUJj-o0?si=csJ_3nPv6RIyhixT"))
        
        img1 = ImageTk.PhotoImage(Image.open("dunki.jpg"))
        button1= Button(frmhin, image = img1, command = showtimes1)
        button1.place(x = 50, y = 150)
        img2 = ImageTk.PhotoImage(Image.open("animal.jpg"))
        button2= Button(frmhin, image = img2, command = showtimes2)
        button2.place(x = 350, y = 150)
        root.mainloop()
        
    def Malayalam():
        root.destroy()
        frmmal=tk.Tk()
        frmmal.geometry("600x600")
        frmmal.title("Malayalam Movies")
        frmmal.configure(bg='light blue')
        bg = ImageTk.PhotoImage(Image.open("bg2.jpg"))
        button3= Button(frmmal, image = bg)
        button3.pack()
        lbllan = tk.Label(frmmal, text ="MALAYALAM MOVIES", fg= 'white', bg= 'black',font=('MV Boli',25,'bold','underline'))
        lbllan.place(x = 120, y = 15)
        
        def loginscreen():
            def funclear():
                txtUser.delete(0,END)
                txtpass.delete(0,END)
                txtUser.focus()

            def funlogin():
                user = txtUser.get() 
                passw = txtpass.get()
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()
                    query="select * from customer where c_name='{}' and pass='{}'".format(user,passw)
                    mycur.execute(query)
                    rs=mycur.fetchone()
                    if rs!=None and user==rs[0] and passw==rs[2]:
                        global ver
                        ver=1
                        global user1
                        user1=user
                        passw=txtpass.get()
                        l=user+passw
                        global i_d1
                        for ch in l:
                            i_d1+=str(ord(ch))
                        messagebox.showinfo("Login ", "Login Successful")
                        login.destroy()
                        btlogin.destroy()
                        lblacc = tk.Label(frmmal, text ="Account name:", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                        lblacc.place(x = 470, y = 5)
                        lblus = tk.Label(frmmal, text =user1, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                        lblus.place(x = 555, y = 5)
                    else:
                        messagebox.showinfo("Login", "Login Failed")
                except Exception as e:
                    print(e)
            
            def register():
                i_d=''
                user=txtUser.get() 
                passw=txtpass.get()
                l=user+passw
                for ch in l:
                    i_d+=str(ord(ch))
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()
                    query="insert into customer values('{}',{},'{}')".format(user,i_d,passw)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Registration", "Registration Successful, you may Login now")
                    funclear()
                except Exception as e:
                    messagebox.showinfo("Login", "Login Failed")
                
        
            login = tk.Tk() 
            login.geometry("300x300")
            login.title("Login Page") 
            C = Canvas(login, bg ="Red", height = 250, width = 300) 
            lbluser = tk.Label(login, text ="Username -",fg="red",font=("Times New Roman Bold", 10) ) 
            lbluser.place(x = 50, y = 20) 
            txtUser = tk.Entry(login, width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
            txtUser.place(x = 150, y = 20, width = 100) 
            lblpass = tk.Label(login, text ="Password -",fg="red",font=("Times New Roman Bold", 10)) 
            lblpass.place(x = 50, y = 50) 
            txtpass = tk.Entry(login,show="*", width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
            txtpass.place(x = 150, y = 50, width = 100) 
            loginbtn = tk.Button(login, text ="Login", fg ='blue', font=("Times New Roman Bold", 10),command = funlogin) 
            loginbtn.place(x = 140, y = 135, width = 55)
            regbtn = tk.Button(login, text ="Register", fg ='blue', font=("Times New Roman Bold", 10),command = register) 
            regbtn.place(x = 80, y = 135, width = 55)
            clearbtn = tk.Button(login, text ="Clear",fg ='blue', font=("Times New Roman Bold", 10),command = funclear) 
            clearbtn.place(x = 200, y = 135, width = 55)
        
        if ver==0:
            btlogin = tk.Button(frmmal, text ="login",fg ='white',bg= 'red',font=("Times New Roman Bold", 10),command=loginscreen) 
            btlogin.place(x = 530, y = 5, width = 60)
        if ver==1:
            lblacc = tk.Label(frmmal, text ="Account name:", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
            lblacc.place(x = 470, y = 5)
            lblus = tk.Label(frmmal, text =user1, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
            lblus.place(x = 555, y = 5)
        
        def showtimes1():
            frmtime=tk.Tk()
            frmtime.geometry("400x300")
            frmtime.title("Neru")
            frmtime.configure(bg='light green')
            def end():
                global nseat,final
                global user1, i_d1
                seat1=snacks1=''
                for ele in seatneru:
                    seat1+= ele + ', '
                for ele in n:
                    snacks1+= ele + ', '
                  
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()

                    query = "INSERT INTO neru (c_name, acc_id, snacks, `number of seats`, seats, cost) VALUES ('{}', '{}', '{}', {}, '{}',{})".format(user1, i_d1, snacks1, nseat, seat1,final)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Booking Successful", "Booking Successful, Enjoy your Movie")
                
                except Exception as e:
                    print(e)
                    
            def book():
                global nseat
                if nseat>=1 and ver==1:
                    book = tk.Tk() 
                    book.geometry("400x400")
                    book.title("Booking")
                    
                    global user1
                    global pop,nacho,pepsi,burger,hotdog
                          
                    btb=Button(book,text="book",fg='black',bg='red', command=end)
                    btb.place(x=200,y=370)
                       
                    table = ttk.Treeview(book, columns = ('name', 'movie','snack', 'seat'), show = 'headings')
                    table.heading('name', text = 'Name')
                    table.heading('movie', text = 'Movie')
                    table.heading('snack', text = 'Snacks')
                    table.heading('seat', text = 'Seats')
                    table.pack()
                    
                    table.column('name', width=100)
                    table.column('movie', width=100)
                    table.column('snack', width=100)
                    table.column('seat', width=100)
                    
                    if pop==1:
                        n.append('Popcorn')
                    if nacho==1:
                        n.append('Nachos')
                    if pepsi==1:
                        n.append('Pepsi')
                    if burger==1:
                        n.append('Burger')
                    if hotdog==1:
                        n.append('Hotdog')

                    name = user1
                    movie = "neru"
                    table.insert(parent='', index=tk.END, values=(name, movie,'',''))
 
                    max_items = max(len(n), len(seatneru))
                    for i in range(max_items):
                        snack_value = n[i] if i < len(n) else ''
                        seat_value = seatneru[i] if i < len(seatneru) else ''
                        table.insert(parent='', index=tk.END, values=('','',snack_value, seat_value))
                        
                    global seatmoney,snckmoney,final
                    total=seatmoney+snckmoney
                    t=pop+nacho+pepsi+burger+hotdog
                    d1=d2=0
                    if nseat>3 and t>2:
                        d1=seatmoney-(0.2*seatmoney)
                        d2=snckmoney-(0.1*snckmoney)
                        final=d1+d2
                    #Discount 1 : 10% off total if seats are greater than 3
                    elif nseat>3:
                        d1=seatmoney-(0.2*seatmoney)
                        final=d1+snckmoney
                    #Discount 2 : 10% off snckmoney if snacks are greater than 2
                    elif t>2:
                        d2=snckmoney-(0.1*snckmoney)
                        final=d2+seatmoney
                    else:
                        final=total
                    
                    lblcost = tk.Label(book, text ="Cost :",fg="black",font=("Arial", 12)) 
                    lblcost.place(x = 100, y = 200)
                    lbl1 = tk.Label(book, text ="$"+str(snckmoney),fg="black",font=("Arial", 12)) 
                    lbl1.place(x = 250, y = 200)
                    lbl2 = tk.Label(book, text ="$"+str(seatmoney),fg="black",font=("Arial", 12)) 
                    lbl2.place(x = 350, y = 200)
                    lbltot = tk.Label(book, text ="Total :",fg="black",font=("Arial", 12)) 
                    lbltot.place(x = 200, y = 230)
                    lbl3 = tk.Label(book, text ="$"+str(total),fg="black",font=("Arial", 12)) 
                    lbl3.place(x = 250, y = 230)
                    lblfinal = tk.Label(book, text ="Total after discount :",fg="black",font=("Arial", 12)) 
                    lblfinal.place(x = 200, y = 260)
                    lbl4 = tk.Label(book, text ="$"+str(final),fg="black",font=("Arial", 12)) 
                    lbl4.place(x = 350, y = 260)
                    lbldis = tk.Label(book, text ="Discounts",fg="black", borderwidth=2, relief='solid', font=("Arial", 10,'underline','bold')) 
                    lbldis.place(x = 180, y = 310)
                    lbldis1 = tk.Label(book, text ="1. For booking more than 3 seats: Reduction of 20% from the cost of seats\n 2. For selecting more than 2 snacks: Reduction of 10% from the cost of snacks",fg="black", borderwidth=2, relief='solid', font=("Times New Roman", 8)) 
                    lbldis1.place(x = 20, y = 330)

                                        
                elif nseat<1:
                        messagebox.showinfo("Booking failed ", "Please Book Seats")
                elif ver==0:
                        messagebox.showinfo("Booking failed ", "Please Login First")

            def snacks():
                global snckmoney
                snack_quantities = {'Popcorn': 0, 'Nachos': 0, 'Pepsi': 0, 'Burger': 0, 'Hotdog': 0}
                def update_display():
                    global snckmoney
                    snckmoney = sum(snack_quantities[snack] * prices[snack] for snack in snacks_list)
                    b1.config(text="$" + str(snckmoney))

                def clear():
                    for snack in snacks_list:
                        scale_vars[snack].set(0)
                        snack_quantities[snack] = 0
                    update_display()

                def on_scale_change(event):
                    snack = event.widget.snack
                    snack_quantities[snack] = scale_vars[snack].get()
                    update_display()
                    global pop,hotdog,nacho,pepsi,burger
                    if snack == 'Popcorn' and snack_quantities[snack] > 0:
                        pop = 1 
                    if snack == 'Hotdog' and snack_quantities[snack] > 0:
                        hotdog = 1 
                    if snack == 'Burger' and snack_quantities[snack] > 0:
                        burger = 1 
                    if snack == 'Pepsi' and snack_quantities[snack] > 0:
                        pepsi = 1 
                    if snack == 'Nachos' and snack_quantities[snack] > 0:
                        nacho = 1 

                frmsnck = tk.Tk()
                frmsnck.geometry("400x500")
                frmsnck.title("Snacks")
                frmsnck.configure(bg='black')

                btclr = tk.Button(frmsnck, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmsnck, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                lbltot = tk.Label(frmsnck, text="Total : ", fg='black', bg='white', font=('Times New Roman', 12, 'bold', 'underline'))
                lbltot.place(x=180, y=350)

                b1 = tk.Label(frmsnck, text="$" + str(snckmoney))
                b1.place(x=230, y=350, width=70)

                snacks_list = ['Popcorn', 'Nachos', 'Pepsi', 'Burger', 'Hotdog']
                prices = {'Popcorn': 5, 'Nachos': 7, 'Pepsi': 2, 'Burger': 15, 'Hotdog': 10}
                scale_vars = {}

                for idx, snack in enumerate(snacks_list):
                    lbl = tk.Label(frmsnck, text=f"{snack} (Cost: ${prices[snack]})", fg='black', bg='grey', font=('Times New Roman', 10, 'bold'))
                    lbl.place(x=50, y=100 + idx * 40)

                    scale_vars[snack] = tk.Scale(frmsnck, from_=0, to=5, orient=tk.HORIZONTAL, length=150)
                    scale_vars[snack].place(x=200, y=100 + idx * 40)
                    scale_vars[snack].snack = snack 
                    scale_vars[snack].bind("<ButtonRelease-1>", on_scale_change)                 
                    
            def booking():
                def taken():
                    nonlocal buttons
                    try:
                        myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                        mycur=myconn.cursor()

                        query = "select seats from neru"
                        mycur.execute(query)
                        result=mycur.fetchall()
                        booked_seats = []
                        for tup in result:
                            elements = [elem.strip() for elem in tup[0].split(',')]
                            booked_seats.extend([elem for elem in elements if elem])
                        myconn.commit()
                        for row in range(len(buttons)):
                            for col in range(len(buttons[row])):
                                seat_label = chr(ord('a') + row) + str(col + 1)
                                if seat_label in booked_seats:
                                    buttons[row][col].configure(bg="grey", state=tk.DISABLED)

                    except Exception as e:
                        print(e)
                        
                def clear():
                    for button_row in buttons:
                        for button in button_row:
                            if button["bg"] == "red":
                                button.configure(bg="green")
                    global seatmoney, nseat
                    seatmoney = 0
                    nseat = 0
                    update_display()
                    seatneru.clear()

                def update_display():
                    b1.config(text="$" + str(seatmoney))

                def button_click(row, col):
                    global seatmoney, nseat
                    button = buttons[row][col]
                    seat_label = chr(ord('a') + row) + str(col + 1)
                    if button["bg"] == "green":
                        button.configure(bg="red")
                        seatmoney += 20
                        nseat += 1
                        seatneru.append(seat_label)
               
                    else:
                        button.configure(bg="green")
                        seatmoney -= 20
                        nseat -= 1
                        seatneru.remove(seat_label)
                    
                    update_display()
                    
                frmbook = tk.Tk()
                frmbook.geometry("400x450")
                frmbook.title("Seat")
                frmbook.configure(bg='black')
                lblscr = tk.Label(frmbook, text="-----------------screen-------------------", fg='white', bg='black',
                                  font=('Times New Roman', 20))
                lblscr.place(x=5, y=100)

                btclr = tk.Button(frmbook, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmbook, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                b1 = tk.Button(frmbook, text="$" + str(seatmoney))
                b1.place(x=120, y=400, width=70)
                
                lbla = tk.Label(frmbook, text="a", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbla.place(x=5, y=150)
                lblb = tk.Label(frmbook, text="b", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblb.place(x=5, y=200)
                lblc = tk.Label(frmbook, text="c", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblc.place(x=5, y=250)
                lbld = tk.Label(frmbook, text="d", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbld.place(x=5, y=300)
                lblno = tk.Label(frmbook, text="1   2   3   4   5   6   7   8   9  10  11 12 13 14 15 16 17 18", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblno.place(x=20, y=325)
                

                buttons = []
                

                for row in range(4):
                    button_row = []
                    for col in range(18):
                        seat_label = chr(ord('a') + row) + str(col + 1)          
                        button = tk.Button(frmbook, bg='green', height=1, width=1, command=lambda r=row, c=col: button_click(r, c))
                        button.place(x=20 + col * 20, y=150 + row * 50)
                        button_row.append(button)
                    buttons.append(button_row)
                taken()
                    
            btbook= tk.Button(frmtime, text ="Book seat",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=booking) 
            btbook.place(x = 250, y = 155, width = 100)
            btsnack= tk.Button(frmtime, text ="Snacks",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=snacks) 
            btsnack.place(x = 250, y = 185, width = 100)
            lblhd = tk.Label(frmtime, text ="Neru", bg= 'light green',font=('MV Boli',15,'bold','underline'))
            lblhd.place(x = 170, y = 10)
            lbldescrpt = tk.Label(frmtime, text ="Description", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lbldescrpt.place(x = 2, y = 40)            
            lbldes = tk.Label(frmtime, text ="Set against the backdrop of the Indian legal system. NERU is a gripping\n legal and emotional drama that unfolds the tale of Sara, a blind sculpture\n artist who seeks justice after a traumatic incident.",
                              bg= 'light green',font=('Times New Roman',10))
            lbldes.place(x = 2, y = 65)
            lblgenre = tk.Label(frmtime, text ="Genre", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblgenre.place(x = 2, y = 110)
            lblgen = tk.Label(frmtime, text ="Drama", bg= 'light green',font=('Times New Roman',10))
            lblgen.place(x = 2, y = 135)
            lblrt = tk.Label(frmtime, text ="Running time", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblrt.place(x = 2, y = 155)
            lblrun = tk.Label(frmtime, text ="165 mins", bg= 'light green',font=('Times New Roman',10))
            lblrun.place(x = 2, y = 180)
            lblstar = tk.Label(frmtime, text ="Starring", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblstar.place(x = 2, y = 200)
            lblact = tk.Label(frmtime, text ="Mohanlal, Siddique,\n Anaswara, Jagadish", bg= 'light green',font=('Times New Roman',10))
            lblact.place(x = 2, y = 225)
            
            link = tk.Label(frmtime, text="Trailer", 
            fg="blue", bg="light green", cursor="hand2",font=['Times',15,'underline'])
            link.place(x=160, y=155)
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://youtu.be/abuLOH7xs8I?si=YgLa7WDfZXsf95lz"))
        
            
        def showtimes2():
            frmtime=tk.Tk()
            frmtime.geometry("400x300")
            frmtime.title("Raastha")
            frmtime.configure(bg='light green')
            def end():
                global nseat,final
                global user1, i_d1
                seat1=snacks1=''
                for ele in seatraastha:
                    seat1+= ele + ', '
                for ele in n:
                    snacks1+= ele + ', '
                  
                try:
                    myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                    mycur=myconn.cursor()

                    query = "INSERT INTO raastha (c_name, acc_id, snacks, `number of seats`, seats, cost) VALUES ('{}', '{}', '{}', {}, '{}',{})".format(user1, i_d1, snacks1, nseat, seat1,final)
                    mycur.execute(query)
                    myconn.commit()
                    messagebox.showinfo("Booking Successful", "Booking Successful, Enjoy your Movie")
                
                except Exception as e:
                    print(e)
                    
            def book():
                global nseat
                if nseat>=1 and ver==1:
                    book = tk.Tk() 
                    book.geometry("400x400")
                    book.title("Booking")
                    
                    global user1
                    global pop,nacho,pepsi,burger,hotdog
                          
                    btb=Button(book,text="book",fg='black',bg='red', command=end)
                    btb.place(x=200,y=370)
                       
                    table = ttk.Treeview(book, columns = ('name', 'movie','snack', 'seat'), show = 'headings')
                    table.heading('name', text = 'Name')
                    table.heading('movie', text = 'Movie')
                    table.heading('snack', text = 'Snacks')
                    table.heading('seat', text = 'Seats')
                    table.pack()
                    
                    table.column('name', width=100)
                    table.column('movie', width=100)
                    table.column('snack', width=100)
                    table.column('seat', width=100)
                    
                    if pop==1:
                        n.append('Popcorn')
                    if nacho==1:
                        n.append('Nachos')
                    if pepsi==1:
                        n.append('Pepsi')
                    if burger==1:
                        n.append('Burger')
                    if hotdog==1:
                        n.append('Hotdog')

                    name = user1
                    movie = "raastha"
                    table.insert(parent='', index=tk.END, values=(name, movie,'',''))
 
                    max_items = max(len(n), len(seatraastha))
                    for i in range(max_items):
                        snack_value = n[i] if i < len(n) else ''
                        seat_value = seatraastha[i] if i < len(seatraastha) else ''
                        table.insert(parent='', index=tk.END, values=('','',snack_value, seat_value))
                        
                    global seatmoney,snckmoney,final
                    total=seatmoney+snckmoney
                    t=pop+nacho+pepsi+burger+hotdog
                    d1=d2=0
                    if nseat>3 and t>2:
                        d1=seatmoney-(0.2*seatmoney)
                        d2=snckmoney-(0.1*snckmoney)
                        final=d1+d2
                    #Discount 1 : 10% off total if seats are greater than 3
                    elif nseat>3:
                        d1=seatmoney-(0.2*seatmoney)
                        final=d1+snckmoney
                    #Discount 2 : 10% off snckmoney if snacks are greater than 2
                    elif t>2:
                        d2=snckmoney-(0.1*snckmoney)
                        final=d2+seatmoney
                    else:
                        final=total
                    
                    lblcost = tk.Label(book, text ="Cost :",fg="black",font=("Arial", 12)) 
                    lblcost.place(x = 100, y = 200)
                    lbl1 = tk.Label(book, text ="$"+str(snckmoney),fg="black",font=("Arial", 12)) 
                    lbl1.place(x = 250, y = 200)
                    lbl2 = tk.Label(book, text ="$"+str(seatmoney),fg="black",font=("Arial", 12)) 
                    lbl2.place(x = 350, y = 200)
                    lbltot = tk.Label(book, text ="Total :",fg="black",font=("Arial", 12)) 
                    lbltot.place(x = 200, y = 230)
                    lbl3 = tk.Label(book, text ="$"+str(total),fg="black",font=("Arial", 12)) 
                    lbl3.place(x = 250, y = 230)
                    lblfinal = tk.Label(book, text ="Total after discount :",fg="black",font=("Arial", 12)) 
                    lblfinal.place(x = 200, y = 260)
                    lbl4 = tk.Label(book, text ="$"+str(final),fg="black",font=("Arial", 12)) 
                    lbl4.place(x = 350, y = 260)
                    lbldis = tk.Label(book, text ="Discounts",fg="black", borderwidth=2, relief='solid', font=("Arial", 10,'underline','bold')) 
                    lbldis.place(x = 180, y = 310)
                    lbldis1 = tk.Label(book, text ="1. For booking more than 3 seats: Reduction of 20% from the cost of seats\n 2. For selecting more than 2 snacks: Reduction of 10% from the cost of snacks",fg="black", borderwidth=2, relief='solid', font=("Times New Roman", 8)) 
                    lbldis1.place(x = 20, y = 330)

                                        
                elif nseat<1:
                        messagebox.showinfo("Booking failed ", "Please Book Seats")
                elif ver==0:
                        messagebox.showinfo("Booking failed ", "Please Login First")

            def snacks():
                global snckmoney
                snack_quantities = {'Popcorn': 0, 'Nachos': 0, 'Pepsi': 0, 'Burger': 0, 'Hotdog': 0}
                def update_display():
                    global snckmoney
                    snckmoney = sum(snack_quantities[snack] * prices[snack] for snack in snacks_list)
                    b1.config(text="$" + str(snckmoney))

                def clear():
                    for snack in snacks_list:
                        scale_vars[snack].set(0)
                        snack_quantities[snack] = 0
                    update_display()

                def on_scale_change(event):
                    snack = event.widget.snack
                    snack_quantities[snack] = scale_vars[snack].get()
                    update_display()
                    global pop,hotdog,nacho,pepsi,burger
                    if snack == 'Popcorn' and snack_quantities[snack] > 0:
                        pop = 1 
                    if snack == 'Hotdog' and snack_quantities[snack] > 0:
                        hotdog = 1 
                    if snack == 'Burger' and snack_quantities[snack] > 0:
                        burger = 1 
                    if snack == 'Pepsi' and snack_quantities[snack] > 0:
                        pepsi = 1 
                    if snack == 'Nachos' and snack_quantities[snack] > 0:
                        nacho = 1 

                frmsnck = tk.Tk()
                frmsnck.geometry("400x500")
                frmsnck.title("Snacks")
                frmsnck.configure(bg='black')

                btclr = tk.Button(frmsnck, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmsnck, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                lbltot = tk.Label(frmsnck, text="Total : ", fg='black', bg='white', font=('Times New Roman', 12, 'bold', 'underline'))
                lbltot.place(x=180, y=350)

                b1 = tk.Label(frmsnck, text="$" + str(snckmoney))
                b1.place(x=230, y=350, width=70)

                snacks_list = ['Popcorn', 'Nachos', 'Pepsi', 'Burger', 'Hotdog']
                prices = {'Popcorn': 5, 'Nachos': 7, 'Pepsi': 2, 'Burger': 15, 'Hotdog': 10}
                scale_vars = {}

                for idx, snack in enumerate(snacks_list):
                    lbl = tk.Label(frmsnck, text=f"{snack} (Cost: ${prices[snack]})", fg='black', bg='grey', font=('Times New Roman', 10, 'bold'))
                    lbl.place(x=50, y=100 + idx * 40)

                    scale_vars[snack] = tk.Scale(frmsnck, from_=0, to=5, orient=tk.HORIZONTAL, length=150)
                    scale_vars[snack].place(x=200, y=100 + idx * 40)
                    scale_vars[snack].snack = snack 
                    scale_vars[snack].bind("<ButtonRelease-1>", on_scale_change)                 
                    
            def booking():
                def taken():
                    nonlocal buttons
                    try:
                        myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                        mycur=myconn.cursor()

                        query = "select seats from raastha"
                        mycur.execute(query)
                        result=mycur.fetchall()
                        booked_seats = []
                        for tup in result:
                            elements = [elem.strip() for elem in tup[0].split(',')]
                            booked_seats.extend([elem for elem in elements if elem])
                        myconn.commit()
                        for row in range(len(buttons)):
                            for col in range(len(buttons[row])):
                                seat_label = chr(ord('a') + row) + str(col + 1)
                                if seat_label in booked_seats:
                                    buttons[row][col].configure(bg="grey", state=tk.DISABLED)

                    except Exception as e:
                        print(e)
                        
                def clear():
                    for button_row in buttons:
                        for button in button_row:
                            if button["bg"] == "red":
                                button.configure(bg="green")
                    global seatmoney, nseat
                    seatmoney = 0
                    nseat = 0
                    update_display()
                    seatraastha.clear()

                def update_display():
                    b1.config(text="$" + str(seatmoney))

                def button_click(row, col):
                    global seatmoney, nseat
                    button = buttons[row][col]
                    seat_label = chr(ord('a') + row) + str(col + 1)
                    if button["bg"] == "green":
                        button.configure(bg="red")
                        seatmoney += 20
                        nseat += 1
                        seatraastha.append(seat_label)
               
                    else:
                        button.configure(bg="green")
                        seatmoney -= 20
                        nseat -= 1
                        seatraastha.remove(seat_label)
                    
                    update_display()
                    
                frmbook = tk.Tk()
                frmbook.geometry("400x450")
                frmbook.title("Seat")
                frmbook.configure(bg='black')
                lblscr = tk.Label(frmbook, text="-----------------screen-------------------", fg='white', bg='black',
                                  font=('Times New Roman', 20))
                lblscr.place(x=5, y=100)

                btclr = tk.Button(frmbook, text="Clear", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=clear)
                btclr.place(x=250, y=400, width=50)

                btbook = tk.Button(frmbook, text="Book", fg='black', bg='Red', font=("Times New Roman Bold", 10), command=book)
                btbook.place(x=300, y=400, width=50)

                b1 = tk.Button(frmbook, text="$" + str(seatmoney))
                b1.place(x=120, y=400, width=70)
                
                lbla = tk.Label(frmbook, text="a", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbla.place(x=5, y=150)
                lblb = tk.Label(frmbook, text="b", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblb.place(x=5, y=200)
                lblc = tk.Label(frmbook, text="c", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblc.place(x=5, y=250)
                lbld = tk.Label(frmbook, text="d", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lbld.place(x=5, y=300)
                lblno = tk.Label(frmbook, text="1   2   3   4   5   6   7   8   9  10  11 12 13 14 15 16 17 18", fg='white', bg='black', font=("Times New Roman Bold", 12))
                lblno.place(x=20, y=325)
                

                buttons = []
                

                for row in range(4):
                    button_row = []
                    for col in range(18):
                        seat_label = chr(ord('a') + row) + str(col + 1)          
                        button = tk.Button(frmbook, bg='green', height=1, width=1, command=lambda r=row, c=col: button_click(r, c))
                        button.place(x=20 + col * 20, y=150 + row * 50)
                        button_row.append(button)
                    buttons.append(button_row)
                taken()
                    
            lblhd = tk.Label(frmtime, text ="Raastha", bg= 'light green',font=('MV Boli',15,'bold','underline'))
            lblhd.place(x = 170, y = 10)
            btbook= tk.Button(frmtime, text ="Book seat",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=booking) 
            btbook.place(x = 250, y = 155, width = 100)
            btsnack= tk.Button(frmtime, text ="Snacks",fg ='red',bg= 'light green',font=("Times New Roman Bold", 10),command=snacks) 
            btsnack.place(x = 250, y = 185, width = 100)
            lbldescrpt = tk.Label(frmtime, text ="Description", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lbldescrpt.place(x = 2, y = 40)            
            lbldes = tk.Label(frmtime, text ="Shahana and Faizal arrive in Oman to find Shahana's mother, missing for\n  22 years. Facing difficulties, they journey deeper into the desert, lost.\n Police try to locate them.",
                              bg= 'light green',font=('Times New Roman',10))
            lbldes.place(x = 2, y = 65)
            lblgenre = tk.Label(frmtime, text ="Genre", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblgenre.place(x = 2, y = 110)
            lblgen = tk.Label(frmtime, text ="Thriller", bg= 'light green',font=('Times New Roman',10))
            lblgen.place(x = 2, y = 135)
            lblrt = tk.Label(frmtime, text ="Running time", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblrt.place(x = 2, y = 155)
            lblrun = tk.Label(frmtime, text ="140 mins", bg= 'light green',font=('Times New Roman',10))
            lblrun.place(x = 2, y = 180)
            lblstar = tk.Label(frmtime, text ="Starring", bg= 'light green',font=('Times New Roman',12, 'underline'))
            lblstar.place(x = 2, y = 200)
            lblact = tk.Label(frmtime, text ="Sarjano Khalid, Anagha Narayanan, Aradhya Ann", bg= 'light green',font=('Times New Roman',10))
            lblact.place(x = 2, y = 225)
            
            link = tk.Label(frmtime, text="Trailer", 
            fg="blue", bg="light green",cursor="hand2",font=['Times',15,'underline'])
            link.place(x=160, y=155)
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://youtu.be/3j99pxFEuys?si=2sYHG-WfowDRGSFb"))
        
        img1 = ImageTk.PhotoImage(Image.open("neru.jpg"))
        button1= Button(frmmal, image = img1, command=showtimes1)
        button1.place(x = 50, y = 150)
        img2 = ImageTk.PhotoImage(Image.open("raastha.jpg"))
        button2= Button(frmmal, image = img2, command=showtimes2)
        button2.place(x = 350, y = 150)
        root.mainloop()
    
    bteng = tk.Button(root, text ="English",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20),command=English) 
    bteng.place(x = 170, y = 300, height = 100, width = 180)
    bthin = tk.Button(root, text ="Hindi",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20),command=Hindi) 
    bthin.place(x = 420, y = 300, height = 100, width = 180)
    btmal = tk.Button(root, text ="Malayalam",fg ='red',bg= 'orange',font=("Segoe Script Bold", 20),command=Malayalam) 
    btmal.place(x = 670, y = 300, height = 100, width = 180)
    imgadm = ImageTk.PhotoImage(Image.open("admin.png"))
    btadm= Button(root, image = imgadm, command=admin)
    btadm.place(x = 10, y = 5)
        
   

    def loginscreen():
        def funclear():
            txtUser.delete(0,END)
            txtpass.delete(0,END)
            txtUser.focus()

        def funlogin():
            user = txtUser.get() 
            passw = txtpass.get()
            try:
                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                mycur=myconn.cursor()
                query="select * from customer where c_name='{}' and pass='{}'".format(user,passw)
                mycur.execute(query)
                rs=mycur.fetchone()
                if rs!=None and user==rs[0] and passw==rs[2]:
                    global ver
                    ver=1
                    global user1
                    user1=user
                    passw=txtpass.get()
                    l=user+passw
                    global i_d1
                    for ch in l:
                        i_d1+=str(ord(ch))
                    messagebox.showinfo("Login ", "Login Successful")
                    login.destroy()
                    btlogin.destroy()
                    lblacc = tk.Label(root, text ="Account name: ", fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                    lblacc.place(x = 850, y = 5)
                    lblus = tk.Label(root, text =user, fg ='red', bg= 'black',font=('Times New Roman',10, "underline"))
                    lblus.place(x = 935, y = 5)
                    
                else:
                    messagebox.showinfo("Login", "Login Failed")
            except Exception as e:
                print(e)
        
        def register():
            i_d=''
            user=txtUser.get() 
            passw=txtpass.get()
            l=user+passw
            for ch in l:
                i_d+=str(ord(ch))
            try:
                myconn=mys.connect(host="localhost",user="root",passwd="adis",database="movie")
                mycur=myconn.cursor()
                query="insert into customer values('{}',{},'{}')".format(user,i_d,passw)
                mycur.execute(query)
                myconn.commit()
                messagebox.showinfo("Registration Successful", "Registration Successful, You may login now")
                funclear()
            except Exception as e:
                messagebox.showinfo("Registration Failed", "Registration Failed, Account already exists")
            
        
        login = tk.Tk() 
        login.geometry("300x300")
        login.title("Login Page") 
        C = Canvas(login, bg ="Red", height = 250, width = 300) 
        lbluser = tk.Label(login, text ="Username -",fg="red",font=("Times New Roman Bold", 10) ) 
        lbluser.place(x = 50, y = 20) 
        txtUser = tk.Entry(login, width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
        txtUser.place(x = 150, y = 20, width = 100) 
        lblpass = tk.Label(login, text ="Password -",fg="red",font=("Times New Roman Bold", 10)) 
        lblpass.place(x = 50, y = 50) 
        txtpass = tk.Entry(login,show="*", width = 35,fg="blue",font=("Times New Roman Bold", 10)) 
        txtpass.place(x = 150, y = 50, width = 100) 
        loginbtn = tk.Button(login, text ="Login", fg ='blue', font=("Times New Roman Bold", 10),command = funlogin) 
        loginbtn.place(x = 140, y = 135, width = 55)
        regbtn = tk.Button(login, text ="Register", fg ='blue', font=("Times New Roman Bold", 10),command = register) 
        regbtn.place(x = 80, y = 135, width = 55)
        clearbtn = tk.Button(login, text ="Clear",fg ='blue', font=("Times New Roman Bold", 10),command = funclear) 
        clearbtn.place(x = 200, y = 135, width = 55)
    
    btlogin = tk.Button(root, text ="login",fg ='white',bg= 'red',font=("Times New Roman Bold", 10),command=loginscreen) 
    btlogin.place(x = 930, y = 5, width = 60)

    root.mainloop()


def WELCOMESCREEN():
    import turtle

    screen = turtle.Screen()
    screen.title("Kalavampara Theater - Welcome Page")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)

    def glowing_text(text, color, x, y, font_size):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x, y)
        for glow in range(5, 0, -1):
            pen.color(color)
            pen.write(text, align="center", font=("Arial", font_size + glow * 2, "bold"))
            pen.penup()
        pen.color("white")
        pen.write(text, align="center", font=("Arial", font_size, "bold"))

    def decorative_border():
        border_pen = turtle.Turtle()
        border_pen.speed(0)
        border_pen.hideturtle()
        border_pen.color("gold")
        border_pen.pensize(5)
        border_pen.penup()
        border_pen.goto(-350, 250)
        border_pen.pendown()
        for _ in range(2):
            border_pen.forward(700)
            border_pen.right(90)
            border_pen.forward(500)
            border_pen.right(90)

    def draw_flower(x, y, color):
        flower = turtle.Turtle()
        flower.speed(0)
        flower.hideturtle()
        flower.penup()
        flower.goto(x, y)
        flower.color(color)
        flower.begin_fill()
        for _ in range(6):
            flower.circle(10, steps=6)
            flower.right(60)
        flower.end_fill()

    decorative_border()
    glowing_text("Kalavampura Theater", "red", 0, 50, 40)
    glowing_text("Welcome!", "blue", 0, -20, 30)

    draw_flower(-300, 200, "red")
    draw_flower(300, 200, "blue")
    draw_flower(-300, -200, "yellow")
    draw_flower(300, -200, "green")
    draw_flower(0, -100, "white")

    turtle.done()

#WELCOMESCREEN()
MENUSCREEN()