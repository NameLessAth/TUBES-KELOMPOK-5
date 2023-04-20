from FungsiUtama import *

def Exit() -> bool:
    # verifikasi user
    verifikasi = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
    while (verifikasi.lower() != "y" and verifikasi.lower() != "n"):
        verifikasi = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
    
    # if else jika user hendak save atau tidak
    if verifikasi.lower() == "y":
        return True
    else:
        return False
