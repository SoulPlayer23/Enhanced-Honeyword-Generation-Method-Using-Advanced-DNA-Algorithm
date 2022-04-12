#from authsite import tk_authsite as auths
import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

db_file = 'database.db'
schema_file = 'schema.sql'


# if check_db(db_file):
#     print('Database already exists. Exiting ... ')
#     exit(0)


# with sqlite3.connect(db_file) as conn:
#     print('Created the connection!')
#     conn.execute("""CREATE TABLE credentials(
#     username text primary key,
#     sweetword text,
#     honeyword1 text,
#     honeyword2 text,
#     honeyword3 text,
#     honeyword4 text,
#     honeyword5 text,
#     honeyword6 text,
#     honeyword7 text,
#     honeyword8 text,
#     honeyword9 text)
#     """)
#     print('Created the table! Now inserting')
#     conn.executescript("""
#                         insert into credentials (username, sweetword, honeyword1, honeyword2, honeyword3, honeyword4, honeyword5, honeyword6, honeyword7, honeyword8, honeyword9)
#                         values
#                         ('User', 'Password@123', 'Password@12|', 'Password@12|', 'Password@12*', 'Password@12J', 'Password@11J', 'PassDP^5OD;}', 'PassDP^5O#*f', 'Paswy|[SdWI2', 'Paswy|[SdWIg');
#                         """)
#     print('Inserted values into the table!')
# print('Closed the connection')

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   select * from credentials
                   """)
    for row in cursor.fetchall():
        username, sweetword, honeyword1, honeyword2, honeyword3, honeyword4, honeyword5, honeyword6, honeyword7, honeyword8, honeyword9 = row
        print(f'{username} {sweetword} {honeyword1} {honeyword2} {honeyword3} {honeyword4} {honeyword5} {honeyword6} {honeyword7} {honeyword8} {honeyword9}')


