import os
import sys
import math
import time
import argparse
import datetime

from FungsiUtama import *
from F01 import *
from F02 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *

userlist = convertuser("user.csv")
candilist = convertcandi("candi.csv")
bahanbangunanlist = convertbb("bahan_bangunan.csv")

Username, Role = None, None
perintah = input("Masukkan command yang akan dijalankan! : ")
while perintah != "exit":

    # F01 - LOGIN
    if perintah == "login":
        Username, Role = Login(userlist, Role, Username)
        perintah = input("Masukkan command yang akan dijalankan! : ")
    
    # F?? - MINIMAL LOGIN
    if Role == None:
        print("Kamu Belum login!")
        perintah = input("Masukkan command yang akan dijalankan! : ")

    # F02 - LOGOUT
    if perintah == "logout":
        Username, Role = logout(Username, Role)
        perintah = input("Masukkan command yang akan dijalankan! : ")
    
    
    # F09 -  AMBIL LAPORAN JIN
    if perintah == "laporanjin" and Role == "bandung_bondowoso":
        LaporanJin(userlist, bahanbangunanlist, candilist)
        perintah = input("Masukkan command yang akan dijalankan! : ")
    elif perintah == "laporanjin" and Role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        perintah = input("Masukkan command yang akan dijalankan! : ")

    # F10 - AMBIL LAPORAN CANDI
    if perintah == "laporancandi" and Role == "bandung_bondowoso":
        LaporanCandi(candilist)
        perintah = input("Masukkan command yang akan dijalankan! : ")
    
    elif perintah == "laporancandi" and Role != "bandung_bondowoso":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        perintah = input("Masukkan command yang akan dijalankan! : ")

    # F11 - HANCURKAN CANDI
    if perintah == "hancurkancandi" and Role == "roro_jonggrang":
        candilist = HancurkanCandi(candilist)
        perintah = input("Masukkan command yang akan dijalankan! : ")
    
    elif perintah == "hancurkancandi" and Role != "roro_jonggrang":
        print("Hancurkan candi hanya bisa dilakukan oleh akun Roro Jonggrang!")
        perintah = input("Masukkan command yang akan dijalankan! : ")

    # F12 - AYAM BERKOKOK
    if perintah == "ayamberkokok" and Role == "roro_jonggrang":
        AyamBerkokok(candilist)
        perintah = "exit"
        
    elif perintah == "ayamberkokok" and Role != "roro_jonggrang":
        print("Ayam Berkokok hanya bisa dilakukan oleh akun Roro Jonggrang")
        perintah = input("Masukkan command yang akan dijalankan! : ")
