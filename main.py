import os
import sys
import math
import time
import argparse
import datetime

from Fungsi-Utama import *
from F09 import *

userlist = convertuser("user.csv")
candilist = convertcandi("candi.csv")
bahanbangunanlist = convertbb("bahan_bangunan.csv")

Username, Password, Role = None, None, None
masukan = input(">>> ")
while masukan != "exit":
  
  
      # F09 - AMBIL LAPORAN JIN
    if masukan == "laporanjin" and Role == "bandung_bondowoso":
        laporan = getLaporan(list_users, list_bahan_bangunan, list_candi)
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
        masukan = input(">>> ")
    elif masukan == "laporanjin" and Role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        masukan = input(">>> ")
