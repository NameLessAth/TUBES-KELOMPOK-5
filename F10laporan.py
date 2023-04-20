from FungsiUtama import *

def LaporanCandi(candi : list, Role : str):
    if Role == "bandung_bondowoso":
        TotalCandi = 0; TotalPasir = 0; TotalBatu = 0; TotalAir = 0; IDMahal = 0; HargaMahal = 0; IDMurah = 0; HargaMurah = 0
            # mengumpulkan data2 seperti total2 dari bahan
        for i in range(Len(candi)):
            if candi[i] != None:
                TotalPasir += candi[i].pasir
                TotalAir += candi[i].air
                TotalBatu += candi[i].batu
                TotalCandi += 1

        if TotalCandi > 0:
            
            # memasukkan harga harga candi ke 
            listhargacandi = [None for i in range(Len(candi)+1)]
            listhargacandi[Len(candi)] = Mark
            for i in range(Len(candi)):
                if candi[i] != None:
                    listhargacandi[i] = (candi[i].pasir) * 10000 + (candi[i].batu) * 15000 + (candi[i].air) * 7500

            # cari nilai max 
            HargaMahal = -9999
            for i in range(Len(listhargacandi)):
                if listhargacandi[i] != None and listhargacandi[i] > HargaMahal:
                    HargaMahal = listhargacandi[i]
                    IDMahal = i+1
            
            # cari nilai min
            HargaMurah = HargaMahal
            if Len(listhargacandi) == 1:
                IDMurah = IDMahal
            else:
                for i in range(Len(listhargacandi)):
                    if listhargacandi[i] != None and listhargacandi[i] < HargaMurah:
                        HargaMurah = listhargacandi[i]
                        IDMurah = i+1
        
        else:
            IDMurah, IDMahal = "-", "-"

        # return sebagai print (fungsi void)
        print(f"""
> Total Candi: {TotalCandi}
> Total Pasir yang digunakan: {TotalPasir}
> Total Batu yang digunakan: {TotalBatu}
> Total Air yang digunakan: {TotalAir}
> ID Candi Termahal: {IDMahal} (Rp {HargaMahal})
> ID Candi Termurah: {IDMurah} (Rp {HargaMurah})""")

    # jika yang mengakses bukan bandung
    else:
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
