import dealer
import nomor
import toko
print("=== SELAMAT DATANG DI DEALER KAMI ===")
print("Silahkan masukkan kebutuhan anda pada aplikasi dealer")
print("Masukkan data jika anda ingin mengecek stok motor di dealer kami")
print("----- WELCOME TO DEALER MOTORCYCLE -----")
print('1. Beli Motor')
print('2. Masukkan Data No.Hp')
print('3. Mengecek Stok Motor')

menu = int(input('silahkan pilih:'))
if(menu==1):
    print('1.Tambah Motor Pembeli')
    print('2.Ubah Motor Pembeli')
    print('3.Hapus Motor Pembeli')
    print('4.Tampilkan Motor Pembeli')
    p = int(input('[pembeli] pilih:'))
    if(p==1):
        nama=input('Nama:')
        motor=input('Jenis Motor:')
        data=[nama,motor]
        dealer.add(data)
    elif(p==2):
        id_dealer=input('No.Kamu:')
        nama=input('Nama:')
        motor=input('Jenis Motor:')
        data=[nama,motor,id_dealer]
        dealer.edit(data)
    elif(p==3):
        id_dealer=input('No.Kamu:')
        data=[id_dealer]
        dealer.search(data)
        confirm=input('Yakin menghapus pembeli ini? [Y/N]:')
        if(confirm=='Y'):
            dealer.delete(data)
        else:
            print('Tidak jadi menghapus data pembeli!')
    elif(p==4):
        dealer.show()
    else:
        print('menu tidak tersedia')
elif(menu==2):
    print('1.Tambah Nomor Pembeli')
    print('2.Ubah Nomor Pembeli')
    print('3.Hapus Nomor Pembeli')
    print('4.Tampilkan Nomor Pembeli')
    p = int(input('[pembeli] pilih:'))
    if(p==1):
        nama=input('Nama:')
        no=input('No.Hp:')
        data=[nama,no]
        nomor.add(data)
    elif(p==2):
        id_nomor=input('No.Pembeli:')
        nama=input('Nama:')
        no=input('No.Hp:')
        data=[nama,no,id_nomor]
        nomor.edit(data)
    elif(p==3):
        id_nomor=input('No.Pembeli:')
        data=[id_nomor]
        nomor.search(data)
        confirm=input('Yakin menghapus pembeli ini? [Y/N]:')
        if(confirm=='Y'):
            nomor.delete(data)
        else:
            print('Tidak jadi menghapus data pembeli!')
    elif(p==4):
        nomor.show()
    else:
        print('menu tidak tersedia')
elif(menu==3):
    print('1.Tambah Stok Motor')
    print('2.Ubah Stok Motor')
    print('3.Hapus Stok Motor')
    print('4.Tampilkan Stok Motor')
    p = int(input('[pembeli] pilih:'))
    if(p==1):
        merk=input('Merk Motor:')
        stok=input('Stok Bulanan:')
        terjual=input('Motor Terjual:')
        sisa=input('Sisa Stok Motor:')
        data=[merk,stok,terjual,sisa]
        toko.add(data)
    elif(p==2):
        id_stok=input('No.Stok:')
        merk=input('Merk Motor:')
        stok=input('Stok Bulanan:')
        terjual=input('Motor Terjual:')
        sisa=input('Sisa Stok Motor:')
        data=[merk,stok,terjual,sisa,id_stok]
        toko.edit(data)
    elif(p==3):
        id_stok=input('No.Stok:')
        data=[id_stok]
        toko.search(data)
        confirm=input('Yakin menghapus data stok ini? [Y/N]:')
        if(confirm=='Y'):
            toko.delete(data)
        else:
            print('Tidak jadi menghapus data stok!')
    elif(p==4):
        toko.show()
    else:
        print('menu tidak tersedia')
else:
    exit()
    
    
    
    
    
    
           
