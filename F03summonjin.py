from FungsiUtama import *

def summonJin(usercsv : list, role : str) -> list:
    if role == "bandung_bondowoso" and LenSejati(usercsv) < 102:
        
        # formatting
        print(f"""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi
""")
        # input jenis jin
        jenisJin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while (jenisJin > 2):
            print(f"\nTidak ada jenis jin bernomor \"{jenisJin}\"\n")
            jenisJin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        
        # switch case jenis jin
        if jenisJin == 1:
            print(f"\nMemilih jin \"Pengumpul\".\n")
            jenisJin = "jin_pengumpul"
        else:
            print(f"\nMemilih jin \"Pembangun\".\n")
            jenisJin = "jin_pembangun"
        
        # input username
        ada = True
        while ada:
            uname = input("Masukkan username jin: "); i = 0
            while (i < NMax):
                if usercsv[i] == Mark:
                    ada = False
                    break
                elif usercsv[i] != None:
                    if usercsv[i].username == uname:
                        print(f"\nUsername \"{uname}\" sudah diambil!\n")
                        break
                i += 1
        
        # input password
        passw = input("Masukkan password jin: ")
        while len(passw) < 5 or len(passw) > 25:
            print(f"\nPassword panjangnya harus 5-25 karakter!\n")
            passw = input("Masukkan password jin: ")

        # append ke userlist
        Append(usercsv, user(uname, passw, jenisJin))

        # formatting
        print(f"""
Mengumpulkan sesajen...
Menyerahkan sesajen...
Membacakan mantra...
        
Jin {uname} berhasil dipanggil!
        """)


    # jika jin sudah 100
    elif role == "bandung_bondowoso" and LenSejati(usercsv) >= 102:
        print(f"Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    
    # jika yang mengakses bukan bandung
    else:
        print(f"Perintah ini hanya bisa dijalankan di akun Bandung Bondowoso.")

    return usercsv
