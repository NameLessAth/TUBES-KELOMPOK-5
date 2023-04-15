import FungsiUtama

def summonJin(role):
    
    userlist = FungsiUtama.convertuser()
    
    while (role == "bandung_bondowoso"):
        
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        
        cekNomor = False
        Neff = 2
        
        while(cekNomor == False):
            nomor = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            
            if (nomor == 1):
                cekNomor = True
                print("Memilih jin 'Pengumpul'.")
                uname = input("Masukkan username jin: ")
                udahAda = True
                while(udahAda):
                    for i in range (Neff):
                        if (userlist[i].username == uname):
                            print(f"Username {uname} sudah diambil!")
                            uname = input("Masukkan username jin: ")
                        elif (i == Neff - 1):
                            udahAda = False
                            userlist[i].username = uname
                            password = input("Masukkan password jin: ")
                            userlist[i].password = password
                            break
                if (len(password) < 5 or len(password) > 26):
                    print("Password panjangnya harus 5-25 karakter!")
                else:
                    print("Mengumpulkan sesajen...")
                    print("Menyerahkan sesajen...")
                    print("Membacakan mantra...")
                    print(f"Jin {uname} berhasil dipanggil!")
            
            elif (nomor == 2):
                cekNomor = True
                print("Memilih jin 'Pembangun'.")
                uname = input("Masukkan username jin: ")
                udahAda = True
                while(udahAda):
                    for i in range (Neff):
                        if (userlist[i].username == uname):
                            print(f"Username {uname} sudah diambil!")
                            uname = input("Masukkan username jin: ")
                        elif (i == Neff - 1):
                            udahAda = False
                            userlist[i].username = uname
                            password = input("Masukkan password jin: ")
                            userlist[i].password = password
                            break
                if (len(password) < 5 or len(password) > 26):
                    print ("Password panjangnya harus 5-25 karakter!")
                else:
                    print("Membangun candi...")
                    print("Membacakan mantra...")
                    print(f"Jin {uname} berhasil dipanggil!")
            
            else:
                print(f"Tidak ada jenis jin bernomor '{nomor}'!")
                cekNomor = False
        
        if (cekNomor):
            for i in range(2, FungsiUtama.NMax):
                if (userlist[i] == None):
                    userlist[i] = FungsiUtama.user(uname, password, "")
                    if (nomor == 1):
                        userlist[i].role = "jin_pengumpul"
                    elif (nomor == 2):
                        userlist[i].role = "jin_pembangun"
                    
                    Neff += 1
                    break
                
        if (Neff == 102):
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            
        break
    
    if (role != "bandung_bondowoso"):
        print("Anda bukan Bondowoso, hanya Bondowoso yang bisa melakukan summonjin!")
        print("Silakan logout dan login kembali dengan user Bondowoso!")
        
summonJin()