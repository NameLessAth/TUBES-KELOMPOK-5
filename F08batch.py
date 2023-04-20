from FungsiUtama import *

def Batch(command : str, userlist : list, candilist : list, bahanlist : list, Role : str) -> tuple[list, list, list]:
    
    # verifikasi role bandung 
    if Role == "bandung_bondowoso":

        # jika command nya batch kumpul
        if command == "batchkumpul":
            
            # menghitung jin pengumpul
            jinpengumpul = 0; i = 0
            while (i<NMax):
                if userlist[i] == Mark:
                    break
                elif userlist[i] != None:
                    if userlist[i].role == "jin_pengumpul":
                        jinpengumpul += 1
                i += 1
            
            # case ketika ada jin pengumpul dan tidak
            if jinpengumpul > 0:
                # printing
                print(f"Mengerahkan {jinpengumpul} untuk mengumpulkan bahan.")

                # proses while loop rng selama banyaknya jin pengumpul
                pasirCandi = 0; batuCandi = 0; airCandi = 0; repeat = 0
                while (repeat != jinpengumpul):
                    pasirCandi += RNG(0,5)
                    batuCandi += RNG(0, 5)
                    airCandi += RNG(0, 5)
                    repeat += 1

                # menambahkan bahan2 yang telah didapat
                bahanlist[0].jumlah += pasirCandi
                bahanlist[1].jumlah += batuCandi
                bahanlist[2].jumlah += airCandi
                print(f"Jin menemukan total {pasirCandi} pasir, {batuCandi} batu, dan {airCandi} air.")

            else: # jika pengumpul tidak ada
                print("kumpul gagal. Anda tidak punya jin pengumpul. Minimal summon jin dulu bang bandung!")
            # return value
            return userlist, candilist, bahanlist
        
        # jika command nya batch bangun
        elif command == "batchbangun":

            # menghitung jin pembangun dan listing jin nya
            jinPembangun = [None for i in range(NMax)]; jinPembangun[0] = Mark
            jinPembangunCount = 0; i = 0 
            while (i<NMax):
                if userlist[i] == Mark:
                    break
                elif userlist[i] != None:
                    if userlist[i].role == "jin_pembangun":
                        Append(jinPembangun, userlist[i].username)
                        jinPembangunCount += 1
                i += 1
            
            # case ketika ada dan tidak ada jin pembangun
            if jinPembangunCount > 0:

                # declare tiap2 bahan bangunan terlebih dahulu
                totalpasir = 0; totalbatu = 0; totalair = 0
                pasirCandi = [None for i in range(NMax)]; pasirCandi[0] = Mark
                batuCandi = [None for i in range(NMax)]; batuCandi[0] = Mark
                airCandi = [None for i in range(NMax)]; airCandi[0] = Mark

                # RNG untuk batch bangun
                repeat = 0
                while (repeat != jinPembangunCount):
                    # append dan menghitung di total 
                    Append(pasirCandi, RNG(1, 5)); totalpasir += pasirCandi[repeat]
                    Append(batuCandi, RNG(1, 5)); totalbatu += batuCandi[repeat]
                    Append(airCandi, RNG(1, 5)); totalair += airCandi[repeat]
                    repeat += 1

                # printing sebelum verifikasi
                print(f"Mengerahkan {jinPembangunCount} jin untuk membangun candi dengan total bahan {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")

                # case ketika bahan cukup
                if bahanlist[0].jumlah >= totalpasir and bahanlist[1].jumlah >= totalbatu and bahanlist[2].jumlah >= totalair:
                    i = 0
                    while (i < NMax):
                        if jinPembangun[i] != Mark:
                            # mencari id candi yang kosong
                            idcandi = 0
                            while (idcandi < NMax):
                                if candilist[idcandi] == None:
                                    idcandi += 1
                                    break
                                elif candilist[idcandi] == Mark:
                                    idcandi += 1
                                    break
                                idcandi += 1
                            
                            # mengappend ke candilist 
                            if LenSejati(candilist) != 100:
                                Append(candilist, candi(idcandi, jinPembangun[i], pasirCandi[i], batuCandi[i], airCandi[i]))
                        else:
                            break
                        i += 1
                    print(f"Jin berhasil membangun total {jinPembangunCount} candi.")
                
                # case ketika bahan tidak cukup
                else:
                    # printing rapi sesuai yang dibutuhkan
                    print(f"Bangun gagal. Kurang ", end="")
                    if bahanlist[0].jumlah < totalpasir:
                        print(f"{totalpasir} pasir, ", end="")
                    if bahanlist[1].jumlah < totalbatu:
                        print(f"{totalbatu} batu, ", end="")
                    if bahanlist[0].jumlah < totalpasir or bahanlist[1].jumlah < totalbatu:
                        print(f"dan {totalair} air.")
                    else:
                        print(f"{totalair} air.")

            else: # jika jin pembangun tidak ada
                print("Bangun gagal. Anda tidak punya jin pembangun. Minimal summon jin dulu bang bandung!")

        else:
            print("perintah tidack valdi, minimal baca help.")
    
    else:
        print("Perintah ini hanya bisa diakses oleh akun Bandung Bondowoso.")
    
    return userlist, candilist, bahanlist               
