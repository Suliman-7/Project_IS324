import sqlite3
import random
import datetime
import tkinter as tk
import tkinter.messagebox
import csv
import Signup
import re


class Admin :

   def __init__(self):

      self.window = tk.Tk()

      self.window.title("Admin")

      self.window.geometry('400x400')
      self.window.geometry("+600+200")  # to position the window in the center

      self.window.configure(bg="#252F4E")

      self.label = tk.Label(self.window, text="KSU Pay", width=10, bg="grey", foreground="Black", font=15).grid(row=0,column=0,columnspan=20,ipadx=150)

      self.Total = tk.StringVar()

      self.Label1 = tk.Label(self.window, text='Total balance :', font=30, bg="#252F4E",foreground="White").grid(row=1, column=1,pady=25,sticky="W")
      self.Label2 = tk.Label(self.window, textvariable=self.Total, font=30, bg="#252F4E",foreground="White").grid(row=1, column=2,pady=25)
      conn = sqlite3.connect("KSUPay.db")
      self.Total.set(0)

      self.T = 0.0
      cursor = conn.execute("SELECT BALANCE FROM KSU_Entities WHERE WALLET_TYPE = 'KSU' ")

      row = cursor.fetchall()

      if (row!=None):

         for x in row :
           self.T = self.T + x[0]

      self.Total.set(f'{self.T} SR')

      conn.close()

      self.Label3 = tk.Label(self.window, text='Entity name :', font=30, bg="#252F4E",foreground="White").grid(row=2, column=1,sticky="W")

      self.Entity = tk.StringVar()

      self.Name = tk.Entry(self.window, textvariable=self.Entity , width=25).grid(row=2, column=2)

      self.button = tk.Button(self.window, text='Submit', command=self.Action).grid(row=2, column=3,padx=25)
      self.buttonDeposite = tk.Button(self.window, text='Pay Stipends', command=self.Deposite).grid(row=4, column=1,pady=40)
      self.buttonReset = tk.Button(self.window, text='Cash Out', command=self.reset).grid(row=4, column=2,pady=40)
      self.backupB = tk.Button(self.window, text='Backup',command=self.backup).grid(row=4, column=3,pady=40)
      self.buttonBack = tk.Button(self.window, text='Back', command=self.SignUp).grid(row=5, column=2)


      self.window.mainloop()



   def Action(self):

      if (self.Entity.get() == '' ) :
         tk.messagebox.showerror('Error', 'Please enter entity name !')

      else :

         reg = "^[A-za-z ]+$"
         Pat = re.compile(reg)
         x = re.search(Pat, self.Entity.get())

         if (x) :
               self.Wallet_Number = random.randrange(1000000000, 10000000000)
               self.Wallet_Type = "KSU"
               self.Balance = 0

               now = datetime.datetime.now()
               self.DT = now.strftime("%y-%m-%d %H:%M:%S")

               conn = sqlite3.connect("KSUPay.db")

               with conn:
                           cursor = conn.cursor()
                           cursor.execute('INSERT INTO KSU_Entities (ENTITY_NAME,WALLET_NUMBER, WALLET_TYPE, BALANCE, WALLET_TIME) VALUES(?,?, ?, ?, ?)',(
                           self.Entity.get(),self.Wallet_Number, self.Wallet_Type, self.Balance, self.DT))

               self.Entity.set('')
               tk.messagebox.showinfo("" , "Entity created successfully")

         else :
            tk.messagebox.showerror('Error', 'Entity Name should be letters only')



   def Deposite(self):


      conn = sqlite3.connect("KSUPay.db")
      cur = conn.cursor()

      cur.execute('SELECT ID FROM KSU_Users WHERE WALLET_TYPE="student" ')

      row = cur.fetchone()

      if row==None :
         tk.messagebox.showerror('Error', 'There is no any student')

      else :


         cur.execute('UPDATE KSU_Users set BALANCE=BALANCE+1000 WHERE WALLET_TYPE="student" ')
         tk.messagebox.showinfo("", "1000 SR deposited to all the student Wallets successfully")
      conn.commit()
      conn.close()

   def reset(self):

      conn = sqlite3.connect("KSUPay.db")
      cur = conn.cursor()

      cur.execute('SELECT ENTITY_NAME FROM KSU_Entities WHERE WALLET_TYPE="KSU" ')

      row = cur.fetchone()

      if row==None :
         tk.messagebox.showerror('Error', 'There is no any KSU entity')

      else :

         if self.T == 0.0 :
            tk.messagebox.showerror("" , "KSU entity wallets is already zero")

         else :

            cur.execute('UPDATE KSU_Entities set BALANCE=0 where WALLET_TYPE="KSU" ')
            self.T = 0.0
            self.Total.set(f"{self.T} SR")
            tk.messagebox.showinfo("", "now all the KSU entity wallets balances is zero")



      conn.commit()
      conn.close()

   def backup(self):
      try :
         conn = sqlite3.connect("KSUPay.db")
         exported_file = open("KSUPay.csv", 'w')
         csvwriter = csv.writer(exported_file, lineterminator="\n")

         usersInfo = conn.execute( f'SELECT * FROM  KSU_Users ;')
         data = usersInfo.fetchall()
         if (data!=None) :

            for row in data:
               L = list(row)

               for I in range(0,len(L)) :


                  if L[I]==None:
                     L[I]=("Null")

               B = L[8]
               if B != "Null" :
                L[8] = ( f'{B} SR')
               csvwriter.writerow(L)






         EntitiesInfo = conn.execute(f'SELECT * FROM  KSU_Entities ;')
         data = EntitiesInfo.fetchall()
         if (data != None):

            for row in data:
               L = list(row)
               for I in range(0, len(L)):
                  if L[I] == None:
                     L[I] = ("Null")

               B = L[3]
               L[3] = (f'{B} SR')
               csvwriter.writerow(L)


         conn.commit()
         exported_file.close()

         tk.messagebox.showinfo("Export Status", "The database of our system is exported in CSV file")
      except:
         tk.messagebox.showerror("Export Status",'Something went wrong')

      conn.close()




   def SignUp(self):

      self.window.destroy()
      Signup.Signup()