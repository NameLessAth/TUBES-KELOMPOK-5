from FungsiUtama import *

def Kumpul(bahanlist : list, role : str) -> list:
    # verifikasi role jin pengumpul
    if role == "jin_pengumpul":

        # mendapatkan bahan dengan random integer
        pasir = RNG(0, 5); batu = RNG(0, 5); air = RNG(0, 5)

        # menambahkan yang terkumpul ke list bahann bangunan
        bahanlist[0].jumlah += pasir
        bahanlist[1].jumlah += batu
        bahanlist[2].jumlah += air

        # printing
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    # jika role bukan jin pengumpul
    else:
        print(f"Perintah hanya dapat dilakukan oleh akun Jin Pengumpul!")

    # return bahanlist lagi
    return bahanlist
