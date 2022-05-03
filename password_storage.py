from authsite import tk_authsite as tas
from honeyword_generation import honeyword_generation as hg
from dna_algorithm import dna_encryption as de
import sqlite3
import os



def check_db(filename):
    return os.path.exists(filename)

db_file = 'database.db'

username, password = tas.credentials.username, tas.credentials.password
honeyword = []

honeyword = hg.create_honeywords(password)

enc_sweetword, ascii_otp, lookupt, case_flag = de.dna_encryption(password)

enc_honeyword = [None]*len(honeyword)
ascii_otp_honeyword = [None]*len(honeyword)
lookupt_honeyword = [None]*len(honeyword)
case_flag_honeyword = [None]*len(honeyword)

j = 0

for i in honeyword:
    while j < len(enc_honeyword):
        enc_honeyword[j], ascii_otp_honeyword[j], lookupt_honeyword[j], case_flag_honeyword[j] = de.dna_encryption(i)
        j = j + 1


def insert_data(username, enc_sweetword, ascii_otp, lookupt, case_flag, enc_honeyword1, ascii_otp_honeyword1, enc_honeyword2, ascii_otp_honeyword2, enc_honeyword3, ascii_otp_honeyword3, enc_honeyword4, ascii_otp_honeyword4, enc_honeyword5, ascii_otp_honeyword5, enc_honeyword6, ascii_otp_honeyword6, enc_honeyword7, ascii_otp_honeyword7, enc_honeyword8, ascii_otp_honeyword8, enc_honeyword9, ascii_otp_honeyword9, lookupt_honeyword, case_flag_honeyword):
    with sqlite3.connect(db_file) as conn:
        conn.execute("insert into credentials (username, sweetword, otp, lookupno, case_flag, honeyword1, otp1, honeyword2, otp2, honeyword3, otp3, honeyword4, otp4, honeyword5, otp5, honeyword6, otp6, honeyword7, otp7, honeyword8, otp8, honeyword9, otp9, lookupno_h, caseflag_h) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                        ,(username, enc_sweetword, ascii_otp, lookupt, case_flag, enc_honeyword1, ascii_otp_honeyword1, enc_honeyword2, ascii_otp_honeyword2, enc_honeyword3, ascii_otp_honeyword3, enc_honeyword4, ascii_otp_honeyword4, enc_honeyword5, ascii_otp_honeyword5, enc_honeyword6, ascii_otp_honeyword6, enc_honeyword7, ascii_otp_honeyword7, enc_honeyword8, ascii_otp_honeyword8, enc_honeyword9, ascii_otp_honeyword9, lookupt_honeyword, case_flag_honeyword))

insert_data(username, enc_sweetword, ascii_otp, lookupt, case_flag, enc_honeyword[0], ascii_otp_honeyword[0], enc_honeyword[1], ascii_otp_honeyword[1], enc_honeyword[2], ascii_otp_honeyword[2], enc_honeyword[3], ascii_otp_honeyword[3], enc_honeyword[4], ascii_otp_honeyword[4], enc_honeyword[5], ascii_otp_honeyword[5], enc_honeyword[6], ascii_otp_honeyword[6], enc_honeyword[7], ascii_otp_honeyword[7], enc_honeyword[8], ascii_otp_honeyword[8], lookupt_honeyword[0], case_flag_honeyword[0])


def show_table():
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                    select * from credentials
                    """)
        print(cursor.fetchall())
        


# with sqlite3.connect(db_file) as conn:
#     print('Created the connection!')
#     conn.execute("""CREATE TABLE credentials(
#     username text primary key,
#     sweetword text,
#     otp text,
#     lookupno integer,
#     case_flag text,
#     honeyword1 text,
#     otp1 text,
#     honeyword2 text,
#     otp2 text,
#     honeyword3 text,
#     otp3 text,
#     honeyword4 text,
#     otp4 text,
#     honeyword5 text,
#     otp5 text,
#     honeyword6 text,
#     otp6 text,
#     honeyword7 text,
#     otp7 text,
#     honeyword8 text,
#     otp8 text,
#     honeyword9 text,
#     otp9 text,
#     lookupno_h integer,
#     caseflag_h text)
#     """)
#     # print('Created the table! Now inserting')
#     conn.executescript("""
#                         insert into credentials (username, sweetword, honeyword1, honeyword2, honeyword3, honeyword4, honeyword5, honeyword6, honeyword7, honeyword8, honeyword9)
#                         values
#                         ('User', 'Password@123', 'Password@12|', 'Password@12|', 'Password@12*', 'Password@12J', 'Password@11J', 'PassDP^5OD;}', 'PassDP^5O#*f', 'Paswy|[SdWI2', 'Paswy|[SdWIg');
#                         """)
#     # print('Inserted values into the table!')
# print('Closed the connection')