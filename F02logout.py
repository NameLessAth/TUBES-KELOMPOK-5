import os
import sys
import math
import time
import argparse
import datetime
from typing import List


from FungsiUtama import *

def logout(Username : str, Role : str) -> tuple[str, str]:
    
    # bila logout dan belum login
    if (Role == None):
        print("Logout gagal!")
        print("Anda belum login, silakan login terlebih dahulu!")
        return Username, Role
    
    # logout dengan lancar
    else:
        print("Terima kasih sudah bermain, sampai jumpa di lain hari!")
        return None, None
