#build in
import mysql.connector
#fungsi koneksi

def koneksi():
    db= mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dealer",
        autocommit= True
        )
    if db.is_connected():
        return db
    else:
        print('DB disconnect!')
        
