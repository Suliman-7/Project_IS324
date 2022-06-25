import tkinter as tk
import sqlite3
import tkinter.messagebox
import Signup
import logging
import re






class StudentWallet :



    def __init__(self,Id,Pass):


        self.window = tk.Tk()
        self.window.title("Student Wallet")
        self.window.geometry('400x400')
        self.window.geometry("+600+200")  # to position the window in the center

        self.window.configure(bg="#252F4E")

        self.label = tk.Label(self.window, text="KSU Pay", width=10, bg="grey", foreground="Black", font=15).grid(row=0,column=0,columnspan=20,ipadx=150)

        conn = sqlite3.connect("KSUPay.db")
        cursor = conn.cursor()

        cursor.execute('SELECT WALLET_NUMBER,BALANCE FROM KSU_Users WHERE ID=? and PASSWORD=? ', (Id,Pass))
        self.WB = cursor.fetchone()
        self.Balance = tk.StringVar()
        self.Balance.set(f'{self.WB[1]} SR')
        self.Balance1 = tk.StringVar()
        self.Balance1.set(self.WB[1])



        self.Label1 = tk.Label(self.window, text='Wallet Number ', font=30, bg="#252F4E",foreground="White").grid(row=1, column=1 ,pady=25,sticky="W")

        self.Label2 = tk.Label(self.window, text='Current balance ', font=30, bg="#252F4E",foreground="White").grid(row=2,column=1,sticky="W")



        self.Label3 = tk.Label(self.window, text=self.WB[0], font=30, bg="#252F4E",foreground="White").grid(row=1, column=2 )

        self.Label4 = tk.Label(self.window, textvariable=self.Balance , font=30,bg="#252F4E",foreground="White").grid(row=2, column=2 )

        self.Label5 = tk.Label(self.window, text='Wallet number ', font=30,bg="#252F4E",foreground="White").grid(row=3, column=1,sticky="W",pady=25)
        self.Wallet = tk.StringVar()
        self.EntityWallet = tk.Entry(self.window, textvariable=self.Wallet,width=25).grid(row=3, column=2)              

        self.Label6 = tk.Label(self.window, text='Amount ', font=30,bg="#252F4E",foreground="White").grid(row=4, column=1,sticky="W")
        self.amonutEntry = tk.StringVar()
        self.amount = tk.Entry(self.window, textvariable=self.amonutEntry,width=25).grid(row=4, column=2)



        self.PAYButton = tk.Button(self.window, text='Pay' , command=self.pay  ).grid(row=5, column=2,pady=25)
        self.buttonBack = tk.Button(self.window, text='Back', command=self.logout).grid(row=8, column=2)

        self.ID = Id

        self.window.mainloop()

    def pay(self):

            conn = sqlite3.connect("KSUPay.db")
            cur = conn.cursor()

            if (self.amonutEntry.get() == '' or self.Wallet.get() == ''):
                tk.messagebox.showerror('Error', 'All feild are reqired')

            else:

                try:
                    if (self.Wallet.get().isdigit() is False):
                        tk.messagebox.showerror("Error", "Wallet number should be numbers only ")
                    else:
                        cur.execute('SELECT WALLET_NUMBER FROM KSU_Users WHERE WALLET_NUMBER = ' + self.Wallet.get())
                        urow = cur.fetchone()
                        cur.execute('SELECT WALLET_NUMBER FROM KSU_Entities WHERE WALLET_NUMBER = ' + self.Wallet.get())
                        erow = cur.fetchone()

                        if urow != None:

                            if int(self.Wallet.get()) == int(self.WB[0]):
                                tk.messagebox.showerror("Error", "Please don't enter your Wallet Number")
                            else:
                                logging.basicConfig(filename='KSUPay.log',
                                                    filemode='a',
                                                    format='%(asctime)s %(message)s',
                                                    level=logging.INFO)
                                cur.execute('SELECT BALANCE FROM KSU_Users WHERE ID= ' + (self.ID))
                                amount = cur.fetchone()

                                if (float(self.amonutEntry.get()) <= 0):
                                    tk.messagebox.showerror('Error', 'Please Enter Positive amount')
                                else:
                                    if (float(amount[0]) < float(self.amonutEntry.get())):
                                        tk.messagebox.showerror('Error', 'There is not enough money')
                                    else:
                                        cur.execute(
                                            f'UPDATE KSU_Users SET BALANCE = BALANCE -{self.amonutEntry.get()} WHERE ID= {(self.ID)}')
                                        self.Balance.set(
                                            f'{float(self.Balance1.get()) - float(self.amonutEntry.get())} SR')
                                        self.Balance1.set(float(self.Balance1.get()) - float(self.amonutEntry.get()))
                                        cur.execute(
                                            f'UPDATE KSU_Users SET BALANCE = BALANCE +{float(self.amonutEntry.get())} WHERE WALLET_NUMBER= {self.Wallet.get()}')
                                        logging.info(
                                            f'\nAmount : {float(self.amonutEntry.get())} SR\nWallet Number of the sender : {self.WB[0]} \nWallet number of the receiver : {self.Wallet.get()} ')
                                        self.amonutEntry.set('')
                                        self.Wallet.set('')
                                        tk.messagebox.showinfo("", "Payment completed successfully")

                        elif erow != None:
                            logging.basicConfig(filename='KSUPay.log',
                                                filemode='a',
                                                format='%(asctime)s %(message)s',
                                                level=logging.INFO)
                            cur.execute('SELECT BALANCE FROM KSU_Users WHERE ID= ' + (self.ID))
                            amount = cur.fetchone()

                            if (float(self.amonutEntry.get()) <= 0):
                                tk.messagebox.showerror('Error', 'Please Enter Positive amount')
                            else:
                                if (float(amount[0]) < float(self.amonutEntry.get())):
                                    tk.messagebox.showerror('Error', 'There is not enough money')
                                else:
                                    cur.execute(
                                        f'UPDATE KSU_Users SET BALANCE = BALANCE -{float(self.amonutEntry.get())} WHERE ID= {(self.ID)}')
                                    self.Balance.set(f'{float(self.Balance1.get()) - float(self.amonutEntry.get())} SR')
                                    self.Balance1.set(float(self.Balance1.get()) - float(self.amonutEntry.get()))
                                    cur.execute(
                                        f'UPDATE KSU_Entities SET BALANCE = BALANCE +{float(self.amonutEntry.get())} WHERE WALLET_NUMBER= {self.Wallet.get()}')
                                    logging.info(
                                        f'\nAmount : {float(self.amonutEntry.get())} SR\nWallet Number of the sender : {self.WB[0]} \nWallet number of the receiver : {self.Wallet.get()} ')
                                    self.amonutEntry.set('')
                                    self.Wallet.set('')
                                    tk.messagebox.showinfo("", "Payment completed successfully")
                        else:
                            tk.messagebox.showerror('Error', 'wallet number does not exist')

                        conn.commit()
                        conn.close()
                except ValueError:
                    tk.messagebox.showerror("Error", "Please enter correct numbers and numbers only for amount")


    def logout(self):

        self.window.destroy()
        Signup.Signup()



