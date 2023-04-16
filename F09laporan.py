import os
import sys
import math
import time
import argparse
import datetime
from typing import List


from FungsiUtama import *

def LaporanJin(user : list, bahan : list, candi : list) -> tuple[int, int, int, str, str, int, int, int]:
    jinpengumpul = 0; jinpembangun = 0; topterajin = "-"; toptermalas = "-"; pasir = 0; batu = 0; air = 0
    
    # menghitung batu pasir air
    for i in range(Len(bahan)):
        if bahan[i].nama == "batu":
            batu = bahan[i].jumlah
        elif bahan[i].nama == "pasir":
            pasir = bahan[i].jumlah
        else:
            air = bahan[i].jumlah
    
    # menghitung jin jin
    for i in range(2, Len(user)):
        if user[i] != None:
            if user[i].role == "jin_pengumpul":
                jinpengumpul += 1
            else:
                jinpembangun += 1
    
    if jinpembangun != 0:
        # menghitung anggota anggota jin nya
        # memasukkan jin jin ke array
        jinlist = [None for i in range(NMax)]; jinlist[0] = Mark
        for i in range(2, Len(user)):
            if user[i] != None:
                if user[i].role == "jin_pembangun":
                    Append(jinlist, user[i].username)

        # declare jumlah2 berapa aja yang dibikin
        jumlahdibangun = [0 for i in range(Len(jinlist)+2)]
        jumlahdibangun[Len(jinlist)] = Mark; jumlahdibangun[Len(jinlist)+1] = None

        # penghitungan 
        for i in range(Len(candi)):
            if candi[i] != None:
                for j in range(Len(jinlist)):
                    if candi[i].pembuat == jinlist[j]:
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
