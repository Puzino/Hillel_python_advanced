import sqlite3

con = sqlite3.connect('emails.db')
cur = con.cursor()
cur.execute(
    '''CREATE TABLE IF NOT EXISTS emails
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(100), phone varchar(20), joiningDate timestamp, joiningTime timestamp);''')

con.commit()
con.close()
