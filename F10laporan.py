import os
import sys
import math
import time
import argparse
import datetime
from typing import List


from Fungsi2Utama import *

def LaporanCandi(candi : list) -> tuple[int, int, int, int, int, int, int, int]:
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
        HargaMahal = 0
        for i in range(Len(listhargacandi)):
            if listhargacandi[i] > HargaMahal and listhargacandi[i] != None:
                HargaMahal = listhargacandi[i]
                IDMahal = i+1
        
        # cari nilai min
        HargaMurah = HargaMahal
        for i in range(Len(listhargacandi)):
            if listhargacandi[i] < HargaMurah and listhargacandi[i] != None:
                HargaMurah = listhargacandi[i]
                IDMurah = i+1

    # return value valuenya untuk diberikan di program main.py
    return [TotalCandi, TotalPasir, TotalBatu, TotalAir, IDMahal, HargaMahal, IDMurah, HargaMurah]
