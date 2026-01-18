from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import messagebox
import mysql.connector as mys
def admin():
        def funclear():
                txtUser.delete(0,END)
                txtpass.delete(0,END)
                txtUser.focus()
        def funlogin():
                if txtUser.get()=="adis" and txtpass.get()=="54321":
                    login.destroy()
                                                   
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
        
admin()