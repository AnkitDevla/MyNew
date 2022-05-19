import sqlite3 as sql

try:
    con = sql.connect(database="banking.sqlite")
    cur = con.cursor()
    cur.execute(
        "create table users(acn integer primary key autoincrement,name text,pass text,email text,mob text,bal int)")
    con.commit()
    con.close()

except sql.Error as error:
    print("Exist")
    
finally:
    if con:
        con.close()
        