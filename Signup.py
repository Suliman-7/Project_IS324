import sqlite3
import tkinter as tk
import tkinter.messagebox
import StudentWallet
import Login
import re
import random
import datetime

conn = sqlite3.connect("KSUPay.db")
cursor = conn.cursor()

Admin_fName = "Mohammed"
Admin_lName = "Abdullah"
Admin_ID = 1234567890
Admin_Pass = 123456
Admin_mail = 'M@ksu.edu.sa'
Admin_PN = '0550550559'

cursor = conn.execute("SELECT FIRST_NAME from KSU_Users WHERE ID = 1234567890")

row = cursor.fetchone()
if row == None:
    cursor.execute('INSERT INTO KSU_Users (FIRST_NAME,LAST_NAME,ID,PASSWORD,EMAIL,PHONE_NUMBER) VALUES (?,?,?,?,?,?)',
                   (Admin_fName, Admin_lName, Admin_ID, Admin_Pass, Admin_mail, Admin_PN))

conn.commit()
conn.close()


class Signup:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sign up")
        self.window.geometry('400x400')
        self.window.geometry("+600+200")  # to position the window in the center
        self.window.configure(bg="#252F4E")

        self.Fname = tk.StringVar()
        self.Lname = tk.StringVar()
        self.SId = tk.StringVar()
        self.PW = tk.StringVar()
        self.Email = tk.StringVar()
        self.PhoneNumber = tk.StringVar()

        self.label = tk.Label(self.window, text="KSU Pay", width=10, bg="grey", foreground="Black", font=15).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  columnspan=20,
                                                                                                                  ipadx=150)

        self.label1 = tk.Label(self.window, text='First Name', width=8, bg="#252F4E", foreground="White").grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=50,
                                                                                                               sticky="W",
                                                                                                               pady=10)
        self.FName = tk.Entry(self.window, textvariable=self.Fname, width=25).grid(row=1, column=1, sticky="W")
        self.label2 = tk.Label(self.window, text='Last Name', width=8, bg="#252F4E", foreground="White").grid(row=2,
                                                                                                              column=0,
                                                                                                              sticky="W",
                                                                                                              padx=50,
                                                                                                              pady=10)
        self.LName = tk.Entry(self.window, textvariable=self.Lname, width=25).grid(row=2, column=1, sticky="W")

        self.label3 = tk.Label(self.window, text='Student ID', width=8, bg="#252F4E", foreground="White").grid(row=3,
                                                                                                               column=0,
                                                                                                               sticky="w",
                                                                                                               padx=50,
                                                                                                               pady=10)
        self.label4 = tk.Label(self.window, text='Password', width=8, bg="#252F4E", foreground="White").grid(row=4,
                                                                                                             column=0,
                                                                                                             sticky="w",
                                                                                                             padx=50,
                                                                                                             pady=10)
        self.label5 = tk.Label(self.window, text='Email address', width=10, bg="#252F4E", foreground="White").grid(
            row=5, column=0, sticky="w", padx=50, pady=10)
        self.label6 = tk.Label(self.window, text='Phone number', width=11, bg="#252F4E", foreground="White").grid(row=6,
                                                                                                                  column=0,
                                                                                                                  sticky="W",
                                                                                                                  padx=50,
                                                                                                                  pady=10)
        self.label7 = tk.Label(self.window, text='You already have account?', width=20, bg="#252F4E",
                               foreground="White").grid(row=8, column=0, sticky="W", padx=10, pady=10)

        self.SID = tk.Entry(self.window, textvariable=self.SId, width=25).grid(row=3, column=1)
        self.Pw = tk.Entry(self.window, textvariable=self.PW, width=25).grid(row=4, column=1)
        self.email = tk.Entry(self.window, textvariable=self.Email, width=25).grid(row=5, column=1)
        self.Phone = tk.Entry(self.window, textvariable=self.PhoneNumber, width=25).grid(row=6, column=1)

        self.Btn = tk.Button(self.window, text=' Submit ', bg='Light grey', font='bold', command=self.Action).grid(
            row=7, column=1, pady=20)
        self.login = tk.Button(self.window, text=' Login ', bg='Light grey', font='bold', command=self.go_Login).grid(
            row=8, column=1)

        self.window.mainloop()

    def Action(self):

        FlagfName = False
        FlaglName = False
        FlagId = False
        FlagPass = False
        FlagEmail = False
        FlagNumber = False

        if (
                self.Fname.get() == '' or self.Lname.get() == '' or self.SId.get() == '' or self.PW.get() == '' or self.Email.get() == '' or self.PhoneNumber.get() == ''):
            tk.messagebox.showerror('Error', 'All fields are required')

        else:
            regfName = "^[A-za-z]+$"
            Pat = re.compile(regfName)
            x = re.search(Pat, self.Fname.get())

            if (x):
                FlagfName = True
            else:
                tk.messagebox.showerror('Error', 'First Name should be letters only')

            reglName = "^[A-za-z]+$"
            Pat = re.compile(reglName)
            x = re.search(Pat, self.Lname.get())

            if (x):
                FlaglName = True
            else:
                tk.messagebox.showerror('Error', 'Last Name should be letters only')

            regId = "^[0-9]{10}$"
            Pat = re.compile(regId)
            x = re.search(Pat, self.SId.get())

            if (x):
                FlagId = True
            else:
                FlagId = tk.messagebox.showerror('Error', 'ID should be 10 digit')

            regPass = "^[0-9A-za-z]{6,}$"
            Pat = re.compile(regPass)
            x = re.search(Pat, self.PW.get())
            if (x):
                FlagPass = True

            else:
                tk.messagebox.showerror('Error', 'Password should be at least 6 Letter or digit only!')

            regEmail = "^([a-zA-Z0-9\._-]+)(@ksu.edu.sa)$"
            Pat = re.compile(regEmail)
            x = re.search(Pat, self.Email.get())

            if (x):
                FlagEmail = True
            else:
                tk.messagebox.showerror('Error', 'Please enter correct KSU Email')

            regPhone = "^(05)[0-9]{8}$"
            Pat = re.compile(regPhone)
            x = re.search(Pat, self.PhoneNumber.get())
            if (x):
                FlagNumber = True
            else:
                tk.messagebox.showerror('Error', 'Phone number should be 10 digits and start with "05" ')

        if (
                FlagfName == True and FlaglName == True and FlagId == True and FlagPass == True and FlagEmail == True and FlagNumber == True):

            self.Wallet_Number = random.randrange(1000000000, 10000000000)
            self.Wallet_Type = "student"
            self.Balance = 1000

            now = datetime.datetime.now()
            self.DT = now.strftime("%y-%m-%d %H:%M:%S")

            FlagSID = False
            FlagEMAIL = True
            FlagPhoneNumber = True

            conn = sqlite3.connect("KSUPay.db")

            cursor = conn.cursor()
            cursor = conn.execute('SELECT * FROM KSU_Users WHERE ID=' + str(self.SId.get()))

            row = cursor.fetchone()

            if row != None:
                tk.messagebox.showerror("Error", "Student ID already exist !")
            else:
                FlagSID = True

            cursor = conn.execute('SELECT EMAIL FROM KSU_Users WHERE WALLET_TYPE ="student" ')

            for row in cursor:
                if (row[0] == self.Email.get()):
                    FlagEMAIL = False
                    tk.messagebox.showerror("Error", "Student Email already exist !")
                    break

            cursor = conn.execute('SELECT PHONE_NUMBER FROM KSU_Users WHERE WALLET_TYPE ="student" ')

            for row in cursor:
                if (row[0] == self.PhoneNumber.get()):
                    FlagPhoneNumber = False
                    tk.messagebox.showerror("Error", "Student Phone Number already exist !")
                    break



            if (FlagSID == True and FlagPhoneNumber == True and FlagEMAIL == True):
                cursor.execute(
                    'INSERT INTO KSU_Users (FIRST_NAME,LAST_NAME,ID,PASSWORD,EMAIL,PHONE_NUMBER,WALLET_NUMBER,WALLET_TYPE,BALANCE,WALLET_TIME) VALUES(?,?,?,?,?,?,?,?,?,?)',
                    (self.Fname.get(), self.Lname.get(), self.SId.get(), self.PW.get(), self.Email.get(),
                     self.PhoneNumber.get(),
                     self.Wallet_Number, self.Wallet_Type, self.Balance, self.DT))
                conn.commit()
                self.go_Wallet()



    def go_Wallet(self):

        self.window.destroy()
        StudentWallet.StudentWallet(self.SId.get(), self.PW.get())

    def go_Login(self):

        self.window.destroy()
        Login.Login()


