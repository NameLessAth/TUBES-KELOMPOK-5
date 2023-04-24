from FungsiUtama import *

def Undo(userlist : list, candilist : list, stackUndo : list, Role : str) -> tuple[list, list, list]:

    # verifikasi role
    if Role == "bandung_bondowoso":
        # mencari stack terluar untuk dikeluarkan sebagai fungsi Undo
        i = 0; stackterluar = None
        while (i < NMax):
            if (stackUndo[i] == Mark):
                break
            elif (stackUndo[i] != None):
                stackterluar = stackUndo[i]
            i += 1

        # if else ketika tidak ada stack (baru memulai load dan belum menghapus jin sama sekali)
        if stackterluar != None:
            # verifikasi terlebih dahulu
            if (input(f"Apakah kamu yakin untuk meng-undo penghapusan jin atas nama {stackterluar[0].username} ? (Y/N) ")).lower() == "y":
                # masukkan kembali ke user list
                Append(userlist, stackterluar[0])
                # masukkan candi yang telah dibuat kembali ke candi list
                if Len(stackterluar[1]) > 0:
                    i = 0
                    # looping O(n^2) untuk mengcross check apakah ada candi atau tidak dan menempatkannya sesuai id nya
                    while (stackterluar[1][i] != Mark):
                        candilist[stackterluar[1][i].id-1] = stackterluar[1][i]
                        i += 1

                # stackterluar dihapus
                stackUndo = Init(stackUndo)
                
                # format printing untuk kreativitas semata
                print(f"""
YOUR DUTY IS NOT OVER, {stackterluar[0].username}!

Undo berhasil dilakukan!
Jin dengan nama {stackterluar[0].username} berhasil dibangkitkan dari alam kubur ke pasukan kembali!""")
            
            # ketika verifikasi == n
            else:
                print("dapat dipahami, semoga harimu menyenangkan")
        
        # ketika stack kosong dan tidak mempunyai anggota
        else:
            print("tidak ada yang dapat dibangkitkan kembali!")

    # ketika yang mengakses bukan Bandung
    else:
        print("Perintah ini hanya dapat diakses oleh akun Bandung Bondowoso")
    
    # return
    return userlist, candilist, stackUndo
    
