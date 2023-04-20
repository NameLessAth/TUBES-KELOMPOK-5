from FungsiUtama import *

def ubahJin(userlist : list, role : str) -> list:
    # verifikasi role bandung
    if role == "bandung_bondowoso":
        uname = input("Masukkan username jin: ")
        
        # pencarian jin di usercsv
        i = 0
        while (i<NMax):
            
            # bila tidak ditemukan nama jin di list
            if userlist[i] == Mark:
                print("\nTidak ada jin dengan username tersebut.")
                return userlist
            # cari tross
            elif userlist[i] != None:

                # bila terdapat username di list
                if userlist[i].username == uname:
                    # ubah masing masing ke tipe negasinya
                    if userlist[i].role == "jin_pembangun":
                        # verifikasi
                        if (input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ") == "Y"):
                            userlist[i].role = "jin_pengumpul"
                    else:
                        # verifikasi
                        if (input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ") == "Y"):
                            userlist[i].role = "jin_pembangun"
                    return userlist   
            i += 1

    # bila role bukan bandung
    else:
        print("Perintah hanya dapat diakses oleh akun Bandung Bondowoso.")
        return userlist
    
