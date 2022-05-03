
from authsite import tk_authsite as tas
import sqlite3
from dna_algorithm import dna_encryption as d

db_file = 'database.db'

usernames = []
credentials = []
h_credentials = []

def honeychecker():
    with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        select username from credentials
                        """)
            usernames= cursor.fetchall()



    username, password = tas.login_credentials.username, tas.login_credentials.password

    flag = 0

    for i in usernames:
        for j in i:
            if j == username:
                flag = 1
                with sqlite3.connect(db_file) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        select sweetword, otp, lookupno, case_flag from credentials
                        """)
                    credentials = cursor.fetchall()
                for i in credentials:
                    passw = d.dna_decryption(i[0], i[1], i[2], i[3])
                if passw == password:
                    tas.login_success()
                else:
                    with sqlite3.connect(db_file) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""
                        select honeyword1, otp1, honeyword2, otp2, honeyword3, otp3, honeyword4, otp4, honeyword5, otp5, honeyword6, otp6, honeyword7, otp7, honeyword8, otp8, honeyword9, otp9, lookupno_h, caseflag_h from credentials where username = ?
                        """, (j,))
                        h_credentials = cursor.fetchall()
                        for i in h_credentials:
                            for j in range(0, 17, 2):
                                passw = d.dna_decryption(i[j], i[j+1], i[-2], i[-1])
                        if passw == password:
                            print("honeyword matched") 
                            tas.password_not_recognised()  

    if flag == 0:
        print("Account not found")
        tas.user_not_found()