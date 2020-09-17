import mysql.connector
import connect
db=connect.koneksi()
#menambahkan data baru ke dalam table member

def add(data):
    cursor=db.cursor()
    sql="""INSERT INTO nomor(nama,no)VALUES(%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembeli berhasil ditambhkan!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel member

def show():
    cursor=db.cursor()
    sql="""SELECT*FROM nomor"""
    cursor.execute(sql)

    result=cursor.fetchall()
    print("--------------------------------------")
    print("|ID|NAMA\t\t|NO\t\t|")
    print("--------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|")



#mengubah data per record berdasarkan id pada table member

def edit(data):
    cursor=db.cursor()
    sql="""UPDATE nomor SET nama=%s,no=%sWHERE id=%s"""

    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembeli berhasil diubah!'.format(cursor.rowcount))


#menghapus data dari tabel member

def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM nomor WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembeli berhasil dihapus!'.format(cursor.rowcount))


#mencari data dari tabel member

def search(id_nomor):
    cursor=db.cursor()
    sql="""SELECT*FROM nomor WHERE id=%s"""
    cursor.execute(sql,id_nomor)

    result=cursor.fetchall()
    print("--------------------------------------")
    print("|ID|NAMA\t\t|NO\t\t|")
    print("--------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|")
        print("--------------------------------------")



    
