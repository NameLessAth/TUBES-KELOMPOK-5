import os
import sys
import math
import time
import argparse
import datetime
from typing import List


from FungsiUtama import *

def HancurkanCandi (candi : list) -> list:
    # input ID Candi yang hendak dihancurkan
    IDCandi = int(input("Masukkan ID candi: ")) 

    # pencarian ID yang telah diinput
    for i in range(Len(candi)):
        if candi[i] != None:

            # bila ID ditemukan
            if candi[i].id == IDCandi:

                # meminta argumen ya atau tidak
                Hancur = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)? ")

                # argumen Y, candi dibuat None dan disimpan listnya
                if Hancur == "Y":
                    candi[i] = None
                    print("\nCandi berhasil dihancurkan")
                    return candi
                
                # argumen N, candi tidak jadi dihancurkan
                else:
                    print("Candi tidak jadi dihancurkan")
                    return candi
                
    # bila tidak ditemukan ID yang dicari
    print("\nTidak ada candi dengan ID tersebut!")
    return candi
