from FungsiUtama import *

def LaporanJin(userlist : list, bahanlist : list, candilist : list, Role : str):
    if Role == "bandung_bondowoso":
        jinpengumpul = 0; jinpembangun = 0; topterajin = "-"; toptermalas = "-"; pasir = 0; batu = 0; air = 0
        
        # menghitung batu pasir air
        for i in range(Len(bahanlist)):
            if bahanlist[i].nama == "batu":
                batu = bahanlist[i].jumlah
            elif bahanlist[i].nama == "pasir":
                pasir = bahanlist[i].jumlah
            else:
                air = bahanlist[i].jumlah
        
        # menghitung jin jin
        for i in range(2, Len(userlist)):
            if userlist[i] != None:
                if userlist[i].role == "jin_pengumpul":
                    jinpengumpul += 1
                else:
                    jinpembangun += 1
        
        if jinpembangun != 0:
            # menghitung anggota anggota jin nya

            # memasukkan jin jin ke array dari array username
            jinlist = [None for i in range(NMax)]; jinlist[0] = Mark
            for i in range(2, Len(userlist)):
                if userlist[i] != None:
                    if userlist[i].role == "jin_pembangun":
                        Append(jinlist, userlist[i].username)

            # memasukkan username jin ke array dari candi yang telah dibentuk
            i = 0
            while (i < NMax):
                if candilist[i] == Mark:
                    break
                if candilist[i] != None:
                    if not AdaatauTidak(jinlist, candilist[i].pembuat):
                        Append(jinlist, candilist[i].pembuat)
                i += 1

            # declare jumlah2 berapa aja yang dibikin
            jumlahdibangun = [0 for i in range(Len(jinlist)+2)]
            jumlahdibangun[Len(jinlist)] = Mark; jumlahdibangun[Len(jinlist)+1] = None

            # penghitungan 
            for i in range(Len(candilist)):
                if candilist[i] != None:
                    for j in range(Len(jinlist)):
                        if candilist[i].pembuat == jinlist[j]:
                            jumlahdibangun[j] += 1
            
            # ambil min dan max
            min = Min(jumlahdibangun)
            max = Max(jumlahdibangun)

            # listing termalas dan terajin
            termalas = [None for i in range(NMax)]; termalas[0] = Mark
            for i in range(Len(jinlist)):
                if jumlahdibangun[i] == min:
                    Append(termalas, jinlist[i])
            
            terajin = [None for i in range(NMax)]; terajin[0] = Mark
            for i in range(Len(jinlist)):
                if jumlahdibangun[i] == max:
                    Append(terajin, jinlist[i])

            toptermalas = termalas[0]
            for i in range(1, Len(termalas)):
                toptermalas = CompareString(toptermalas, termalas[i])
            
            topterajin = terajin[0]
            for i in range(1, Len(terajin)):
                topterajin = CompareString(topterajin, terajin[i])
        
        else:
            topterajin, toptermalas = "-", "-"

        # printing fungsi sebagai fungsi void
        print(f"""
> Total Jin: {jinpembangun+jinpengumpul}
> Total Jin Pengumpul: {jinpengumpul}  
> Total Jin Pembangun: {jinpembangun}
> Jin Terajin: {topterajin}
> Jin Termalas: {toptermalas}
> Jumlah Pasir: {pasir} unit
> Jumlah Air: {air} unit
> Jumlah Batu : {batu} unit""")

    # yang mengakses bukan bandung
    else:
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
