import sqlite3
class KSUPay :
    conn = sqlite3.connect("KSUPay.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS KSU_Users

                                              (
                                              FIRST_NAME    TEXT NOT NULL,
                                              LAST_NAME     TEXT NOT NULL,
                                              ID            TEXT  PRIMERY KEY NOT NULL,
                                              PASSWORD      TEXT NOT NULL,
                                              EMAIL         TEXT  KEY NOT NULL,
                                              PHONE_NUMBER  TEXT  KEY NOT NULL,
                                              WALLET_NUMBER TEXT  KEY  ,
                                              WALLET_TYPE   TEXT ,
                                              BALANCE       FLOAT ,
                                              WALLET_TIME   TEXT );''')

    conn.execute('''            CREATE TABLE IF NOT EXISTS KSU_Entities

                                              (
                                              ENTITY_NAME   TEXT  NOT NULL,
                                              WALLET_NUMBER TEXT  NOT NULL,
                                              WALLET_TYPE   TEXT  NOT NULL,
                                              BALANCE       FLOAT NOT NULL,
                                              WALLET_TIME   TEXT  NOT NULL


                                              );''')
    conn.close()

    import Signup
    Signup.Signup()











