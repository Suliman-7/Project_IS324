import tkinter as tk
import tkinter.messagebox
import sqlite3
import re
import StudentWallet
import Admin
import Signup



class Login:


    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry('400x400')
        self.window.geometry("+600+200")
        self.window.configure(bg="#252F4E")

        self.label = tk.Label(self.window , text="KSU Pay" , width=10 , bg="grey" , foreground="Black",font=15).grid(row=0,column=0,columnspan=20,ipadx=150)



        self.label1 = tk.Label(self.window, text='ID',font=(30), bg="#252F4E",foreground="White").grid(row=1, column=1,pady=25)
        self.label2 = tk.Label(self.window, text='Password',font=(30), bg="#252F4E",foreground="White").grid(row=2, column=1)
        self.label3 = tk.Label(self.window, text="You don't have account ?",bg="#252F4E",foreground="White").grid(row=5, column=1,padx=10)

        self.SId = tk.StringVar()
        self.PW = tk.StringVar()

        self.SID = tk.Entry(self.window, textvariable=self.SId,width=25).grid(row=1, column=2)
        self.Pw = tk.Entry(self.window, textvariable=self.PW,width=25).grid(row=2, column=2)

        self.Btn = tk.Button(self.window, text='Login', bg='Light grey', font='bold' , command=self.Action ).grid(row=3, column=2,pady=25)
        self.buttonBack = tk.Button(self.window, text=' Signup ', bg='Light grey', font='bold' ,  command=self.go_signup ).grid(row=5, column=2,pady=40)



    def Action(self) :

            if ( self.SId.get() == '' or self.PW.get() == '' ) :
                tk.messagebox.showerror('Error', 'All feild are reqired')

            else :

                FlagId = False
                FlagPass = False

                regId = "^[0-9]{10}$"
                Pat = re.compile(regId)
                x = re.search(Pat, self.SId.get())

                if (x):
                    FlagId = True
                else:
                    FlagId = tk.messagebox.showerror('Error', 'ID should be 10 digit')

                reg = "^[0-9A-za-z]{6,}$"
                Pat = re.compile(reg)
                x = re.search(Pat, self.PW.get())

                if (x):
                    FlagPass = True

                else:
                    tk.messagebox.showerror('Error', 'Password should be at least 6 Letter or digit only!')


                if ( FlagId == True and FlagPass == True ) :
                    conn = sqlite3.connect("KSUPay.db")
                    cur = conn.cursor()
                    cur.execute('SELECT WALLET_TYPE FROM KSU_Users WHERE ID = ? and PASSWORD = ?' , (self.SId.get(),self.PW.get()))

                    row = cur.fetchone()


                    if row == None:
                        tk.messagebox.showerror("Error", "Invalid ID or password ")

                    else:

                        if (row[0] == "student") :
                                       self.go_Wallet()

                        else :
                                       self.go_Admin()


            self.window.mainloop()



    def go_Wallet(self):

        self.window.destroy()
        StudentWallet.StudentWallet(self.SId.get() , self.PW.get() )


    def go_Admin(self):

        self.window.destroy()
        Admin.Admin()


    def go_signup(self):

        self.window.destroy()
        Signup.Signup()
