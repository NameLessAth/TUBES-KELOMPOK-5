from FungsiUtama import *
from F01 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
from B04 import *

# stack untuk melakukan Undo
stackUndo = [None for i in range(NMax)]; stackUndo[0] = Mark
# variabel user candi dan bahanbangunan untuk menyimpan hasil csv parser
userlist, candilist, bahanbangunanlist = Load()
# variabel username dan Role untuk crosschecking akses dan juga printing username dari macam2 fungsi 
Username, Role = None, None

# input pertama kali
perintah = (input("Masukkan command yang akan dijalankan! : ")).lower()
# looping
while perintah != "exit":
    while True:
        # F14 - SAVE
        if perintah == "save":
            Save(userlist, candilist, bahanbangunanlist)

        # F15 - HELP
        if perintah == "help":
            Help(Username, Role)

        # F01 - LOGIN
        if perintah == "login":
            Username, Role = Login(userlist, Role, Username)
        
        # F?? - MINIMAL LOGIN
        if Role == None and perintah != "login" and perintah != "help":
            print("Kamu Belum login!")
        
        # F02 - LOGOUT
        elif perintah == "logout":
            Username, Role = Logout(Username, Role)
        
        # F03 - SUMMON JIN
        elif perintah == "summonjin":
            userlist = summonJin(userlist, Role)

        # F04 - HILANGKAN JIN
        elif perintah == "hapusjin":
            userlist, candilist, stackUndo = hapusJin(userlist, candilist, stackUndo, Role)

        # F05 - UBAH ROLE JIN
        elif perintah == "ubahjin":
            userlist = ubahJin(userlist, Role)

        # F06 - JIN PEMBANGUN
        elif perintah == "bangun":
            candilist, bahanbangunanlist = Bangun(candilist, bahanbangunanlist, Username, Role)

        # F07 - JIN PENGUMPUL
        elif perintah == "kumpul":
            bahanbangunanlist = Kumpul(bahanbangunanlist, Role)

        # F08 - BATCH KUMPUL/BANGUN
        elif perintah == "batchkumpul" or perintah == "batchbangun":
            userlist, candilist, bahanbangunanlist = Batch(perintah, userlist, candilist, bahanbangunanlist, Role)

        # F09 - AMBIL LAPORAN JIN
        elif perintah == "laporanjin":
            LaporanJin(userlist, bahanbangunanlist, candilist, Role)

        # F10 - AMBIL LAPORAN CANDI
        elif perintah == "laporancandi":
            LaporanCandi(candilist, Role)

        # F11 - HANCURKAN CANDI
        elif perintah == "hancurkancandi":
            candilist = HancurkanCandi(candilist, Role)

        # F12 - AYAM BERKOKOK
        elif perintah == "ayamberkokok":
            AyamBerkokok(candilist, Role)

        # B04 - UNDO
        elif perintah == "undo":
            userlist, candilist, stackUndo = Undo(userlist, candilist, stackUndo, Role)

        break
    
    # ketika ayamberkokok, permainan berakhir
    if perintah == "ayamberkokok" and Role == "roro_jonggrang":
        break
    
    perintah = (input("Masukkan command yang akan dijalankan! : ")).lower()

# F16 - EXIT
if perintah == "exit":
    if Exit():
        Save(userlist, candilist, bahanbangunanlist)

# goodbye message
print("sampai jumpa di lain waktu!!!")
