import mysql.connector
import connect
db=connect.koneksi()
#menambahkan data baru ke dalam table dealer

def add(data):
    cursor=db.cursor()
    sql="""INSERT INTO dealer(nama,motor)VALUES(%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembeli berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel dealer

def show():
    cursor=db.cursor()
    sql="""SELECT*FROM dealer"""
    cursor.execute(sql)

    result=cursor.fetchall()
    print("--------------------------------------")
    print("|ID|NAMA\t\t|MOTOR\t\t|")
    print("--------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|")



#mengubah data per record berdasarkan id pada table dealer

def edit(data):
    cursor=db.cursor()
    sql="""UPDATE dealer SET nama=%s,motor=%sWHERE id=%s"""

    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembeli berhasil diubah!'.format(cursor.rowcount))


#menghapus data dari tabel dealer

def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM dealer WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembeli berhasil dihapus!'.format(cursor.rowcount))


#mencari data dari tabel dealer

def search(id_dealer):
    cursor=db.cursor()
    sql="""SELECT*FROM dealer WHERE id=%s"""
    cursor.execute(sql,id_dealer)

    result=cursor.fetchall()
    print("--------------------------------------")
    print("|ID|NAMA\t\t|MOTOR\t\t|")
    print("--------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|")
        print("--------------------------------------")



    
