import os
import sys
import math
import time
import argparse
import datetime
from typing import List


from FungsiUtama import *

def Login(userlist, Role, uname):
    
    # ketika belum login
    if Role == None:
        # input username dan password
        uname = input("Username: ")
        passw = input("Password: ")
        
        # looping untuk mencari username dan passwordnya
        i = 0
        while (i < NMax):
            if userlist[i] != None:
                # jika sudah di mark maka break
                if (userlist[i] == Mark):
                    break

                else:

                    # jika username ada
                    if (uname == userlist[i].username):

                        # cek password
                        if (passw == userlist[i].password):
                            print(f"Selamat datang, {uname}!")
                            print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                            return uname, userlist[i].role
                        
                        # password salah
                        else:
                            print("Password salah!")
                            return None, None
            i += 1

        # username tidak terdaftar
        print("Username tidak terdaftar! ")       
        return None, None
    
    else:
        print("Login gagal!")
        print(f"Anda telah login dengan username {uname}, silakan lakukan 'logout' sebelum melakukan login kembali!")
        return uname, Role
