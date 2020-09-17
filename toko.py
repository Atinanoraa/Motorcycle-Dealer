import mysql.connector
import connect
db=connect.koneksi()
#menambahkan data baru ke dalam table stok

def add(data):
    cursor=db.cursor()
    sql="""INSERT INTO stok(merk,stok,terjual,sisa)VALUES(%s,%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data stok motor berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel stok

def show():
    cursor=db.cursor()
    sql="""SELECT*FROM stok"""
    cursor.execute(sql)

    result=cursor.fetchall()
    print("------------------------------------------------------------------------------------")
    print("|ID|MERK\t\t|STOK\t\t|TERJUAL\t\t|SISA\t\t|")
    print("------------------------------------------------------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|",data[3],"\t\t|",data[4],"\t\t|")



#mengubah data per record berdasarkan id pada table stok

def edit(data):
    cursor=db.cursor()
    sql="""UPDATE stok SET merk=%s,stok=%s,terjual=%s,sisa=%sWHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data stok berhasil diubah!'.format(cursor.rowcount))


#menghapus data dari tabel stok

def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM stok WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data stok berhasil dihapus!'.format(cursor.rowcount))


#mencari data dari tabel stok

def search(id_stok):
    cursor=db.cursor()
    sql="""SELECT*FROM stok WHERE id=%s"""
    cursor.execute(sql,id_stok)

    result=cursor.fetchall()
    print("------------------------------------------------------------------------------------")
    print("|ID|MERK\t\t|STOK\t\t|TERJUAL\t\t|SISA\t\t|")
    print("------------------------------------------------------------------------------------")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|",data[3],"\t\t|",data[4],"\t\t|")
        print("------------------------------------------------------------------------------------")



    
