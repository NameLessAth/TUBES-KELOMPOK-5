import os
import sys
import math
import time
import argparse
import datetime
from typing import List


from Fungsi2Utama import *

def AyamBerkokok(candilist : str):
    
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
