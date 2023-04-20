from FungsiUtama import *

def AyamBerkokok(candilist : str, Role : str):
    if Role == "roro_jonggrang":
        
        # hitung berapa banyak candi
        candicount = 0
        for i in range(Len(candilist)):
            if candilist[i] != None:
                candicount += 1

        if candicount < 100:
            print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {candicount}

Selamat, Roro Jonggrang memenangkan permainan!

*Bandung Bondowoso angry noise*
Roro Jonggrang dikutuk menjadi candi.""")
    
        else:
            print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: 100

Yah, Bandung Bondowoso memenangkan permainan!""")

    # yang mengakses bukan Roro jonggrang    
    else:
        print("Ayam Berkokok hanya bisa dilakukan oleh akun Roro Jonggrang")
