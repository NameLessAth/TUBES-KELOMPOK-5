import os
import sys
import math
import time
import argparse
import datetime

from Fungsi-Utama import *
from F09 import *
from F10 import *

userlist = convertuser("user.csv")
candilist = convertcandi("candi.csv")
bahanbangunanlist = convertbb("bahan_bangunan.csv")

Username, Password, Role = None, None, None
perintah = input("Masukkan command yang akan dijalankan! : ")
while perintah != "exit":
  
  
    # F09 - AMBIL LAPORAN JIN
    if masukan == "laporanjin" and Role == "bandung_bondowoso":
        laporan = getLaporan(userlist, bahanbangunanlist, candilist)
        print(f"""
> Total Jin: {laporan[0]}
> Total Jin Pengumpul: {laporan[1]}  
> Total Jin Pembangun: {laporan[2]}
> Jin Terajin: {laporan[3]}
> Jin Termalas: {laporan[4]}
> Jumlah Pasir: {laporan[5]} unit
> Jumlah Air: {laporan[6]} unit
> Jumlah Batu : {laporan[7]} unit
""")
        perintah = input("Masukkan command yang akan dijalankan! : ")
    # KETIKA BUKAN BANDUNG BONDOWOSO YANG MENGAKSES
    elif masukan == "laporanjin" and Role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        perintah = input("Masukkan command yang akan dijalankan! : ")
        
        
    
    # F10 - AMBIL LAPORAN CANDI
    if perintah == "laporancandi" and Role == "bandung_bondowoso":
        laporan = LaporanCandi(list_candi)

        # printing ketika ada setidaknya 1 candi
        if laporan[0] != 0:
            print(f"""
> Total Candi: {laporan[0]}
> Total Pasir yang digunakan: {laporan[1]}
> Total Batu yang digunakan: {laporan[2]}
> Total Air yang digunakan: {laporan[3]}
> ID Candi Termahal: {laporan[4]} (Rp {laporan[5]})
> ID Candi Termurah: {laporan[6]} (Rp {laporan[7]})""")
        
        # printing ketika tidak ada candi sama sekali
        else:
            print(f"""
> Total Candi: {laporan[0]}
> Total Pasir yang digunakan: {laporan[1]}
> Total Batu yang digunakan: {laporan[2]}
> Total Air yang digunakan: {laporan[3]}
> ID Candi Termahal: -
> ID Candi Termurah: -""")
        perintah = input("Masukkan command yang akan dijalankan! : ")
    # KETIKA BUKAN BANDUNG BONDOWOSO YANG MENGAKSES
    elif perintah == "laporancandi" and Role != "bandung_bondowoso":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        perintah = input("Masukkan command yang akan dijalankan! : ")
