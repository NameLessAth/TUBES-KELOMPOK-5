from FungsiUtama import *

def hapusJin(userlist : list, candilist : list, stackUndo : list, role : str) -> tuple[list, list, list]:
    # validasi yang mengakses bandung
    if role == "bandung_bondowoso":

        # input username jin 
        uname = input("Masukkan username jin: ")

        # mencari uname dari jin
        i = 0; j=0
        while (i < NMax):

            # bila tidak ketemu sama sekali
            if userlist[i] == Mark:
                print("\nTidak ada jin dengan username tersebut!")
                return userlist, candilist, stackUndo
            
            # mencari
            elif userlist[i] != None:

                # bila ketemu
                if userlist[i].username == uname:

                    # verifikasi
                    if (input(f"Apakah anda yakin ingin menghapus jin dengan username {uname} (Y/N)? ") == "Y"):
                        
                        userUndo = userlist[i]
                        candiUndo = [None for i in range(NMax)]; candiUndo[0] = Mark

                        userlist[i] = None
                        print("\nJin telah berhasil dihapus dari alam gaib.")

                        # mencari candi yang telah dibuat oleh jin tersebut
                        while (j < NMax):
                            
                            # return
                            if candilist[j] == Mark:
                                return userlist, candilist, Append(stackUndo, [userUndo, candiUndo])
                            
                            elif candilist[j] != None:
                                # bila ada yang dibuat candi oleh jin nya
                                if candilist[j].pembuat == uname:
                                    Append(candiUndo, candilist[j])
                                    candilist[j] = None
                            j += 1
                    
                    # bila tidak jadi dihancurkan (verif == N)
                    else:
                        print("\ndipahami, semoga harimu menyenangkan, Bandung!")
                        return userlist, candilist, stackUndo
            i += 1

    else:

        print("Perintah hanya dapat diakses oleh akun Bandung Bondowoso.")
        return userlist, candilist, stackUndo
