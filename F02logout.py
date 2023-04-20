from FungsiUtama import *

def Logout(Username : str, Role : str) -> tuple[str, str]:
    if (Role == None):
        print("Logout gagal!")
        print("Anda belum login, silakan login terlebih dahulu!")
        return Username, Role
    else:
        print("Terima kasih sudah bermain, sampai jumpa di lain hari!")
        return None, None
